from datetime import date
import pytest
from pytest_bdd import scenarios, given, when, then, parsers

from core.expense_service import ExpenseService
from core.in_memory_expense_repository import InMemoryExpenseRepository

scenarios("./expense_management.feature")


@pytest.fixture
def context():
    repo = InMemoryExpenseRepository()
    service = ExpenseService(repo)
    return {"service": service, "db": repo}


@given(parsers.parse("un gestor de gastos vacío"))
def empty_manager(context):
    pass


@given(parsers.parse("un gestor con un gasto de {amount:d} euros"))
def manager_with_one_expense(context, amount):
    context["service"].create_expense(
        title="Gasto inicial", amount=amount, description="", expense_date=date.today()
    )


@when(parsers.parse("añado un gasto de {amount:d} euros llamado {title}"))
def add_expense(context, amount, title):
    context["service"].create_expense(
        title=title, amount=amount, description="", expense_date=date.today()
    )


@when(parsers.parse("elimino el gasto con id {expense_id:d}"))
def remove_expense(context, expense_id):
    context["service"].remove_expense(expense_id)


@when(parsers.parse("añado dos gastos de {amount:d} euros llamado {title}"))
def add_two_expense(context, amount, title):
    context["service"].create_expense(
        title=title, amount=amount, description="", expense_date=date.today()
    )
    context["service"].create_expense(
        title=title, amount=amount, description="", expense_date=date.today()
    )


@when(parsers.parse("añado tres gastos de {amount:d} euros llamado {title}"))
def add_three_expense(context, amount, title):
    for i in range(3):
        context["service"].create_expense(
            title=title, amount=amount, description="", expense_date=date.today()
        )


@when(parsers.parse("elimino el ultimo gasto de {amount:d} euros llamado {title}"))
def remove_last_expense(context, amount, title):
    expenses = context["service"].list_expenses()
    for expense in reversed(expenses):
        if expense.amount == amount and expense.title == title:
            context["service"].remove_expense(expense.id)
            break


@when(parsers.parse("aplico un descuento del {discount:d}%"))
def apply_discount(context, discount):
    context["service"].apply_discount(discount)


@when(
    parsers.parse(
        "aplico un descuento del {discount:d}% si el gasto total es mayor a {total:d} euros"
    )
)
def apply_discount_if_total(context, discount, total):
    context["service"].apply_discount_if_total_is_greater_than(discount, total)


@when(
    parsers.parse(
        "elimino el ultimo gasto de {amount:d} euros llamado {title} si el gasto total es mayor a {total:d} euros"
    )
)
def remove_expense_if_total(context, amount, title, total):
    context["service"].remove_expense_if_total_is_greater_than(amount, title, total)


@then(parsers.parse("el total de dinero gastado debe ser {total:d} euros"))
def check_total(context, total):
    assert int(context["service"].total_amount()) == total


@then(parsers.parse("{month_name} debe sumar {expected_total:d} euros"))
def check_month_total(context, month_name, expected_total):
    total_actual = context["totals"].get(month_name, 0)
    assert total_actual == expected_total


@then(parsers.parse("debe haber {expenses:d} gastos registrados"))
def check_expenses_length(context, expenses):
    total = len(context["db"]._expenses)
    assert expenses == total
