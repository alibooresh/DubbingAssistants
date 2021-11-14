import tkinter
from tkinter import messagebox as mb
import tkinter.filedialog
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


videoPath = ''


def renderInput():
    #
    urlLabel = tkinter.Label(text="آدرس URL را وارد کنید:")
    urlInput = tkinter.Entry(mainWindow)

    urlLabel.grid(row=0, column=0)
    urlInput.grid(row=0, column=1)


def onClick():
    label = tkinter.Label(text="hello")
    label.pack()


def answer():
    mb.showerror("Answer", "Sorry, no answer available")


def callback():
    if mb.askyesno('Verify', 'Really quit?'):
        mb.showwarning('Yes', 'Not yet implemented')
    else:
        mb.showinfo('No', 'Quit has been cancelled')


def select_file():
    filetypes = (
        ('Video File', '*.mp4'),
        ('All files', '*.*')
    )

    videoPath = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=videoPath
    )


# def main():
#     main.getSubtitle()


def renderInputButton():
    submitButton = tkinter.Button(mainWindow, text='Get Subtitle',
                                  width=10, height=2,
                                  bg='#00d3eb')

    exitButton = tkinter.Button(mainWindow, text='Exit',
                                width=10, height=2, command=mainWindow.destroy,
                                bg='#00d3eb')

    exitButton.grid(row=2, column=0)
    submitButton.grid(row=2, column=1)


mainWindow = tkinter.Tk()
mainWindow.title('Dubberenfa')
mainWindow.minsize(width=700, height=700)
mainWindow.maxsize(width=700, height=700)
#mb.showinfo('Welcome :)', 'Hello there,\n Welcome to Dubberenfa :) ')
renderInput()
renderInputButton()

mainWindow.mainloop()
