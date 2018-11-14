#coding=utf-8
import MySQLdb as mdb
import re
import time

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': '123456',
    'db': 'cop2param',
    'charset': 'utf8'
}
def without_agent():
    '''
    找出未安装通用代理的机器
    :return:
    '''
    conn = mdb.connect(**config)
    # 使用cursor()方法获取操作游标
    cursor = conn.cursor()
    cursor.execute("SELECT * from tbl_cop2param_host WHERE cagt_version is NULL;")

    #获取所有未安装agent的数据

    data = cursor.fetchall()
    whole=len(data)
    num=0
    with open('data.txt','a') as f:
        f.write(time.asctime( time.localtime(time.time())))
        f.write('\n')
        for each in data:
            if re.search('db',each[1]) is None and re.search('hsm',each[1]) is None and re.search('proxy',each[1]) is None:
                num=num+1
                hostname=each[1]
                manage_ip=each[2]
                f.write(hostname)
                f.write(' ')
                f.write(str(manage_ip))
                f.write('\n')
        f.write("未安装通用代理的主机数为："+str(num))
        f.close()


def incorrct_agent():
    conn = mdb.connect(**config)
    # 使用cursor()方法获取操作游标
    cursor = conn.cursor()
    cursor.execute("SELECT * from tbl_cop2param_host WHERE cagt_version is NOT NULL;")
    # print cursor.fetchone()

    data = cursor.fetchall()
    num=0
    with open('data.txt','a') as f:
        f.write('\n')
        f.write('-------------------分割线-----------------------')
        f.write('\n')
        for each in data:
            if re.search('"agent":"0"',each[len(each)-1]) is not None:
                num=num+1
                hostname = each[1]
                manage_ip = each[2]
                f.write(hostname)
                f.write(' ')
                f.write(str(manage_ip))
                f.write('\n')
        f.write("通用代理状态异常的主机数为：" + str(num))
        f.close()


if __name__=='__main__':
    without_agent()
    incorrct_agent()

