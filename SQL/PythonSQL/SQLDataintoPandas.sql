EXEC sp_execute_external_script
@language = N'Python', --comments here follow SQL Syntax
@script = N'
OutputDataSet = InputDataSet.iloc[5:15] # comments here follow Python syntax
',
@input_data_1 = N'SELECT DISTINCT City,StateProvinceCode
  FROM [AdventureWorksDW2017].[dbo].[DimGeography]
  ORDER BY City;'
  WITH RESULT SETS (([City] nvarchar(100), [State Province Code] nvarchar(50)));