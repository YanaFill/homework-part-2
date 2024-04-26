import json, pickle


class Author:
    def __init__(self, name, gender, nationaly):
        self.name = name
        self.gender = gender
        self.nationaly = nationaly

    def __str__(self):
        return f"{self.name} ({self.gender}) - {self.nationaly}"


class Book:
    def __init__(self, title, year, authors: list) -> None:
        self.title = title
        self.year = year
        self.authors = authors

    def __str__(self):
        return f"Title: {self.title}\nYear: {self.year}\nAuthors: {''.join([str(author) for author in self.authors])}"

    def to_dict(self):
        return {
            "title": self.title,
            "year": self.year,
            "authors":  [
        {
            "name": author1.name,
            "gender": author1.gender,
            "nationality": author1.nationaly
        },
        {
            "name": author2.name,
            "gender": author2.gender,
            "nationality": author2.nationaly
        }
            ]

        }

    def save_to_json(self, filename):
        with open(filename, "w") as f:
            json.dump(self.to_dict(), f, indent=4)

    @staticmethod
    def load_from_json(filename):
        with open(filename, "r") as file:
            data = json.load(file)
            new_title = data["title"]
            new_year = data["year"]
            new_authors = [Author(author['name'], author["gender"], author["nationality"]) for author in
                           data["authors"]]
            return Book(new_title, new_year, new_authors)


    def serialize(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    def deserialize(self, filename):
        with open(filename, "rb") as file:
            data = pickle.load(file)
        return data


author1 = Author("J.K. Rowling", "Female", "British")
author2 = Author("Stephen King", "Male", "American")
a = Book("Harry Potter", 1997, [author1, author2])
a.save_to_json("book.json")
b = Book.load_from_json("book.json")
print(b)

print()
data = a.serialize("book1.json")
data1 = b.deserialize("book1.json")
print(data1)

