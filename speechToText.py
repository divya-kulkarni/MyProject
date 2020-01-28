import sys
import speech_recognition as sr
import pyaudio
import webbrowser
import bs4
import mysql.connector
from enum import Enum
import re

class Command:
    def __init__(self, command_id, command_name, command_type, lst_command_tokens):
        self.command_id = command_id
        self.command_name = command_name
        self.command_type = command_type
        self.lst_command_token = lst_command_tokens

class CommandToken:
    def __init__(self,command_no,command_id,token_id,pos,token_type):
        self.command_no = command_no
        self.command_id = command_id
        self.token_id = token_id
        self.positionInCommand = pos
        self.token_type = token_type

class CommandType(Enum):
    MASTER_COMMAND = 1
    CUSTOM_COMMAND = 2

class TokenType(Enum):
    UNDEFINED = 12
    VALUE = 7
    CUSTOM = 11


class Initializer:
    dictCommand = dict()

    def __init__():
        pass
    
    @staticmethod
    def fetchAllCommands():
        mydb = mysql.connector.connect(host="localhost",
        user="root",
        # passwd="divyaanuja",
        passwd="developer@brainchild",
        database="project")
        try:
            mycursor = mydb.cursor()

        except(BaseException):
            print(BaseException)
        
        SQL = "select CommandID, CommandName, CommandType from commandmaster"
        mycursor.execute(SQL)
        rec = mycursor.fetchall()

        for row in rec:
            obj = Command(row["CommandID"],row["CommandName"],row["CommandType"],None)
            Initializer.dictCommand[row["CommandID"]] = obj

        SQL = "select CT.cno, CT.CommandID, CT.TokenID, CT.PositionInCommand, T.TypeID from CommandToken CT join Token T on CT.TokenID = T.TokenID"
        mycursor.execute(SQL)
        rec = mycursor.fetchall()

        for row in rec:
            oCommandToken = CommandToken(row["cno"],row["CommandID"],row["TokenID"],row["PositionInCommand"],row["TypeID"])
            command = Initializer.dictCommand.get(row["CommandID"])
            if command.lst_command_token == None:
                command.lst_command_token = list()

            command.lst_command_token.append(oCommandToken)

      #  print('ENDDD')

# This function finds the exact command match based on tokenIDs, position in command and token types
def getMatchingCommandIDAndType():
    i = 0
    for commandID, command in Initializer.dictCommand.items():
        if len(command.lst_command_token) == len(sequence):
            for i in range(0, len(sequence)):
                if any((tokenInCommand.token_id == sequence[i].token_id and tokenInCommand.positionInCommand == i + 1) or \
                        ((tokenInCommand.positionInCommand == i + 1 and sequence[i].token_type == TokenType.UNDEFINED and \
                        (tokenInCommand.token_type == TokenType.VALUE or tokenInCommand.token_type == TokenType.UNDEFINED) and tokenInCommand.token_id != sequence[i].token_id)) for \
                        tokenInCommand in command.lst_command_token) == False:
                    break
            if i == len(sequence) - 1:
            #    print('COMMAND ID:',commandID)
                return commandID, command.command_type
    return -1, -1
     

class Token:
    def __init__(self,token_id,value,token_type):
        self.token_id = token_id
        self.value = value
        self.token_type = token_type

    def displayDetails(self):
        print('Token ID is ',self.token_id)

sequence = []

mydb = mysql.connector.connect(host="localhost",
    user="root",
    # passwd="divyaanuja",
    passwd="developer@brainchild",
    database="project")

# This function will get the token record from the database if exists or gets the record for UNDEFINED token
def getTokenRecord(myToken):
 
    try:
        SQL = "select TokenID, Value, TypeID from token where value='" + myToken + "'"
        mycursor = mydb.cursor() 
        mycursor.execute(SQL)
        rec = mycursor.fetchall()
        if mycursor.rowcount != 0:
            for x in rec:
                print(x)
                obj = Token(x["TokenID"],x["Value"],x["TypeID"])
            obj.displayDetails()
            sequence.append(obj)
        else:
            SQL = "select TokenID, Value, TypeID from token where value='UNDEFINED'"
            mycursor = mydb.cursor()
            mycursor.execute(SQL)
            rec = mycursor.fetchall()
            if mycursor.rowcount != 0:
                for x in rec:
                    print(x)
                    obj = Token(x["TokenID"],x["Value"],x["TypeID"])
                #obj.displayDetails()
                sequence.append(obj)
            else:
                return False
        return True
        
    except(exception):
        print(exception)

# This function will check if each token exists or not
def recognizeTokens(tokens):
    for token in tokens:
        if getTokenRecord(token) == False:
            return False
    return True

