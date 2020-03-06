from flask import *

app = Flask(__name__)


@app.route('/')
def index():
	return render_template("home.html")

@app.route('/gallery')
def gallery():
	return render_template("gallery.html")


@app.route('/gallery-single')
def gallery_single():
	return render_template("gallery-single.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/contact')
def contact():
	return render_template("contact.html")

if '__main__' == __name__:
	app.run()