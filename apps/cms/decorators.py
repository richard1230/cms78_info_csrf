from flask import session,redirect,url_for
from functools import wraps
import config
def login_required(func):

    @wraps(func)
    def inner(*args,**kwargs):
        if config.CMS_USER_ID in session:
            return func(*args,**kwargs)
        else:
            return redirect(url_for('cms.login'))

    return inner


"""

装饰器的一些说明:
@login_required
def index():
    return 'cms index'

上面三行等价于:
index = login_required(index)  <===>  而login_required函数的返回值为inner这个函数   <===>inner这个函数
联系views这个模块

"""
