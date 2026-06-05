import local_libraries.signing as signing
#id_table = []
#rx_table = []
id_table, rx_table = signing.load_blacklist()
try:
	while True:
		#"sending" side:
		msg = input("msg: ")
		id = input("id: ")
		out = signing.sign(msg, id)
		print(out.replace("\n", "\\n")) #this replace \n with \\n is just so it prints how it actually is

		#"recieving" side
		_, __, rx_tables = signing.verify(out, rx_table)
		print("Is a real message: " + str(_) + ", message: " + str(__))
finally:
	signing.save_blacklist()
