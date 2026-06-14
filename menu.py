import csv_parser

def printMainMenu():
    print("Main Menu")
    print("---------")
    print("1. show edited data")
    print("2. show raw data")
    print("3. pre show import")
    print("4. import data")


class Menu:
    def __init__(self):
        pass

    def start(self):
        while True:
            printMainMenu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.parseDocument(".personal_files/Umsatzanzeige_DE97500105175441090453_20260613.csv")
                break

            [print("") for i in range(20)]

    def parseDocument(self, filename:str):
        parser = csv_parser.Parser()
        parser.parse(filename)
