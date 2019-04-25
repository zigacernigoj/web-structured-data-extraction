# main file that contains main function
import sys
from os import listdir
from os.path import isfile, join
from src import xpath
from src import re

if __name__ == "__main__":

    # TODO implement
    type = 're'
    page = 'overstock.com'

    if len(sys.argv) >= 2:
        type = sys.argv[1]

    if len(sys.argv) >= 3:
        page = sys.argv[2]

    print("Inputed page {} with type {}".format(page, type))

    path = "../input/" + page + "/"

    for f in listdir(path):
        file = join(path, f)
        if isfile(file):
            print(file)
            f = open(file, "r", encoding='utf-8', errors='ignore')
            content = f.read()
            if type == 'xpath':
                xpath.process_file(content, page)
            elif type == 're':
                re.process_file(content, page)
            f.close()

    print("ended")
