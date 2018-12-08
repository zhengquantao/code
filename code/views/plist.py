from flask import Blueprint, render_template, request
from ..tools import helper, mypage

pli = Blueprint('pli', __name__, static_folder='', static_url_path='')

# @pli.before_request()
@pli.route('/plist/<int:id>')
def plist(id):
    #　page_num = request.form.get('get')
    num_list = helper.fetch_all('select * from Ncode where user_id=%s', (id,))
    num = helper.fetch_all('select count(*) from Ncode where user_id=%s', (id,))
    print(num)
    # page_html = mypage.Page(page_num, total_count, url_prefix='/plist', per_page=10, max_page=8)
    return render_template('code.html', num_list=num_list, )