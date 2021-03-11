/****** Script for SelectTopNRows command from SSMS  ******/
SELECT [FirstName],LastName,[Title]
FROM [AdventureWorksDW2017].[dbo].[DimEmployee]
WHERE Title = 'Marketing Manager' OR Title = 'Sales Representative';