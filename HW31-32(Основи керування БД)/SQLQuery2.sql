SELECT * FROM Products 
WHERE Calories < 20 and Type = 'vegetable'

SELECT * FROM Products
WHERE Calories BETWEEN 25 and 30 and Type = 'fruit'

SELECT * FROM Products
WHERE Type = 'vegetable' and Name = 'cucumber'

SELECT * FROM Products
WHERE Description like '%that%'

SELECT * FROM Products
WHERE Color = 'red' or Color = 'yellow'