from flask import Flask, render_template,request,json
import pymysql.cursors
# from pathlib import Path
import databaseconfig as c

# Create a file named databaseconfig with db variables
# Connect to the database
connection = c.connection

app = Flask(__name__)

# Landing page where user enters name
@app.route("/")
def home():
    return render_template('index.html')

# Success page greets user, states visit count
@app.route('/success', methods = ['POST', 'GET'])
def success():
    if request.method=='POST':
        name = request.form['name']
        print(">>>>>>>>>>>>>>>" + "Hello Try")
        # print(connection.cursor())        
        try:
            print("Hi Visitor")
            with connection.cursor() as cursor:
            # modify  records
                cursor.execute("SELECT visits FROM user_duplicates WHERE username = %s", (name))
                query_result = cursor.fetchall()
                # query_result represents row of table 
                print("Querying...")
                name_var = name
                connection.commit()

                # if no record: insert and print
                if len(query_result) == 0:
                    print("No results, visits = ")
                    sql = "INSERT INTO user_duplicates (username, visits) VALUES (%s, 1) " 
                    cursor.execute(sql, (name))
                    # inserts new record of name entered in form
                    connection.commit()
                    number_to_website = 1
                    time_var = "time"
                    print(number_to_website)
                # if name exists: update and print
                elif len(query_result) >= 1:
                    print("Results > 1, visits = ")
                    exists = "UPDATE user_duplicates SET visits = visits + 1 WHERE username = %s"
                    cursor.execute(exists, (name))
                    # increments the visits column only
                    connection.commit()
                    for row in query_result:
                        for i in row:
                            number_to_website = row[i] + 1
                            time_var = "times"
                            print(number_to_website)
                            '''Would be more ideal to get number_to_website from a query'''
                else:
                    print("error: no operation executed")

        finally:
            # cursor.close()
            pass
            # keeping connection open
        return render_template('success.html', name=name, visits=number_to_website, time_var=time_var)


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

