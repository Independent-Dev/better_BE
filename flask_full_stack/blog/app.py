from flask import Flask, jsonify, request, render_template, make_response
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_cors import CORS
from view import blog
import os

# https만 지원하는 기능을 http에서 테스트할 때 필요한 설정
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__, static_url_path='/static')
CORS(app)
app.secret_key = 'Jinoh_server'

app.register_blueprint(blog.blog_abtest, url_prefix='/blog')
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'  # 이걸 strong으로 해주어야 세션을 보다 복잡하게 만들 수 있음.

# flask_login에서는 두 개의 함수를 정의해줄 필요가 있는데 이게 그 둘 가운데 하나. 로그인한 유저의 정보를 가져오는 것에 이용
# 이 정보는 current_user 등에서 이용될 것 같다. 이건 나중에 문서를 읽어보는 것이 필요할 것 같음.
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# flask_login에서 구현이 필요한 다른 하나의 함수. 허가받지 않은 유저를 처리하는 데 필요.
@login_manager.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success=False), 401)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='405', debug=True)


# practice before section13
# from flask import Flask, jsonify, request, render_template, make_response
# from flask_cors import CORS
# import requests, logging
# # static_url_path와 관련해서는 아래 url 참조
# # https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask
# app = Flask(__name__, static_url_path='/static')

# # same origin policy에 따라 script 태그(<script>) 내에서는 cross origin request를 금지하고 있는데 
# # 이렇게 선언을 해주면 모든 요청/응답에 대하여 CORS 지원 헤더를 넣어준다고 함. 헤더명은 Access-Control-Allow-Origin
# CORS(app)
# logging.basicConfig(filename="test.txt", level=logging.DEBUG )

# @app.route("/")
# def hello():
#     return 'Hello world!!'

# @app.errorhandler(404)
# def page_not_found(error):
#     app.logger.error(error)
#     return "<h1>Not Found 404</h1>", 404

# @app.route("/google")
# def google():
#     result = requests.get('https://www.google.com')
#     return result.text

# @app.route('/test', methods=["GET", "POST", "PUT", "DELETE"])
# def test():
#     if request.method == "POST":
#         data = request.get_json()  # post로 보낸 경우에는 이러한 방식으로 데이터를 가져올 수 있음!!
#     if request.method == "GET":
#         data = request.args.get('data', None)  # get으로 request한 경우에는 이렇게 써야함!!
#     if request.method == "PUT":
#         pass
#     if request.method == "DELETE":
#         pass

#     return make_response(jsonify(status=True), 200)


# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port="8081", debug=False)