from tkinter import *
import urllib.request
import os

# Variables
URLEditrans = "https://www2.agenciatributaria.gob.es/L/inwinvoc/es.aeat.dit.adu.adht.editran.NumRefEditran?mod=347"
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
numberOfEditrans = 50
textToSearch = 'Justificante: <strong>'
nameWindow = "Obtener números Editrans"
lblURLText = "URLEditrans"
lblNumberCodesText = "Justificantes a Obtener"
lblTextGenerated = 'Fichero Generado'

# Create Windows GUI
window = Tk()

window.title(nameWindow)
window.geometry('500x150')

# Labels
lblURLAEAT = Label(window, text=lblURLText)
lblURLAEAT.grid(column=0, row=0)
lblNumberCodes = Label(window, text=lblNumberCodesText)
lblNumberCodes.grid(column=0, row=1)

# Text Entries default values
txtURLAEATByDefault = StringVar(window, value=URLEditrans)
txtURLAEAT = Entry(window, width=50, textvariable=txtURLAEATByDefault)
txtURLAEAT.grid(column=1, row=0)

# TextEntries
txtNumberCodesEditransByDefault = IntVar(window, value=numberOfEditrans)
txtNumberCodesEditrans = Entry(window, width=10, textvariable=txtNumberCodesEditransByDefault)
txtNumberCodesEditrans.grid(column=1, row=1)


# Function to obtain Editrans codes and create the file on Desktop
def getEditransCodes(url, numberCodes):
    # Delete file if exists and create a new one
    if os.path.exists(desktop + "//editrans.txt"):
        os.remove(desktop + "//editrans.txt")
    f = open(desktop + "//editrans.txt", "a")

    # Get number and write it on the file
    for x in range(numberCodes):
        response = urllib.request.urlopen(URLEditrans)
        the_page = response.read().decode('latin-1')
        codeEditrans = the_page[the_page.find(textToSearch) + 22:the_page.find(textToSearch) + 36].replace(" ", "")

        if x == numberCodes - 1:
            f.write(codeEditrans)
        else:
            f.write(codeEditrans + "\n")
    f.close()

    label2 = Label(window, text=lblTextGenerated, fg='green', font=('helvetica', 12, 'bold'))
    label2.grid(column=0, row=4)


def clicked():
    getEditransCodes(txtURLAEAT.get(), int(txtNumberCodesEditrans.get()))

btn = Button(window, text="Generar", command=clicked)
btn.grid(column=1, row=3)

window.mainloop()
