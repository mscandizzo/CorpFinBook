USE AdventureWorksDW2017

SELECT E.FirstName, E.LastName, S.SalesTerritoryRegion, S.SalesTerritoryCountry, G.StateProvinceName

FROM DimEmployee AS E INNER JOIN DimSalesTerritory AS S ON E.SalesTerritoryKey = S.SalesTerritoryKey 
INNER JOIN DimGeography AS G 
ON G.SalesTerritoryKey = E.SalesTerritoryKey

WHERE S.SalesTerritoryKey !=11
