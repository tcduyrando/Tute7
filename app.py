from flask import Flask, render_template
#Only for FLASK
import os

app = Flask(__name__)

#Main page
@app.route('/templates')
def main_page():
	return render_template('random.html')

#Testing to check if it works
@app.route('/test')
def test():
    return "Frontend Testing Works!"
    return "extra line not important"
