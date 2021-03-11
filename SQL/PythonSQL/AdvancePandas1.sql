EXEC sp_execute_external_script
@language = N'Python', --comments here follow SQL Syntax
@script = N'
print("The Shape of the Dataframe is:" + str(InputDataSet.shape))
print("The number of elements is:" + str(InputDataSet.size))
OutputDataSet = InputDataSet.head()
',
@input_data_1 = N'SELECT DISTINCT City,StateProvinceCode
  FROM [AdventureWorksDW2017].[dbo].[DimGeography]
  WHERE GeographyKey < 20
  ORDER BY City;'
WITH RESULT SETS (([City] nvarchar(100), [State Province Code] nvarchar(50)));