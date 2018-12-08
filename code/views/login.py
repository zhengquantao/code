from flask import Blueprint, render_template, request, session, redirect
from ..tools.md5 import md5
from ..tools.helper import fetch_one
import json
import pymysql


log = Blueprint('log', __name__, static_folder='', static_url_path='')

@log.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form.get('username')
    password = request.form.get('password')
    md5_password = md5(password)
    msg = "用户名密码错误"
    sql_mes = fetch_one('select * from user where username=%s and password=%s', (username, md5_password))
    if not sql_mes:
        return render_template('login.html', msg=msg)
    session['user_info'] = {'id': sql_mes['id'], 'nickname': sql_mes['nickname']}  # 把id nickname封装到session中
    return redirect('/home')

