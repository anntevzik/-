from extensions import db, app, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Profession(db.Model):
    __tablename__ = "professions"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image_url = db.Column(db.String)
    text = db.Column(db.String)


class University(db.Model):
    __tablename__ = "universities"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image_url = db.Column(db.String)
    text = db.Column(db.String)


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    role = db.Column(db.String, default = "user")

    def __init__(self,password,username,email,role="user"):
        self.password = generate_password_hash(password)
        self.username = username
        self.email = email
        self.role = role

    def check_password(self, password):
        return check_password_hash(self.password, password)


if __name__ =="__main__":
    with app.app_context():
        db.create_all()
        print("db was created")
        admin= User(email = "admin@gmail.com", password = "admin123", username = "admin", role = "admin")
        db.session.add(admin)
        db.session.commit()





@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)