# Importing the modules
import PyPDF2
import pdfplumber
from deep_translator import GoogleTranslator
from gtts import gTTS
from tkinter import *
from tkinter import Tk,filedialog
from pygame import mixer
from tabulate import tabulate
import os

mixer.init()

# Define the MusicPlayer class
class MusicPlayer:
    def __init__(self, window):
        window.geometry('430x80')
        window.title(tfilename)
        window.resizable(0, 0)
        Load = Button(window, text='Load', width=10, font=('Times', 10), command=self.load)
        Play = Button(window, text='Play', width=10, font=('Times', 10), command=self.play)
        Pause = Button(window, text='Pause', width=10, font=('Times', 10), command=self.pause)
        Stop = Button(window, text='Stop', width=10, font=('Times', 10), command=self.stop)
        Load.place(x=0, y=20)
        Play.place(x=110, y=20)
        Pause.place(x=220, y=20)
        Stop.place(x=330, y=20)
        self.music_file = False
        self.playing_state = False

    def load(self):
        self.music_file = filedialog.askopenfilename()

    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()

    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
        else:
            mixer.music.unpause()
            self.playing_state = False

    def stop(self):
        mixer.music.stop()


# Welcome message
print("-----------------------------------------------------------------------------")
print(" Hey user! Welcome to the application of Multilingual Audiobooks Generator!!")
print("-----------------------------------------------------------------------------\n")


# Use file dialog to select the PDF file
pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
pdf = pdf_path if pdf_path.endswith(".pdf") else pdf_path + ".pdf"

# Getting PDF from user
#pdf_path = input("Please enter the full path of the PDF file: ")
pdf = pdf_path if pdf_path.endswith(".pdf") else pdf_path + ".pdf"
print("")

