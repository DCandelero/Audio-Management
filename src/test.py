from pydub import AudioSegment
from pydub.silence import split_on_silence
import os
import requests
import json
import unidecode
import base64

def split_audio(filename):
    sound = AudioSegment.from_file(filename+'_adjusted.wav')

    audio_chunks = split_on_silence(sound, 
        # must be silent for at least half a second
        min_silence_len=1000,

        # consider it silent if quieter than -16 dBFS
        silence_thresh=-32
    )

    if not os.path.isdir(filename+'_splitted'):
        os.mkdir(filename+'_splitted')

    print("Number of chunks splitteds: ", len(audio_chunks))

    base64chunks = []
    for i, chunk in enumerate(audio_chunks):
        out_file = filename+"_splitted/chunk(2)-{0}.wav".format(i)
        print("exporting", out_file)
        chunk.export(out_file, format="ogg")

        f1 = open(out_file, 'rb')
        encoded_f1 = base64.b64encode(f1.read())
        base64chunks.append(str(encoded_f1,'ascii', 'ignore'))
    
    return base64chunks

serverurl = '104.131.48.82'
localurl = '127.0.0.1:8080'

data_query_auth = '{"username": "desenvolvimento@tagchat.com", "password": "Devs@tagchat!@#"}'
my_headers_auth = {'Content-Type': 'application/json'}
response = requests.post('http://'+localurl+'/auth', data=data_query_auth, headers=my_headers_auth)

access_token = 'JWT ' + str(response.json()['access_token'])
print(access_token)

base64chunks = split_audio('../Audios/audio3')
final_response = ""

my_headers = {'Authorization': access_token}
for base64chunk in base64chunks:
    data_query = {"base64audio": base64chunk}
    response = requests.post('http://'+serverurl+'/audio-to-text', data=json.dumps(data_query), headers=my_headers)
    print(response.json())
    print(type(response))
    print(response)
    final_response += " " + response.json()

print(final_response)