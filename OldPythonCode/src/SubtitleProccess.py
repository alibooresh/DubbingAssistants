#!/usr/bin/python
import re
import datetime
from googletrans import Translator
import arabic_reshaper
from bidi.algorithm import get_display


translator = Translator()


def translateText(src: str, dest: str, text: str) -> str:
    text = translator.translate(src=src, dest=dest, text=text).text
    reshaped_text = arabic_reshaper.reshape(text)    # correct its shape
    bidi_text = get_display(reshaped_text)
    return bidi_text


def strToDate(strTime) -> datetime:
    times = strTime.split(",")
    seperated = times[0].split(":")

    hour = 0
    minute = 0
    second = 0
    milisec = 0
    if(len(strTime) > 0):
        hour = int(seperated[0])
        minute = int(seperated[1])
        second = int(seperated[2])
        milisec = int(times[1])
    return (datetime.time(hour=hour, minute=minute, second=second, microsecond=milisec))


def displaySentences(sentences):
    print('displaying sentences with order and structure \n')
    for sentence in sentences:
        print('Sentence is : \n\t\t')
        print(translateText("en", "fa", sentence['sentence']))
        print('\n Start Time is : \n\t\t')
        print(sentence['sentenceStartTime'])
        print('\n End Time is : \n\t\t')
        print(sentence['sentenceEndTime'])
        # event.wait(1000)


def mainProccess():

    file = open('subtitle.srt', mode='r', encoding='utf-8')
    subtitleLines = file.read()
    splited = subtitleLines.split('\n')
    lines = []
    for line in splited:
        if(len(line) > 0):
            lines.append(line)
    print('starsting \n')
    file.close()
    # print(datetime.time(hour=0, minute=10, second=25, microsecond=100))
    strToDate("00:40:22,5654")
    sentences = []

    lineStartTime = ''
    lineEndTime = ''
    lineTimeLen = 0

    sentenceStartTime = ''
    sentenceEndTime = ''
    sentenceTimeLen = 0
    sentence = ''
    print('starsting \n')
    for index in range(0, len(lines)):

    	# get time information

        isTime = re.search(r'-->', lines[index], re.M | re.I)
        isLineNum = re.search(r'^\d+', lines[index], re.M | re.I)
        isNewLine = re.search(r'^"\\"', lines[index], re.M | re.I)
        isText = not(bool(re.search(r'-->', lines[index], re.M | re.I))) and not(
            bool(re.search(r'^\d+', lines[index], re.M | re.I)))
        isEndOfSentence = re.search(r'\.', lines[index], re.M | re.I)
        if isTime:

            timeInfo = lines[index].split("-->")

            lineStartTime = timeInfo[0]
            lineEndTime = timeInfo[1]

            sentenceStartTime = strToDate(lineStartTime)

            # search = re.search( r'\.', lines[index+1], re.M|re.I)
            sentence = sentence+' '+lines[index+1]
            if(index < (len(lines)-2)):
                if(len(lines[index+2]) < 1):
                    print(lines[index+2])
                else:
                    sentence = sentence+' '+lines[index+2]
            sentenceEndTime = strToDate(lineEndTime)
            # sentenceTimeLen = sentenceEndTime - sentenceStartTime

            tmpDic = {
                "sentenceStartTime": sentenceStartTime,
                "sentenceEndTime": sentenceEndTime,
                "sentenceTimeLen": sentenceTimeLen,
                "sentence": sentence
            }

            sentences.append(tmpDic)
            sentenceStartTime = ''
            sentenceEndTime = ''
            sentenceTimeLen = 0
            sentence = ''
            #reset
    print("\t\t********All sentences is showing below: ********")
    print(sentences)
    print(len(sentences))
    displaySentences(sentences)
    return sentences
