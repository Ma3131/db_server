import socket
from cryptography.fernet import Fernet
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.connect(('localhost',8000))

name = input('Введите логин ' )
name = name.encode('utf-8')
sock.send(name)
while True:
    data = sock.recv(1024)
    print((data).decode('utf-8'))
    if (data).decode('utf-8') == 'ошибка ввода':
        print('Сервер разорвал соединение')
        sock.close()
        break
    data1 = sock.recv(1024)
    data1 = str((data1).decode('utf-8'))
    if data1 == 'Введите логин':
                name3 = input("Введите логин ")
                name2 = name3.encode('utf-8')
                sock.send(name2)
                data2 = sock.recv(1024)
                print((data2).decode('utf-8'))
                break
    
    else:
        print('Error')
    sock.close()