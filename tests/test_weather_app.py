import pytest
from weather_app import WeatherApp
from weather_service import WeatherService

# Preparing test data and test environment

@pytest.fixture
def weather_service(mocker):
    return mocker.Mock()


@pytest.fixture
def weather_app(weather_service):
    return WeatherApp(weather_service)


# Tests to verify WeatherApp methods

def test_search_city(weather_app, weather_service):
    """
    Tests search_city() method correctly returns the weather and calls get_weather() with correct city
    """

    weather_service.get_weather.return_value = "Sunny"

    result = weather_app.search_city("Gothenburg")

    assert result == "Sunny"
    weather_service.get_weather.assert_called_once_with("Gothenburg")



def test_get_city_rain_probability(weather_app, weather_service):

    weather_service.get_rain_probability.return_value = 35

    result = weather_app.get_city_rain_probability("Gothenburg")

    assert result == 35
    weather_service.get_rain_probability.assert_called_once_with("Gothenburg")



def test_get_city_temperature(weather_app, weather_service):

    weather_service.get_temperature.return_value = 26

    result = weather_app.get_city_temperature("Gothenburg")

    assert result == 26
    weather_service.get_temperature.assert_called_once_with("Gothenburg")




