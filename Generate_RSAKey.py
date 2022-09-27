from Crypto.PublicKey import RSA


def Generate_Key():
	key = RSA.generate(1024)

	public_key = key.publickey().exportKey()
	with open('public.pem','wb') as f:
		f.write(public_key)

	private_key = key.exportKey()
	with open('private.pem', 'wb') as f:
		f.write(private_key)

Generate_Key()







