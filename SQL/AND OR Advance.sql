SELECT [FirstName],LastName,[Title]
FROM [AdventureWorksDW2017].[dbo].[DimEmployee]
WHERE 
FirstName = 'David' 
AND
(Title = 'Marketing Manager' OR Title = 'Sales Representative');