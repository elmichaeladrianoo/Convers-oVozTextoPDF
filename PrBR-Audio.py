#!/usr/bin/env python3                                                                                

import speech_recognition as reconheceVoz  

# Capturando áudio com o microfone do sistema                                                                       
microfone = reconheceVoz.Recognizer()                                                                                   
with reconheceVoz.Microphone() as source:                                                                       
    print("Diga algo:")                                                                                   
    audio = microfone .listen(source)   

try:
    print("Voce disse \n" + microfone .recognize_google(audio, language='pt-BR'))
except reconheceVoz.UnknownValueError:
    print("Desculpe, Não consegui enteder")
except reconheceVoz.RequestError as e:
    print("Ops, Deu algum erro!; {0}".format(e))


from reportlab.pdfgen import canvas

pdf = canvas.Canvas("TesteIA.pdf")

pdf.drawString (30, 740, microfone .recognize_google(audio, language='pt-BR'))

pdf.save()
