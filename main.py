#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import datetime
import paramiko
import tkinter
from tkinter import *
from tkinter import messagebox, Label
import tkinter as tk
import tkinter.ttk as ttk

def window_deleted():
    print('Connection closed ...')
    ts = str(datetime.datetime.now())
    log.write('Program closed ... ' + ts + ' \n')
    log.write(' \n')
    client.close()
    log.close()
    print ('Program closed')
    print('Logging closed')
    root.quit() # явное указание на выход из программы

def make_connection(): 
    global client
    global chan
    global host
    global port
    global user
    global pass1

        #переменные для Paramico
    host = str(host_in.get())
    port = str(port_in.get())
    user = str(user_in.get())
    pass1 = str(pass_in.get())

    #time.sleep(0.5)  # задержка на подключение Paramico которое еще не используется

    # интерфейс с настройками роутера имя пользователя, адрес удаленного сервера и т.д.
    try:
        ts = str(datetime.datetime.now())
        log.write('Try connect with : ' + ts + ' \n')
        log.write('HOST : ' + host + ' \n')
        log.write('PORT : ' + port + ' \n')
        log.write('USER : ' + user + ' \n')
        client.connect(hostname=host, username=user, password=pass1, port=port)
    except TimeoutError:
        timeout_error()
        #print("Попытка установить соединение была безуспешной, т.к. от другого компьютера за требуемое время не получен нужный отклик, или было разорвано уже установленное соединение из-за неверного отклика уже подключенного компьютера!")
    except paramiko.ssh_exception.AuthenticationException:
        auth_error()
        print("Authentication failed!")
    except paramiko.ssh_exception.NoValidConnectionsError:
        port_error()
        print("Unable to connect to port!")
    except:
        other_error()
        print("Something wrong...")
    else:
        print("No error occurred!")
        chan = client.invoke_shell()    
        connected()
    finally:
    		print("Thanks for Using © Andrew Denisow 2019")

def timeout_error():
    clear()
    global a5_label
    global a6_label
    global a7_label
    global a8_label
    global a9_label
    global a10_label
    a5_label = Label(text='Timeout Error!', font='Consolas 12')
    a6_label = Label(text=' ', font='Consolas 5')
    a7_label = Label(text='No connection', font='Consolas 12')
    a8_label = Label(text='To', font='Consolas 12')
    a9_label = Label(text='SERVER', font='Consolas 12')
    a10_label = Label(text=' ', font='Consolas 12')

    a5_label.grid(row=5, columnspan=2, sticky="s")
    a6_label.grid(row=6, columnspan=2, sticky="s")
    a7_label.grid(row=7, columnspan=2, sticky="s")
    a8_label.grid(row=8, columnspan=2, sticky="s")
    a9_label.grid(row=9, columnspan=2, sticky="s")
    a10_label.grid(row=10, columnspan=2, sticky="s")
    print('Error timeout')

    ts = str(datetime.datetime.now())  # logging
    log.write('Error timeout (No connection): ' + ts + ' \n')

def auth_error():
    clear()
    global a5_label
    global a6_label
    global a7_label
    global a8_label
    global a9_label
    global a10_label
    a5_label = Label(text='Authentication Failed!', font='Consolas 12')
    a6_label = Label(text=' ', font='Consolas 5')
    a7_label = Label(text='User or Password', font='Consolas 12')
    a8_label = Label(text='are', font='Consolas 12')
    a9_label = Label(text='Incorrect', font='Consolas 12')
    a10_label = Label(text=' ', font='Consolas 12')

    a5_label.grid(row=5, columnspan=2, sticky="s")
    a6_label.grid(row=6, columnspan=2, sticky="s")
    a7_label.grid(row=7, columnspan=2, sticky="s")
    a8_label.grid(row=8, columnspan=2, sticky="s")
    a9_label.grid(row=9, columnspan=2, sticky="s")
    a10_label.grid(row=10, columnspan=2, sticky="s")
    print('Error Auth')

    ts = str(datetime.datetime.now())
    log.write('Error Auth (User or Password Incorrect) : ' + ts + ' \n')

