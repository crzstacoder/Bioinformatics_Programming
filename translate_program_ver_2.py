
from distutils.log import error
from flask import Flask, request, jsonify
import pymysql
from codon_forupgrade import translating
# connect mySQL DB ---------------------------------------------
portfolio_db = pymysql.connect(
    user = 'root',
    passwd = 'pks51700',
    host = '127.0.0.1',
    db = 'portfolio',
    charset = 'utf8'
)
# 딕셔너리형태 설정-----------------------------------------------------
cur = portfolio_db.cursor(pymysql.cursors.DictCursor)
# ---------------------------------------------------------------------


app = Flask(__name__)


sql = """SELECT * FROM USER"""
cur.execute(sql)
M = cur.fetchall()


#post
@app.route('/insertinfo', methods=['POST']) 
def post_userinfo():
    request_data = request.form
    user_mRNA = request_data['user_mRNA']

    
    user_id = request_data["user_id"]
    translated = translating(user_mRNA)

    error_mRNA = True
    error_translate = True


    if translating(user_mRNA) == 'mRNA 염기서열이 아닙니다.' :
        user_mRNA = 'null'
        error_mRNA = False

    if translating(user_mRNA) == '개시코돈이 존재하지 않습니다.' :
        translated = 'null'
        error_translate = False

    sql = """INSERT INTO USER VALUES('%s','%s','%s')"""%(user_id, user_mRNA, translated)
    cur.execute(sql)
    portfolio_db.commit()
    
    if error_mRNA == False:
        return jsonify({
            "success" : "Fail",
            "response" : "mRNA염기서열이 아닙니다."
        })
    elif error_translate == False :
        return jsonify({
            "success" : "Fail",
            "error_name" : "개시코돈이 존재하지 않습니다"
        })
    else :
        return jsonify({
            "success" : "success",
            "response" : "success"
        })
@app.route('/')
def mainstring() :
    return '31310 박광성 - 생명II 발표용 서버'



if __name__ == '__main__' :
    app.run()