# This function will tokenize the given command into different tokens
def tokenize(text):
    tokens = []
    str = "%"
    str1 = " percent"
    if text.find(str) >= 0:
        text = text.replace(str,str1)
    tokens = text.split(" ")
    #print('TOKENS ARE: ',tokens)
    return tokens

# This function will get the voice input and convert it to the text
def recognizeCommands():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Your wish is my command ->')
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            
            print('You said: {}'.format(text))
            return text
            
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

# This function gives the suggestions by checking all the existing commands and matching their tokens with the tokens in given command
# Maximum of 20% difference will be allowed in the given command and existing command for treating it as suggestion
def getSuggestions():
    i = 0
    suggestions = list()
    for commandID, command in Initializer.dictCommand.items():
        if len(command.lst_command_token) == len(sequence):
            cntMismatch = 0
            for i in range(0, len(sequence)):
                if (any(tokenInCommand.token_id == sequence[i].token_id and tokenInCommand.positionInCommand == i + 1) or \
                        (tokenInCommand.positionInCommand == i + 1 and sequence[i].token_type == TokenType.UNDEFINED and \
                        (tokenInCommand.token_type == TokenType.VALUE or tokenInCommand.token_type == TokenType.UNDEFINED) and tokenInCommand.token_id != sequence[i].token_id) for tokenInCommand in command.lst_command_token) == False:
                    cntMismatch += 1
            if 20 >= cntMismatch * 100 / len(sequence): # if given command is varying less than or equal to 20% of the present command then it will be considered as suggestion
                suggestions.append(command)
        elif len(command.lst_command_token) > len(sequence):
            cntNonExistingTokens = 0
            cntMissingTokens = 0
            lastMatchFound = 0
            for i in range(0, len(sequence)):
                if (any((tokenInCommand.token_id == sequence[i].token_id and tokenInCommand.positionInCommand > lastMatchFound) or \
                        (tokenInCommand.positionInCommand > lastMatchFound and sequence[i].token_type == TokenType.UNDEFINED and \
                        (tokenInCommand.token_type == TokenType.VALUE or tokenInCommand.token_type == TokenType.UNDEFINED) and tokenInCommand.token_id != sequence[i].token_id)) for tokenInCommand in command.lst_command_token) == True:
                    cntMissingTokens += tokenInCommand.positionInCommand - lastMatchFound - 1
                    lastMatchFound = tokenInCommand.positionInCommand
                else:
                    cntNonExistingTokens += 1
            cntMissingTokens += len(command.lst_command_token) - lastMatchFound
            if 20 >= (cntNonExistingTokens + cntMissingTokens) * 100 / len(sequence): # if given command is varying less than or equal to 20% of the present command then it will be considered as suggestion
                suggestions.append(command)
        else:
            cntNonExistingTokens = 0
            cntMissingTokens = 0
            lastMatchFound = 0
            for i in range(0, len(sequence)):
                if (any((tokenInCommand.token_id == sequence[i].token_id and tokenInCommand.positionInCommand >= lastMatchFound) or \
                        (tokenInCommand.positionInCommand >= lastMatchFound and sequence[i].token_type == TokenType.UNDEFINED and \
                        (tokenInCommand.token_type == TokenType.VALUE or tokenInCommand.token_type == TokenType.UNDEFINED) and tokenInCommand.token_id != sequence[i].token_id)) for tokenInCommand in command.lst_command_token) == True:
                    cntMissingTokens += tokenInCommand.positionInCommand - lastMatchFound - 1
                    lastMatchFound = tokenInCommand.positionInCommand
                else:
                    cntNonExistingTokens += 1
                if lastMatchFound == len(command.lst_command_token):
                    break
            cntNonExistingTokens += len(sequence) - i - 1
            if 20 >= (cntNonExistingTokens + cntMissingTokens) * 100 / len(sequence): # if given command is varying less than or equal to 20% of the present command then it will be considered as suggestion
                suggestions.append(command)
            
    return suggestions

def remVowel(string): 
    return (re.sub("[aeiouAEIOU]","",string))

