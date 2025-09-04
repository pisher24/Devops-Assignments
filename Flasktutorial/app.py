#Flask-tutorial

# the main file name should be app.py as it's a industry standard, though it's not a madatory the name can be anything

from flask import Flask, request, render_template

from datetime import datetime

#app= {__name__} 

app = Flask(__name__)# here we are just creating flask application instance it's just the syntax to create application instance nothing special about it

@app.route('/') # defining a route for home page of a website

def home():
	#return 'Hello Guys this is my first flask application'
	day_of_the_week=datetime.now().strftime('%A')
	print(day_of_the_week)
	return render_template('index.html', A=day_of_the_week)

@app.route('/api/<name1>') # here <name> is the any variable that is put after the /api route;. This is one way passing data from front end to back-end via URI path

#if u want to pass multiple variables u cand do @app.route('/api/<name1>/<name2>')
# and then in ur def do def name (name1,name2)

def x(name1):
	#print (name)
	resp= 'Hello ' +name1+ ' welcome to next page of the sample application.'
	#print(resp)
	return resp

@app.route('/api') # this method shows how to get data from from front-end client to back-end via query strings
def name():
	name=request.values.get('name')
	
	age=request.values.get('age')

	result={"name": name,
			"age" : age	}

	return result
if __name__ == '__main__': 
							# the lines 16 and 18 is syntax of how to run a flask program
	app.run(debug='True') 
	# if debug is set to true what happens is when make changes in the code directly refresh the page for the changes to take effect 

