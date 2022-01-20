import socket
from cryptography.fernet import Fernet


key = open('crypto.txt','rb')
session_key = key.read()
cipher = Fernet(session_key)
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.connect(('localhost',9090))

name = input('Please tell me your name...' )
name = cipher.encrypt(name.encode('utf-8'))
sock.send(name)



while True:
    data = sock.recv(1024)
    print((cipher.decrypt(data)).decode('utf-8'))
    if (cipher.decrypt(data)).decode('utf-8') == 'Connect NO':
        print('Соединение разорвано')
        sock.close()
        break
    data = sock.recv(1024)
    data = str((cipher.decrypt(data)).decode('utf-8'))
    if data  == '0':
        print('Вы зашли как обычный пользователь \n')
        data = sock.recv(1024)
        data2 = (cipher.decrypt(data)).decode('utf-8') 
        if data2 == 'Введите ваш запрос':
            print("Выберите информацию которую хотите получить, \n (1) Получить информацию обо всех пользователях, \n (2) получить информацию о конкретном пользователе \n (5) выход\n")
            name2 = input("Введите значение ")
            name2 = cipher.encrypt(name2.encode('utf-8'))
            sock.send(name2)
            data1 = sock.recv(1024)
            if (cipher.decrypt(data1)).decode('utf-8') == 'Информация о пользователях ':
                data2 = sock.recv(1024)
                print(((cipher.decrypt(data2)).decode('utf-8')))
                break
            elif (cipher.decrypt(data1)).decode('utf-8') == 'Введите имя польхователя, о котором хотите узнать информацию ':
                print(((cipher.decrypt(data1)).decode('utf-8')))
                name3 = input("Введите имя ")
                name3 = cipher.encrypt(name3.encode('utf-8'))
                sock.send(name3)
                data2 = sock.recv(1024)
                print(((cipher.decrypt(data2)).decode('utf-8')))
                break
            elif (cipher.decrypt(data1)).decode('utf-8') == 'Соединение будет разорвано':
                print((cipher.decrypt(data1)).decode('utf-8'))
                break
            elif (cipher.decrypt(data1)).decode('utf-8') == 'Не то ':
                print((cipher.decrypt(data1)).decode('utf-8'))
                break
            
        sock.close()
        
        break
    elif data  != '0':
        print('Вы зашли как администратор \n')
        data = sock.recv(1024)
        data2 = (cipher.decrypt(data)).decode('utf-8')
        if data2 == 'Введите ваш запрос':
            print("Выберите информацию которую хотите получить, \n (1) Получить информацию обо всех пользователях, \n (2) получить информацию о конкретном пользователе ")
            print("3) получить информацию о сессии\n  (4) добавить пользователя \n (5) выход\n")
            name2 = input("Введите значение ")
            name2 = cipher.encrypt(name2.encode('utf-8'))
            sock.send(name2)
            data1 = sock.recv(1024)
            if (cipher.decrypt(data1)).decode('utf-8') == 'Информация о пользователях ':
                data2 = sock.recv(1024)
                print(((cipher.decrypt(data2)).decode('utf-8')))
                break
            elif (cipher.decrypt(data1)).decode('utf-8') == 'Введите имя польхователя, о котором хотите узнать информацию ':
                print(((cipher.decrypt(data1)).decode('utf-8')))
                name3 = input("Введите имя ")
                name3 = cipher.encrypt(name3.encode('utf-8'))
                sock.send(name3)
                data2 = sock.recv(1024)
                print(((cipher.decrypt(data2)).decode('utf-8')))
                break
            elif (cipher.decrypt(data1)).decode('utf-8') == '10 последних сессий ':
                print(((cipher.decrypt(data1)).decode('utf-8')))
                data2 = sock.recv(1024)
                print((cipher.decrypt(data2)).decode('utf-8'))
                break
            
            elif (cipher.decrypt(data1)).decode('utf-8') == 'Для того чтобы добавить пользователя введите его имя и права доступа ':
                print(((cipher.decrypt(data1)).decode('utf-8')))
                name4 = input("Введите имя ")
                name4 = cipher.encrypt(name4.encode('utf-8'))
                sock.send(name4)
                name5 = input("Введите права доступа  \n 0 - обычный пользователь, 1 - админ ")
                name5 = cipher.encrypt(name5.encode('utf-8'))
                sock.send(name5)
            elif (cipher.decrypt(data1)).decode('utf-8') == 'Соединение будет разорвано':
                print((cipher.decrypt(data1)).decode('utf-8'))
                break
            elif (cipher.decrypt(data1)).decode('utf-8') == 'Не то ':
                print((cipher.decrypt(data1)).decode('utf-8'))
                break
            data2 = sock.recv(1024)
            print((cipher.decrypt(data2)).decode('utf-8'))
        sock.close()
        break