# This function adds the new custom command into the database once user selects one of the given suggestion
# First command is added into commandmaster. Then the tokens will be added into the tokens table. At the end tokens will be mapped with the command in commandtoken table.
def addNewCustomCommand(selectedChoice, userInputValues):
    commandName = "_".join(userInputValues)
    commandName = remVowel(commandName)
    masterCommandID = sequence[selectedChoice - 1].command_id
    commandType = CommandType.CUSTOM_COMMAND.value
    try:
        cursor = mydb.cursor()
        sql = "INSERT INTO CommandMaster (CommandName, CommandType, MasterCommandID) VALUES (%s, %s, %s)"
        values = (commandName, commandType, selectedChoice)
        cursor.execute(sql, values)
        commandID = cursor.lastrowid

        sql = "INSERT INTO Token (Value, TypeID) VALUES (%s, %s)"

        commandTokenRecords = []

        # Prepare tokens which are to be added from the input values given by user
        if len(suggestions[selectedChoice-1].lst_command_token) == len(sequence):
            isExistingToken = False

            for i in range(0, len(sequence)):
                isExistingToken = False
                tokenType = TokenType.UNDEFINED

                if (any((tokenInCommand.token_id == sequence[i].token_id and tokenInCommand.positionInCommand == i + 1)) for tokenInCommand in suggestions[selectedChoice-1].lst_command_token) == False:
                    isExistingToken = True # as match is found, token is identified and no need to add it to DB again
                    tokenID = tokenInCommand.token_id

                elif (any((tokenInCommand.positionInCommand == i + 1 and sequence[i].token_type == TokenType.UNDEFINED and \
                        (tokenInCommand.token_type == TokenType.VALUE or tokenInCommand.token_type == TokenType.UNDEFINED) and tokenInCommand.token_id != sequence[i].token_id)) for tokenInCommand in suggestions[selectedChoice-1].lst_command_token) == False:
                    tokenType = tokenInCommand.token_type # tokenType will be set to token type of corresponding command
                else:
                    # tokenType is already set to UNDEFINED
                    pass

                if isExistingToken == False:
                    values = (sequence[i].value.upper(), tokenType)
                    cursor.execute(sql, values)
                    tokenID = cursor.lastrowid
                    # print("New token added: ", sequence[i].value)

                commandTokenRecords.append((commandID, tokenID, i+1))

        elif len(suggestions[selectedChoice-1].lst_command_token) > len(sequence):
            lastMatchFound = 0
            isExistingToken = False

            for i in range(0, len(sequence)):
                isExistingToken = False
                tokenType = TokenType.UNDEFINED

                if (any(tokenInCommand.token_id == sequence[i].token_id and tokenInCommand.positionInCommand > lastMatchFound) for tokenInCommand in suggestions[selectedChoice-1].lst_command_token) == True:
                    isExistingToken = True # as match is found, token is identified and no need to add it to DB again
                    lastMatchFound = tokenInCommand.positionInCommand
                    tokenID = tokenInCommand.token_id
                        
                if (any(tokenInCommand.positionInCommand > lastMatchFound and sequence[i].token_type == TokenType.UNDEFINED and \
                        (tokenInCommand.token_type == TokenType.VALUE or tokenInCommand.token_type == TokenType.UNDEFINED) and tokenInCommand.token_id != sequence[i].token_id) for tokenInCommand in suggestions[selectedChoice-1].lst_command_token) == True:
                    tokenType = tokenInCommand.token_type # tokenType will be set to token type of corresponding command
                    lastMatchFound = tokenInCommand.positionInCommand
                else:
                    # tokenType is already set to UNDEFINED
                    pass

                if isExistingToken == False:
                    values = (sequence[i].value.upper(), tokenType)
                    cursor.execute(sql, values)
                    tokenID = cursor.lastrowid
                    # print("New token added: ", sequence[i].value)

                commandTokenRecords.append((commandID, tokenID, i+1))
        else:
            isExistingToken = False
            lastMatchFound = 0
            for i in range(0, len(sequence)):
                isExistingToken = False
                tokenType = TokenType.UNDEFINED

                if lastMatchFound != len(suggestions[selectedChoice-1].lst_command_token):
                    if (any((tokenInCommand.token_id == sequence[i].token_id and tokenInCommand.positionInCommand >= lastMatchFound)) for tokenInCommand in suggestions[selectedChoice-1].lst_command_token) == True:
                        sExistingToken = True # as match is found, token is identified and no need to add it to DB again
                        lastMatchFound = tokenInCommand.positionInCommand
                        tokenID = tokenInCommand.token_id

                    elif ( any(tokenInCommand.positionInCommand >= lastMatchFound and sequence[i].token_type == TokenType.UNDEFINED and \
                            (tokenInCommand.token_type == TokenType.VALUE or tokenInCommand.token_type == TokenType.UNDEFINED) and tokenInCommand.token_id != sequence[i].token_id) for tokenInCommand in suggestions[selectedChoice-1].lst_command_token) == True:
                        tokenType = tokenInCommand.token_type # tokenType will be set to token type of corresponding command
                        lastMatchFound = tokenInCommand.positionInCommand
                    else:
                        # tokenType is already set to UNDEFINED
                        pass

                if isExistingToken == False:
                    values = (sequence[i].value.upper(), tokenType)
                    cursor.execute(sql, values)
                    tokenID = cursor.lastrowid
                    # print("New token added: ", sequence[i].value)

                commandTokenRecords.append((commandID, tokenID, i+1))

        sql = "INSERT INTO CommandToken (CommandID, TokenID, PositionInCommand) VALUES (%s, %s, %s)"
        cursor.execute(sql, commandTokenRecords)
        mydb.commit()
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to insert new custom command. {}".format(error))
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



