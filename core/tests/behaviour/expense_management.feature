Feature: Gestión de gastos
  Como estudiante
  Quiero registrar mis gastos
  Para controlar cuánto dinero gasto

  Scenario: Crear un gasto y comprobar cual es el total que llevo gastado
    Given un gestor de gastos vacío
    When añado un gasto de 5 euros llamado Café
    Then el total de dinero gastado debe ser 5 euros

  Scenario: Eliminar un gasto y comprobar cual es el total que llevo gastado
    Given un gestor con un gasto de 5 euros
    When elimino el gasto con id 1
    Then debe haber 0 gastos registrados

  Scenario: Crear y eliminar un gasto y comprobar que no he gastado dinero
    Given un gestor de gastos vacío
    When añado un gasto de 5 euros llamado Café
    And elimino el gasto con id 1
    Then debe haber 0 gastos registrados

  Scenario: Crear dos gastos diferentes y comprobar que el total que llevo gastado es la suma de ambos
    Given un gestor de gastos vacío
    When añado un gasto de 5 euros llamado Café
    And añado un gasto de 10 euros llamado Comida
    Then el total de dinero gastado debe ser 15 euros

  Scenario: Crear tres gastos diferentes que sumen 30 euros hace que el total sean 30 euros
    Given un gestor de gastos vacío
    When añado dos gastos de 15 euros llamado Almogrote
    Then el total de dinero gastado debe ser 30 euros

  Scenario: Crear tres gastos de 10, 30, 30 euros y elimino el ultimo gasto la suma son 40 euros
    Given un gestor de gastos vacío
    When añado un gasto de 10 euros llamado Miel
    And añado dos gastos de 30 euros llamado Sartén
    And elimino el ultimo gasto de 30 euros llamado Sartén
    Then el total de dinero gastado debe ser 40 euros

  Scenario: Crear dos gastos de 43 euros que sumen 86 euros y luego le aplico un descuento del 10% y el total es 77 euros
    Given un gestor de gastos vacío
    When añado dos gastos de 43 euros llamado Salmón
    And aplico un descuento del 10%
    Then el total de dinero gastado debe ser 77 euros
  
  Scenario: Crear 2 gastos de 10 euros y 3 gastos de 5 euros y luego le aplico un descuento del 20% si el gasto total es mayor a 50 euros
    Given un gestor de gastos vacío
    When añado dos gastos de 10 euros llamado Limonada
    And añado tres gastos de 5 euros llamado Galletas
    And aplico un descuento del 20% si el gasto total es mayor a 50 euros
    Then el total de dinero gastado debe ser 35 euros
  
  Scenario: Crear un gasto de 10 euros, otro de 20 euros y otro de 30 euros y eliminar el ultimo gasto si el gasto total es mayor a 35 euros
    Given un gestor de gastos vacío
    When añado un gasto de 10 euros llamado Agua
    And añado un gasto de 20 euros llamado Cerveza
    And añado un gasto de 30 euros llamado Vino
    And elimino el ultimo gasto de 30 euros llamado Vino si el gasto total es mayor a 35 euros
    Then el total de dinero gastado debe ser 30 euros