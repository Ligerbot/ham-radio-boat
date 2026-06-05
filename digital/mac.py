import local_libraries.tones as tones
import time
import reedsolo
import subprocess
import local_libraries.signing as signing

rsc = reedsolo.RSCodec(10)
id_table, rx_table = signing.load_blacklist()

#file = True
def recieve():
	global rx_table
	global id_table
	global proc
	global newframes
	newframes = []
	breaknow = False
	proc = subprocess.Popen(
		['minimodem', '--rx', '300', '--confidence', '0.1', '-q'],
		stdout=subprocess.PIPE,
		stderr=subprocess.DEVNULL
	)
	while not breaknow:
		recieved = proc.stdout.readline()
#		print(recieved)
		message = unframe(recieved)
#		print(message)
		if message != None and message != "":
			genuine, message, rx_tables = signing.verify(message, rx_table)
			if genuine:
				return message
			else:
				print("Message is from a replay attack")
				return None
def unframe(raw):
	global breaknow
	global newframes
	splitted = raw.split(b"{|{|{|")
	breaknow = False
	for item in splitted:
		if breaknow:
			break
		if b"|}|}|}" in item or b"|||" in item:
			try:
				fixed = rsc.decode(b"{|{|{|" + item)[0]
				tones.play(1000, 500)
				newframes.append(fixed) #does this fix it?
			except Exception as e:
				print(e)
		elif b"{OK}" in item:
			breaknow = True
			tones.play(1000, 500)
			content = ""
			i = 0
			for frame in newframes:
				frame = frame.replace(b"{|{|{|", b"")
				frame = frame.split(b"|}|}|}")[0] #this instead of the commented line below makes it so that there aren't extra parity bits messing stuff up
				text = frame.split(b"|||")[1]
				sequencenum = int(frame.split(b"|||")[0])
				text = text.decode("ascii", errors="ignore")
				if sequencenum == i:
					content = content + str(text)
				else:
					i = i - 1
				i = i + 1
			#	print(content)
			return content
def chonk(message):
	if len(message) <= 4:
		print("Message does not need to be chunked")
		oneitemarray = []
		oneitemarray.append(message)
		return oneitemarray
	else:
		chunks = []
		i = 0
		while i < len(message):
			start = i
			end = i + 10
			chunk = message[start:end]
			chunks.append(chunk)
			i += 10
		return chunks
def format(message):
	chunks = chonk(message)
	frames = []
	i = 0
	for chunk in chunks:
		thebytes = chunk.encode("ascii")

		if i <= 9:
			padded = b"0" + bytes(str(i), "ascii")
		frame = b"{|{|{|" + padded + b"|||" + thebytes + b"|}|}|}"
		frames.append(rsc.encode(frame))
		i = i + 1
	return frames

def send(message):
	global proc
#	print("Sending: " + str(message))
	proc = subprocess.Popen(
		['minimodem', '--tx', '300', '--confidence', '0.3'],
		stdin=subprocess.PIPE,
		stderr=subprocess.DEVNULL
	)
	proc.stdin.write(message)
	proc.stdin.close()
	proc.wait()
	proc.terminate()
	proc.terminate()
	proc.terminate()
	proc.terminate()

def gen_rand_id():
	global rx_table
	global id_table
	while True:
		randnum = int(random.random()* 1000000000000)
		if randnum not in id_table:
			break
		else:
			print("Random number taken, getting another")
	return randnum
def send_data(msg):
	global id_table
	global rx_table
	id = gen_rand_id()
	msg = signing.sign(msg, id)
	frames = format(msg)
	for frame in frames:
		while True:
			send(b"\n" + bytes(frame) + b"\n")
			if tones.listen(1000, duration_ms=500):
				print("Ackgnowledged")
				break
			print("Resending frame")
	while True:
		if tones.listen(1000, duration_ms=500):
			print("Transmission done")
			break
		print("Retransmitting connection close signal")
		send(b"\n{OK}\n")

if __name__ == "__main__":
	try:
		role = input("Sender(1) or reciever(2): ")
		if role == "1":
			msg = input("Message: ")
			frames = format(msg)

			for frame in frames:
				while True:
					send(b"\n" + bytes(frame) + b"\n")
					if tones.listen(1000, duration_ms=500):
						print("Got ackgnowledgement, continuing to next packet")
						break
					print("Didn't recieve ackgnowledgement. Resending the frame")
	#			time.sleep(1)
	#			send(b"\n" + bytes(frame) + b"\n")
			while True:
				if tones.listen(1000, duration_ms=500):
					print("Done")
					break
				print("Never recieved ack")
				send(b"\n{OK}\n{OK}\n")
		elif role == "2":
			print(recieve())
		else:
			print("Invalid option")
	finally:
		proc.terminate()
		proc.terminate()
		proc.terminate()
		proc.terminate()
		proc.terminate()
		proc.terminate()
		print("Killed off minimodem")
		signing.save_blacklist()
		print("Saved blacklist")
