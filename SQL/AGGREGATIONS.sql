/****** Script for SelectTopNRows command from SSMS  ******/
SELECT  SUM(Amount) AS Sum_Amount,
		COUNT(Amount) Count_Amount,
        COUNT(DISTINCT Amount) Count_Amount_Distinct,
		MIN(Amount) Min_Amount,
		MAX(Amount) Max_Amount,
		AVG(Amount) Avg_Amount
FROM [AdventureWorksDW2017].[dbo].[FactFinance]