from flask import Flask, request
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

sql = "INSERT INTO USER (user_id, user_mRNA) VALUES()"



app = Flask(__name__)

@app.route('/')
def mainstring() :
    return '31310 박광성 - 생명II 발표용 서버'



if __name__ == '__main__' :
    app.run()