def port_error():
    clear()
    global a5_label
    global a6_label
    global a7_label
    global a8_label
    global a9_label
    global a10_label
    a5_label = Label(text='Connection Error!', font='Consolas 12')
    a6_label = Label(text=' ', font='Consolas 5')
    a7_label = Label(text='Unable', font='Consolas 12')
    a8_label = Label(text='to connect', font='Consolas 12')
    a9_label = Label(text='to port', font='Consolas 12')
    a10_label = Label(text=' ', font='Consolas 12')

    a5_label.grid(row=5, columnspan=2, sticky="s")
    a6_label.grid(row=6, columnspan=2, sticky="s")
    a7_label.grid(row=7, columnspan=2, sticky="s")
    a8_label.grid(row=8, columnspan=2, sticky="s")
    a9_label.grid(row=9, columnspan=2, sticky="s")
    a10_label.grid(row=10, columnspan=2, sticky="s")
    print('Error Port')

    ts = str(datetime.datetime.now())
    log.write('Error Port : ' + ts + ' \n')

def other_error():
    clear()
    global a5_label
    global a6_label
    global a7_label
    global a8_label
    global a9_label
    global a10_label
    a5_label = Label(text='An Error Occured!', font='Consolas 12')
    a6_label = Label(text=' ', font='Consolas 5')
    a7_label = Label(text='Please check input', font='Consolas 12')
    a8_label = Label(text=' ', font='Consolas 12')
    a9_label = Label(text='Try Again', font='Consolas 12')
    a10_label = Label(text=' ', font='Consolas 12')

    a5_label.grid(row=5, columnspan=2, sticky="s")
    a6_label.grid(row=6, columnspan=2, sticky="s")
    a7_label.grid(row=7, columnspan=2, sticky="s")
    a8_label.grid(row=8, columnspan=2, sticky="s")
    a9_label.grid(row=9, columnspan=2, sticky="s")
    a10_label.grid(row=10, columnspan=2, sticky="s")
    print('An Error Occured')

    ts = str(datetime.datetime.now())
    log.write('An Error Occured _ Something wrong: ' + ts + ' \n')

def clear():    #очищаем поле "недоступности настроек"
    a5_label.grid_remove()
    a6_label.grid_remove()
    a7_label.grid_remove()
    a8_label.grid_remove()
    a9_label.grid_remove()
    a10_label.grid_remove()

def connected():#в этом блоке видоизменяем цвет кнопок

    global connect_button
    global start_button
    global stop_button
    global auto_button #убираем работоспособность авто кнопки

    ts = str(datetime.datetime.now())
    log.write('Connection Successfull ! : ' + ts + ' \n')

    pass_in.delete(0, END)
    pass_in.insert(0, str('********'))#заменяем пароль на звездочки предварительно записав его в переменную password


    connect_button.grid_remove()
    connected_button = Button(bg='green', fg='white', font='Consolas 12', text="CONNECTED",)
    connected_button.grid(row=4, column=1, ipadx=28, ipady=10)

    auto_button.grid_remove()
    auto_button = Button(bg='#c5ccd8', fg='grey', font='Consolas 12', text="AUTO")
    auto_button.grid(row=4, column=0, ipadx=10, ipady=10, )

    start_button.grid_remove()
    start_button = Button(bg='blue', fg='white', font='Consolas 12', text=" Start Tunnel", command=start)
    start_button.grid(row=11, columnspan=2, ipadx=45, ipady=10, sticky="s")

    stop_button.grid_remove()
    stop_button = Button(bg='orange', fg='white', font='Consolas 12', text=" Stop  Tunnel", command=stop)
    stop_button.grid(row=12, columnspan=2, ipadx=45, ipady=10, sticky="s")

    #когда подключение установлено открываем для ввода новые поля настройки
    clear()

    info_label = Label(text='Fill in and click Start/Stop', font='Consolas 8')
    name_vpn_label = Label(text='NAME', font='Consolas 9')
    server_vpn_label = Label(text='SERVER', font='Consolas 9')
    user_vpn_label = Label(text='VPN USER', font='Consolas 9')
    password_vpn_label = Label(text='VPN PASS', font='Consolas 9')
    secretkey_vpn_label = Label(text='SECRET', font='Consolas 9')

    info_label.grid(row=5, columnspan=2, sticky="s")
    name_vpn_label.grid(row=6, column=0, padx=5, pady=2, sticky="e")
    server_vpn_label.grid(row=7, column=0, padx=5, pady=2, sticky="e")
    user_vpn_label.grid(row=8, column=0, padx=5, pady=2, sticky="e")
    password_vpn_label.grid(row=9, column=0, padx=5, pady=2, sticky="e")
    secretkey_vpn_label.grid(row=10, column=0, padx=5, pady=2, sticky="e")

    name_vpn_in.grid(row=6, column=1, padx=5, pady=2, sticky="")
    server_vpn_in.grid(row=7, column=1, padx=5, pady=2, sticky="")
    user_vpn_in.grid(row=8, column=1, padx=5, pady=2, sticky="")
    password_vpn_in.grid(row=9, column=1, padx=5, pady=2, sticky="")
    secretkey_vpn_in.grid(row=10, column=1, padx=5, pady=2, sticky="")

    ts = str(datetime.datetime.now())
    log.write('Connected at : ' + ts + ' \n')



