# Import packages to convert an play audio
from pydub import AudioSegment
from pydub.playback import play  

filename = './Audios/audio3'

# convert .ogg to .wav
sound = AudioSegment.from_ogg(filename+'.ogg')
sound.export(filename+'.wav', format='wav')

# Play
playaudio = AudioSegment.from_file(filename+'.wav', format='wav')
play(playaudio)

