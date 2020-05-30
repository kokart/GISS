import urllib.request
import os

#Variables
URLEditrans="https://www2.agenciatributaria.gob.es/L/inwinvoc/es.aeat.dit.adu.adht.editran.NumRefEditran?mod=347"
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
numberOfEditrans= 2
textToSearch = 'Justificante: <strong>'

#Deleting previous file and creating a new one
if os.path.exists(desktop +"//editrans.txt"):
    os.remove(desktop +"//editrans.txt")
f = open(desktop +"//editrans.txt","a")

#Get number and write it on the file
for x in range(numberOfEditrans):
    response = urllib.request.urlopen(URLEditrans)
    the_page = response.read().decode('latin-1')
    codeEditrans = the_page[the_page.find(textToSearch) + 22:the_page.find(textToSearch) + 36].replace(" ", "")

    if x == numberOfEditrans-1:
        f.write(codeEditrans)
    else:
        f.write(codeEditrans + "\n")
f.close()



