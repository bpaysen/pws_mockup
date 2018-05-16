from flask import Flask, render_template, request, jsonify, redirect, url_for, make_response, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

 
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