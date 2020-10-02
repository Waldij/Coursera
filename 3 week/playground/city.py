import pprint
import requests
from dateutil.parser import parse

class YahooWeatherForecast():

	def get(self, city):
		url = ""
		data = requests.get(url).json()

		forecast_data = data[""]

class CityInfo():

	def __init__(seld, city):
		self.city = city

	def weather_forecast():
		pass


def _main():
	city_info = CityInfo()
	forecast = city_info.weather_forecast()
	pprint.pprint(forecast)

if __name__ == '__main__':
	_main()