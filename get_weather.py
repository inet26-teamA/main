"""
・天気を取得する
get_weather('都市名')
"""

import requests
from datetime import datetime, timedelta

# OpenWeatherMapのAPIキー
API_KEY = '4d11781b6190ab2bd390e6df45db4356'  # ここに自分のAPIキーを入力
# 取得したい都市名

def get_weather(lat, lon):
    # APIエンドポイントURL
    url = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_data = []
        now = datetime.now()
        
        for forecast in data['list']:
            forecast_time = datetime.strptime(forecast['dt_txt'], '%Y-%m-%d %H:%M:%S')
            if forecast_time >= now:
                hour = forecast_time.hour
                weather = forecast['weather'][0]['description']
                weather_data.append([hour, weather])
                
                if len(weather_data) >= 6:
                    break
    else:
        print('Error:', response.status_code, response.text)
    
    #return weather_data #時刻と天気を2次元リストで取得する
    return [sublist[1] for sublist in weather_data] #天気だけをリストで取得する

#print(get_weather('tokyo'))