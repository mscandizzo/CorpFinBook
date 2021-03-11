use AdventureWorksDW2017

SELECT FF.FinanceKey,DO.OrganizationName,DA.AccountDescription, DA.AccountType,FF.Amount

FROM FactFinance as FF JOIN DimOrganization AS DO
ON FF.OrganizationKey = DO.OrganizationKey
JOIN DimAccount AS DA
ON FF.AccountKey = DA.AccountKey