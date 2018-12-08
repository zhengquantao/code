from flask import Flask
from .views.login import log
from .views.index import ind
from .views.plist import pli
from .views.upload import upl
from .views.logout import logt

def create_app():

    app = Flask(__name__,)
    app.config.from_object('settings.Config')  # 导入配置文件
    app.register_blueprint(log)  # 导入蓝图 注册蓝图
    app.register_blueprint(ind)
    app.register_blueprint(pli)
    app.register_blueprint(upl)
    app.register_blueprint(logt)

    return app