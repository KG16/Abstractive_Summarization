import os

import pandas as pd


def main():
    path = "C:\\Users\\kriti\\Documents\\Project\\Abstractive_Summarization\\Dataset"
    files = os.listdir(path)
    for file in files:
        df = pd.read_csv("C:\\Users\\kriti\\Documents\\Project\\Abstractive_Summarization\\Results")
        col_names = ['Precision', 'Recall', 'F-measure']
        data = pd.read_csv('test.csv', names=col_names)
