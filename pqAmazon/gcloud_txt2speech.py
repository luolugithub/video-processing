# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 下午5:22
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : gcloud_txt2speech.py
# @Software: PyCharm

"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
# export GOOGLE_APPLICATION_CREDENTIALS='/home/luolu/Downloads/my-project-82452-txt2speech-d2f355055141.json'
# export GOOGLE_CLOUD_PROJECT="my-project-82452-txt2speech"
# export GCLOUD_PROJECT=$GOOGLE_CLOUD_PROJECT
from google.cloud import texttospeech
from google.cloud import texttospeech_v1
from google.cloud import texttospeech_v1beta1
import os

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/luolu/PycharmProjects/video-processing/pqAmazon/my-project-82452-txt2speech-32250ea466e8.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/luolu/Downloads/my-project-82452-txt2speech-d2f355055141.json"
# Instantiates a client
client = texttospeech_v1.TextToSpeechClient()
print("client list: ", client.list_voices())
with open("/home/luolu/Desktop/amazontest/test/B07F81VDL2.txt", 'r') as file:
    txt_data = file.read().replace('\n', '')

# Set the text input to be synthesized
synthesis_input = texttospeech_v1.SynthesisInput(text=txt_data)

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech_v1.VoiceSelectionParams(
    language_code="en-US",
    name="en-US-Wavenet-E",
    ssml_gender=texttospeech_v1.SsmlVoiceGender.FEMALE

)
print(voice.name)
# Select the type of audio file you want returned
audio_config = texttospeech_v1.AudioConfig(
    audio_encoding=texttospeech_v1.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config, timeout=2000
)

# The response's audio_content is binary.
with open("output.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')
