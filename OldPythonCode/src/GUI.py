import os
from tkinter import *
from tkinter import ttk
import SubtitleProccess
import re
import datetime
from googletrans import Translator
import arabic_reshaper
from bidi.algorithm import get_display

videoPath = ''
isInputView = True
isProccessFinish = False
isProccessStart = False
subtitles = []
subtitleIndex = 0
translator = Translator()
sentences = []


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
    subtitles = sentences
    print(sentences)
    print(subtitles)
    renderOutputView()


def progressBarStart():
    pBar.start(1)


# def startProccess():
#     subtitles = SubtitleProccess.mainProccess()
#     isProccessFinish = True
#     isInputView = False
#     renderOutputView()


def renderInputView():
    Label(text='Put your Subtitle file (srt) in the project directory.', font="arial 15",
          background="#111111", fg="white").pack()
    Button(mainWindow, font="arial 20", text='Start Proccess',
           border=0, fg="white", command=mainProccess,
           bg='#4a4a4a').pack(pady=30)


def renderOutputView():

    p = sentences[subtitleIndex]
    print(p)
    text = translateText("en", "fa", p['sentence'])
    print(text)
    Label(text='Proccess finished successfully!', font="arial 15",
          background="#111111", fg="white").pack()
    Label(text=text, font="arial 13",
          background="#111111", fg="white").pack()
    Button(mainWindow, font="arial 20", text='Next',
           border=0, fg="white", command=increase,
           bg='#4a4a4a').pack(pady=30)
    Button(mainWindow, font="arial 20", text='Previes',
           border=0, fg="white", command=decrease,
           bg='#4a4a4a').pack(pady=30)


def increase():
    global subtitleIndex
    subtitleIndex += 1
    renderOutputView()


def decrease():
    global subtitleIndex
    subtitleIndex -= 1


mainWindow = Tk()
mainWindow.title('Dubberenfa')
mainWindow.minsize(width=600, height=700)
mainWindow.configure(background="#111111")
sb = Scrollbar(mainWindow)
sb.pack(side=RIGHT, fill=Y)
# icon
base_folder = os.path.dirname(__file__)
image_path = os.path.join(base_folder, 'logo.png')
image_icon = PhotoImage(file=image_path)
mainWindow.iconphoto(False, image_icon)

# logo
myImage = Label(image=image_icon, background="#111111")
myImage.pack(padx=1, pady=1)
Label(text="Dubb Assistant", font="arial 20 bold",
      background="#111111", fg="white").pack()
Label(text='Put your Subtitle file (srt) in the project directory.', font="arial 10",
      background="#111111", fg="white").pack()
renderInputView()

# pBar = ttk.Progressbar(mainWindow, Length=400, orient=HORIZONTAL,
#                        mode='determinate')
# pBar.pack(pady=20)
# mb.showinfo('Welcome :)', 'Hello there,\n Welcome to Dubberenfa :) ')
# renderInput()
# renderInputButton()

mainWindow.mainloop()
