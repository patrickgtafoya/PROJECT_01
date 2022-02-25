import tkinter as tk
from time import sleep


class Application:
    def __init__(self):
        # application layout
        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.root.title('Application')
        # status
        self.status = False
        self.status_dict = {False: ['Disconnected', 'grey'], True: ['Connected', 'green']}
        self.status_label = tk.Label(text=self.status_text(),
                                     width=20,
                                     height=5,
                                     fg='black',
                                     bg=self.status_color())
        self.status_label.place(x=200, y=10)
        # buttons
        self.default_color = 'grey'
        self.count = 0
        self.con_button = tk.Button(self.root,
                                    text='Connect',
                                    width=10,
                                    height=2,
                                    bg=self.default_color,
                                    command=self.connect)
        self.con_button.place(x=190, y=100)
        self.dis_button = tk.Button(self.root,
                                    text='Disconnect',
                                    width=10,
                                    height=2,
                                    bg=self.default_color,
                                    command=self.disconnect)
        self.dis_button.place(x=275, y=100)
        # run application
        self.root.mainloop()

    def connect(self):
        self.status = True
        self.status_label.configure(text=self.status_text(),
                                    bg=self.status_color())

    def disconnect(self):
        self.status = False
        self.status_label.configure(text=self.status_text(), background=self.status_color())

    def status_text(self):
        if self.status:
            return self.status_dict[True][0]
        else:
            return self.status_dict[False][0]

    def status_color(self):
        if self.status:
            return self.status_dict[True][1]
        else:
            return self.status_dict[False][1]

    def change_status(self):
        if self.status:
            self.status = False
        else:
            self.status = True


def init_gui():
    app = Application()


def main():
    init_gui()


if __name__ == "__main__":
    main()
