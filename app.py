
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()
admin = Admin()

#models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    posts = db.relationship("Post", back_populates="user")

    def __str__(self):
        return self.name


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text)
    user_id = db.Column(db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", back_populates="posts")


class PostView(ModelView):
    can_delete = False
    form_columns = ["title", "body", "user"] #fields to display , create
    column_list = ["title", "body", "user"]  # display list

admin.add_view(ModelView(User, db.session))
admin.add_view(PostView(Post, db.session))

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db1.sqlite3" # db1 is the name of the db 
    app.config["SECRET_KEY"] = "mysecret"

    db.init_app(app)
    admin.init_app(app)

    return app

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_admin import Admin
# from flask_admin.contrib.sqla import ModelView

# db = SQLAlchemy()
# admin = Admin()

# #model
# class User(db.Model):
#     id=db.Column(db.Integer, primary_key=True)
#     name=db.Column(db.String(100))
#     posts=db.relationship("Post", back_populates="user")

#     def __str__(self):
#         return self.name

# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100))   
#     body = db.Column(db.Text)
#     user_id = db.Column(db.ForeignKey("user.id"),nullable=False)   
#     user = db.relationship("User", back_populates="posts")

# class PostView(ModelView): #inherits from MOdelView
#     can_delete= False 
#     form_columns =["title","body","user"]  #fields to display , create
#     column_list = ["title","body","user"] # display list 

# admin.add_view(ModelView(User, db.session))
# admin.add_view(PostView(Post, db.session))



# def create_app():
#     app=Flask(__name__)
#     app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///db.sqlite3"
#     app.config['SECRET_KEY']='mysecretkey'

#     db.init_app(app)
#     admin.init_app(app)

#     return app
