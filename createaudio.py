import json
import random
import pyttsx3 
from pydub import AudioSegment
from gtts import gTTS

import fileinput
import mutagen
from mutagen.mp3 import MP3

def get_audio_length(file_name):
    audio = MP3(file_name)
    audio_info = audio.info
    return float(audio_info.length)

if __name__ == '__main__':

    f = open('posts.json')
    posts = json.load(f)

    for index, post in enumerate(posts['posts']):
        print(f'Creating audio for video {index + 1}')

        file_name = f'audio/{index}_post.mp3'
        gTTS(post['post'], tld="ca").save(file_name)
        
        post['post_audio'] = (file_name, get_audio_length(file_name))
        post['comment_audio'] = []

        for cindex, comment in enumerate(post['top_comments']):
            file_name = f'audio/{index}_{cindex}_post.mp3'
            gTTS(comment, tld="ca").save(file_name)


            post['comment_audio'].append((file_name, get_audio_length(file_name)))

    json_object = json.dumps(posts, indent=4)
    with open("posts_and_audio.json", "w") as outfile:
        outfile.write(json_object)
