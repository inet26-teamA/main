import requests

def get_weather_by_zip(zip_code, country_code, api_key):
    # OpenWeatherMapのエンドポイントURL (郵便番号用)
    url = f"http://api.openweathermap.org/data/2.5/weather?units=metric&q={zip_code}&APPID={api_key}"
    
    # APIリクエストを送信
    response = requests.get(url)
    
    # ステータスコードが200の場合のみ処理を進める
    if response.status_code == 200:
        data = response.json()
        # 必要な情報を取得
        city = data['name']
        main = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        # 結果を出力
        print(f"都市: {city}")
        print(f"天気: {main}")
        print(f"気温: {temp}℃")
        print(f"湿度: {humidity}%")
        print(f"風速: {wind_speed}m/s")
    else:
        print(f"エラーが発生しました: {response.status_code}")

# 使用例
api_key = "d3cfff3d64a8c653aaf9441b1a575b35"  # 取得したAPIキーをここに入力
zip_code = "tokyo"  # 日本の郵便番号 (例: 東京)
country_code = "JP"  # 国コード（日本は "JP"）
get_weather_by_zip(zip_code, country_code, api_key)
