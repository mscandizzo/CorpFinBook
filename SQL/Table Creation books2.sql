USE PyCorFin3
GO

CREATE TABLE Books2
    ( Title_id int PRIMARY KEY,
    Title varchar(30) NOT NULL,
    Author varchar(20) NOT NULL,
    Author_Nationality varchar(30) NULL,
    Pages int NULL,
    Thickness int NULL,
    Genre_id int NULL,
    Genre_name varchar(30) NULL,
    Publisher_id int NOT NULL);

CREATE TABLE FormatPrices
(   Title_id int ,
    Title varchar(30) NOT NULL,
    Format_id int, 
    Formats varchar(20) NOT NULL,
    Price decimal(6,2)
    PRIMARY KEY (Title_id,Format_id));

