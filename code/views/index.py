from flask import Blueprint, render_template
from ..tools import helper
ind = Blueprint('ind', __name__, static_folder='', static_url_path='')

@ind.route('/home')
def home():
    return render_template('home.html')

@ind.route('/user_list')
def user_list():
    import pymysql
    conn = pymysql.Connect(host='127.0.0.1', user='root', password='12345678', db='mypro', charset='utf8')
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('select * from user')
    mes_user = cursor.fetchall()
    return render_template('list.html', mes_user=mes_user)