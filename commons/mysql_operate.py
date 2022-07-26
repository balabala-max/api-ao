from configs.config_test import *
import pymysql
import logging
DB_CONF = {
    "host": MYSQL_HOST,
    "port": MYSQL_PORT,
    "user": MYSQL_USER,
    "password": MYSQL_PASSWD,
    "db": MYSQL_DB
}

class Mysqldb():

    def __init__(self,db_conf=DB_CONF):
        self.conn = pymysql.connect(**db_conf,autocommit=True)
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)


    def select_db(self,sql):
        #检查是否断开，如果断开就继续重连
        self.conn.ping(reconnect=True)
        #使用 execute 执行MySQL
        self.cur.execute(sql)
        #使用fetchall() 获取查询结果
        data = self.cur.fetchall()
        return data

    def execute(self,sql):
        ''' 更新/新增/删除'''
        try:
            #检查连接是否断开，如果断开就重连
            self.conn.ping(reconnect=True)
            #使用 execute()  执行sql
            self.cur.execute(sql)
            #提交事务
            self.conn.commit()
        except Exception as e:
            logging.info("操作Mysql出现错误:{}".format((e)))
            self.conn.rollback()

    def __del__(self):
        #关闭游标
        self.cur.close()
        self.conn.close()

db = Mysqldb(DB_CONF)

