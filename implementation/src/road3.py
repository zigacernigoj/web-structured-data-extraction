from bs4 import BeautifulSoup
import numpy as np

def compare_by_line(cons1, cons2):

    max1 = len(cons1)
    i1 = 0

    max2 = len(cons2)
    i2 = 0

    regex_string = ""
    new_stuff = []

    while i1 < max1-1 or i2 < max2-1:
        # print(cons1[i1], cons2[i2])

        cons1[i1] = cons1[i1].strip()
        cons2[i2] = cons2[i2].strip()

        # get types
        if cons1[i1].startswith("<") and cons1[i1].endswith(">"):
            type1 = "tag"
        else:
            type1 = "string"

        if cons2[i2].startswith("<") and cons2[i2].endswith(">"):
            type2 = "tag"
        else:
            type2 = "string"

        # check if same
        if cons1[i1] == cons2[i2]:
            print(i1, i2)
            new_stuff.append(cons1[i1])

        else:

            # string mismatch
            if type1 == "string" and type1 == "string":
                new_stuff.append("#PCDATA")

            # tag mismatch
            if type1 == "tag" and type1 == "tag":

                # first check for iterations of same element

                for i in reversed(range(len(new_stuff))):
                    print("rs", i, new_stuff[i])
                    if new_stuff[i].startswith("</"):
                        last_tag = new_stuff[i]
                        break

                print("last tag", last_tag)
                print(new_stuff)
                break



        if i1 < max1-1:
            i1 += 1
        if i2 < max2-1:
            i2 += 1

    print(i1, max1)
    print(i2, max2)

    print(regex_string)



def process_file(all_contents):
    print("roadrunner, num of contents", len(all_contents))

    content1 = all_contents[0]
    content2 = all_contents[1]

    # create trees from contents
    parsed1 = BeautifulSoup(content1, 'html.parser')
    parsed2 = BeautifulSoup(content2, 'html.parser')

    for tag in parsed1.recursiveChildGenerator():
        if hasattr(tag, 'attrs'):
            tag.attrs = None

    for tag in parsed2.recursiveChildGenerator():
        if hasattr(tag, 'attrs'):
            tag.attrs = None

    prepared1 = parsed1.body.prettify().split("\n")
    prepared2 = parsed2.body.prettify().split("\n")

    print(prepared1)
    print(prepared2)

    compare_by_line(prepared1, prepared2)