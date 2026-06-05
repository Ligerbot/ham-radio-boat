# digital communications

Put all of the digital communications related programs here.

This includes remotely controlling parts of the boat and telemetry.

The baud rate doesn't need to be too high maybe a rate of 30 will be fine. I think it is worth adding error correction of some sort when we send it commands so it doesn't recieve the wrong command.

Telemetry probably doesn't require error correction.

The lower the baudrate, the longer it takes to transmit, while the higher the baud rate, the less time to transmit until it is so high a bit of noise requires a retransmission.

# FSK library

I made a simple library for python to send text using FSK.

To use it in a program import it by adding `import fsk`.

To send text add the line `fsk.send_text("message", baud rate in integer)`

This function is blocking, meaning that it won't let the program continue to the next line until it is done playing.

To recieve, add `output = fsk.recive_text(300, 0.1, None, 3)` to your program, where output is a string recieved by the function. In this case, 300 is the baud rate and 0.1 is the confidence (must always be a float).

The first NoneType entry is for the string delimiter, which means when it recieves a certain string the function stops recieving and returns what it recieved. The 3 in this example is the amount of characters it recieves before exiting. The last two can be used at the same time but at least one must be used otherwise the function never exits.
