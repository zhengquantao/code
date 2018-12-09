from flask import Blueprint, render_template, session

logt = Blueprint('logt', __name__)

@logt.route('/logout')
def logout():
    print(session['user_info'])
    session.clear()  # 清除session
    return render_template('login.html')