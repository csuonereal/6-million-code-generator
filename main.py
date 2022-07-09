import string
import random

from dummy import HashTable


ht = HashTable()

#6000000


def main():
    global ht
    for i in range(6000000):
        ht.insert()
    ht.closeFile()

if __name__ == "__main__":
    main()
