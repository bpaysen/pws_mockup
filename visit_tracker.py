from flask import Flask, render_template, request, jsonify, redirect, url_for, make_response, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:temporarypassword@localhost/testDB'
# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username

# @app.route('/')
# def index():
# 	return render_template('index.html')
 
@app.route('/', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		user = request.form['name']
		return redirect(url_for('success', name=user))
	else:
		return render_template('q')

	# name = request.form.get('name', 0)
	# data = {'name': name}
	# data = jsonify(data)
	# return data
@app.route('/success', methods = ['POST', 'GET'])
def success():
	user = request.form.get('name')
	return render_template('success.html', name=user)

# def visits():
# 	if 'visits' in session:
# 		session['visits'] = session.get('visits') + 1  # reading and updating session data
# 	else:
# 		session['visits'] = 1 # setting session data
# 	# return "Total visits: {}".format(session.get('visits'))


@app.after_request
def add_headers(response):
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	return response

if __name__ == '__main__':
	app.run(debug=True)