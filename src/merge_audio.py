import os
from pydub import AudioSegment
import glob

filename = './Audios/audio1'
dirname = filename+'_splitted'

if not os.path.isdir(dirname):
    os.mkdir(dirname)

wavfiles = glob.glob(dirname+'/chunk*.wav')
print(wavfiles)


# Loopting each file and include in Audio Segment
wavs = [AudioSegment.from_wav(wav) for wav in wavfiles]

combined = wavs[0]
for wav in wavs[1:]:
    combined = combined.append(wav)

combined.export(filename+'_merged.wav', format='wav')

