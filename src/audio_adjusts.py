from pydub import AudioSegment

filename = '../Audios/audio3'

sound = AudioSegment.from_file(filename+'.wav')

print("----------Before Conversion--------")
print("Frame Rate", sound.frame_rate)
print("Channel", sound.channels)
print("Sample Width",sound.sample_width)

# Setting Frame rate as 16KHz
sound = sound.set_frame_rate(16000)
# Setting channel as mono
sound = sound.set_channels(1)
# Setting width as 16 bit Signed Integer PCM
sound = sound.set_sample_width(2)
sound.export(filename+"_adjusted.wav", format ="wav")

print("----------After Conversion--------")
print("Frame Rate", sound.frame_rate)
print("Channel", sound.channels)
print("Sample Width",sound.sample_width)