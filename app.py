from flask import Flask, render_template,request, redirect, flash , session
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from datetime import datetime
import os
from datetime import datetime

from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "radhavallabh_secret"

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# DATABASE CONFIG
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///temple_new.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# EMAIL CONFIG
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'yourgmail@gmail.com'
app.config['MAIL_PASSWORD'] = 'your-app-password'

mail = Mail(app)

# DATABASE MODEL
class Prayer(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(100)
    )
    city = db.Column(
        db.String(100)
    )
    prayer = db.Column(
        db.Text
    )
    created_at = db.Column(
        db.DateTime,
        default=datetime.now
    )

# admin event table
class Event(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    title = db.Column(
        db.String(200)
    )
    description = db.Column(
        db.Text
    )
    date = db.Column(
        db.String(100)
    )
    image = db.Column(
        db.String(300)
    )

class Darshan(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    quote = db.Column(
        db.Text
    )

    image = db.Column(
        db.String(300)
    )
    created_at= db.Column(
        db.DateTime,
        default=datetime.now
    )

from datetime import datetime

class GalleryImage(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    title = db.Column(
        db.String(200)
    )
    description = db.Column(
        db.Text
    )
    image = db.Column(
        db.String(300)
    )
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


class Book(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    title = db.Column(
        db.String(200)
    )
    pdf_link = db.Column(
        db.String(500)
    )
    image= db.Column(
        db.String(300)
    )
    description = db.Column(
        db.Text
    )
    


# HOME ROUTE
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password == "1234":
            session["admin"] = True
            return redirect("/admin")
    return render_template(
        "admin/login.html"
    )


# SAVE PRAYER
@app.route("/submit-prayer",
methods=["POST"])
def submit_prayer():

    # GET FORM DATA
    name = request.form["name"]
    city = request.form["city"]
    prayer_text = request.form["prayer"]

    # CREATE NEW PRAYER OBJECT
    new_prayer = Prayer(
        name=name,
        city=city,
        prayer=prayer_text
    )
    # SAVE TO DATABASE
    db.session.add(new_prayer)
    db.session.commit()

    # SUCCESS MESSAGe
    flash("🙏 Your prayer has been received 🌸")
    # REDIRECT BACK
    return render_template("contact.html")


# ADMIN PAGE
@app.route("/admin")
def admin():
    if "admin" not in session:
        return redirect("/login")

    prayers = Prayer.query.all()
    prayer_count=Prayer.query.count()
    event_count=Event.query.count()
    gallery_count=GalleryImage.query.count()
    book_count=Book.query.count()
    

    return render_template(
        "admin/dashboard.html",
        prayers=prayers,
        prayer_count=prayer_count,
        event_count=event_count,
        gallery_count=gallery_count,
        book_count=book_count
    )


@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/darshan")
def darshan():
    darshan = Darshan.query.order_by(
    Darshan.id.desc()
).first()
    return render_template(
        "darshan.html",
        darshan=darshan
    )


@app.route("/events")
def events():
    events = Event.query.order_by(
        Event.id.desc()
    ).all()
    return render_template(
        "events.html",
        events=events
    )

# user gallery route
@app.route("/gallery")
def gallery():
    images = GalleryImage.query.order_by(
        GalleryImage.id.desc()
    ).all()
    for img in images:
        print(img.image)

    return render_template(
        "gallery.html",
        images=images
    )

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/calendar")
def calendar():
    return render_template("calendar.html")

@app.route("/book")
def books():
    books = Book.query.all()
    return render_template(
        "book.html",
        books=books
    )

@app.route("/virtual-darshan")
def virtual_tour():
    return render_template("virtual-darshan.html")


# for admin panel

@app.route("/prayers")
def prayers():
    if "admin" not in session:
        return redirect("/login")
    all_prayers = Prayer.query.all()

    return render_template(
        "admin/prayers.html",
        prayers=all_prayers
    )

# GALLERY ADMIN
@app.route(
    "/gallery-admin",
    methods=["GET","POST"]
)
def gallery_admin():

    if request.method == "POST":

        title = request.form["title"]

        images = request.files.getlist(
            "images"
        )

        for image in images:

            if image.filename != "":
                filename = secure_filename(
                    image.filename
                )
                image.save(
                    os.path.join(
                        "static/uploads/gallery",
                        filename
                    )
                )
                new_image = GalleryImage(
                    title=title,
                    image=filename
                )

                db.session.add(
                    new_image
                )
        db.session.commit()
        return redirect(
            "/gallery-admin"
        )

    gallery = GalleryImage.query.order_by(
        GalleryImage.id.desc()
    ).all()

    return render_template(
        "admin/gallery.html",
        gallery=gallery
    )

# delete image
@app.route(
    "/delete-gallery/<int:id>"
)
def delete_gallery(id):

    image = GalleryImage.query.get(id)

    if image:

        db.session.delete(image)

        db.session.commit()

    return redirect(
        "/gallery-admin"
    )


# ADD BOOKS ADMIN
from werkzeug.utils import secure_filename
import os

@app.route("/add-book", methods=["POST"])
def add_book():

    image = request.files["image"]

    filename = secure_filename(
        image.filename
    )
    image.save(
        os.path.join(
            "static/uploads/books",
            filename
        )
    )
    new_book = Book(
        title=request.form["title"],
        image=filename,
        pdf_link=request.form["pdf_link"],
        description=request.form["description"]
    )

    db.session.add(new_book)
    db.session.commit()

    return redirect("/books-admin")

# delete book
@app.route("/delete-book/<int:id>")
def delete_book(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect("/books-admin")


# book admin route
@app.route("/books-admin")
def books_admin():
    books = Book.query.all()
    return render_template(
        "admin/books.html",
        books=books
    )


# EVENTS ADMIN
@app.route( "/events-admin",
    methods=["GET","POST"]
)
def events_admin():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        date = request.form["date"]
        image = request.files["image"]
        filename = secure_filename(
            image.filename
        )
        image.save(
            os.path.join(
                app.config["UPLOAD_FOLDER"],
                filename
            )
        )
        new_event = Event(
            title=title,
            description=description,
            date=date,
            image=filename
        )
        db.session.add(new_event)
        db.session.commit()
    events = Event.query.all()
    return render_template(
        "admin/events.html",
        events=events
    )


# DARSHAN ADMIN
@app.route("/darshan-admin",methods=["GET", "POST"])
def darshan_admin():
    if request.method == "POST":
        quote = request.form["quote"]
        image = request.files["image"]
        filename = secure_filename(
            image.filename
        )
        image.save(
            os.path.join(
                "static/uploads/darshan",
                filename
            )
        )
        latest_darshan = Darshan.query.order_by(
           Darshan.id.desc()
        ).first()

        history = Darshan.query.order_by(
           Darshan.id.desc()
        ).all()
        new_darshan = Darshan(
            quote=quote,
            image=filename
        )
        db.session.add(new_darshan)
        db.session.commit()
    darshan = Darshan.query.order_by(
    Darshan.id.desc()
).first()
    return render_template(
        "admin/darshan.html",
        darshan=darshan
    )
# temporary route to count total no of darshan
@app.route("/check-darshan")
def check_darshan():
    all_darshan = Darshan.query.all()
    return str(len(all_darshan))


@app.route(
    "/delete-darshan/<int:id>"
)
def delete_darshan(id):
    darshan = Darshan.query.get(id)
    if darshan:
        db.session.delete(darshan)
        db.session.commit()
    return redirect(
        "/darshan-admin"
    )


# LOGOUT
@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect("/login")

# CREATE DATABASE
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True  , port=5002)