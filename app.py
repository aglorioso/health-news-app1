import csv 
from flask import abort
from flask import Flask
from flask import render_template
app = Flask(__name__)

def get_csv():
	csv_path = "static/la-riots-deaths.csv"
	csv_file = open(csv_path, 'rb')
	csv_obj = csv.DictReader(csv_file)
	csv_list = list(csv_obj)
	return csv_list

#/ is the homepage of our website. 
# With this one line of code, we are pointing this code to our website. 
# Route can also talk to a database and make queries.
@app.route('/')
def index():
	template = "index.html"
	object_list = get_csv()
	#after the comma, goes the thing you want to put onto the template
	return render_template(template, object_list = object_list)

#Here we are setting up a pattern for the url so that it connects the row id to the url.
#This is all to make a new url for every person in the dataset. 
@app.route('/<row_id>/')
def detail(row_id):
	template = "detail.html"
	object_list = get_csv()
	for row in object_list:
		if row["id"] == row_id:
			return render_template(template, object=row)
	abort(404)


# We need a place to store our template


#If this script is run from the command line
if __name__ == "__main__":
	# Fire up the Flask test server
	app.run(debug=True, use_reloader=True)
