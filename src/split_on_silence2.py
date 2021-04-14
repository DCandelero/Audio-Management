from pydub import AudioSegment
from pydub.silence import split_on_silence
import os


filename = '../Audios/audio3'

sound = AudioSegment.from_file(filename+'_adjusted.wav')

audio_chunks = split_on_silence(sound, 
    # must be silent for at least half a second
    min_silence_len=750,

    # consider it silent if quieter than -16 dBFS
    silence_thresh=-32
)

if not os.path.isdir(filename+'_splitted'):
    os.mkdir(filename+'_splitted')

print("Number of chunks splitteds: ", len(audio_chunks))

for i, chunk in enumerate(audio_chunks):
    out_file = filename+"_splitted/chunk(2)-{0}.wav".format(i)
    print("exporting", out_file)
    chunk.export(out_file, format="wav")
