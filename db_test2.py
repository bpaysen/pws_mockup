from flask import Flask, render_template,request,json
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='Julian',
                             db='UserTest_db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
app = Flask(__name__)




@app.route("/get-reg")
def login():
    print("hello logs")
    return render_template('index.html')

@app.route('/success', methods = ['POST', 'GET'])
def success():
    print("hello world")
    if request.method=='POST':
     name=request.form['name']
     email=request.form['email']
     try:
  

      with connection.cursor() as cursor:
      # Read a single record
        sql = "INSERT INTO userdata (username,email) VALUES (%s, %s)"
        cursor.execute(sql, (name,email))
        userdata = "SELECT * FROM userdata"
        connection.commit()
        # print(userdata)
     finally:
      connection.close()
      return render_template('success.html', name=name, email=email)
    else:
      return "error"
       
# @app.route('/success', methods = ['POST', 'GET'])
# def success():
#   print("hello success")
#   user = request.form.get('name')
#   e_adr = request.form.get('email')
#   return render_template('success.html', name=user, email=e_adr)

if __name__ == "__main__":
    app.run(debug=True)