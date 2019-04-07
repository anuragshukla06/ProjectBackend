from django.shortcuts import render
from django.core.files import File
from django.http import HttpResponse
from .models import wordEntry
import pandas as pd
import random
import json

data = pd.read_excel("C:/Users/Anurag Shukla/Desktop/Microsoft Gondi/ProjectBackend/Main/mainpage/res/wordsData.xlsx")
DATA_LEN = len(data)
presentDicti = {} # dictionary for current word

# Create your views here.
def home(request):
    return HttpResponse(data.iloc[1]["Hindi"])

def storeAnswer(request, entryId, answer):
    entry = wordEntry.objects.get(pId=entryId)
    file = open("C:/hindiToGondi/" + str(entry.word) + ".txt", "r+")

    dicti = {}
    fileContent = file.read()
    file.seek(0) # for both reading and writing

    if len(fileContent)!=0:
        dicti = json.loads(fileContent)

    if answer in dicti:
        dicti[answer] += 1
    else:
        dicti[answer] = 1
    file.write(json.dumps(dicti))
    path = str(entry.word) + ".txt"
    entry.gondiFile.name = path
    entry.save()
    file.close()

    return HttpResponse(json.dumps(dicti, ensure_ascii=False))



def getTen(request):
    wordsInd = []
    random.seed(9001)
    while len(wordsInd) != 10:
        num = random.randint(0, DATA_LEN-1)
        if num not in wordsInd:
            wordsInd.append(num)

    dicti = {}
    for ind in wordsInd:
        key = data.iloc[ind]["rowid"]
        existingArray = wordEntry.objects.filter(pId=key)
        assert 0<=len(existingArray)<=1
        if len(existingArray) == 0: # initialising model entry for each new Word
            newEntry = wordEntry()
            newEntry.word = data.iloc[ind]["Hindi"]
            newEntry.pId = data.iloc[ind]["rowid"]
            file = open("C:/hindiToGondi/" + str(newEntry.word) + ".txt", "a+")
            path = str(newEntry.word) + ".txt"
            newEntry.gondiFile.name = path
            newEntry.save()
            file.close()
        dicti[int(data.iloc[ind]["rowid"])] = data.iloc[ind]["Hindi"]
    return HttpResponse(json.dumps(dicti, ensure_ascii=False))




    # for ind in wordsInd:
    #     key = data.iloc[ind]["rowid"]
    #     existingArray = wordEntry.objects.filter(pId=key)
    #     if len(existingArray):
    #         entry = wordEntry.objects.get(pId=key)
    #         file = entry.gondiFile
    #         global presentDicti
    #         presentDicti = json.loads(file.read())





# def showText(request, text):
#     dicti[text] = text
#     return HttpResponse(dicti)