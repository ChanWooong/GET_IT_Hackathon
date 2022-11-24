from codecs import unicode_escape_decode, unicode_escape_encode
from dis import code_info
import importlib
import random
import time
import re
from flask import Flask, request,render_template
app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello, World!'
@app.errorhandler(404)
def page_not_found(error):
    return "페이지가 없습니다. URL를 확인 하세요", 404
@app.route('/main_page') #메인페이지
def main_page():
    return render_template('main_page.html')
@app.route('/login') #로그인
def login():
    return render_template('login.html')
@app.route('/intro') #회사 소개
def intro():
    return render_template('intro.html')
@app.route('/companyList') 
def companyList():
    return render_template('companyList.html')
@app.route('/comapply') 
def comapply():
    return render_template('comapply.html')
@app.route('/complain') 
def complain():
    return render_template('complain.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000 , debug=True)
    
