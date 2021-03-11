SELECT EmployeeKey,[FirstName],LastName,[Title]
FROM [AdventureWorksDW2017].[dbo].[DimEmployee]
WHERE 
(FirstName = 'David' 
AND Title = 'Marketing Manager' )
OR 
(FirstName = 'Jillian' 
AND Title = 'Sales Representative' )
;