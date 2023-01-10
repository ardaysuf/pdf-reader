import pyttsx3
import PyPDF2

file = input("File Name (python.pdf): ")
rate = input("Reading Rate: ")

story = open(file,"rb")
pdfReader = PyPDF2.PdfFileReader(story)

engine = pyttsx3.init()
voices = engine.getProperty("voices")

engine.setProperty("voice", voices[0].id) 
engine.setProperty("rate" , int(rate))

for pageNumber in range(0, pdfReader.numPages):
    page = pdfReader.getPage(pageNumber)
    article = page.extractText()
    engine.say(article)
    engine.runAndWait()
    engine.stop()

    
