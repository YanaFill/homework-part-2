CREATE DATABASE Airportdb
GO

USE Airportdb

CREATE TABLE Flights (
	flight_id INT PRIMARY KEY,
	flight_number NVARCHAR(10),
	departure_time DATETIME,
	arrival_time DATETIME,
	origin NVARCHAR(50),
	destination NVARCHAR(50),
	airline NVARCHAR(50)
);
GO

INSERT INTO Flights (flight_id, flight_number, departure_time, arrival_time, origin, destination, airline)
VALUES
(1, 'TK808', '2024-09-01 09:00:00', '2024-09-01 11:00:00', 'Ivano-Frankivsk', 'Istanbul', 'Turkish Airlines'),
(2, 'UA202', '2024-09-02 09:30:00', '2024-09-02 13:00:00', 'Kyiv', 'Prague', 'United Airlines'),
(3, 'LH303', '2024-09-03 10:15:00', '2024-09-03 12:45:00', 'Lviv', 'Munich', 'Lufthansa'),
(4, 'BA404', '2024-09-04 11:45:00', '2024-09-04 14:15:00', 'Odesa', 'London', 'British Airways'),
(5, 'AF505', '2024-09-05 13:00:00', '2024-09-05 15:30:00', 'Kharkiv', 'Paris', 'Air France'),
(6, 'SU606', '2024-09-06 14:30:00', '2024-09-06 18:00:00', 'Dnipro', 'Rome', 'Alitalia'),
(7, 'FR707', '2024-09-07 15:45:00', '2024-09-07 17:45:00', 'Zaporizhzhia', 'Warsaw', 'Ryanair'),


CREATE TABLE Passengers (
    passenger_id INT PRIMARY KEY,
    first_name NVARCHAR(50) NOT NULL,
    last_name NVARCHAR(50) NOT NULL,
    passport_number NVARCHAR(20) NOT NULL,
    nationality NVARCHAR(50) NOT NULL
);
GO

INSERT INTO Passengers (passenger_id, first_name, last_name, passport_number, nationality)
VALUES
(1, 'Ivan', 'Shevchenko', 'UA123456', 'Ukraine'),
(2, 'Maria', 'Garcia', 'ES789012', 'Spain'),
(3, 'Liam', 'Connor', 'IE345678', 'Ireland'),
(4, 'Yuki', 'Tanaka', 'JP901234', 'Japan'),
(5, 'Olivia', 'Brown', 'US567890', 'USA');
GO


CREATE TABLE Tickets (
    ticket_id INT PRIMARY KEY,
    flight_id INT NOT NULL,
    ticket_class NVARCHAR(20) NOT NULL,
    price MONEY NOT NULL,
    passenger_id INT,
    FOREIGN KEY (flight_id) REFERENCES Flights(flight_id),
    FOREIGN KEY (passenger_id) REFERENCES Passengers(passenger_id)
);
GO

INSERT INTO Tickets (ticket_id, flight_id, ticket_class, price, passenger_id)
VALUES
(1, 1, 'Economy', 150.00, 1),
(2, 2, 'Business', 450.00, 2),
(3, 2, 'First Class', 750.00, 3),
(4, 3, 'Economy', 120.00, 4),
(5, 3, 'Economy', 200.00, 5),
(6, 4, 'Business', 500.00, 2),
(7, 5, 'Economy', 180.00, 1),
(8, 6, 'First Class', 800.00, 2),
(9, 6, 'Economy', 170.00, 3),
(10, 7, 'Business', 470.00, 4);
GO


CREATE TABLE Ticket_Log (
    log_id INT PRIMARY KEY IDENTITY(1, 1),
    ticket_id INT,
    flight_id INT,
    passenger_id INT,
    purchase_time DATETIME DEFAULT GETDATE()
);


CREATE VIEW View_Flights_Duration AS
SELECT flight_id, flight_number, origin, destination,
    departure_time, arrival_time,
    DATEDIFF(HOUR, departure_time, arrival_time) AS duration_hours
FROM Flights


CREATE VIEW View_Today_Flights AS
SELECT *
FROM Flights
WHERE CONVERT(DATE, departure_time) = CONVERT(DATE, GETDATE())


CREATE TRIGGER trg_AfterInsertTicket
ON Tickets
AFTER INSERT
AS
BEGIN
    INSERT INTO Ticket_Log (ticket_id, flight_id, passenger_id)
    SELECT ticket_id, flight_id, passenger_id
    FROM inserted
END;
