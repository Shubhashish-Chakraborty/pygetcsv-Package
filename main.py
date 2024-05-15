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




# convertToCSV("C:/codepurposes/ImportantFiles/SampleBin")

# ReadFile("C:/codepurposes/ImportantFiles/SampleBin")