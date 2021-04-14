from pydub import AudioSegment
import os

filename = '../Audios/audio1'

if not os.path.isdir(filename+'_splitted'):
    os.mkdir(filename+'_splitted')

audio = AudioSegment.from_file(filename+'.wav')
lengthaudio = len(audio)
print("Length of Audio File: ", lengthaudio)

start = 0
split_threshold = 6000 # 10 seconds
end = 0
counter = 0

while start < lengthaudio:
    end += split_threshold
    print(start, end)
    chunk = audio[start:end]
    splitted_filename = filename+'_splitted'+'/chunk'+str(counter)+'.wav'
    chunk.export(splitted_filename, format='wav')
    counter += 1
    start += split_threshold


