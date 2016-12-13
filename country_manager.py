class Country(object):
	def __init__(self, name, price):
		self.name = name
		self.price = price

bahamas = Country("The Bahamas",
	["may", "june"])

cambodia = Country("Cambodia",
	["october", "november"])

costa_rica = Country("Costa Rica",
	["may", "june", "july", "november"])

ireland = Country("Ireland",
	["april","may", "september", "october"])

jamaica = Country("Jamaica",
	["april", "may"])

laos = Country("Laos",
	["july", "august"])

liechtenstein = Country("Liechtenstein",
	["april","may", "september", "october", "november"])

scotland = Country("Scotland",
	["may", "june", "september"])

switzerland = Country("Switzerland",
	["april","may", "june", "september"])

thailand = Country("Thailand",
	["september", "october"])

vietnam = Country("Vietnam",
	["january","february", "march", "december"])







country_list = [bahamas, cambodia, costa_rica, ireland, jamaica, liechtenstein, scotland, switzerland, vietnam]


def get_country(month):
	price_list = []
	for country in country_list:
		if month.lower() in country.price:
			price_list.append(country.name)
	return price_list





