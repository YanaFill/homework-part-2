from controller import ArticleController
from view import ArticleView

if __name__ == "__main__":
    controller = ArticleController()
    view = ArticleView(controller)
    view.start()