def auto_in():#автозаполнение полей вверху
    host_in.delete(0, END)
    host_in.insert(0,str('192.168.1.1'))
    port_in.delete(0, END)
    port_in.insert(0,str('22'))
    user_in.delete(0, END)
    user_in.insert(0, str('admin'))
    pass_in.delete(0, END)
    pass_in.insert(0,str('123456'))
    ts = str(datetime.datetime.now())
    log.write('Use Auto in at : ' + ts + ' \n')

def start():# тестовый скрипт , основной код Paramico используем print
    global name_vpn
    global server_vpn
    global user_vpn
    global password_vpn
    global secretkey_vpn

    name_vpn = str(name_vpn_in.get())
    server_vpn = str(server_vpn_in.get())
    user_vpn = str(user_vpn_in.get())
    password_vpn = str(password_vpn_in.get())
    secretkey_vpn = str(secretkey_vpn_in.get())

    print('START TUNNEL')
    chan.send('no interface L2TP0 \n')  #для избежания создания множественных туннелей и петли маршрутизации
    time.sleep(1.5) #задержка хоста на обработку
    chan.send('interface L2TP0 \n')
    time.sleep(0.5)
    chan.send('description '+name_vpn+' \n')
    time.sleep(0.2)
    chan.send('role misc \n')
    time.sleep(0.5)
    chan.send('peer '+server_vpn+' \n')
    time.sleep(0.2)
    chan.send('no ipv6cp \n')
    time.sleep(0.2)
    chan.send('lcp echo 30 3 \n')
    time.sleep(0.2)
    chan.send('ipcp default-route \n')
    time.sleep(0.2)
    chan.send('ipcp name-servers \n')
    time.sleep(0.2)
    chan.send('ipcp dns-routes \n')
    time.sleep(0.2)
    chan.send('no ccp \n')
    time.sleep(0.2)
    chan.send('authentication identity '+user_vpn+' \n')
    time.sleep(0.2)
    chan.send('authentication password '+password_vpn+' \n')
    time.sleep(0.2)
    chan.send('ip dhcp client dns-routes \n')
    time.sleep(0.2)
    chan.send('ip dhcp client name-servers \n')
    time.sleep(0.2)
    chan.send('ip tcp adjust-mss pmtu \n')
    time.sleep(0.2)
    chan.send('ipsec preshared-key '+secretkey_vpn+' \n')
    time.sleep(0.4)
    chan.send('connect \n')
    time.sleep(0.2)
    chan.send('up \n')
    time.sleep(0.2)
    chan.send('exit \n')
    time.sleep(0.3)
    #chan.send('system configuration save \n')
    #в тестовом окружении нет смысла сохранять настройки в энергонезависимую память

    print('SYSTEM CONFIG SAVED')#вывод успешной работы скрипта

    ts = str(datetime.datetime.now())   #logging
    log.write('Starting Tunnel at : ' + ts + ' \n')


    global start_button
    global stop_button

    start_button.grid_remove()
    start_button = Button(bg='gray', fg='white', font='Consolas 12', text=" Start Tunnel",)
    start_button.grid(row=11, columnspan=2, ipadx=45, ipady=10, sticky="s")

    stop_button.grid_remove()
    stop_button = Button(bg='red', fg='white', font='Consolas 12', text=" Stop  Tunnel", command=stop)
    stop_button.grid(row=12, columnspan=2, ipadx=45, ipady=10, sticky="s")

