import socket
from threading import Thread
from tkinter import *

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = '127.0.0.1'
PORT = 8000

client.connect((IP, PORT))

print('Server has started...')

class GUI:
    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()

        self.login = Toplevel()
        self.login.title("Login")

        self.login.resizable(width=False, height=False)
        self.login.configure(width=400,height=300)

        self.pls = Label(self.login,
                         text = "Please login to continue",
					     justify = CENTER,
					     font = "Helvetica 14 bold")
        self.pls.place( relheight = 0.15,
                        relx = 0.2,
                        rely = 0.07)
        self.nameLabel = Label(self.login,
                               text = "Name: ",
                               font = "Helvetica 12")
        self.nameLabel.place(relheight= 0.2,
                             relx = 0.1,
                             rely = 0.2)
        self.nameEntry = Entry(self.login,
                               font = "Helvetica 14")
        self.nameEntry.place(relwidth=0.4,
                             relheight=0.12,
                             relx=0.35,
                             rely=0.2)
        self.nameEntry.focus()
        self.button = Button(self.login,
                             text="CONTINUE",
                             font="Helvetica 14 bold",
                             command= lambda: self.goAhead(self.nameEntry.get()))
        self.button.place(relx=0.4,rely=0.5)
        self.Window.mainloop()
    def goAhead(self,name):
        self.login.destroy()
        self.name = name
        rcv = Thread(target=self.receive)
        rcv.start()
    def receive(self):
        while True:
            try:
                message = client.recv(2048).decode('utf-8')
                if message == 'NICKNAME':
                    client.send(self.name.encode('utf-8'))
                else:
                    pass
            except:
                print("An error occured!")
                client.close()
                break


g = GUI()

# def write(client_socket):
#     while True:
#         message = input()
#         client_socket.send(message.encode('utf-8'))

# receive_thread = Thread(target=receive, args=(client_socket,))
# receive_thread.start()

# write_thread = Thread(target=write, args=(client_socket,))
# write_thread.start()
