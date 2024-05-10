import pickle
import csv
import time
import os


def convertToCSV(path , CSVname = "CSVFile"):

    with open(path + ".dat", "rb") as f:

        global File_Data
        File_Data = []

        try:
            while True:
                File_Data.append(pickle.load(f))
        except EOFError:
            pass