from flask import Flask, render_template, jsonify, request, redirect
import get_weather as getweather #天気の取得を行うライブラリ
# import gemini_api as gemini #geminiからメッセージを受け取るライブラリ
import register_events

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

@app.route('/add_pin_data', methods = ['GET'])
def add_pin():
    return jsonify(register_events.get_events('住所'))

@app.route('/event_reg')
def event_reg():
    return render_template('event_reg.html')

# 新しいピンを追加するページのエンドポイント
@app.route('/submit', methods=['POST'])
def submit():
    eventname = request.form.get('eventname')
    zipcode = request.form.get('zipcode')
    address = request.form.get('address')
    start_date = request.form.get('start-date')

    # address = f"{zipcode}, {address}" 郵便番号を付ける
    address = address #郵便番号を付けない
    year, month, date = map(int, start_date.split('-'))
    #print(f'イベント名: {eventname} , 住所: {address} , 日時: {year},{month},{date}')
    register_events.add_events(year, month, date, eventname, address)
    

    #return f"イベント名: {eventname}, 郵便番号: {zipcode}, 住所: {address}, 番地: {username}, 開始日: {start_date}, 終了日: {end_date}"
    return render_template('event_reg.html')

@app.route('/past_events', methods=['GET'])
def past_events():
    all_events = register_events.get_all_col()
    events = [[item for i, item in enumerate(sublist) if i != 4] for sublist in all_events]
    return render_template('past_events.html', events=events)

if __name__ == '__main__':
    app.run(debug=True)
