from flask_frozen import Freezer
from app import app, get_csv
freezer = Freezer(app)

#we need to tell it to make a detail view for every row in our spreadsheet
#This has to mirror the detail function in our app doc
@freezer.register_generator
def detail():
	for row in get_csv():
		yield {'row_id': row['id']}

if __name__ == "__main__": 
	freezer.freeze()
