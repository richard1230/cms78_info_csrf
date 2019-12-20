
from exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash


class CMSUser(db.Model):
    __tablename__='cms_user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(50),nullable=False)
    _password = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(50),nullable=False,unique=True)
    join_time =db.Column(db.DateTime,default=datetime.now)
    """
    想要映射到数据库里面必须添加到manage.py里面
  
    """


    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email

    @property
    def password(self):
        return self._password


    @password.setter
    def password(self,raw_password):
        self._password= generate_password_hash(raw_password)

    def check_password(self,raw_password):
        result = check_password_hash(self.password,raw_password)
        #这里也可以写为self._password(代表的是password方法下面的返回值)，其实这里的self.password指的就是这个password方法
        return result



#
# user = CMSUser()
# print(user.password)



# 密码：对外的字段名叫做password
# 密码：对内的字段名叫做_password

