CREATE TABLE Products
(
	Name nvarchar(50) NOT NULL,
	Type nvarchar(50) NOT NULL,
	Color nvarchar(50) NOT NULL,
	Calories int NOT NULL,
	Description nvarchar(90)
)

INSERT INTO Products(Name, Type, Color, Calories, Description)
VALUES 
('Tangerine', 'fruit', 'orange', 53, 'it is a fruit that people are eating in winter'),
('Lemon', 'fruit', 'yellow', 29, 'a sour fruit that is added to tea'),
('Cucumber', 'vegetable', 'green', 15, 'the best vegetable for salad'),
('Tomato', 'vegetable', 'red', 18, 'vegetable that i hate so much')

SELECT * FROM Products