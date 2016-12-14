from flask import Flask, request
import country_manager

app = Flask(__name__)

@app.route("/")
def month_form():
	return """
<!DOCTYPE html>
    <html>
      <head>
      <link rel="stylesheet" href="./style.css">
        <title> Wanderlust Ave </title>
      </head>
      <style>	
		body {
		text-align: center;
    background-image: url("http://i.huffpost.com/gen/1557701/images/o-TRAVEL-facebook.jpg");
	}
	</style>
        <h1>Wanderlust (n.) - A strong desire to travel and explore the world </h1>
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
	return "Countries with %s as a shoulder season: " % (month_input) + ', '.join(price_list)



if __name__ == "__main__":
	app.run()


