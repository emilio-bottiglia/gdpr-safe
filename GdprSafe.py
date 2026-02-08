#v1.1 see CHANGELOG.MD

import os
import fnmatch
import csv
from time import sleep
import openpyxl
import docx
from tqdm import tqdm
import pymupdf

#global variables to hold filenames
TXT_FILES = []
CSV_FILES = []
PDF_FILES = []
DOCX_FILES = []
EXCEL_FILES = []

#gdpr sample keywords
WORDS = ["name", "surname", "first name", "second name", "maiden name", "address",
         "passport", "driving license", "national id", "pps", "ppsn",
         "social security number", "sex", "sexual", "phone", "health", "religion",
         "photo", "genetic", "political", "straight", "gay", "bisex", "transex",
         "orientation", "location", "ip address", "child", "kid", "coordinates",
         "physical", "mental", "lgbt", "racial", "religious", "philosophical",
        "trade union", "children", "biological", "biomedical", "medical", "diagnostic",
        "physiology", "behavior", "behavioural", "facial", "visual", "dactyloscopic",
        "fingerprint", "disease", "disability", "risk", "clinical", "treatment", "physiological", "physician"]


#helper method to ask user to enter directory to scan and check whether this exist or is valid
def helper_path():
    count = 0
    while count < 5:
        #ask user to  enter directory, 5 attempts
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


#inform user to close any open application. If they want to proceed, ask for
#directory to scan. This function returns the path
def start():
    print('''
Welcome to GdprSafe v1.0 by EmilioB @All rights reserved
For library this application use, please refer to README.txt
This application is resource intensive, if you have lot of data to scan I recommend you close
any application in use before initiate scanning.
Also make sure you have access to the folder you want to scan.
''')
    user_choice = input ("Do you want to continue? y/n (press Enter for y): ")
    if user_choice == "y" or user_choice == "":# if user enter y or press Enter
        return helper_path()#call helperPath() to verify directory exist
    elif user_choice == "n":# if user enter n, exit after 3 seconds
        print("Goodbye!")
        sleep(3)
        exit()
    else:
        # if user type any other char, give a second chance
        user_choice = input("Invalid entry. Type y/n or Enter for y :")
        if user_choice == "y" or user_choice == "":
            return helper_path()
        else:
            #if again a invalid entry, exit
            print("Invalid entry! Try again later, goodbye.")
            sleep(3)
            exit()


#check the directory for file with specific extensions and add them to the relevant lists.
# Print a summary of the number of files by type
def file_type():
    txt_count = 0
    csv_count = 0
    pdf_count = 0
    docx_count = 0
    excel_count = 0
    for root, dirs, files in os.walk(start()): #start() function contains path to scan
        for filename in files:
            if fnmatch.fnmatch(filename, "*.txt"):
                file_path = os.path.join(root, filename)
                TXT_FILES.append(file_path)
                txt_count = txt_count + 1
            elif fnmatch.fnmatch(filename, "*.csv"):
                file_path = os.path.join(root, filename)
                CSV_FILES.append(file_path)
                csv_count = csv_count + 1
            elif fnmatch.fnmatch(filename, "*.pdf"):
                file_path = os.path.join(root, filename)
                PDF_FILES.append(file_path)
                pdf_count = pdf_count + 1
            elif fnmatch.fnmatch(filename, "*.xlsx"):
                file_path = os.path.join(root, filename)
                EXCEL_FILES.append(file_path)
                excel_count = excel_count + 1
            elif fnmatch.fnmatch(filename, "*.docx"):
                file_path = os.path.join(root, filename)
                DOCX_FILES.append(file_path)
                docx_count = docx_count + 1
            else:
                pass
    #print summary of files by type
    print("Summary of files found by extension:")
    print(f"txt: {txt_count}")
    print(f"csv: {csv_count}")
    print(f"pdf: {pdf_count}")
    print(f"docx: {docx_count}")
    print(f"excel: {excel_count}")

