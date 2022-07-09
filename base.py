import string
import random


class HashTable:

    def __init__(self):
        self.codesDict = dict()

    def idGenerator(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def insert(self):
        item = self.idGenerator()
        if not self.codesDict.__contains__(item):
            self.codesDict[item] = item

    def printCodes(self):
        ind = 0
        for key, value in self.codesDict.items():
            print(ind, value)
            ind += 1

    def printDictLength(self):
        print(len(self.codesDict))