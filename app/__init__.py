from flask import Flask, render_template
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_sse import sse
from config import config

mail = Mail()
db = SQLAlchemy()
room_map = {
    "48242894131452": "bbl",
    "79958556256998": "moe"
}
admin_id = ['55555555555']
admin_cmd = ['addtext', 'addimg']

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    mail.init_app(app)
    db.init_app(app)
    # 附加路由和自定义的错误页面
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')
    
    return app
