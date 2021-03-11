/****** Script for SelectTopNRows command from SSMS  ******/
SELECT [AccountKey],SUM([Amount]) AS Total_Amount
  FROM [AdventureWorksDW2017].[dbo].[FactFinance]
  WHERE AccountKey IN (6,7,8)
  OR
  AccountKey BETWEEN 70 AND 80 
  GROUP BY AccountKey
  HAVING COUNT(Amount) > 1000

  