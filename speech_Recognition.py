from ctypes import sizeof
from PySimpleGUI import PySimpleGUI as sg
import speech_recognition as sr
import speech_recognition as sr
import os

# sg.theme('DarkTeal9')
# font = ('Arial')

# layout = [
#         [sg.Text('Precione o botão para começar a ouvir', font=font, size=(30,1))],
#         [sg.Button('Ouvir',font=font, size=(10,1)),sg.Button('Sair',font=font, size=(10,1))],
        
        
# ]
# janela = sg.Window('Ouvir em Python', layout,font= font, size=(320,70))

# while True:
#     eventos, valores = janela.read()
#     if eventos == sg.WIN_CLOSED or eventos =='Ouvir':
        
    
#     if eventos == sg.WIN_CLOSED or eventos == 'Sair':
#         break
def ouvir_microfone():
  microfone = sr.Recognizer()

  #usando o microfone
  with sr.Microphone() as source:
      #chama um algoritmo de redução de ruidos no som
      microfone.adjust_for_ambient_noise(source)

      print("Diga alguma coisa")

      audio = microfone.listen(source)
    
      try:

        frase = microfone.recognize_google(audio,language='pt-BR')
        if "navegador" in frase:
          os.system("start Chrome.exe")
        if "Excel" in frase:
          os.system("start Excel.exe")

        print("Voce disse" + frase)
      
      except sr.UnknownValueError:
        print("Nao entendi")

      return frase

ouvir_microfone()

