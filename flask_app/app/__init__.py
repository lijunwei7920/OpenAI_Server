# flask_app/__init__.py

from flask import Flask

from .auth import auth_bp
from .db import init_db
from .routes import routes_bp  # 导入 routes_bp 蓝图

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')  # 加载配置

    init_db()  # 初始化数据库

    # 注册蓝图
    app.register_blueprint(auth_bp)
    app.register_blueprint(routes_bp)  # 注册 routes_bp 蓝图

    return app
