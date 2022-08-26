from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import inference
import requests
import time
import os
import argparse

from pydub import AudioSegment

import os
import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
from asteroid.asteroid.models import BaseModel

updater = Updater("5751698292:AAE6hwgk9WBuFSjtSaSZRywIyhxRJ82_QeY",
                  use_context=True)

base_url = "https://api.telegram.org/bot5751698292:AAE6hwgk9WBuFSjtSaSZRywIyhxRJ82_QeY/sendAudio"


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello! Welcome to the Audio Source Separation Bot.Please write /help to see the commands available.")


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :
	/separate - To separate sources
	/receive to receive your voice
    /est1 to receive the first source estimation
    /est2 to recieve the second source estimation

    Now you can send your voice!
    Note that your voice must be in mp3 format    
    """)


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)


def downloader(update: Update, context: CallbackContext):
    context.bot.get_file(update.message.document).download()

    # writing to a custom file
    with open("file.mp3", 'wb') as f:
        context.bot.get_file(update.message.document).download(out=f)
    # with open("file.wav", 'wb') as f:
    #     context.bot.get_file(update.message.document).download(out=f)
    #     os.system(f"ffmpeg -i C:/Users/A/Desktop/کارآموزی/Code/last/file.wav C:/Users/A/Desktop/کارآموزی/Code/last/file.mp3")

def File_Handler():
    file_path = 'voice.mp3'
    if os.path.isfile(file_path):
        os.remove(file_path)
    file_path = 'voice.wav'
    if os.path.isfile(file_path):
        os.remove(file_path)
    file_path = 'voice_est1.mp3'
    if os.path.isfile(file_path):
        os.remove(file_path)
    file_path = 'voice_est2.mp3'
    if os.path.isfile(file_path):
        os.remove(file_path)
    file_path = 'voice_est1.wav'
    if os.path.isfile(file_path):
        os.remove(file_path)
    file_path = 'voice_est2.wav'
    if os.path.isfile(file_path):
        os.remove(file_path)


def voice_handler(update: Update, context: CallbackContext):
    bot = context.bot
    File_Handler()
    file = bot.getFile(update.message.voice.file_id)
    file.download('C:/Users/A/Desktop/کارآموزی/Code/last/voice.mp3')

    update.message.reply_text("""Your voice is received!
    You can use command /separate - To separate sources
    and command /receive to receive your original voice
    """)


def audio_handler(update: Update, context: CallbackContext):
    bot = context.bot
    File_Handler()
    file = bot.getFile(update.message.audio.file_id)
    file.download('C:/Users/A/Desktop/کارآموزی/Code/last/voice.mp3')

    update.message.reply_text("Voice downloaded!")



def separate(update: Update, context: CallbackContext):
    # chat_id = update.message.chat_id
    update.message.reply_text("Running...")
    # exec(open("main.py").read())

    model = BaseModel.from_pretrained("mpariente/DPRNNTasNet-ks2_WHAM_sepclean")
    # model = BaseModel.from_pretrained("mpariente/ConvTasNet_WHAM_sepclean")
    # model = BaseModel.from_pretrained("mpariente/DPRNNTasNet_WHAM!_sepclean")
    # model = BaseModel.from_pretrained("mpariente/DPRNNTasNet(ks=16)_WHAM!_sepclean")

    # for separate 3 sources use this model
    # model = BaseModel.from_pretrained("tmirzaev-dotcom/ConvTasNet_Libri3Mix_sepnoisy")

    # model = BaseModel.from_pretrained("JorisCos/ConvTasNet_Libri1Mix_enhsingle_16k")
    # model = BaseModel.from_pretrained("JorisCos/ConvTasNet_Libri2Mix_sepnoisy_16k")
    # model = BaseModel.from_pretrained("mpariente/ConvTasNet_Libri1Mix_enhsingle_8k")
    # model = BaseModel.from_pretrained("JorisCos/ConvTasNet_Libri2Mix_sepclean_16k")
    # model = BaseModel.from_pretrained("JorisCos/DCCRNet_Libri1Mix_enhsingle_16k")
    # model = BaseModel.from_pretrained("cankeles/DPTNet_WHAMR_enhsingle_16k")
    # model = BaseModel.from_pretrained("JorisCos/DPRNNTasNet-ks2_Libri1Mix_enhsingle_16k")
    # model = BaseModel.from_pretrained("JorisCos/DPTNet_Libri1Mix_enhsingle_16k")
    # model = BaseModel.from_pretrained("julien-c/DPRNNTasNet-ks16_WHAM_sepclean")
    # model = BaseModel.from_pretrained("Awais/Audio_Source_Separation")
    # model = BaseModel.from_pretrained("cankeles/ConvTasNet_WHAMR_enhsingle_16k")
    # model = BaseModel.from_pretrained("JorisCos/ConvTasNet_Libri3Mix_sepnoisy_16k")
    # model = BaseModel.from_pretrained("JorisCos/ConvTasNet_Libri3Mix_sepclean_16k")



    os.system(f"ffmpeg -i C:/Users/A/Desktop/کارآموزی/Code/last/voice.mp3 -ar 8000 C:/Users/A/Desktop/کارآموزی/Code/last/voice.wav")
    model.separate("voice.wav")
    est1 = sf.read("voice_est1.wav")[0]
    est2 = sf.read("voice_est2.wav")[0]
    os.system(f"ffmpeg -i C:/Users/A/Desktop/کارآموزی/Code/last/voice_est1.wav C:/Users/A/Desktop/کارآموزی/Code/last/voice_est1.mp3")
    os.system(f"ffmpeg -i C:/Users/A/Desktop/کارآموزی/Code/last/voice_est2.wav C:/Users/A/Desktop/کارآموزی/Code/last/voice_est2.mp3")

    update.message.reply_text("""Sources are separated!
    Now, you can use these commands:
    /est1 to receive the first source estimation
    /est2 to receive the second source estimation
    """)

    # document = open('audio.mp3', 'rb')
    # context.bot.send_document(chat_id, document)


def send_document(update, context):
    chat_id = update.message.chat_id
    document = open('C:/Users/A/Desktop/کارآموزی/Code/last/voice.mp3', 'rb')

    context.bot.send_document(chat_id, document)


def send_v(update, context):
    chat_id = update.message.chat_id

    file_path = 'voice_est1.mp3'
    if os.path.isfile(file_path):
        AudioSegment.from_wav("voice_est1.wav").export("voice_est1.mp3", format="mp3")
        document = open('C:/Users/A/Desktop/کارآموزی/Code/last/voice_est1.mp3', 'rb')
        context.bot.send_document(chat_id, document)
    else :
        update.message.reply_text("""Sources has not separated yet! you must use /separate command first and then use /est1 to receive the first source estimation
            """)

def send_i(update, context):
    chat_id = update.message.chat_id

    file_path = 'voice_est2.mp3'
    if os.path.isfile(file_path):
        AudioSegment.from_wav("voice_est2.wav").export("voice_est2.mp3", format="mp3")
        document = open('C:/Users/A/Desktop/کارآموزی/Code/last/voice_est2.mp3', 'rb')
        context.bot.send_document(chat_id, document)
    else:
        update.message.reply_text("""Sources has not separated yet! you must use /separate command first and then use /est2 to receive the second source estimation
                """)


# python inference.py --input path/to/an/audio/file


updater.dispatcher.add_handler(CommandHandler("receive", send_document))
updater.dispatcher.add_handler(MessageHandler(Filters.document, downloader))
updater.dispatcher.add_handler(MessageHandler(Filters.voice, voice_handler))
updater.dispatcher.add_handler(MessageHandler(Filters.audio, audio_handler))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('separate', separate))
updater.dispatcher.add_handler(CommandHandler('est1', send_v))
updater.dispatcher.add_handler(CommandHandler('est2', send_i))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
