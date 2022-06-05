from distutils.log import error
from flask import Flask, request, Response, jsonify
import pymysql
# connect mySQL DB ---------------------------------------------
portfolio_db = pymysql.connect(
    user = 'root',
    passwd = 'pks51700',
    host = '127.0.0.1',
    db = 'portfolio',
    charset = 'utf8'
)
# 딕셔너리형태 설정-----------------------------------------------------
cursor = portfolio_db.cursor(pymysql.cursors.DictCursor)
# ---------------------------------------------------------------------

app = Flask(__name__)

#get
@app.route('/user/<param>') 
def get_user(param):
    return jsonify({"param": param})

#post
@app.route('/userinfo', methods=['POST']) 
def post_userinfo():
    data = data.loads(request.data)
    param = request.get_json()

    
    return jsonify(param)



@app.route('/')
def mainstring() :
    return '31310 박광성 - 생명II 발표용 서버'



if __name__ == '__main__' :
    app.run()

