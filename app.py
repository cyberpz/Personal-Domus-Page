from flask import Flask, abort, redirect, url_for, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/")
def index():
	return "Pz"


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))


@app.route('/tracks')
def soundcloud():
	return redirect(url_for('https://soundcloud.com/peppuz/tracks'))

@app.route('/fb')
def facebook():
	return redirect(url_for('https://facebook.com/p3ppu'))
