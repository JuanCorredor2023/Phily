import random
import json

from unicodedata import normalize

import os
import time
from playsound import playsound
import speech_recognition as sr
from gtts import gTTS


import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize


def get_audio():
  r= sr.Recognizer()
  with sr.Microphone() as source:
    audio = r.listen(source)
    said = ""


    try:
      said= r.recognize_google(audio, language="es-ES")
      print (said)
    except Exception as e:
      print("exception"+str(e))

  return said
#speak


def speak (text):
    tts = gTTS(text = text, lang="es", tld="us" )
    filename = 'voice.mp3'
    tts.save(filename)
    playsound(filename)
    os.remove(filename)
 

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()



bot_name = "Phily"
print("Hablemos! (di 'chao' para salir)")

while True:
    sentence = get_audio()
    if sentence == "chao" or sentence  =="adios" or sentence  == "Goodbye" or sentence  == "gracias" or sentence  == "quit" or sentence  == "exit" or sentence  =="salir":
        print("chao! estoy aqui para lo que necesites. Suerte en tu presentacion")
        speak("chao! estoy aqui para lo que necesites. Suerte en tu presentacion")
        break

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.55:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                print(f"{bot_name}: {random.choice(intent['responses'])}")
                speak(f"{bot_name}: {random.choice(intent['responses'])}")
    else:
        print(f"{bot_name}: disculpa no entiendo, puedes decirlo de otra manera")
        (f"{bot_name}: disculpa no entiendo, puedes decirlo de otra manera")