class Article:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"**Назва:** {self.title}\n**Автор:** {self.author}\n**Рік:** {self.year}"

    @staticmethod
    def create():
        title = input("Введіть назву статті: ")
        author = input("Введіть автора статті: ")
        year = int(input("Введіть рік публікації: "))
        return Article(title, author, year)

    def read(self):
        print(self)

    def update(self):
        new_title = input("Введіть нову назву статті (або натисніть Enter, щоб пропустити): ")
        new_author = input("Введіть нового автора статті (або натисніть Enter, щоб пропустити): ")
        new_year = input("Введіть новий рік публікації (або натисніть Enter, щоб пропустити): ")

        if new_title:
            self.title = new_title
        if new_author:
            self.author = new_author
        if new_year:
            self.year = int(new_year)

    def delete(self):
        confirmation = input("Ви впевнені, що хочете видалити цю статтю? (y/n): ")
        if confirmation.lower() == "y":
            print("Стаття видалена.")
            return None
        else:
            print("Видалення статті скасовано.")
            return self
