USE PyCorFin3
GO

INSERT INTO Books2
VALUES
(1,'Beginning MySQL Database Design and Optimization','Chad Russell','American',520,'Thick',1,'Tutorial',1),
(2,'Python For Finance','Yves Hipish','German',720,'very Thick',1,'Tutorial',2),
(3,'Python for Data Analysis','Wes McKinney','American',550,'Thick',1,'Tutorial',2),
(4,'The Relational Model for Database Management: Version 2','E.F.Codd','British',538,'Thick',2,'Popular science',2);

INSERT INTO FormatPrices
VALUES
(1,'Beginning MySQL Database Design and Optimization',1,'Hardcover',49.99),	
(2,'Python For Finance',3,'Hardcover',50.00),	
(3,'Python for Data Analysis',5,'Hardcover',36.00),	
(1,'Beginning MySQL Database Design and Optimization',2,'E-book',22.34),	
(4,'The Relational Model for Database Management: Version 2',7,'E-book',13.88),	
(4,'The Relational Model for Database Management: Version 2',8,'Paperback',39.99),	
(2,'Python For Finance',4,'E-book',50.00),	
(3,'Python for Data Analysis',6,'E-book',36.00);