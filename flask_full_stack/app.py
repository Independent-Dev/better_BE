from flask import Flask, jsonify, request, render_template
import requests
# static_url_path와 관련해서는 아래 url 참조
# https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask
app = Flask(__name__, static_url_path='/static')

@app.route("/")
def hello():
    return 'Hello world!!'

@app.route("/google")
def google():
    result = requests.get('https://www.google.com')
    return result.text

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8081", debug=True)