from flask import render_template, redirect
from forms import Addprofession, Adduniversity, SignUp, Login
from extensions import app, db
from flask_login import login_user, logout_user, login_required, current_user
import os
from models import Profession, University, User

@app.route("/")
def opening():
    return render_template("opening.html")


@app.route("/home")
def home():
    return render_template("homepage.html", professions = Profession.query.all(), universities = University.query.all())


@app.route("/signup", methods=['POST', 'GET'])
def signup():
    form = SignUp()
    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect("/home")
    
    return render_template("signup.html", form=form)



@app.route("/login", methods=['POST', 'GET'])
def login():
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user) 
            return redirect("/home")
    return render_template("login.html", form=form)




@app.route("/logout", methods =['POST', 'GET'])
def logout():
    logout_user()
    return redirect("/home")



@app.route("/search/<string:profession_name>")
def search(profession_name):
    professions = Profession.query.filter(Profession.name.ilike(f"%{profession_name}%")).all()
    return render_template("homepage.html", professions = professions)



@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/compsci")
def compsci():
    return render_template("compsci.html")

@app.route("/medicine")
def medicine():
    return render_template("medicine.html")

@app.route("/teaching")
def teaching():
    return render_template("teaching.html")

@app.route("/all_professions")
def all_professions():
    return render_template("all_professions.html")

@app.route("/all_universities")
def all_universities():
    return render_template("all_universities.html")



@app.route("/add_profession", methods = ['POST', 'GET'])
@login_required
def add_profession():
    if current_user.role != "admin":
        return redirect("/home")
    form = Addprofession()

    if form.validate_on_submit():
        #image = form.image.data
        #file_path = os.path.join("static", "images", image.filename)
        new_profession = Profession(name=form.name.data, text=form.text.data, image_url=form.image_url.data)
        
        db.session.add(new_profession)
        db.session.commit()

        #image.save((os.path.join(app.root_path, file_path)))

    else:
        print(form.errors)

    return render_template("add_profession.html", form = form)


@app.route("/add_university", methods = ['POST', 'GET'])
@login_required
def add_university():
    form = Adduniversity()

    if form.validate_on_submit():
        #image = form.image.data
        #file_path = os.path.join("static", "images", image.filename)
        new_university = University(name=form.name.data, text=form.text.data, image_url=form.image_url.data)
        
        db.session.add(new_university)
        db.session.commit()
        
        #image.save((os.path.join(app.root_path, file_path)))

    else:
        print(form.errors)

    return render_template("add_university.html", form = form)



#პროფესიის შეცვლის ოპერაცია
@app.route("/edit_profession/<int:profession_id>", methods=['POST', 'GET'])
def edit_profession(profession_id):
    profession = Profession.query.get(profession_id)
    if not profession: 
        return render_template("404.html")
    

    form = Addprofession(name=profession.name, text=profession.text, image_url=profession.image_url)


    if form.validate_on_submit():
        profession.name = form.name.data
        profession.text = form.text.data
        profession.image_url = form.image_url.data


        db.session.commit()
        return redirect("/home")

    return render_template("edit_profession.html", form= form)    


#პროფესიის წაშლის ოპერაცია
@app.route("/delete_profession/<int:profession_id>", methods=['GET', 'DELETE'])
def delete_profession(profession_id):
    profession  = Profession.query.get(profession_id)
    if not profession:
        return render_template("404.html")
    
    db.session.delete(profession)
    db.session.commit()
    

    return redirect("/home")





#უნივერსიტეტის შეცვლის ოპერაცია
@app.route("/edit_university/<int:university_id>", methods=['POST', 'GET'])
def edit_university(university_id):
    university = University.query.get(university_id)
    if not university: 
        return render_template("404.html")
    

    form = Adduniversity(name=university.name, text=university.text, image_url=university.image_url)


    if form.validate_on_submit():
        university.name = form.name.data
        university.text = form.text.data
        university.image_url = form.image_url.data


        db.session.commit()
        return redirect("/home")

    return render_template("edit_university.html", form= form)  




#უნივერსიტეტის წაშლის ოპერაცია
@app.route("/delete_university/<int:university_id>", methods=['GET', 'DELETE'])
def delete_university(university_id):
    university  = University.query.get(university_id)
    if not university:
        return render_template("404.html")
    
    db.session.delete(university)
    db.session.commit()
    

    return redirect("/home")
