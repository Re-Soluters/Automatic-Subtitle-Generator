from fileinput import filename
from django.shortcuts import render
from flask import Flask,render_template,request
from gtts import gTTS
from playsound import playsound
import os
import pyttsx3 as p
import moviepy.editor
import speech_recognition as sr
from googletrans import Translator
from tkinter.filedialog import *
import speech_recognition as sr
import sys
from youtube_transcript_api import YouTubeTranscriptApi
import speech_recognition as sr
from googletrans import Translator
from tkinter.filedialog import *
from re import sub
import sys
from pytube import YouTube
import moviepy.editor
import speech_recognition as sr
from googletrans import Translator
from tkinter.filedialog import *
import sys
import utubeapi
from googletrans import Translator
import moviepy.editor
from pytube import YouTube
import os
import moviepy.editor
import speech_recognition as sr
from googletrans import Translator
from tkinter.filedialog import *
import sys
app = Flask(__name__)
@app.route('/', methods=['POST','GET'])
def index_home():
    return render_template('homepagemain.html')
@app.route('/ltt', methods=['POST','GET'])
def index_tool1():
    if request.method=='POST':
        tool1=request.form.get('link')
        url = tool1
        a = url.split('=')
        b = a[1:]
        c = " ".join(b)
        id = c
        transcript, no_of_words = utubeapi.generate_transcript(id)
        translator = Translator()
        lang = request.form.get('lang')
        words = (transcript.split())
        s=''
        for i in range(0,len(words),20):
            my_list = words[i:i+20]
            string = " ".join(my_list)
            text = string
            output = translator.translate(text,dest=lang)
            s+=output.text
        return render_template('tool1.html',sn=s)
    return render_template('tool1.html')    
@app.route('/yvd', methods=['POST','GET'])
def index_2():
    if request.method=='POST':
        tool2=request.form.get('url')
        destination = "D:\Dream Project"
        video_link = tool2
        try:
            video = YouTube(video_link)
            audio = video.streams.filter(only_audio=True, file_extension='mp4').first()
            audio.download()
        except:
            print()
        return render_template('2.html')
    return render_template("2.html")
@app.route('/ae', methods=['POST','GET'])
def index_tool3():
    if request.method=='POST':
        tool3=request.form.get('link1')
        yt = YouTube(str(tool3))
        video = yt.streams.filter(only_audio=True).first()
        destination = "D:\Dream Project"
        out_file = video.download(output_path=destination)
        new_file = '.mp3'
        os.rename(out_file, new_file)
    return render_template('tool3.html')
@app.route('/ovt', methods=['POST','GET'])
def index_4():
    return render_template('4.html')
@app.route('/ovt1', methods=['POST','GET'])
def index_41():
    vi_au = askopenfilename()
    video = moviepy.editor.VideoFileClip(vi_au)
    audio = video.audio
    audio.write_audiofile("newaudio.wav")
    r = sr.Recognizer()
    with sr.AudioFile("newaudio.wav") as source:
            audio = r.record(source)
            mer_text = r.recognize_google(audio)
            print(mer_text)
    translator = Translator()
    lang = request.form.get('lang')
    print(lang)
    words = (mer_text.split())
    sa = ''
    for i in range(0,len(words),20):
        my_list = words[i:i+20]
        string = " ".join(my_list)
        text = string
        output = translator.translate(text,dest=lang)
        sa+=output.text
    print(sa)
    return render_template('4.html',sa=sa)
@app.route('/ttt', methods=['POST','GET'])
def index_tool5():
    if request.method=='POST':
        t1=request.form.get('text')
        tool5=request.form.get('lang')
        translator = Translator()
        a = t1
        result=''
        words = (a.split())
        for i in range(0,len(words),20):
            my_list = words[i:i+20]
            string = " ".join(my_list)
            text = string
            output = translator.translate(text,dest=tool5)
            print(output.text)
            result += output.text
        return render_template('tool5.html',x = result)
    return render_template('tool5.html')
@app.route('/ova', methods=['POST','GET'])
def index_6():
    return render_template('6.html')
@app.route('/ova1', methods=['POST','GET'])
def index_61():
    vi_au = askopenfilename()
    video = moviepy.editor.VideoFileClip(vi_au)
    audio = video.audio
    audio.write_audiofile("urnewaudio.wav")
    return render_template('6.html')
@app.route('/aft', methods=['POST','GET'])
def index_7():
    return render_template('tool7.html')
@app.route('/aft1', methods=['POST','GET'])
def index_71():
    r = sr.Recognizer()
    vi_au = askopenfilename()
    with sr.AudioFile(vi_au) as source:
            audio = r.record(source)
            text = r.recognize_google(audio)
    tool7=request.form.get('lang')
    translator = Translator()
    output = translator.translate(text,dest=tool7)
    c = output.text
    return render_template('tool7.html',c=c)
@app.route('/tts', methods=['POST','GET'])
def index_tts():
    if request.method=='POST':
        t1=request.form.get('entry')
        engine = p.init()
        en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        engine.setProperty('voice', en_voice_id)
        engine.setProperty('rate', 130)
        def speak(audio):
            engine.say(audio)
            engine.runAndWait()
        speak(t1)
        return render_template('tool8.html',z=t1)
    return render_template('tool8.html')
@app.route('/att', methods=['POST','GET'])
def mic1():
    return render_template('tool9.html')
@app.route('/att1', methods=['POST','GET'])
def mic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        text = r.recognize_google(audio)
        a = text
    return render_template('tool9.html',a = a)
@app.route('/contact_us', methods=['POST','GET'])
def index_contact():
    if request.method=='POST':
        t1=request.form.get('fname')
        t2=request.form.get('email')
        t3=request.form.get('sub')
        t4=request.form.get('msg')
        return render_template('card.html',x=t1)
    return render_template('contact.html')
@app.route('/abs', methods=['POST','GET'])
def index_abt():
    return render_template('about_us.html')
app.run(debug=True,port=1718)