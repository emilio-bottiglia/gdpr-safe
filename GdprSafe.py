import os
import fnmatch
import pathlib
import csv
from time import sleep
import sys
import openpyxl
import PyPDF2
import docx
from tqdm import tqdm

#global variables to hold filenames  
txtFiles = []
csvFiles = []
pdfFiles = []
docxFiles = []
excelFiles = []

#gdpr keywords
words = ["name", "surname", "first name", "second name", "maiden name", "address", 
         "passport", "driving license", "national id", "pps", "ppsn", 
         "social security number", "sex", "sexual", "phone", "health", "religion", 
         "photo", "genetic", "political", "straight", "gay", "bisex", "transex", 
         "orientation", "location", "ip address", "child", "kid", "coordinates", 
         "physical", "mental", "lgbt", "racial", "religious", "philosophical", 
        "trade union", "children", "biological", "biomedical", "medical", "diagnostic", 
        "physiology", "behavior", "behavioural", "facial", "visual", "dactyloscopic", 
        "fingerprint", "disease", "disability", "risk", "clinical", "treatment", "physiological", "physician"]

#helper method to ask user to enter directory to scan and check whether this exist or is valid
def helperPath():
    count = 0
    while count < 5:
        #ask user to  enter directory
        dir = input(r"Enter directory to scan, for example C:\Windows\Documents: ")
        #check if the directory exist. If not, exit the app after 5 attempts
        if not (os.path.exists(dir) or os.path.isdir(dir)) and not (count == 4):
            print("Invalid directory, check and try again")
            count+= 1
        elif count == 4:
            print("Invalid directory, try again later, goodbye!")
            sleep(3)
            exit()
        #if directory is valid
        else:
            return dir #return the directory

#inform user to close any open applicaton. If they want to proceed, ask for
#directory to scan. This function returns the path
def start():
    print('''
Welcome to GdprSafe v1.0 by EmilioB @All rights reserved
For library this application use, please refer to README.txt
This application is resource intensive, if you have lot of data to scan I recommend you close
any application in use before initiate scanning.
Also make sure you have access to the folder you want to scan.
''')
    dir = input ("Do you want to continue? y/n (press Enter for y): ")
    if ((dir == "y") or (dir == "")):# if user enter y or n
        return helperPath()#call helperPath() to verify directory exist
    elif dir == "n":# if user enter n, exit after 3 seconds
        print("Goodbye!")
        sleep(3)
        exit()
    else:
        # if user type any other char, give a second chance
        dir = input("Invalid entry. Type y/n or Enter for y :")
        if ((dir == "y") or (dir == "")):
            return helperPath()
        else:
            #if again a invalid entry, exit
            print("Invalid entry! Try again later, goodbye.")
            sleep(3)
            exit()

#check the directory for file with specific extensions and add them to the relevant lists. Print a summary of the number of files by type
def fileType():
    txtCount = 0
    csvCount = 0
    pdfCount = 0
    docxCount = 0
    excelCount = 0
    for root, dirs, files in os.walk(start()): #start() function contains path to scan
        for filename in files:
            if fnmatch.fnmatch(filename, "*.txt"):
                filePath = os.path.join(root, filename)
                txtFiles.append(filePath)
                txtCount = txtCount + 1
            elif fnmatch.fnmatch(filename, "*.csv"):
                filePath = os.path.join(root, filename)
                csvFiles.append(filePath)
                csvCount = csvCount + 1
            elif fnmatch.fnmatch(filename, "*.pdf"):
                filePath = os.path.join(root, filename)
                pdfFiles.append(filePath)
                pdfCount = pdfCount + 1
            elif fnmatch.fnmatch(filename, "*.xlsx"):
                filePath = os.path.join(root, filename)
                excelFiles.append(filePath)
                excelCount = excelCount + 1
            elif fnmatch.fnmatch(filename, "*.docx"):
                filePath = os.path.join(root, filename)
                docxFiles.append(filePath)
                docxCount = docxCount + 1
            else:
                pass
    #print summary of files by type
    print("Summary of files found by extension:")
    print(f"txt: {txtCount}")
    print(f"csv: {csvCount}")
    print(f"pdf: {pdfCount}")
    print(f"docx: {docxCount}")
    print(f"excel: {excelCount}")
 