#parse txt file list seeking key words
def txt_parse():
    txt_key_words = []
    list_of_lists = []
    print("Reading txt files...")
    for txt in tqdm(TXT_FILES): #tqdm - progress bar
        with open(txt, "r", encoding="utf-8") as f:
            text = f.read().replace("\n", "").strip()
            txt_key_words.append(txt) #add file path to the list
            for word in WORDS:
                #file.lower change the text in lower case to pick also words that were only uppercase
                if word in text.lower() and word not in txt_key_words:
                    txt_key_words.append(word) #add key word to the list
        list_of_lists.append(txt_key_words)
        txt_key_words = [] # reset list
    sleep(1)
    return list_of_lists


#parse pdf file list seeking key words
def pdf_parse():
    pdf_key_words = []
    list_of_lists = []
    print("Reading pdf files...")
    for pdf in tqdm(PDF_FILES):
        pdf_key_words.append(pdf) #add file path to the list
        document = pymupdf.open(pdf)
        for page in document:
            text = page.get_text().split()#return a list (text)
            for word in text:
                word_lowercase = word.lower()
                if word_lowercase in WORDS and word_lowercase not in pdf_key_words:
                    pdf_key_words.append(word_lowercase)
            list_of_lists.append(pdf_key_words)
            pdf_key_words = []
    sleep(1)
    return list_of_lists


#parse excel file list seeking key words
def excel_parse():
    xlsx_key_words = []
    list_of_lists = []
    print("Reading excel files...")
    for xlsx in tqdm(EXCEL_FILES):
        wb = openpyxl.load_workbook(xlsx) #workbook
        xlsx_key_words.append(xlsx)
        ws = wb.worksheets #return a list of sheets in the wb
        for sheet in ws:
            for row in sheet:
                for cell in row:
                    for word in WORDS:
                        if word == cell.value and word not in xlsx_key_words:
                            xlsx_key_words.append(word) #add key word to the list
        list_of_lists.append(xlsx_key_words)
        xlsx_key_words = []
    sleep(1)
    return list_of_lists

#parse csv file list seeking key words
def csv_parse():
    csv_key_words = []
    list_of_lists = []
    print("Reading csv files...")
    for cs in tqdm(CSV_FILES):
        file = open(cs, "r", encoding="utf-8", newline="")
        csv_key_words.append(cs)
        csvReader = csv.reader(file)
        for line in csvReader: #read each line
            for word in WORDS:
                if word in line and word not in csv_key_words:
                    csv_key_words.append(word) #add key word to the list
        list_of_lists.append(csv_key_words)
        csv_key_words = []
    sleep(1)
    return list_of_lists

#parse docx file list seeking key words
def docx_parse():
    print("Reading word files...")
    docx_key_words = []
    list_of_lists = []
    for doc in tqdm(DOCX_FILES):
        doc_open = docx.Document(doc)
        docx_key_words.append(doc)
        for par in doc_open.paragraphs: #paragraphs
            for p in par.runs:
                for word in WORDS:
                    if ((word in p.text) and (word not in docx_key_words)):
                        docx_key_words.append(word)
        list_of_lists.append(docx_key_words)
        docx_key_words = []
    sleep(1)
    return list_of_lists

#add each file link and their keywords in a single line in csv file
# parameter: list of lists returned by each scanner
def add_to_report(_key_words):
    print("Writing to csv report...")
    report = open("report.csv", "a", newline="")
    csv_writer = csv.writer(report)
    for w in _key_words:
        csv_writer.writerow(w)
    report.close()
    print("Complete!")

#final function
def end():
    work_dir = os.getcwd()
    print(f'''
Pick your csv report in the {work_dir} folder. Goodbye!
''')
    input("Close the window or press enter to exit the program")

#main
def main():
    file_type()
    print("\n")
    txt_key_words = txt_parse()
    add_to_report(txt_key_words)
    print("\n")
    pdf_key_words = pdf_parse()
    add_to_report(pdf_key_words)
    print("\n")
    xlsx_key_words = excel_parse()
    add_to_report(xlsx_key_words)
    print()
    csv_key_words = csv_parse()
    add_to_report(csv_key_words)
    print("\n")
    docx_key_words = docx_parse()
    add_to_report(docx_key_words)
    end()
         

if __name__ == "__main__":
    main()

