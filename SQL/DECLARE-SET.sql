USE AdventureWorksDW2017
DECLARE @nombre VARCHAR(100)
SET @nombre = 'David'

SELECT TOP(10) FirstName, EmployeeKey, ParentEmployeeKey
FROM DimEmployee 
WHERE FirstName <> @nombre
ORDER BY FirstName
