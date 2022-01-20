import MySQLdb
from cryptography.fernet import Fernet
import socket
import datetime
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('',8000))
print(sock)
connect = MySQLdb.connect(user="root",password="lhjrfhbc",host="localhost", port=3307,database="project")
print('Начало работы сервера')
session = 0
print('ожидайте присоединения')
while True:
    cursor = connect.cursor()
    data,addres =  sock.recvfrom(2048)
    time = str(datetime.datetime.now().time())
    time = time.rsplit('.',1)
    name = (data).decode('utf-8')
    adr = "{0}:{1}".format(addres[0],addres[1])
    name  = cursor.execute("SELECT USER FROM maintable  WHERE USER = '{0}' ".format(name))
    if name == 0:
            sock.sendto(("ошибка ввода").encode("utf-8"),addres)
            break
    else:
        sock.sendto(("Соединение установлено").encode("utf-8"),addres)
        sock.sendto(("Введите логин").encode("utf-8"),addres)
        name3,addres =  sock.recvfrom(2048) 
        name2 = str((name3).decode('utf-8'))
        dat = cursor.execute("SELECT * FROM maintable WHERE USER = '{0}' ".format(name2))
        result = cursor.fetchall()
        if dat == 0:
            sock.sendto(("There is no such user").encode("utf-8"),addres)
        else:
            sock.sendto((str(result).encode("utf-8")),addres)
        continue

