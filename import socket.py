import socket
import datetime
import MySQLdb
from cryptography.fernet import Fernet
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('',9090))
print(sock)
connect = MySQLdb.connect(user="root",password="lhjrfhbc",host="localhost", port=3307,database="test")

print('Start Server')
session = 0
while 1:
   
    if session == 0:
        check = cursor.execute("SELECT ip FROM users WHERE name = '{0}'".format(nickname))
        if check == 0:
            cursor1.execute("INSERT INTO session VALUES ('{0}','{1}','{2}')".format(nickname,adr,time[0]))

        sock.sendto("Connect to server".encode("utf-8"))
        season = 1 
    conn.send(data.upper())
while True:
    print('Ожидание соединения...')
    connection, client_address = sock.accept()
    try:
       
        while True:
            cursor = connect.cursor()
            cursor1 = connect.cursor()
            data,addres =  sock.recvfrom(2048)
            time = str(datetime.datetime.now().time())
            time = time.rsplit('.',1)
            nickname = str(data.decode('utf-8'))
            adr = "{0}:{1}".format(addres[0],addres[1])
            if session == 0:
                check = cursor.execute("SELECT ip FROM users WHERE name = '{0}'".format(nickname))
                check = crypto(check)
                if check == 0:
                    cursor1.execute("INSERT INTO session VALUES ('{0}','{1}','{2}')".format(nickname,adr,time[0]))

                sock.sendto("Connect to server".encode("utf-8"))
                season = 1 
            else:
                print('Нет данных от:', client_address)
                break             
    finally:

            connection.close()
def crypto(date):
    cipher_key = Fernet.generate_key()
    cipher = Fernet(cipher_key)
    text = date
    encrypted_text = cipher.encrypt(text)
    print(encrypted_text)