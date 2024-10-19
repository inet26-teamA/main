from flask import Flask, render_template, jsonify, request, redirect

app = Flask(__name__)

# ピン情報を格納するリスト
pins = []

# APIエンドポイントの定義
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"message": "Hello from Python!"}
    return jsonify(data)

# 地図表示ページのエンドポイント
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', pins=pins)

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
