# main file that contains main function
import sys
from os import listdir
from os.path import isfile, join, abspath, dirname
from src import xpath
from src import re
from src import road


def get_files_contents(path):
    all_contents = []
    for el in listdir(path):
        file = join(path, el)
        if isfile(file):
            print(file)
            f = open(file, "r", encoding='utf-8', errors='ignore')
            content = f.read()
            all_contents.append(content)
            f.close()

    return all_contents


def main(start_arguments):
    # TODO implement
    approach_type = 'xpath'
    page_type = 'rtvslo.si'

    if len(start_arguments) >= 2:
        approach_type = start_arguments[1]

    if len(start_arguments) >= 3:
        page_type = start_arguments[2]

    print("Inputed page {} with type {}".format(page_type, approach_type))

    path = "../input/" + page_type + "/"
    path = join(dirname(abspath(__file__)), path)

    all_contents = get_files_contents(path)
    print("number of contents:", len(all_contents))

    if approach_type == 'xpath':
        for content in all_contents:
            xpath.process_file(content, page_type)
    elif approach_type == 're':
        for content in all_contents:
            re.process_file(content, page_type)
    elif approach_type == 'road':
        road.process_file(all_contents)

    print("ended")


if __name__ == "__main__":
    main(sys.argv)
