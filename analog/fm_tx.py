import subprocess
from mutagen.wave import WAVE
import time

audio = WAVE("input.wav")
broadcast = subprocess.Popen(["sudo", "./testnfm.sh", "434", "input.wav"],
	stdin=subprocess.PIPE,
	stderr=subprocess.DEVNULL
)
timenow = audio.info.length
time.sleep(timenow)
broadcast.terminate()

#runs sudo ./testnfm.sh 434 src/resources/SAMPLE_MONO_AUDIO.wav

