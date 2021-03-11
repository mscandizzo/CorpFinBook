SELECT EmployeeKey,[FirstName],LastName,[Title]
FROM [AdventureWorksDW2017].[dbo].[DimEmployee]
WHERE FirstName LIKE 'a____%';