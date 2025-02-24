from flask import Flask, render_template, request
import requests

app = Flask(__name__)


API_KEY = 'b2d1063b5e3dcdb93388f43ec686af25'

@app.route('/')
def index():
 return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
 city = request.form['city']
 url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
 response = requests.get(url).json()

 if response.get('cod') != 200:
     return render_template('index.html', error="City not found.")

 weather_data = {
     'city': city,
     'temperature': response['main']['temp'],
     'description': response['weather'][0]['description'],
     'humidity': response['main']['humidity'],
     'wind_speed': response['wind']['speed'],
     'icon': response['weather'][0]['icon'],
 }
 return render_template('result.html', weather=weather_data)

if __name__ == '__main__':
 app.run(debug=True)
