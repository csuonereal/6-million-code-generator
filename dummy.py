import string
import random
import sqlite3

from codeGenerator import *


class HashTable:

    def __init__(self):
        self.codesDict = dict()
        self.outputfile = open('6million.csv', "w")
        self.bannedWords = ["AM", "AMK", "AQ", "AW", "SIK", "ASS","HOLE","ALLAH", "TANRI", "AMCIK", "MATURE", "AMIK", "MEME", "OC", "ORAL", "ANAL", "PENIS", "SEX", "PIC", "PIPI", "YARAK", "YARRAK", "GOT", "FCK", "FUCK", "GEY", "GAY", "LEZ", "TRANS", "LGBT", "DOMAL", "GAVAT", "IBNE", "IPNE", "KAHBE", "KALTAK", "KANCIK", "OROS", "ORSPU", "SKIK", "YAVSAK", "S3X", "S3KS", "SX", "YVSK", "YRK", "SEKS", "SIKIS", "AMIK", "MAST", "DIE", "DEATH",
                            "ORSP", "SIC", "SICIS", "OPUS", "SPERM", "DOL", "YRRK", "CHP", "AKP", "HDP", "MHP", "DP", "DEVA", "SP", "ANAN", "ANNE", "ANAAN", "BACI", "EBE", "BOK", "BITCH", "BOSAL", "DILDO", "KAKA", "KASAR", "MAL", "SALAK", "LAVUK", "OGLAN", "OSBIR", "PEZO", "SAKSO", "SAXO", "SURT", "TASAK", "VELET", "VELED", "WHORE", "YALA", "ZIK", "ETI", "ULKER", "NESTLE", "SAGRA", "KINDER", "ALGIDA", "MILF", "PORN", "PORNO", "LEZB", "LEZBI", "PUSSY", "BTCH", "AMQ"]

    def printBannedWords(self):
        for bannedWord in self.bannedWords:
            print(bannedWord)

    # def idGenerator(self, size=6, chars=string.ascii_uppercase + string.digits):
    #     code = ''.join(random.choice(chars) for _ in range(size))
    #     return code

    def closeFile(self):
        self.outputfile.close()

    def insert(self):
        # item = self.idGenerator()
        item = generateCode()
        if not self.codesDict.__contains__(item) and self.isCodeConfirmed(item):
            self.codesDict[item] = item
            self.outputfile.write(item+"\n")
        else:
            self.insert()

    def isCodeConfirmed(self, code):
        for bannedWord in self.bannedWords:
            if bannedWord in code:
                return False
        return True

    def printCodes(self):
        ind = 0
        for key, value in self.codesDict.items():
            print(ind, value)
            ind += 1

    def printDictLength(self):
        print(len(self.codesDict))

    def dbInitializer(self):
        connection = sqlite3.connect('test.db')
        cursor = connection.cursor()

        tableCommand = """ CREATE TABLE IF NOT EXISTS CODES (
            code CHAR(255) NOT NULL
        ); """
        cursor.execute(tableCommand)
        connection.close()

    def insertCodeIntoTable(self, code):
        try:
            connection = sqlite3.connect('test.db')
            cursor = connection.cursor()

            cursor.execute("INSERT INTO CODES VALUES(?)", (code,))
            connection.commit()
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)
        finally:
            if connection:
                connection.close()

    def controlIfCodeExist(self, code):
        try:
            connection = sqlite3.connect('test.db')
            cursor = connection.cursor()
            cursor.execute("SELECT 1 FROM CODES WHERE code=?", (code,))
            if cursor.fetchone():
                connection.commit()
                cursor.close()
                return True
            else:
                connection.commit()
                cursor.close()
                return False

        except sqlite3.Error as error:
            print(error)
        finally:
            if connection:
                connection.close()
