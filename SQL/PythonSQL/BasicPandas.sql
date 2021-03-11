EXEC sp_execute_external_script
@language = N'Python',
@script = N'
print(InputDataSet.iloc[5:15])
',
@input_data_1 = N'SELECT DISTINCT City,StateProvinceCode
  FROM [AdventureWorksDW2017].[dbo].[DimGeography]
  ORDER BY City;'
 