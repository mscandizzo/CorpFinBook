/****** Script for SelectTopNRows command from SSMS  ******/
SELECT SpanishPromotionName,MinQty,MaxQty
  FROM [AdventureWorksDW2017].[dbo].[DimPromotion]
  WHERE MaxQty IS NOT NULL;