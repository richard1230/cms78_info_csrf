from flask import  Blueprint

bp = Blueprint("front",__name__)#url_prefix='cms'表示一个前缀,这里不需要

@bp.route('/')
def index():
    return 'front index'

