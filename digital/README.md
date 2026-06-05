# digital communications

Put all of the digital communications related programs here.

This includes remotely controlling parts of the boat and telemetry.

The baud rate doesn't need to be too high maybe a rate of 30 will be fine. I think it is worth adding error correction of some sort when we send it commands so it doesn't recieve the wrong command.

Telemetry probably doesn't require error correction.

The lower the baudrate, the longer it takes to transmit, while the higher the baud rate, the less time to transmit until it is so high a bit of noise requires a retransmission.

# FSK library

I made a simple library for python to send text using FSK. This requires the program `minimodem` which can be installed on Debian by running `sudo apt install minimodem`.

To use it in a program import it by adding `import fsk`.

To send text add the line `fsk.send_text("message", baud rate in integer)`

This function is blocking, meaning that it won't let the program continue to the next line until it is done playing.

To recieve, add `output = fsk.recive_text(300, 0.1, None, 3)` to your program, where output is a string recieved by the function. In this case, 300 is the baud rate and 0.1 is the confidence (must always be a float).

The first NoneType entry is for the string delimiter, which means when it recieves a certain string the function stops recieving and returns what it recieved. The 3 in this example is the amount of characters it recieves before exiting. The last two can be used at the same time but at least one must be used otherwise the function never exits.

This is probably just useful for sending telemetry. Use the other library for error tolerant things.

# Data Link Layer protocol

(I added the signing library to this now)

(copied from the repository)

The goal of this project to to make my own data link layer protocol for ham radio. I've tried to use AX.25, but it is seemingly impossible to decode it using AFSK in python.

Eventually, when this is finished, the program will be importable to other python programs to be used as a library. I want to move my other repo rtty-email to use this protocol.

The goal of this is for reliable communications even when there is lots of noise. Currently, the program chunks the message to be sent into ten character long pieces. Then, it encapsulates it in a frame which looks something like this: `{|{|{|length of packet|||body|}|}|}error correcting bits`. I want to add functionality to make one side request a higher speed if there is less noise, or a lower speed if there is more noise.

For every frame, the recieving side needs to ackgnowledge, otherwise the sending side retransmits the frame.

# Library Usage

To use this as a library run `import mac` then to send you run `mac.send_data("data here")` or to recieve `output = mac.recieve()`.

# Signing

I will add documentation later, right now I'm too lazy so read signing-test-example.py
