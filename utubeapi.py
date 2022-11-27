from youtube_transcript_api import YouTubeTranscriptApi
import speech_recognition as sr
from googletrans import Translator
from re import sub
import sys
def generate_transcript(id):
	transcript = YouTubeTranscriptApi.get_transcript(id)
	script = ""

	for text in transcript:
		t = text["text"]
		if t != '[Music]':
			script += t + " "
	return script, len(script.split())
# url = input("Enter youtube video link other than shorts : ")
# print("Processing...Hold tight")
# a = url.split('=')
# b = a[1:]
# c = " ".join(b)
# id = c
# transcript, no_of_words = generate_transcript(id)
# print("\n",transcript)
# translator = Translator()
# lang = input("\nEnter first two letters of your desired language : ")
# words = (transcript.split())
# for i in range(0,len(words),20):
#     my_list = words[i:i+20]
#     string = " ".join(my_list)
#     text = string
#     output = translator.translate(text,dest=lang)

#     print(output.text)
# print("\nThank you :) \n")