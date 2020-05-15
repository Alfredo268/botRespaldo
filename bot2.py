import telegram
from telegram.ext import *
import random
import time
import os
import sys
import numbers
import subprocess

bot=telegram.Bot(token="TU_TOKEN_BOT")
bot_updater=Updater(bot.token)

def listener(bot,update):
    id=update.message.chat_id
    mensaje=update.message.text
    print("ID: "+str(id)+" Mensaje: "+ mensaje)
    
def start(bot,update,pass_chat_data=True):
    update.message.chat_id
    lista=["Wena los cabros!","Un saluoo pal leon que es terrible shoroo!"]
    bot.sendMessage(chat_id=update.message.chat_id,text=random.choice(lista))

def info(bot,update,pass_chat_data=True):
    update.message.chat_id
    lista=["@xuloski","@rootql","@emiaj","@EmiajDrake","@tornadodaniel","@kallfukeupu"]#qliaos wenos pal webeo
    bot.sendMessage(chat_id=update.message.chat_id,text="Este bot es mas vio que el "+random.choice(lista))

def archivo_recibido(bot, update):#esto hace que el videeo se respalde 
    global esperando_archivo
    global ruta_poner_archivo
    ruta_poner_archivo="/home/tu_usuario/"#la ruta de tu carpeta owncloud o donde quieras
    nombre_archivo = update.message.video.file_id+".mp4"
    id_archivo = update.message.video.file_id
    archivo = bot.getFile(id_archivo)
    ruta_actual = os.getcwd()
    os.chdir(ruta_poner_archivo)
    archivo.download(nombre_archivo)
    os.chdir(ruta_poner_archivo)
    esperando_archivo = 0
    subprocess.call('cd /var/www/owncloud/ ; sudo -u www-data php occ files:scan --all', shell=True)#comando para que se guarde el video en owncloud

def archivo_recibido_documento(bot, update):#esto hace que el documento se respalde 
    global esperando_archivo
    global ruta_poner_archivo
    ruta_poner_archivo="/home/tu_usuario/"#la ruta de tu carpeta owncloud o donde quieras
    nombre_archivo = (update.message.document.file_name.split)('.')
    nombre_archivo_con_id=nombre_archivo[0]+'_'+update.message.document.file_id+'.'+nombre_archivo[1]
    id_archivo = update.message.document.file_id
    archivo = bot.getFile(id_archivo)
    ruta_actual = os.getcwd()
    os.chdir(ruta_poner_archivo)
    archivo.download(nombre_archivo)
    os.chdir(ruta_poner_archivo)
    esperando_archivo = 0
    subprocess.call('cd /var/www/owncloud/ ; sudo -u www-data php occ files:scan --all', shell=True)#comando para que el documento se guarde en owncloud

def archivo_recibido_imagen(bot, update):#esto hace que las fotos se respalden 
    global esperando_archivo
    global ruta_poner_archivo
    ruta_poner_archivo="/home/tu_usuario/"#la ruta de tu carpeta owncloud o donde quieras
    nombre_archivo = update.message.photo[-1].file_id+".jpg"
    id_archivo = update.message.photo[-1].file_id
    archivo = bot.getFile(id_archivo)
    ruta_actual = os.getcwd()
    os.chdir(ruta_poner_archivo)
    archivo.download(nombre_archivo)
    os.chdir(ruta_poner_archivo)
    esperando_archivo = 0
    subprocess.call('cd /var/www/owncloud/ ; sudo -u www-data php occ files:scan --all', shell=True)#comando para que el documento se guarde en owncloud

start_handler=CommandHandler("hola",start)
info_handler=CommandHandler("info",info)
listener_handler=MessageHandler(Filters.text,listener)
archivo_recibido=MessageHandler(Filters.video,archivo_recibido)
archivo_recibido_documento=MessageHandler(Filters.document,archivo_recibido_documento)
archivo_recibido_imagen=MessageHandler(Filters.photo,archivo_recibido_imagen)


dispatcher=bot_updater.dispatcher

dispatcher.add_handler(archivo_recibido_imagen)
dispatcher.add_handler(archivo_recibido_documento)
dispatcher.add_handler(archivo_recibido)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(listener_handler)


bot_updater.start_polling()
bot_updater.idle()

while True:
    pass

