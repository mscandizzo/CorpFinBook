/****** Script for SelectTopNRows command from SSMS  ******/
SELECT [AccountKey],[Amount]
FROM [AdventureWorksDW2017].[dbo].[FactFinance]
WHERE AccountKey = 60 OR Amount = 2000