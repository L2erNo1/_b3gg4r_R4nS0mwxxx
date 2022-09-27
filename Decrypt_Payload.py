
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
import sys
import getopt



def Decrypt_Key(a_message, private_key):

    a_message = base64.b64decode(a_message)
    decryptor = PKCS1_OAEP.new(private_key)
    decrypted_msg = decryptor.decrypt(a_message)

    print('[***] PASSWORD: \"'+ decrypted_msg.decode('utf-8')+'\" [***]')

    print("Decrypted:", len(decrypted_msg))
    return decrypted_msg

def Get_Input():

    payload = None

    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, 'p:')
    except:
        print('Error')

    for opt, arg in opts:
        if opt in ['-p']:
            payload = arg

    return payload

data = Get_Input()
#data = base64.b64decode(data)
#print(len(data))

x510pem = """-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----"""

private_key = RSA.import_key(x510pem)

Decrypt_Key(data, private_key)
