import os

from telegram.ext import Updater, Commandhandler, Messagehandler, filters

from pytube import YouTube

def start(update ,context):
    
    update.message.reply_text("Bienvenue!Veuillez utiliser ce service pour télécharger")

def download_video(update ,context):

 lien=input("Veuillez entrer le lien de la vidéo svp: ")

def YouTube(lien):
 
 def yt():

  print(yt.title)

yt=YouTube('lien')

yt.streams.get_highest_resolution()

video.download()

def convert_to_mp3(update ,context):
    
    video_filename=video.default_filename

    mp3_filename=os.path.splitext(video_filename).mp3

    def main():
        
        updater=updater(token , use_context=true)

dp=updater.dipatcher

updater.start_polling()

updater.idle()

if_name_=="_main_"

token="6219615016:AAHI0Og5eSSiFih-4dZ57Wez5rSpWB"

if  __name__ =="__main__": 

    main()