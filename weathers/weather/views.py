from django.shortcuts import render
import json
import urllib.request

# Replace 'your_api_key_here' with your actual WeatherAPI key
api_key = 'ce3abf7c65b64996a0075617251205'

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=cameroon").read()
        json_data = json.loads(res)
        
        weather_data = {
            'city': json_data['location']['name'],
            'country': json_data['location']['country'],
            'temperature': json_data['current']['temp_c'],
            'condition': str(json_data['current']['wind_dir']),
            'temp_min': json_data['current']['temp_c'],  # Replace with appropriate key
            'temp_max': json_data['current']['temp_c'],  # Replace with appropriate key
            'temp_fahrenheit': json_data['current']['temp_f'],
            'dewpoint' : json_data['current']['dewpoint_c'],
            'update': str(json_data['current']['last_updated']),
            }

    else:
        weather_data = ''
    return render(request, 'index.html', {'weather_data': weather_data})
