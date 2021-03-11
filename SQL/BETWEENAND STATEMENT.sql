USE AdventureWorksDW2017

SELECT TOP(10) FirstName, EmployeeKey, ParentEmployeeKey
FROM DimEmployee 
WHERE FirstName <> 'David'
AND
EmployeeKey NOT BETWEEN 100 AND 200
ORDER BY FirstName
