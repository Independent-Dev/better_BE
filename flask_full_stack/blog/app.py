from flask import Flask, jsonify, request, render_template, make_response
from flask_cors import CORS
import requests, logging
# static_url_path와 관련해서는 아래 url 참조
# https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask
app = Flask(__name__, static_url_path='/static')

# same origin policy에 따라 script 태그(<script>) 내에서는 cross origin request를 금지하고 있는데 
# 이렇게 선언을 해주면 모든 요청/응답에 대하여 CORS 지원 헤더를 넣어준다고 함. 헤더명은 Access-Control-Allow-Origin
CORS(app)
logging.basicConfig(filename="test.txt", level=logging.DEBUG )

@app.route("/")
def hello():
    return 'Hello world!!'

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return "<h1>Not Found 404</h1>", 404

@app.route("/google")
def google():
    result = requests.get('https://www.google.com')
    return result.text

@app.route('/test', methods=["GET", "POST", "PUT", "DELETE"])
def test():
    if request.method == "POST":
        data = request.get_json()  # post로 보낸 경우에는 이러한 방식으로 데이터를 가져올 수 있음!!
    if request.method == "GET":
        data = request.args.get('data', None)  # get으로 request한 경우에는 이렇게 써야함!!
    if request.method == "PUT":
        pass
    if request.method == "DELETE":
        pass

    return make_response(jsonify(status=True), 200)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8081", debug=False)