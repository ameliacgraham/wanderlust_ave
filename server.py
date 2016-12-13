from flask import Flask, request
import country_manager

app = Flask(__name__)

@app.route("/")
def month_form():
	return """
	<!DOCTYPE html>
	    <html>
	      <head>
	        <title>Hi There!</title>
	      </head>	
		<body>
	        <h1>Hi There!</h1>
	        <form action="/month">
	          What month do you want to travel?
	          <input type="text" name="month">
	          <input type="submit">
	        </form>
	        </body>
	   		</html>
			"""

@app.route("/month")
def get_countries_list():
	month_input = request.args.get("month")
	price_list = country_manager.get_country(month_input)
	return ', '.join(price_list)



if __name__ == "__main__":
	app.run()


