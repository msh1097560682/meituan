# -*- coding: utf-8 -*- 
# @Time : 2019/6/24 15:07


from apps import app
from views import app_user

APP_CONFIG={
    'host': '0.0.0.0',
    'port': 9001,
    'debug': True
}

if __name__ == '__main__':
    app.register_blueprint(app_user.blue)
    app.run(**APP_CONFIG)