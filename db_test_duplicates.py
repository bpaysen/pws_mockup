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
    return render_template('index.html')


@app.route('/success', methods = ['POST', 'GET'])
def success():
    if request.method=='POST':
     name = request.form['name']
     visits = 1
     try:
  
      with connection.cursor() as cursor:
      # modify  records
        
        sql = "INSERT INTO user_duplicates (username, visits) VALUES (%s, %s) ON DUPLICATE KEY UPDATE visits = visits + 1"
        cursor.execute(sql, (name,visits))
        connection.commit()

        cursor.execute("SELECT visits FROM user_duplicates WHERE username = %s", (name))
        results = cursor.fetchall()
        for row in results:
            for i in row:
                number_to_website = row[i]
                time_statement = ""
                if number_to_website == 1:
                    time_statement = " time."
                else:
                    time_statement = " times."

        connection.commit()

     finally:
      connection.close()
      return render_template('success.html', name=name, visits=number_to_website, time_statement=time_statement)
    else:
      return "error"

def reroute_to_index():
    if request.method=='GET':
        return redirect('index.html')

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response

       

if __name__ == "__main__":
    app.run(debug=True)

