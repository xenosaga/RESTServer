from flask import Blueprint

main = Blueprint('main', __name__)

# 避免循環依賴
from . import views, errors
