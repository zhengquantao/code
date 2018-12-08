from DBUtils.PooledDB import PooledDB
import pymysql
class Config(object):
    SALT = b'dab123'
    SECRET_KEY = 'dsb'
    MAX_CONTENT_LENGTH = 1024*1024*7  # flask自动会限制最大上传文件大小
    POOL = PooledDB(
        creator=pymysql,  # 使用连接数据库
        maxconnections=6,  # 连接池允许的最大连接数，0和none表示不限制连接数
        mincached=2,  # 初始化时， 连接池中至少创建的空闲的连接， 0表示不创建
        maxcached=5,  # 连接池中最多闲置的连接0和none不限制
        maxshared=3,  # 连接池中最多共享的链接数量， 0和none表示全部共享。ps无用，因为pymysql和MySQLdb等模块的threadsafety都为1
        blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。Ture,等待，False不等待报错
        maxusage=None,  # 一个连接最多被重复使用的次数，none表示无限制
        setsession=[],  # 开始会话前执行的命令列表。如：["set dotestyle to..."]
        ping=0,
        # ping MySQL服务端，检查是否服务可用。如：0=none=never，1=default=whenever it is requested,2=when a cursor is created
        host='127.0.0.1',
        port=3306,
        user='root',
        password='12345678',
        db='mypro',
        charset='utf8'
    )