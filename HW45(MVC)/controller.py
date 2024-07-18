from model import Article

class ArticleController:
    def __init__(self):
        self.article = None

    def create_article(self):
        self.article = Article.create()

    def read_article(self):
        if self.article:
            self.article.read()
        else:
            print("Стаття не створена.")

    def update_article(self):
        if self.article:
            self.article.update()
        else:
            print("Стаття не створена.")

    def delete_article(self):
        if self.article:
            self.article = self.article.delete()
        else:
            print("Стаття не створена.")
