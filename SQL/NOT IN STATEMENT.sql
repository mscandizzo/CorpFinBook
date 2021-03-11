SELECT EmployeeKey,[FirstName],LastName,[Title]
FROM [AdventureWorksDW2017].[dbo].[DimEmployee]
WHERE FirstName NOT IN ('Kevin','Roberto')
AND 
(Title = 'Marketing Assistant' OR Title = 'Engineering Manager');