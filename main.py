import speech_recognition as sr
import pyaudio
import webbrowser
import bs4
import mysql.connector
import myModules

sequence = []

mydb = mysql.connector.connect(host="localhost",
    user="root",
    passwd="divyaanuja",
    database="project")

  
def recognizeCommands():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Your wish is my command--> ')
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print('You said: {}'.format(text))
            return text
            
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

def editStyleTag(styleString):
    styleList = styleString.split(';')
    styleList = list(filter(None, styleList))
    styleDict = dict()
    for attr in styleList:
        dictKey = attr.split(':')
        styleDict[dictKey[0]] = dictKey[1]
    print(styleDict)
    print(type(styleDict))
    return styleDict


myModule.Initializer.fetchAllCommands()
voiceCommand = recognizeCommands()
userInputValues = tokenize(voiceCommand)

if recognizeTokens(userInputValues):
    commandID = getMatchingCommandID()
    print('Matching command ID: ', commandID)
    if executeCommand(commandID,userInputValues):
        #refresh html
        pass
    else:
        print('### COMMAND NOT EXECUTED!! ###')
else:
    print('@@@ Could not process command!! @@@')
