from flask import Flask
from apps.cms import bp as cms_bp
from apps.front import bp as front_bp
from apps.common import bp as common_bp
import config
from exts import db
from flask_wtf import CSRFProtect




def create_app():
    app = Flask(__name__)
    app.register_blueprint(cms_bp)
    app.register_blueprint(front_bp)
    app.register_blueprint(common_bp)
    app.config.from_object(config)

    db.init_app(app)
    CSRFProtect(app)

    return app



#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'


if __name__ == '__main__':
    app= create_app()
    app.run()


"""
程序流程:
(my_env) $python3 manage.py create_cms_user -u admin -p 111111 -e richard@163.com
cms用户添加成功
(my_env) $

而后直接运行此程序
"""