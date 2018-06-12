WELCOME to Visit Tracker!

Visit tracker is a python Flask site that accepts a name in an input field on the home page. 

A POST sends the name into a mysql database table and tracks the number of visits.
	Database is queried for record of the name. If a name does not exist, the program inserts a new record into the table. If it already exists, it updates the numbers of visits next to that name. An example of the database is below.

	+-----+------------------+--------+
	| id  | username         | visits |
	+-----+------------------+--------+
	|   1 | Jan              |     64 |
	|   2 | Bob              |     64 |
	|   3 | Grace            |      1 |
	+------------------------+--------+

After submission, the site directs the user to a second page where the message welcomes the visitor and how many times they have visited.

A "Try Again" button redirects the user back to the home page for another submission.


INSTALLATION INSTRUCTIONS

Clone the repository from https://github.com/bpaysen/pws_mockup

Confirm that all view pages are in the templates folder [index.html and success.html]
The db_test_duplicates.py is the main app and the databaseconfig.py is the configuration file.

Visit Tracker is a Flask app that uses Python 3.6.3 and PyMySQL as a database connector to a MySQL database. The connection defined in the config file uses placeholders:

connection = pymysql.connect(host=cfg["host"],
							user=cfg["user"],
							password=cfg["password"],
							db=cfg["db"],
							charset=cfg["charset"],
							cursorclass=pymysql.cursors.DictCursor)

The cursor 'Dictionary' class is hardcoded into the connection therefore only the other keys will need to be defined in a separate hidden file. I use a YAML file that fills in this data. 

Few dependencies are needed:

from flask:
	-Flask
	-render_template
	-request

-pymysql.cursors

-yaml

Your database will need the a primary 'id' key and a unique 'username' key and a 'visits' key that takes an integer:

	+----------+-------------+------+-----+---------+----------------+
	| Field    | Type        | Null | Key | Default | Extra          |
	+----------+-------------+------+-----+---------+----------------+
	| id       | int(2)      | NO   | PRI | NULL    | auto_increment |
	| username | varchar(35) | YES  | UNI | NULL    |                |
	| visits   | int(11)     | YES  |     | NULL    |                |
	+----------+-------------+------+-----+---------+----------------+

