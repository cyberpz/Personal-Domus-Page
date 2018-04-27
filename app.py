from flask import Flask, abort, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

# ROUTES
@app.route("/")
def index():
	return render_template('index.html')

@app.route("/spendTheCash")
def pricing():
	pass
	# return render_template('pricing.html')

# REDIRECTS
@app.route("/twitter")
def twitter():
	return redirect('https://twitter.com/zuppep')

@app.route("/tracks")
def soundcloud():
	return redirect(url_for('https://soundcloud.com/peppuz/tracks'))

@app.route("/fb")
def facebook():
	return redirect('https://facebook.com/p3ppu')

@app.route("/2stoned")
def youtube2():
	return redirect('https://ddg.gg')
