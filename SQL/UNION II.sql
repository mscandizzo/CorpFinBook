/****** Script for SelectTopNRows command from SSMS  ******/
SELECT [AccountKey] ,[Amount] 
  FROM [AdventureWorksDW2017].[dbo].[FactFinance]
  WHERE AccountKey IN (60,61)
  UNION 
  SELECT [AccountKey] ,[Amount] 
  FROM [AdventureWorksDW2017].[dbo].[FactFinance]
  WHERE AccountKey IN (71,73)