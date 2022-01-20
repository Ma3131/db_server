import MySQLdb
from cryptography.fernet import Fernet
import socket
import datetime

key = open('crypt.txt','wb')
cipher_key = Fernet.generate_key()
cipher = Fernet(cipher_key)
key.write(cipher_key)
key.close()

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('',9090))
print(sock)
connect = MySQLdb.connect(user="root",password="lhjrfhbc",host="localhost", port=3307,database="test")
print('Start Server')
session = 0
print('Ожидание соединения...')
while True:
    cursor = connect.cursor()
    cursor1 = connect.cursor()
    cursor2 = connect.cursor()
    data,addres =  sock.recvfrom(2048)
    time = str(datetime.datetime.now().time())
    time = time.rsplit('.',1)

    nickname = (cipher.decrypt(data)).decode('utf-8')
    adr = "{0}:{1}".format(addres[0],addres[1])

    data3  = cursor.execute("SELECT NAME FROM users WHERE NAME = %s",(nickname,))
    cursor2.execute("SELECT root FROM users WHERE NAME = '{0}'".format(nickname))
    root = cursor2.fetchone()
    if root == None:
        sock.sendto(cipher.encrypt(("Connect NO").encode("utf-8")),addres)
    else:
        for x in root:
            print(x)

        if data3 == 0:
            data1 = cursor1.execute("""INSERT INTO session  VALUES ('{0}','{1}','{2}')""".format(nickname,adr,time[0]))
            connect.commit()
            sock.sendto(cipher.encrypt(("Connect NO").encode("utf-8")),addres)
            break
        else:
            data1 = cursor1.execute("INSERT INTO session VALUES ('{0}','{1}','{2}')".format(nickname,adr,time[0]))
            connect.commit()
        sock.sendto(cipher.encrypt(("Connect to server").encode("utf-8")),addres)
        sock.sendto(cipher.encrypt(((str(x))).encode("utf-8")),addres)
        sock.sendto(cipher.encrypt(("Введите ваш запрос").encode("utf-8")),addres)
        
        number,addres =  sock.recvfrom(2048) 
        number1 = str((cipher.decrypt(number)).decode('utf-8'))
        if number1 == '1':
            sock.sendto(cipher.encrypt(("Информация о пользователях ").encode("utf-8")),addres)
            cursor.execute("SELECT * FROM users DESC LIMIT 10")
            result = cursor.fetchall()
            sock.sendto(cipher.encrypt((str(result)).encode("utf-8")),addres)
            continue
        elif number1 == '2':
            sock.sendto(cipher.encrypt(("Введите имя польхователя, о котором хотите узнать информацию ").encode("utf-8")),addres)
            dat,addres =  sock.recvfrom(2048)
            nick1 = str((cipher.decrypt(dat)).decode('utf-8'))
            data6 = cursor.execute("SELECT * FROM users WHERE NAME = '{0}' ".format(nick1))
            result = cursor.fetchall()
            print('jjj ',result)
            print('jjj ',data6)
            if data6 == 0:
                sock.sendto(cipher.encrypt(("Нет такого пользователя").encode("utf-8")),addres)
            else:
                sock.sendto(cipher.encrypt((str(result)).encode("utf-8")),addres)
            continue
        elif number1 == '3' and x !=0:
            sock.sendto(cipher.encrypt(("10 последних сессий ").encode("utf-8")),addres)
            cursor.execute("SELECT * FROM session ORDER BY time DESC LIMIT 5")
            result = cursor.fetchall()
            result2 = ''
            for row in result:
                result2 += row[0] + ' ' + row[1] + ' ' + str(row[2]) + ' '
                result2 += ' '
            sock.sendto(cipher.encrypt((str(result2)).encode("utf-8")),addres)
            continue
        elif number1 == '4' and x !=0:
            sock.sendto(cipher.encrypt(("Для того чтобы добавить пользователя введите его имя и права доступа ").encode("utf-8")),addres)
            dat,addres =  sock.recvfrom(2048)
            nick1 = str((cipher.decrypt(dat)).decode('utf-8'))
            print(nick1)
            dat2,addres =  sock.recvfrom(2048)
            try:
                root = int((cipher.decrypt(dat2)).decode('utf-8'))
                data6 = cursor.execute("INSERT INTO users VALUES('{0}','{1}','{2}','{3}')".format(nick1,time[0],adr,root))
                connect.commit()
                
            except:
                sock.sendto(cipher.encrypt(("Вы ввели некоректные значения или пользователь с таким именем уже существует.").encode("utf-8")),addres)
            else:
                sock.sendto(cipher.encrypt(('Пользователь добавлен').encode("utf-8")),addres)
            continue
        elif number1 == '5':
            sock.sendto(cipher.encrypt(("Соединение будет разорвано").encode("utf-8")),addres)
            continue
        else:
            sock.sendto(cipher.encrypt(("Не то ").encode("utf-8")),addres)
            continue

            

