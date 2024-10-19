from flask import Flask, render_template, jsonify, request, redirect
import add_app_file.get_weather as getweather#天気の取得を行うライブラリ

app = Flask(__name__)

# ピン情報を格納するリスト
pins = []

# 地図表示ページのエンドポイント
@app.route('/', methods=['GET'])
def index():
    weather_img = getweather.get_weather('tokyo')
    print(weather_img)
    return render_template('index.html', pins=pins, images = weather_img)

# 新しいピンを追加するページのエンドポイント
@app.route('/event_reg', methods=['GET', 'POST'])
def event_reg():
    # まだ仮
    if request.method == 'POST':
        # フォームからピンの情報を取得
        name = request.form['name']
        latitude = float(request.form['latitude'])
        longitude = float(request.form['longitude'])

        # ピン情報をリストに追加
        pins.append({
            'name': name,
            'latitude': latitude,
            'longitude': longitude
        })

        # 地図ページにリダイレクト
        return redirect('/')
    return render_template('event_reg.html')

if __name__ == '__main__':
    app.run(debug=True)
