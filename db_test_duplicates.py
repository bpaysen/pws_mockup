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
     name = request.form['name']
     visits = 0
     try:
  

      with connection.cursor() as cursor:
      # modify a record
        sql = "INSERT INTO user_duplicates (username, visits) VALUES (%s, %s) ON DUPLICATE KEY UPDATE visits = visits + 1"
        # evidence = "SELECT * FROM user_duplicates"
        cursor.execute(sql, (name,visits))
        connection.commit()
        # print(evidence)
        # print(userduplicates)
     finally:
      connection.close()
      return render_template('success.html', name=name)
    else:
      return "error"
       

if __name__ == "__main__":
    app.run(debug=True)
