README.md

Visit tracker site accepts a name (any varchar) in an input field in the home page (case insensitive). 

POST sends value into a mysql database table and tracks number of visits.
	DB is queried for record of name. If a name does not exist, program inserts new record into the table. If it already exists, it updates the numbers of visits.

The number of visits is sent to the place holder on the second page.

Second page displays your name and how many times you've visited the site.
A button redirects you to the home page for another try.
