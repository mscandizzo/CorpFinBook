use AdventureWorksDW2017

SELECT FF.FinanceKey,DD.FullDateAlternateKey,DO.OrganizationName,DDep.DepartmentGroupName,DS.ScenarioName, DA.AccountDescription, DA.AccountType,FF.Amount

FROM FactFinance as FF JOIN DimDate as DD ON FF.DateKey = DD.DateKey
JOIN DimOrganization AS DO
ON FF.OrganizationKey = DO.OrganizationKey
JOIN DimDepartmentGroup AS DDep
ON FF.DepartmentGroupKey = DDep.DepartmentGroupKey
JOIN DimScenario AS DS
ON FF.ScenarioKey = DS.ScenarioKey
JOIN DimAccount AS DA
ON FF.AccountKey = DA.AccountKey
