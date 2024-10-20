from flask import Flask, render_template, jsonify, request, redirect
import get_weather as getweather #天気の取得を行うライブラリ
# import gemini_api as gemini #geminiからメッセージを受け取るライブラリ
import register_events as register_events

app = Flask(__name__)

# ピン情報を格納するリスト
pins = []

# 地図表示ページのエンドポイント
@app.route('/', methods=['GET'])
def index():
    weather_img = getweather.get_weather('tokyo')
    #pronpt = f"次のリストは3時間ごと合計18時間の天気です。一言で天気のポイントをまとめてください。語尾は「になるでしょう」15文字以内 {weather_img}"
    message = "てすと"
    #message = gemini.ask_gemini(pronpt)
    return render_template('index.html', pins=pins, images = weather_img, gemini_message = message)

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

@app.route('/past_events', methods=['GET'])
def past_events():
    all_events = register_events.get_all_col()
    events = [[item for i, item in enumerate(sublist) if i != 4] for sublist in all_events]
    return render_template('past_events.html', events=events)

if __name__ == '__main__':
    app.run(debug=True)