def stop():#останавливаем туннель

    print('STOP TUNNEL')
    chan.send('no interface L2TP0 \n')
    time.sleep(0.2)
    #chan.send('system configuration save \n')
    print('STOPPED')

    global start_button
    global stop_button

    start_button.grid_remove()
    start_button = Button(bg='blue', fg='white', font='Consolas 12', text=" Start Tunnel", command=start)
    start_button.grid(row=11, columnspan=2, ipadx=45, ipady=10, sticky="s")

    stop_button.grid_remove()
    stop_button = Button(bg='gray', fg='white', font='Consolas 12', text=" Stop  Tunnel")
    stop_button.grid(row=12, columnspan=2, ipadx=45, ipady=10, sticky="s")

    ts = str(datetime.datetime.now())  # logging
    log.write('Stopping Tunnel at : ' + ts + ' \n')


ts = str(datetime.datetime.now())#timestamp
root = Tk() #создаем окно
root.title("SSH Client: ")
root.geometry('220x402')
root.protocol('WM_DELETE_WINDOW', window_deleted) # обработчик закрытия окна
root.resizable(False, False) # разрешение менять размер окна

log = open("log.txt","a")
log.write('Start logging: '+ts+' \n')

host = StringVar()  #Paramico parameters
port = StringVar()  #Paramico parameters
user = StringVar()  #Paramico parameters
pass1 = StringVar()  #Paramico parameters

name_vpn = StringVar()  #zuxel parameters
server_vpn = StringVar()  #zuxel parameters
user_vpn = StringVar()  #zuxel parameters
password_vpn = StringVar()  #zuxel parameters
secretkey_vpn = StringVar()  #zuxel parameters

host_label = Label(text='HOST', font='Consolas 9')
port_label = Label(text='PORT',font='Consolas 9')
user_label = Label(text='USER',font='Consolas 9')
pass_label = Label(text='PASSWORD',font='Consolas 9')

host_in = Entry()
port_in = Entry()
user_in = Entry()
pass_in = Entry()

name_vpn_in = Entry()
server_vpn_in = Entry()
user_vpn_in = Entry()
password_vpn_in = Entry()
secretkey_vpn_in = Entry()

host_label.grid(row=0,column = 0, padx=5, pady=3, sticky="e")
port_label.grid(row=1,column = 0, padx=5, pady=3, sticky="e")
user_label.grid(row=2,column = 0, padx=5, pady=3, sticky="e")
pass_label.grid(row=3,column = 0, padx=5, pady=3, sticky="e")

host_in.grid(row=0,column = 1, padx=5, pady=3, sticky="")
port_in.grid(row=1,column = 1, padx=5, pady=3, sticky="")
user_in.grid(row=2,column = 1, padx=5, pady=3, sticky="")
pass_in.grid(row=3,column = 1, padx=5, pady=3, sticky="")


connect_button = Button(bg='red',fg='white',font='Consolas 12', text="► Connect", command=make_connection)
connect_button.grid(row=4, column = 1, ipadx=28, ipady=10,)
auto_button = Button(bg='#56119b',fg='white',font='Consolas 12', text="AUTO", command=auto_in)
auto_button.grid(row=4, column = 0, ipadx=10, ipady=10,)
start_button = Button(bg='#c5ccd8',fg='#9a9ca0',font='Consolas 12', text=" Start Tunnel")
start_button.grid(row=11, columnspan = 2, ipadx=45, ipady=10,sticky="s" )
stop_button = Button(bg='#c5ccd8',fg='#9a9ca0',font='Consolas 12', text=" Stop  Tunnel")
stop_button.grid(row=12, columnspan = 2, ipadx=45, ipady=10, sticky="s" )

#ниже для блока "настройки временно недоступны" после скрывается командой remove
a5_label = Label(text=' ',font='Consolas 12')
a6_label = Label(text=' ',font='Consolas 5')
a7_label = Label(text='SETTINGS',font='Consolas 12')
a8_label = Label(text='TEMPORARY',font='Consolas 12')
a9_label = Label(text='NOT AVAILABLE',font='Consolas 12')
a10_label = Label(text=' ',font='Consolas 12')

a5_label.grid(row=5,columnspan = 2, sticky="s")
a6_label.grid(row=6,columnspan = 2, sticky="s")
a7_label.grid(row=7, columnspan = 2, sticky="s")
a8_label.grid(row=8, columnspan = 2, sticky="s")
a9_label.grid(row=9, columnspan = 2, sticky="s")
a10_label.grid(row=10,columnspan = 2, sticky="s")

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

root.mainloop()
