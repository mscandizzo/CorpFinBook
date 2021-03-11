/****** Script for SelectTopNRows command from SSMS  ******/
SELECT EmployeeKey,[FirstName],[LastName],[Title]
      
  FROM [AdventureWorksDW2017].[dbo].[DimEmployee]
  WHERE FirstName IN ('David','Paul')
  AND Title LIKE 'Production Technician%'
UNION 
SELECT EmployeeKey,[FirstName],[LastName],[Title]
      
  FROM [AdventureWorksDW2017].[dbo].[DimEmployee]
  WHERE FirstName IN ('David')
 