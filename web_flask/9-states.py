#!/usr/bin/python3
"""Script that list all states"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__, template_folder="templates")
app.url_map.strict_slashes = False

@app.route('/states')
def states_list():
	"""displays a new HTML page"""
	new_dict = storage.all('State')
	return render_template('9-states.html', states=new_dict)

@app.route('/states/<id>')
def states_id():
	"""Display a HTML page with the state id's"""
	new_dict = storage.all('State')
	if id:
		key = '{}.{}'.format('State', id)
		if key in new_dict:
			new_dict = new_dict[key]
		else:
			new_dict = None
	else:
		new_dict = storage.all('State')
	return render_template('9-states.html', states=new_dict, id=id)

@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')