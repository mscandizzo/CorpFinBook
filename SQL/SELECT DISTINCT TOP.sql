SELECT DISTINCT TOP(10)[StateProvinceCode] AS State_Code,
				       [StateProvinceName] AS State_Name,
				       [CountryRegionCode] AS Country_Code
  FROM [AdventureWorksDW2017].[dbo].[DimGeography]
  ORDER BY 
  StateProvinceName DESC,
  CountryRegionCode DESC;