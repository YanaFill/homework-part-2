SELECT * FROM Products

SELECT * FROM Products
WHERE Type = 'Vegetable' AND Calories < 40

SELECT * FROM Products
WHERE Type = 'Fruit' AND Calories >= 10 AND Calories <= 50

SELECT * FROM Products
WHERE Type = 'Vegetable' AND Name LIKE '%root%'

SELECT * FROM Products
WHERE Description LIKE '%salad%'

SELECT * FROM Products
WHERE Color = 'Green' OR Color = 'Red'