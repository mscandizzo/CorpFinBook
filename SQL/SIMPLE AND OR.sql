SELECT [FirstName],LastName,[Title]
FROM [AdventureWorksDW2017].[dbo].[DimEmployee]
WHERE 
    FirstName = 'David' 
AND LastName = 'Bradley'
OR Title = 'Tool Designer';