# Checking if the file exists
if os.path.exists(pdf):
    pdfFileObj = open(pdf, "rb")

    # Printing the total number of pages
    pdflen = len(pdf)
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    #pages = pdfReader.numPages
    pages = len(pdfReader.pages)
    hyphencount1 = (36 + pdflen) * "-"
    print(hyphencount1)
    print(" The total number of pages in", '"', pdf, '"', "is: ", pages)
    print(hyphencount1)
    print("")

    # Closing the PDF file
    pdfFileObj.close()

    mytext = ""

    # Extracting the text from the PDF
    with pdfplumber.open(pdf) as pdf:
        for i in range(0, pages):
            page = pdf.pages[i]
            mytext += page.extract_text()

    # Printing the text
    print("-----------------------")
    print(" The text in this PDF is :- ")
    print("-----------------------")
    print("")
    print(mytext)
    print("")
    print("")

    # Listing the Languages available for translation
    print("------------------------------------------------")
    print(" The list of languages for translation includes :- ")
    print("------------------------------------------------")
    print("")

    llist = [
        [1, "Afrikaans"], [2, "Albanian"], [3, "Amharic"], [4, "Arabic"], [5, "Armenian"],
        [6, "Azerbaijani"], [7, "Basque"], [8, "Belarusian"], [9, "Bengali"], [10, "Bosnian"],
        [11, "Bulgarian"], [12, "Catalan"], [13, "Cebuano"], [14, "Chinese"], [15, "Corsican"],
        [16, "Croatian"], [17, "Czech"], [18, "Danish"], [19, "Dutch"], [20, "English"],
        [21, "Esperanto"], [22, "Estonian"], [23, "Finnish"], [24, "French"], [25, "Frisian"],
        [26, "Galician"], [27, "Georgian"], [28, "German"], [29, "Greek"], [30, "Gujarati"],
        [31, "Hausa"], [32, "Haitian Creole"], [33, "Hawaiian"], [34, "Hebrew"], [35, "Hindi"],
        [36, "Hmong"], [37, "Hungarian"], [38, "Icelandic"], [39, "Igbo"], [40, "Indonesian"],
        [41, "Irish"], [42, "Italian"], [43, "Japanese"], [44, "Javanese"], [45, "Kannada"],
        [46, "Kazakh"], [47, "Khmer"], [48, "Kinyarwanda"], [49, "Korean"], [50, "Kurdish"],
        [51, "Kyrgyz"], [52, "Lao"], [53, "Latvian"], [54, "Lithuanian"], [55, "Luxembourgish"],
        [56, "Macedonian"], [57, "Malagasy"], [58, "Malay"], [59, "Malayalam"], [60, "Maltese"],
        [61, "Maori"], [62, "Marathi"], [63, "Mongolian"], [64, "Myanmar"], [65, "Nepali"],
        [66, "Norwegian"], [67, "Nyanja"], [68, "Odia"], [69, "Pashto"], [70, "Persian"],
        [71, "Polish"], [72, "Portuguese"], [73, "Punjabi"], [74, "Romanian"], [75, "Russian"],
        [76, "Samoan"], [77, "Scots Gaelic"], [78, "Serbian"], [79, "Sesotho"], [80, "Shona"],
        [81, "Sindhi"], [82, "Sinhala"], [83, "Slovak"], [84, "Slovenian"], [85, "Somali"],
        [86, "Spanish"], [87, "Sundanese"], [88, "Swahili"], [89, "Swedish"], [90, "Tagalog"],
        [91, "Tajik"], [92, "Tamil"], [93, "Tatar"], [94, "Telugu"], [95, "Thai"], [96, "Turkish"],
        [97, "Turkmen"], [98, "Ukrainian"], [99, "Urdu"], [100, "Uyghur"], [101, "Uzbek"],
        [102, "Vietnamese"], [103, "Welsh"], [104, "Xhosa"], [105, "Yiddish"], [106, "Yoruba"],
        [107, "Zulu"]
    ]

    # Arranging the languages in tabular form
    print(tabulate(llist, headers=["S.No", "Languages"], tablefmt="fancy_grid"))
    print("")
    print("---------------------------------------------------")

    # Getting user's choice for translation language
    lang = input("To which language do you want to TRANSLATE this text: ")
    print("---------------------------------------------------")
    print("")
    print("")

    # Translating the text from English to the user's preferred language
    to_translate = mytext
    translated = GoogleTranslator(source="auto", target=lang).translate(to_translate)

    # Printing the translated text
    print("-------------------------------------")
    print(" The translated text from this PDF : ")
    print("-------------------------------------")
    print("")
    print(translated)
    print("")
    print("")

    # Getting the language code from the language chosen by the user
    languages = {
        "Afrikaans": "af", "Albanian": "sq", "Amharic": "am", "Arabic": "ar",
        "Armenian": "hy", "Azerbaijani": "az", "Basque": "eu", "Belarusian": "be",
        "Bengali": "bn", "Bosnian": "bs", "Bulgarian": "bg", "Catalan": "ca",
        "Cebuano": "ceb", "Chinese": "zh", "Corsican": "co", "Croatian": "hr",
        "Czech": "cs", "Danish": "da", "Dutch": "nl", "English": "en", "Esperanto": "eo",
        "Estonian": "et", "Finnish": "fi", "French": "fr", "Galician": "gl", "Georgian": "ka",
        "German": "de", "Greek": "el", "Gujarati": "gu", "Haitian Creole": "ht", "Hausa": "ha",
        "Hawaiian": "haw", "Hebrew": "he", "Hindi": "hi", "Hmong": "hmn", "Hungarian": "hu",
        "Icelandic": "is", "Igbo": "ig", "Indonesian": "id", "Irish": "ga", "Italian": "it",
        "Japanese": "ja", "Javanese": "jv", "Kannada": "kn", "Kazakh": "kk", "Khmer": "km",
        "Kinyarwanda": "rw", "Korean": "ko", "Kurdish": "ku", "Kyrgyz": "ky", "Lao": "lo",
        "Latvian": "lv", "Lithuanian": "lt", "Luxembourgish": "lb", "Macedonian": "mk",
        "Malagasy": "mg", "Malay": "ms", "Malayalam": "ml", "Maltese": "mt", "Maori": "mi",
        "Marathi": "mr", "Mongolian": "mn", "Myanmar": "my", "Nepali": "ne", "Norwegian": "no",
        "Nyanja": "ny", "Odia": "or", "Pashto": "ps", "Persian": "fa", "Polish": "pl",
        "Portuguese": "pt", "Punjabi": "pa", "Romanian": "ro", "Russian": "ru", "Samoan": "sm",
        "Scots Gaelic": "gd", "Serbian": "sr", "Sesotho": "st", "Shona": "sn", "Sindhi": "sd",
        "Sinhala": "si", "Slovak": "sk", "Slovenian": "sl", "Somali": "so", "Spanish": "es",
        "Sundanese": "su", "Swahili": "sw", "Swedish": "sv", "Tagalog": "tl", "Tajik": "tg",
        "Tamil": "ta", "Tatar": "tt", "Telugu": "te", "Thai": "th", "Turkish": "tr", "Turkmen": "tk",
        "Ukrainian": "uk", "Urdu": "ur", "Uyghur": "ug", "Uzbek": "ug", "Vietnamese": "vi",
        "Welsh": "cy", "Xhosa": "xh", "Yiddish": "yi", "Yoruba": "yo", "Zulu": "zu"
    }
    langcode = languages.get(lang.title())

    # Getting the file name for saving the audio file
    print("-" * 56)

    root = Tk()
    root.withdraw()  # Hide the main window
    audio_folder = filedialog.askdirectory(title="Select Folder to Save Audio")
    root.destroy()
    
    if not audio_folder:
        print("Error: No folder selected. Exiting.")
        exit()

    # getting the file name for saving the audio file
    taudio = input(" Enter the Name for saving the audio file  ")
    tfilename = os.path.join(audio_folder, f"{taudio}.mp3")
    print("File path for saving the audio:", os.path.abspath(tfilename))

    #tfilename = taudio + ".mp3"
    print("-" * 56)
    print("")
    print(" Your Audio file is downloading, please wait till the audio player pops up")
    print("---------------------------------------------------------------------------")

    # converting the translated text to speech and saving it
    text_speech = gTTS(text=translated, lang=langcode)

    try:
        text_speech.save(tfilename)
        print("Audio file saved at:", os.path.abspath(tfilename))
        print("")
    except Exception as e:
        print(f"Error saving audio file: {e}")
        exit()

    #text_speech.save(tfilename)
    
    print("")

    print("NOTE :")
    print("")
    print("   Click on load and play ")
    print("---------------------------------")
    print("")
    print("")
    print("Enjoy the Audiobook!!!")

    # The below space is for the audio player
    print("""
    """)

    # Thank you message
    print("-------------------------------------------------------")
    print(" Thank you! Visit Again!! keeping gaining knowledge!!!")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    # Create an instance of MusicPlayer
    root = Tk()
    app = MusicPlayer(root)
    root.mainloop()

