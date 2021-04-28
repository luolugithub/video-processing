# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 下午4:47
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : change_voice.py
# @Software: PyCharm
# !/usr/bin/env python

# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Cloud Text-To-Speech API sample application .
Example usage:
    python quickstart.py
"""
import os

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/luolu/PycharmProjects/video-processing/pqAmazon/my-project-82452-txt2speech-32250ea466e8.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/luolu/Downloads/my-project-82452-txt2speech-d2f355055141.json"

# def run_quickstart():
#     # [START tts_quickstart]
#     """Synthesizes speech from the input string of text or ssml.
#     Note: ssml must be well-formed according to:
#         https://www.w3.org/TR/speech-synthesis/
#     """
#     from google.cloud import texttospeech
#
#     # Instantiates a client
#     client = texttospeech.TextToSpeechClient()
#
#     # Set the text input to be synthesized
#     synthesis_input = texttospeech.SynthesisInput(text="Hello, World!")
#
#     # Build the voice request, select the language code ("en-US") and the ssml
#     # voice gender ("neutral")
#     voice = texttospeech.VoiceSelectionParams(
#         language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE.NEUTRAL
#     )
#
#     # Select the type of audio file you want returned
#     audio_config = texttospeech.AudioConfig(
#         audio_encoding=texttospeech.AudioEncoding.MP3
#     )
#
#     # Perform the text-to-speech request on the text input with the selected
#     # voice parameters and audio file type
#     response = client.synthesize_speech(
#         input=synthesis_input, voice=voice, audio_config=audio_config
#     )
#
#     # The response's audio_content is binary.
#     with open("output.mp3", "wb") as out:
#         # Write the response to the output file.
#         out.write(response.audio_content)
#         print('Audio content written to file "output.mp3"')
#     # [END tts_quickstart]

def list_voices():
    """Lists the available voices."""
    from google.cloud import texttospeech_v1beta1

    client = texttospeech_v1beta1.TextToSpeechClient()

    # Performs the list voices request
    voices = client.list_voices()

    for voice in voices.voices:
        # Display the voice's name. Example: tpc-vocoded
        print(f"Name: {voice.name}")

        # Display the supported language codes for this voice. Example: "en-US"
        for language_code in voice.language_codes:
            print(f"Supported language: {language_code}")

        ssml_gender = texttospeech_v1beta1.SsmlVoiceGender(voice.ssml_gender)

        # Display the SSML Voice Gender
        print(f"SSML Voice Gender: {ssml_gender.name}")

        # Display the natural sample rate hertz for this voice. Example: 24000
        print(f"Natural Sample Rate Hertz: {voice.natural_sample_rate_hertz}\n")


if __name__ == "__main__":
    list_voices()
