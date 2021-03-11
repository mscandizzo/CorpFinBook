USE PyCorFin
GO

SELECT B.Title, S.Subject_name
FROM Book AS B INNER JOIN Title_Subject AS T
ON B.Title_id = T.Title_id
INNER JOIN Subject as S
ON S.Subject_id = T.Subject_id
WHERE B.Title = 'Python For Finance'

