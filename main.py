import pickle
import csv
import time
import os

def ReadFile(path):

    with open(path + ".dat", "rb") as f:

        try:
            while True:
                print(pickle.load(f))
        except EOFError:
            pass



def convertToCSV(path , CSVFileName = "CSVFile"):

    with open(path + ".dat", "rb") as f:

        global File_Data
        File_Data = []

        try:
            while True:
                File_Data.append(pickle.load(f))
        except EOFError:
            pass


    
    #WRITING TITLE FOR THE CSV FILE

    with open(CSVFileName + ".csv", "w", newline="") as f:


        HeadingList = []
        for d in range(len(File_Data)):


            for k in range(len(File_Data[d])):
                
                
                for h in File_Data[d]:

                    HeadingList.append(h)
                    
        
        CSVheading = HeadingList[0 : len(File_Data[d]) : 1]

        wobjH = csv.writer(f)

        wobjH.writerow(CSVheading)



    #WRITING DATA FOR THE CSV FILE

    with open(CSVFileName + ".csv", "a", newline="") as f:

        wobjD = csv.writer(f)


        for data in range(len(File_Data)):

            AddDataList = []
            for key in File_Data[data]:

                AddDataList.append(File_Data[data][key])

            wobjD.writerow(AddDataList)




# convertToCSV("C:/codepurposes/ImportantFiles/SampleBin1")
# convertToCSV("C:/codepurposes/ImportantFiles/SampleBin2")

# ReadFile("C:/codepurposes/ImportantFiles/SampleBin1")
# ReadFile("C:/codepurposes/ImportantFiles/SampleBin2")