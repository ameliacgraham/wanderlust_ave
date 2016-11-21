class Country(object):
	def __init__(self, name, weather, price, crowdedness):
		self.name = name
		self.weather = weather
		self.price = price
		self.crowdedness = crowdedness

jamaica = Country("jamaica",
	["november","december"],
	["april", "may", "june", "july", "august", "september", "october", "november"],
	["may", "june", "july", "august", "september", "october", "november"])

costa_rica = Country("costa rica",
	["november", "december", "january", "february", "march", "april" ],
	["january", "february", "march", "april","may", "june", "july", "august", "september", "october", "november"],
	["may", "june", "september", "october", "november"])

country_list = [costa_rica, jamaica]

weather_list = []
price_list = []
crowdedness_list = []
travel_month = raw_input("What month do you want to travel? ").lower()

def get_weather(travel_month, country):
	if travel_month in country.weather:
		global weather_list
		weather_list.append(country.name)
		return weather_list

def get_price(travel_month, country):
	if travel_month in country.price:
		global price_list
		price_list.append(country.name)
		return price_list

def get_crowdedness(travel_month, country):
	if travel_month in country.crowdedness:
		global crowdedness_list
		crowdedness_list.append(country.name)
		return 	crowdedness_list


def main():
	for country in country_list:
		get_weather(travel_month, country)
		get_price(travel_month, country)
		get_crowdedness(travel_month, country)
		if country.name in weather_list and country.name in price_list and country.name in crowdedness_list:
			print country.name


if __name__ == '__main__':
	main()