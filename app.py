from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

# APIエンドポイントの定義
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"message": "Hello from Python!"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)