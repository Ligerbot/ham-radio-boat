import sys
import signing
id_table = []
rx_table = []

while True:
	msg = input("msg: ")
	id = input("id: ")
	out = signing.sign(msg, id)
	print(out)

	recieved = str(sys.stdin.read())
	print(signing.verify(recieved, rx_table))
