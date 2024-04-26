from pydantic import BaseModel, ValidationError, Field, field_validator
import json


class Author(BaseModel):
    name: str = Field(min_length=2, max_length=15)
    gender: str
    nationality: str

    @field_validator("gender")
    def validate_gender(cls, value):
        allowed_genders = ["Male", "Female"]
        if value not in allowed_genders:
            raise ValueError("Gender must be 'Male' or 'Female'")
        return value

    def __str__(self):
        return f"{self.name} ({self.gender}) - {self.nationality}"


class Book(BaseModel):
    id: int
    title: str = Field(alias="nameBook")
    year: int = Field(ge=1900, le=2024)
    authors: list[Author]

    def __str__(self):
        authors_str = ", ".join([str(author) for author in self.authors])
        return f"Book: {self.title} ({self.year}) by {authors_str}"


    def save_to_json(self, filename):
        with open(filename, "w") as f:
            json.dump(self.dict(exclude={"id"}), f, indent=4)


    @classmethod
    def load_from_json(cls, filename="book.json"):
        with open(filename, "r") as f:
            data = json.load(f)
            return cls(**data)


try:
    a = Book.load_from_json(filename="book.json")
except ValidationError as e:
    response = e.json()
    print(e)
else:
    a.year = 1998
    print(a)
    a.save_to_json("new_book.json")
