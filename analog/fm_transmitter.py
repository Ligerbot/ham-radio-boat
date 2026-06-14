import subprocess
from mutagen.wave import WAVE
import time

def tx(wavfile):
	audio = WAVE(str(wavfile))
	#TODO: make sure this program doesn't get stuck with the transmitter on
	#also TODO: bandpass filter so rpitx doesn't kill people with pacemakers
	#another TODO: make it so it doesn't ask the sudo password eveyr time or any time at all

	broadcast = subprocess.Popen(["sudo", "./fm_transmitting/testnfm.sh", "434", str(wavfile)],
		stdin=subprocess.PIPE,
		stderr=subprocess.DEVNULL
	)
	timenow = audio.info.length #get the length of the file to play
	time.sleep(timenow) #block
	broadcast.terminate() #terminate once file is done


#this library is basically a wrapper for the following command:
#sudo ./testnfm.sh 434 src/resources/SAMPLE_MONO_AUDIO.wav

