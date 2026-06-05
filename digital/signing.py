#simple library that claude helped make for signing messages
import cryptography.hazmat.primitives.serialization
from cryptography.exceptions import InvalidSignature
import base64
id_table = []
rx_table = []
def sign(text, id):
	global id_table
	with open("private.pem", "rb") as f:
		privatekey = f.read()
		f.close()
	loaded = cryptography.hazmat.primitives.serialization.load_pem_private_key(privatekey, password=None)
	text = text + "\nid: " + str(id)
	encoded = text.encode("ascii")
	signature = loaded.sign(encoded)
	b64one = base64.b64encode(signature).decode()
	result = text + "\nsignature: " + b64one
	id_table.append(id)
	return result

def verify(text, rx_table):
	msg, id, sig_line = text.strip().splitlines()
	sig = base64.b64decode(sig_line.replace("signature: ",""))
	id = id.replace("id: ", "")

	if id in rx_table:
		print("Replay attack detected")
		return False, None, None
	else:
		rx_table.append(id) #this id can't be used again
		with open("public.pem", "rb") as f:
			pubkey = f.read()
			f.close()
		pub = cryptography.hazmat.primitives.serialization.load_pem_public_key(pubkey)
	try:
		pub.verify(sig, msg.encode("ascii"))
		return True, msg, rx_table
	except InvalidSignature:
		return False, None, None