fileType()

#parse txt file list seeking key words. Add file link and key words in columns in csv file
def txtParse():
    keyWords = []
    print("Reading txt files...")
    for txt in tqdm(txtFiles): #tqdm - progress bar
        file = open(txt, "r").read()
        keyWords.append(txt) #add file path to the list
        for word in words:
            #file.lower change the text in lower case to pick also words that were only uppercase
            if ((word in file.lower()) and (word not in keyWords)): 
                keyWords.append(word) #add key word to the list
        report = open("report.csv", "a", newline="") 
        csvWriter = csv.writer(report)
        csvWriter.writerow(keyWords)
        report.close()
        keyWords = [] #empty list
        
txtParse()

#parse excel file seeking key words. Add file link and key words in columns in csv file
def excelParse():
    keyWords = []
    print("Reading excel files...")
    for xlsx in tqdm(excelFiles):
        wb = openpyxl.load_workbook(xlsx) #workbook
        keyWords.append(xlsx)
        ws = wb.worksheets #return a list of sheets in the wb
        for sheet in ws:
            for row in sheet:
                for cell in row:
                    for word in words:
                        if ((word == cell.value) and (word not in keyWords)):
                            keyWords.append(word) #add key word to the list
        report = open("report.csv", "a", newline="") 
        csvWriter = csv.writer(report)
        csvWriter.writerow(keyWords)
        report.close()
        keyWords = [] #empty list

excelParse()

#parse csv file seeking key words. Add file link and key words in columns in csv file
def csvParse():
    keyWords = []
    print("Reading csv files...")
    for cs in tqdm(csvFiles):
        file = open(cs, "r", encoding="utf-8", newline="")
        keyWords.append(cs)
        csvReader = csv.reader(file)
        for line in csvReader: #read each line 
            for word in words:
                if ((word in line) and (word not in keyWords)):
                    keyWords.append(word) #add key word to the list
        report = open("report.csv", "a", newline="") 
        csvWriter = csv.writer(report)
        csvWriter.writerow(keyWords)
        report.close()
        keyWords = []

csvParse()

#parse pdf file seeking key words. Add file link and key words in columns in csv file
def pdfParse():
    print("Reading pdf files...")
    keyWords = []
    pdfPages = []
    text = ""
    for pdfDoc in tqdm(pdfFiles): 
        keyWords.append(pdfDoc)
        pdfFile = open(pdfDoc, "rb") #rb, read in bynary mode
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        pdfPages = pdfReader.numPages
        for page in range(pdfPages): 
            pObject = pdfReader.getPage(page)
            text = pObject.extractText()
            if text != "":
                text = text
            else: #ocr module that read scanned pdf files
                text = textract.process(fileurl, method='tesseract', language='eng')
            for word in words:
                if ((word in text) and (word not in keyWords)):
                    keyWords.append(word) #add key word to the list
        report = open("report.csv", "a", newline="") 
        csvWriter = csv.writer(report)
        csvWriter.writerow(keyWords)
        report.close()
        keyWords = []

pdfParse()

#parse docx file seeking key words. Add file link and key words in columns in csv file
def docxParse():
    print("Reading word files...")
    keyWords = []
    for doc in tqdm(docxFiles):
        docOpen = docx.Document(doc)
        keyWords.append(doc)
        for par in docOpen.paragraphs: #paragraphs 
            for p in par.runs:
                for word in words:
                    if ((word in p.text) and (word not in keyWords)):
                        keyWords.append(word)
        report = open("report.csv", "a", newline="") 
        csvWriter = csv.writer(report)
        csvWriter.writerow(keyWords)
        report.close()
        keyWords =[]

docxParse()

#final function
def end():
    print('''

Pick your csv report in the python folder. Goodbye!
''')
    input("Close the window to exit the program")
    
end()