def editStyleTag(styleString):
    styleList = styleString.split(';')
    styleList = list(filter(None, styleList))
    styleDict = dict()
    for attr in styleList:
        dictKey = attr.split(':')
        styleDict[dictKey[0]] = dictKey[1]
    #print(styleDict)
    #print(type(styleDict))
    return styleDict
# This function executes the command
def executeCommand(commandID,words):
    
    if commandID == 2:
        url = "file://C:/Users/divya/.vscode/sorry/samplePage.html"
        with open("samplePage.html") as page:
            txt = page.read()
            content = bs4.BeautifulSoup(txt,features="html.parser")
            color = words[4]
            content.body['bgcolor'] = color
        with open("samplePage.html","w") as page:
            print('CHANGING BACKGROUND COLOUR')
            page.write(str(content))
            webbrowser.open(url,new=0)
        return True

    elif commandID in [5,6]:
        url = "file://C:/Users/divya/.vscode/sorry/samplePage.html"
        with open("samplePage.html") as page:
            txt = page.read()
            content = bs4.BeautifulSoup(txt,features="html.parser")
            position = words[3]
            styleTag = content.div['style']
            #print(styleTag)
            styleDictionary = editStyleTag(styleTag)
            styleDictionary['float'] = position
            newStyleTag = ''
            for attr,val in styleDictionary.items():
                newStyleTag+= attr + ':' + val + ';'
            content.div['style'] = newStyleTag

        with open("samplePage.html","w") as page:
            print('DIV FLOATED TO ',position)
            page.write(str(content))
            webbrowser.open(url,new=0)
        return True

    elif commandID in [9,10,11,12]: #percent
        url = "file://C:/Users/divya/.vscode/sorry/samplePage.html"
        with open("samplePage.html") as page:
            txt = page.read()
            content = bs4.BeautifulSoup(txt,features="html.parser")
            position = words[3]
            value = words[5]
            styleTag = content.div['style']
            #print(styleTag)
            styleDictionary = editStyleTag(styleTag)
            
            if position == 'left':
                oldVal = styleDictionary.get("margin-right")
                oldVal = oldVal.replace('px','')
                oldVal = int(oldVal)
                newValue = oldVal + (oldVal * int(value)) / 100
                newValue = str(int(newValue))
                styleDictionary['margin-right'] = newValue + 'px'
            elif position == 'right':
                oldVal = styleDictionary.get("margin-left")
                oldVal = oldVal.replace('px','')
                oldVal = int(oldVal)
                newValue = oldVal + (oldVal * int(value)) / 100
                newValue = str(int(newValue))
                styleDictionary['margin-left'] = newValue + 'px'
            elif position == 'upwards':
                oldVal = styleDictionary.get("margin-bottom")
                oldVal = oldVal.replace('px','')
                oldVal = int(oldVal)
                newValue = oldVal + (oldVal * int(value)) / 100
                newValue = str(int(newValue))
                styleDictionary['margin-bottom'] = newValue + 'px'
            else:
                oldVal = styleDictionary.get("margin-top")
                oldVal = oldVal.replace('px','')
                oldVal = int(oldVal)
                newValue = oldVal + (oldVal * int(value)) / 100
                newValue = str(int(newValue))
                styleDictionary['margin-top'] = newValue + 'px'

            newStyleTag = ''
            for attr,val in styleDictionary.items():
                newStyleTag+= attr + ':' + val + ';'
            content.div['style'] = newStyleTag

        with open("samplePage.html","w") as page:
            print('DIV MOVED TO ',position,' BY ',value,'%')
            page.write(str(content))
            webbrowser.open(url,new=0)
        return True


    elif commandID in [13,14,15,16]: #pixels
        url = "file://C:/Users/divya/.vscode/sorry/samplePage.html"
        with open("samplePage.html") as page:
            txt = page.read()
            content = bs4.BeautifulSoup(txt,features="html.parser")
            
            position = words[3]
            value = words[4]
            
            styleTag = content.div['style']
            print(styleTag)
            styleDictionary = editStyleTag(styleTag)
            
            if position == 'left':
                oldVal = styleDictionary.get("margin-right")
                oldVal = oldVal.replace('px','')
                oldVal = int(oldVal)
                newValue = oldVal + int(value)
                newValue = str(int(newValue))
                styleDictionary['margin-right'] = newValue + 'px'
            elif position == 'right':
                oldVal = styleDictionary.get("margin-left")
                oldVal = oldVal.replace('px','')
                oldVal = int(oldVal)
                newValue = oldVal + int(value)
                newValue = str(int(newValue))
                styleDictionary['margin-left'] = newValue + 'px'
            elif words[2] == 'upwards':
                oldVal = styleDictionary.get("margin-bottom")
                oldVal = oldVal.replace('px','')
                oldVal = int(oldVal)
                newValue = oldVal + int(value)
                newValue = str(int(newValue))
                styleDictionary['margin-bottom'] = newValue + 'px'
            else:
                oldVal = styleDictionary.get("margin-top")
                oldVal = oldVal.replace('px','')
                oldVal = int(oldVal)
                newValue = oldVal + int(value)
                newValue = str(int(newValue))
                styleDictionary['margin-top'] = newValue + 'px'

            newStyleTag = ''
            for attr,val in styleDictionary.items():
                newStyleTag+= attr + ':' + val + ';'
            content.div['style'] = newStyleTag

        with open("samplePage.html","w") as page:
            print('DIV SHIFTED TO ',position,' BY ',value,' PIXELS')
            page.write(str(content))
            webbrowser.open(url,new=0)
        return True

    elif commandID in [17,18,19,20]:
        url = "file://C:/Users/divya/.vscode/sorry/samplePage.html"
        with open("samplePage.html") as page:
            txt = page.read()
            content = bs4.BeautifulSoup(txt,features="html.parser")
            position = words[3]
            value = words[5]

            styleTag = content.body.h3['style']
            print(styleTag)
            styleDictionary = editStyleTag(styleTag)
            
            if position == 'left':
                oldVal = styleDictionary.get("margin-right")
                oldVal = oldVal.replace('px','')
                oldVal = int(oldVal)
                newValue = oldVal + int(value)
                newValue = str(int(newValue))
                styleDictionary['margin-right'] = newValue + 'px'

            elif position == 'right':
                oldVal = styleDictionary.get("margin-left")
                oldVal = oldVal.replace('px','')
                oldVal = int(oldVal)
                newValue = oldVal + int(value)
                newValue = str(newValue)
                styleDictionary['margin-left'] = newValue + 'px'

            elif position == 'upwards':
                oldVal = styleDictionary.get("margin-bottom")
                oldVal = oldVal.replace('px','')
                oldVal = int(oldVal)
                newValue = oldVal + int(value)
                newValue = str(int(newValue))
                styleDictionary['margin-bottom'] = newValue + 'px'

            else:
                oldVal = styleDictionary.get("margin-top")
                oldVal = oldVal.replace('px','')
                oldVal = int(oldVal)
                newValue = oldVal + int(value)
                newValue = str(int(newValue))
                styleDictionary['margin-top'] = newValue + 'px'

            newStyleTag = ''
            for attr,val in styleDictionary.items():
                newStyleTag+= attr + ':' + val + ';'
            content.body.h3['style'] = newStyleTag

    else:
        return False


Initializer.fetchAllCommands()

while(True):
    voiceCommand = recognizeCommands()

    if voiceCommand == 'exit':
        break
    userInputValues = tokenize(voiceCommand)
    if recognizeTokens(userInputValues):
        commandID, commandType = getMatchingCommandIDAndType()
        if commandID == -1:
            suggestions = getSuggestions()
            print(suggestions)
            selectedChoice = recognizeCommands()
            selectedChoice = int(selectedChoice)
            print('You have selected ', selectedChoice)
            if  1 <= selectedChoice <= len(suggestions):
                addNewCustomCommand(selectedChoice, userInputValues)
                modifyToMasterCommand(userInputValues)
                if executeCommand(suggestions[selectedChoice-1].command_id,userInputValues):
                    print('Command found and executed successfully!')
                else:
                    print('### COMMAND NOT EXECUTED!! ###')
            else:
               print("I DIDN'T RECOGNIZE GIVEN CHOICE. PLEASE GIVING THE COMMAND AGAIN..")
        else:
            if executeCommand(commandID,userInputValues):
                print('Command found and executed successfully!')
            else:
                print('### COMMAND NOT EXECUTED!! ###')
    else:
        print('@@@ Could not process command!! @@@')
