import pymysql.cursors

connection = pymysql.connect(host='127.0.0.1',
							user='root',
							password='Julian',
							db='UserTest_db',
							charset='utf8mb4',
							cursorclass=pymysql.cursors.DictCursor)