-- Створення таблиць
CREATE TABLE Product (
    id INT PRIMARY KEY IDENTITY,
    name NVARCHAR(100),
    type NVARCHAR(50),
    color NVARCHAR(50),
    calories INT,
    description NVARCHAR(255)
);

CREATE TABLE Category (
    id INT PRIMARY KEY IDENTITY,
    name NVARCHAR(100)
);

CREATE TABLE ProductCategory (
    product_id INT,
    category_id INT,
    PRIMARY KEY (product_id, category_id),
    FOREIGN KEY (product_id) REFERENCES Product(id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES Category(id) ON DELETE CASCADE
);

-- Додавання даних
INSERT INTO Product (name, type, color, calories, description)
VALUES 
('Tomato', 'vegetable', 'red', 18, 'it is a fruit that people eat in winter'),
('Tangerine', 'fruit', 'orange', 53, 'Citrus fruit.');

INSERT INTO Category (name) VALUES ('Fresh products'), ('Healthy food');

INSERT INTO ProductCategory (product_id, category_id) VALUES (1, 1), (1, 2), (2, 1);

-- Перевірка зв'язків
SELECT p.name AS ProductName, c.name AS CategoryName
FROM Product p
JOIN ProductCategory pc ON p.id = pc.product_id
JOIN Category c ON c.id = pc.category_id;

-- Видалення продукту
DELETE FROM Product WHERE id = 1;
-- Це автоматично видалить всі записи у таблиці ProductCategory, де product_id = 1.