else:
    print(f"Error: File '{pdf_path}' not found.")
    exit()



'''# Importing the modules

import PyPDF2
import pdfplumber
from deep_translator import GoogleTranslator
from gtts import gTTS

from tkinter import *
import pygame
from tkinter import filedialog
from pygame import mixer
from tabulate import tabulate

#_______________________________________________________________________________________________________________________________________________________________________________
print("")
print("-----------------------------------------------------------------------------")
print(" Hey user! Welcome to the application of Multilingual Audiobooks Generator!!")
print("-----------------------------------------------------------------------------")
print("")
print("")

# Getting PDF from user

pdfname = input(" Please enter the Name of the PDF : ")
pdf = pdfname+".pdf"
print("")
pdflen = len(pdf)

# Reading the data in PDF

pdfFileObj = open(pdf, "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pages=pdfReader.numPages

hyphencount1 = (36 + pdflen) * "-"

# Printing the total number of pages

print(hyphencount1)
print(" The total number of pages in",'"',pdf,'"',"is : " ,pages)
print(hyphencount1)
print("")
pdfFileObj.close()

mytext = ""

# Extracting the text from the PDF

with pdfplumber.open(pdf) as pdf:
    for i in range(0,pages):
        page=pdf.pages[i]
        mytext += page.extract_text()

# Printing the text

print("-----------------------")        
print(" The text in this PDF is :- ")
print("-----------------------")
print("")
print(mytext)
print("")
print("")

# Listing the Languages available for translation

print("------------------------------------------------")
print(" The list of languages for translation includes :- " )
print("------------------------------------------------")
print("")

llist = [[1,"Afrikaans"],[2," Albanian"],[3," Amharic"], [4,"Arabic"],[5," Armenian"],
         
        [6," Azerbaijani"], [7,"Basque"],[8,"Belarusian"],[9," Bengali"],[10,"Bosnian"],
         
        [11,"Bulgarian"],[12," Catalan"],[13," Cebuano"],[14," Chinese"],[15,"Corsican"],
         
        [16," Croatian"],[17," Czech"],[18," Danish"],[19," Dutch"],[20," English"],
         
        [21,"Esperanto"],[22,"Estonian"],[23," Finnish"],[24," French"],[25," Frisian"],
         
        [26," Galician"],[27," Georgian"],[28," German"],[29,"Greek"],[30," Gujarati"],
         
        [31," Hausa"],[32,"Haitian Creole"],[33," Hawaiian"],[34," Hebrew"],[35," Hindi"],
         
        [36,"Hmong"],[37," Hungarian"],[38," Icelandic"],[39," Igbo"],[40," Indonesian"],
         
        [41,"Irish"],[42,"Italian"],[43," Japanese"],[44," Javanese"],[45," Kannada"],
         
        [46," Kazakh"],[47," Khmer"],[48," Kinyarwanda"],[49," Korean"],[50," Kurdish"],
         
        [51,"Kyrgyz"],[52," Lao"],[53,"Latvian"],[54," Lithuanian"],[55," Luxembourgish"],
         
        [56," Macedonian"],[57,"Malagasy"],[58," Malay"],[59," Malayalam"],[60," Maltese"],
         
        [61,"Maori"],[62," Marathi"],[63,"Mongolian"],[64," Myanmar"],[65," Nepali"],
         
        [66," Norwegian"],[67," Nyanja"],[68," Odia"],[69," Pashto"],[70," Persian"],
         
        [71,"Polish"],[72," Portuguese"],[73," Punjabi"],[74,"Romanian"],[75," Russian"],
         
        [76," Samoan"],[77," Scots Gaelic"],[78," Serbian"],[79," Sesotho"],[80," Shona"],
         
        [81,"Sindhi"],[82," Sinhala"],[83," Slovak"],[84," Slovenian"],[85,"Somali"],
         
        [86," Spanish"],[87," Sundanese"],[88," Swahili"],[89," Swedish"],[90," Tagalog"],
         
        [91,"Tajik"],[92," Tamil"],[93," Tatar"],[94," Telugu"],[95," Thai"],[96," Turkish"],
         
        [97,"Turkmen"],[98," Ukrainian"],[99," Urdu"],[100," Uyghur"],[101,"Uzbek"],
         
        [102," Vietnamese"],[103," Welsh"],[104," Xhosa"],[105," Yiddish"],[106," Yoruba"],[107," Zulu"]]

# Arranging the languages in tabular form

print(tabulate(llist,headers=["S.No","Languages"],tablefmt="fancy_grid"))
print("")
print("---------------------------------------------------")

# Getting user's choice for translation language

lang = input("To which language do you want to TRANSLATE this text : ")
print("---------------------------------------------------")
print("")
print("")
 
# Translating the text from English to user's preferred language

to_translate = mytext
translated = GoogleTranslator(source="auto",target=lang).translate(to_translate)

# Printing the translated text

print("-------------------------------------")
print(" The translated text from this PDF : ")
print("-------------------------------------")
print("")
print(translated)
print("")
print("")

# Getting the language code from the language chosen by the user

languages= {"Afrikaans": "af", "Albanian" : "sq", "Amharic" : "am", "Arabic" :"ar",
            
            "Armenian":"hy","Azerbaijani":"az","Basque":"eu", "Belarusian":"be",
            
            "Bengali":"bn","Bosnian":"bs","Bulgarian":"bg","Catalan":"ca",
            
            "Cebuano":"ceb","Chinese":"zh","Corsican":"co","Croatian":"hr",
            
            "Czech":"cs","Danish":"da","Dutch":"nl","English":"en","Esperanto":"eo",
            
            "Estonian":"et","Finnish":"fi","French":"fr","Galician":"gl","Georgian":"ka",
            
            "German":"de","Greek":"el","Gujarati":"gu","Haitian Creole":"ht","Hausa":"ha",
            
            "Hawaiian":"haw","Hebrew":"he","Hindi":"hi","Hmong":"hmn","Hungarian":"hu",
            
            "Icelandic":"is","Igbo":"ig","Indonesian":"id","Irish":"ga","Italian":"it",
            
            "Japanese":"ja","Javanese":"jv","Kannada":"kn","Kazakh":"kk","Khmer":"km",
            
            "Kinyarwanda":"rw","Korean":"ko","Kurdish":"ku","Kyrgyz":"ky","Lao":"lo",
            
            "Latvian":"lv","Lithuanian":"lt","Luxembourgish":"lb","Macedonian":"mk",
            
            "Malagasy":"mg","Malay":"ms","Malayalam":"ml","Maltese":"mt","Maori":"mi",
            
            "Marathi":"mr","Mongolian":"mn","Myanmar":"my","Nepali":"ne","Norwegian":"no",
            
            "Nyanja":"ny","Odia":"or","Pashto":"ps","Persian":"fa","Polish":"pl",
            
            "Portuguese":"pt","Punjabi":"pa","Romanian":"ro","Russian":"ru","Samoan":"sm",
            
            "Scots Gaelic":"gd","Serbian":"sr","Sesotho":"st","Shona":"sn","Sindhi":"sd",
            
            "Sinhala":"si","Slovak":"sk","Slovenian":"sl","Somali":"so","Spanish":"es",
            
            "Sundanese":"su","Swahili":"sw","Swedish":"sv","Tagalog":"tl","Tajik":"tg",
            
            "Tamil":"ta","Tatar":"tt","Telugu":"te","Thai":"th","Turkish":"tr","Turkmen":"tk",
            
            "Ukrainian":"uk","Urdu":"ur","Uyghur":"ug","Uzbek":"ug","Vietnamese":"vi",
            
            "Welsh":"cy","Xhosa":"xh","Yiddish":"yi","Yoruba":"yo","Zulu":"zu"}

langcode = languages.get(lang.title())

# Getting the file name for saving the audio file

print("-" * 56)
taudio = input(" Enter the Name in which the audio file should be saved : ")
tfilename = taudio+".mp3"
print("-" * 56)
print("")
print(" Your Audio file is downloading, please wait till the audio player pops up")
print("---------------------------------------------------------------------------")

# converting the translated text to speech and saving it

text_speech = gTTS(text=translated, lang=langcode)
text_speech.save(tfilename)
print("")

print("NOTE :")
print("")
print("   Click on load and play ")
print("---------------------------------")
print("")
print("")
print("Enjoy the Audiobook!!!")


# The below space is for the audio player

print("-------------------------------------------------------")
print(" Thank you! Visit Again!! keeping gaining knowledge!!!")
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")

# Building an audio player for playing the saved file

class MusicPlayer:

# Defining the geometry of the Music Player

    def __init__(self, window ):
        window.geometry('430x80'); window.title(tfilename); window.resizable(0,0)
        Load = Button(window, text = 'Load',  width = 10, font = ('Times', 10), command = self.load)
        Play = Button(window, text = 'Play',  width = 10,font = ('Times', 10), command = self.play)
        Pause = Button(window,text = 'Pause',  width = 10, font = ('Times', 10), command = self.pause)
        Stop = Button(window ,text = 'Stop',  width = 10, font = ('Times', 10), command = self.stop)
        Load.place(x=0,y=20);Play.place(x=110,y=20);Pause.place(x=220,y=20);Stop.place(x=330,y=20) 
        self.music_file = False
        self.playing_state = False

#  Defining the functionality of the Music player

    def load(self):
        self.music_file = filedialog.askopenfilename()
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False
    def stop(self):
        mixer.music.stop()

# Calling the function
        
root = Tk()
app= MusicPlayer(root)
root.mainloop()

#_______________________________________________________________________________________________________________________________________________________________________________
'''