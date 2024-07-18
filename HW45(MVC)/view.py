class ArticleView:
    def __init__(self, controller):
        self.controller = controller

    def display_menu(self):
        print("\nМеню:")
        print("1. Створити статтю")
        print("2. Переглянути статтю")
        print("3. Оновити статтю")
        print("4. Видалити статтю")
        print("5. Вийти")

    def get_user_choice(self):
        while True:
            choice = input("Введіть свій вибір: ")
            if choice.isdigit() and 1 <= int(choice) <= 5:
                return int(choice)
            else:
                print("Неправильний вибір. Спробуйте ще раз.")

    def start(self):
        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == 1:
                self.controller.create_article()
            elif choice == 2:
                self.controller.read_article()
            elif choice == 3:
                self.controller.update_article()
            elif choice == 4:
                self.controller.delete_article()
            elif choice == 5:
                break
