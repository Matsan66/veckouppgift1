

class WeatherApp:
    """
    WeatherApp represents the user interface for the weather service.
    """
    def __init__(self, weather_service):
        self.weather_service = weather_service

    def search_city(self, city):
        """
        Returns the weather in provided city
        """
        return self.weather_service.get_weather(city)

    def get_city_rain_probability(self, city):
        """
        Returns the probability of rain for the provided city
        """
        return self.weather_service.get_rain_probability(city)

    def get_city_temperature(self, city):
        """
        Returns the temperature in provided city
        """
        return self.weather_service.get_temperature(city)