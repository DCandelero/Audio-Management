from pydub import AudioSegment

def speed_change(sound, speed, filename):
    audio_accelerated = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    })

    new_filename = filename+'_accelerated({}).wav'.format(speed)
    audio_accelerated.export(new_filename, format='wav')

filename = '../Audios/audio1'

sound = AudioSegment.from_file(filename+'.wav')

speed_change(sound, 1.5, filename)



