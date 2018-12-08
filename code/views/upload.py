from flask import Blueprint, request, render_template, session
from ..tools import helper
import os
import uuid

upl = Blueprint('upl', __name__, static_folder='', static_url_path='')

@upl.route('/upload', methods=["GET", "POST"])
def upload():
    if request.method == "GET":
        return render_template('upload.html')
    file = request.files.get('code')
    if not file.filename.endswith('.zip'):
        return '请上传压缩文件'
    import shutil
    target_path = os.path.join('files', str(uuid.uuid4()))
    # 通过open打开压缩文件， 读取内容进行解压
    shutil._unpack_zipfile(file.stream, target_path)
    # 遍历目录下的所有文件
    total_num = 0
    for base_path, folder_name,  file_list in os.walk(target_path):
        for file_name in file_list:
            file_path = os.path.join(base_path, file_name)
            file_ext = file_path.rsplit('.', maxsplit=1)
            if len(file_ext) != 2:
                continue
            if file_ext[1] != 'py':
                continue
            file_num = 0
            with open(file_path, 'rb') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    if line.startswith('#'):
                        continue
                    file_num += 1
            total_num += file_name
    import datetime
    ctime = datetime.date.today()
    mes = helper.fetch_one('select * from Ncode where ctime=%s and user_id=%s', (ctime, session['user_info']['id']))
    if mes:
        return '震惊，今天已经上传过了'
    helper.insert_m('insert into Ncode(number, ctime, user_id) values (%s, %s, %s)', (total_num, ctime, session['user_info']['id']))
    return '上传成功'