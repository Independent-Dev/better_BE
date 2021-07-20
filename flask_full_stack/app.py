from flask import Flask, jsonify, request, render_template, make_response
from flask_cors import CORS
import requests
# static_url_path와 관련해서는 아래 url 참조
# https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask
app = Flask(__name__, static_url_path='/static')
# same origin policy에 따라 script 태그(<script>) 내에서는 cross origin request를 금지하고 있는데 
# 이렇게 선언을 해주면 모든 요청/응답에 대하여 CORS 지원 헤더를 넣어준다고 함. 헤더명은 Access-Control-Allow-Origin
CORS(app)

@app.route("/")
def hello():
    return 'Hello world!!'

@app.route("/google")
def google():
    result = requests.get('https://www.google.com')
    return result.text

@app.

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8081", debug=True)