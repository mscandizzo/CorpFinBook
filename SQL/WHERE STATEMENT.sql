USE AdventureWorksDW2017

SELECT TOP(10) FirstName, EmployeeKey, ParentEmployeeKey
FROM DimEmployee 
WHERE FirstName <> 'David'
ORDER BY FirstName
