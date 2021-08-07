from flask import Flask, jsonify, g, request

app = Flask(__name__)

@app.route('/test')
def test():
    return jsonify({'Hello': 'World'})

# g 객체 전역 공간 이용
@app.before_request
def authentification():
    if request.authorization:
        g.user = request.authorization['username']
    else:
        g.user = 'Anonymous'

@app.route('/ch2/try_g/')
def try_g():
    return jsonify({'Hello': g.user})

# error handling
# @app.errorhandler(Exception)으로 하면 모든 것 핸들링 가능(https://stackoverflow.com/questions/20258159/how-to-intercept-all-exceptions-in-flask)
@app.errorhandler(404)
def error_handling_404(error):
    print(dir(error))
    return jsonify({'Error': str(error)}), error.code
app.config['DEBUG'] = True
if __name__ == "__main__":
    
    app.run()
