EXEC sp_execute_external_script
@language = N'Python', --comments here follow SQL Syntax
@script = N'
import matplotlib.pyplot as plt
x = InputDataSet.AccountKey
y = InputDataSet.Amount
plt.scatter(x,y)
plt.xlabel("AccountKey")
plt.ylabel("Amount")
plt.show()
',
@input_data_1 = N'SELECT AccountKey,Amount   
  FROM [AdventureWorksDW2017].[dbo].[FactFinance];'

