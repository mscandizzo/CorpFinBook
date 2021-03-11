USE PyCorFin3
GO

CREATE TABLE FormatPrices
(
    Title_id int NOT NULL,
    Title varchar(100) NOT NULL,
    Format_id int PRIMARY KEY NOT NULL,
    Prices decimal(6,2) NOT NULL
);
INSERT INTO FormatPrices
VALUES
    (1, 'Beginning MySQL Database Design and Optimization', 1, 'Hardcover', 49.99),
    (2, 'Python For Finance', 3, 'Hardcover', 50.00),
    (3, 'Python for Data Analysis', 5, 'Hardcover', 36.00),
    (1, 'Beginning MySQL Database Design and Optimization', 2, 'E-book', 22.34),
    (4, 'The Relational Model for Database Management: Version 2', 7, 'E-book', 13.88),
    (4, 'The Relational Model for Database Management: Version 2', 8, 'Paperback', 39.99),
    (2, 'Python For Finance', 4, 'E-book', 50.00),
    (3, 'Python for Data Analysis', 6, 'E-book', 36.00);