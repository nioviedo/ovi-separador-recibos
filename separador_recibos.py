# -*- coding: utf-8 -*-
"""
Created on Mon May 31 20:12:56 2021

@author: Ovi
"""
#==================================================#
#                                                  #
#               Separador de pdf                   #
#                                                  #
#                                                  #
#==================================================#

#Mise en place

import os 
#pip install PyPDF2
import PyPDF2

os.getcwd()  

#User input
os.chdir('C:\\Users\\Ovi\\Desktop\\separador_recibos') # working directory with receipts
year = 2021 #AAAA
month = 6   #MM

#Get PDF
def PDFsplit(pdf, splits):
    pdfFileObj = open(pdf, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    start = 0
    end = splits[0]

    for i in range(len(splits)+1):
        # creating pdf writer object for (i+1)th split
        pdfWriter = PyPDF2.PdfFileWriter()
         
        # output pdf file name
        pageObj = pdfReader.getPage(2*i)
        surname = pageObj.extractText()
        surname = surname.replace("\n \n", "**")
        surname = surname.split("*",2)
        surname = surname[0]
        surname = surname.replace("\n", "_")

        outputpdf = pdf.split('.pdf')[0] + str(i) + surname + str(month) + str(year) +'.pdf'
        
        # robust version: comment previous block and uncomment this line:
        #outputpdf = pdf.split('.pdf')[0] + str(i) + str(month) + str(year) +'.pdf'
        
        # adding pages to pdf writer object
        for page in range(start,end):
            pdfWriter.addPage(pdfReader.getPage(page))
         
        # writing split pdf pages to pdf file
        with open(outputpdf, "wb") as f:
            pdfWriter.write(f)
 
        # interchanging page split start position for next split
        start = end
        try:
            # setting split end position for next split
            end = splits[i+1]
        except IndexError:
            # setting split end position for last split
            end = pdfReader.numPages
         
    # closing the input pdf file object
    pdfFileObj.close()
             
def main():
    # pdf file to split
    pdf = 'sueldos_premier.pdf'
     
    # split page positions
    splits = [2,4,6,8,10,12,14,16,18,20,22,24]
     
    # calling PDFsplit function to split pdf
    PDFsplit(pdf, splits)
 
if __name__ == "__main__":
    # calling the main function
    main()

#Testing ground
"""
pdfFileObj = open('sueldos_premier.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(10)
print(pageObj.extractText())

surname = pageObj.extractText()
surname = surname.replace("\n \n", "**")
surname = surname.split("*",2)
surname = surname[0]
surname = surname.replace("\n", "_")
surname = surname.replace(" ", "_")
surname = surname.replace("-", "_")
"""