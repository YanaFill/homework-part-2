from controller import ArticleController
from view import ArticleView

controller = ArticleController()
view = ArticleView(controller)
view.start()
