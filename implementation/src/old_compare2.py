def check_if_all(cons1, cons2, allx):
    allx = [x[1:-2] if x.startswith("(") else x for x in allx]

    print("CHECK 1:")
    for c1 in cons1:
        if c1 not in allx:
            print("missing", c1)

    print("CHECK 2:")
    for c2 in cons2:
        if c2 not in allx:
            print("missing", c2)


    allx = list(filter(lambda a: not(a in cons1 and a in cons2) , allx))

    print("doubled")
    print(allx)



def compare_contents(cons1, cons2):

    cons1 = list(filter(lambda el: el != '\n', cons1))
    cons2 = list(filter(lambda el: el != '\n', cons2))

    pretty1 = [x.prettify() if hasattr(x, 'prettify') else "<!--" + x + "-->\n" for x in cons1]
    pretty2 = [x.prettify() if hasattr(x, 'prettify') else "<!--" + x + "-->\n" for x in cons2]

    regex = ""
    combined = []

    while cons1 and cons2:

        if cons1[0] in cons2 and cons2.index(cons1[0]) == 0:
            print("on same spot")

            addition = cons1[0]
            if hasattr(addition, 'prettify'):
                addition = addition.prettify()
            else:
                addition = "<!--" + addition + "-->\n"
            regex += addition

            combined.append(addition)

            cons1.pop(0)
            cons2.pop(0)

        elif cons1[0] in cons2:
            if 0 < cons2.index(cons1[0]):
                print("v Cons2 je se nekaj vmes", 0, cons2.index(cons1[0]))  # cons2[idx]
                print(cons2[0], "\n")

                addition = cons2[0]
                if hasattr(addition, 'prettify'):
                    addition = addition.prettify()
                else:
                    addition = "(<!--" + addition + "-->\n)?"
                regex += "(" + addition + ")?"

                combined.append("(" + addition + ")?")

                # primerjaj z vsemi iz c1

                print("cons2[0] in cons1?", cons2[0] in cons1)


                cons2.pop(0)

            else:
                print("AAAAAAAAAAAAAAAAAA")
                break

            # if idx > cons2.index(c1):
            #     print("v Cons1 je se nekaj vmes", idx, cons2.index(c1))  # cons1[idx]
            #     print(cons1[idx], "\n")
            #     # regex += "(" + cons1[idx].prettify() + ")?"
            #     regex += "\nTODO"


        else:
            print("\nne obstaja v Cons2", cons1[0], "\n")
            # primerjaj posebej v globino

            addition = cons1[0]
            if hasattr(addition, 'prettify'):
                addition = addition.prettify()
            else:
                addition = "(<!--" + addition + "-->\n)?"
            regex += addition

            combined.append("(" + addition + ")?")

            cons1.pop(0)




    # print("REGEX:")
    # print(regex)

    print(pretty1)
    print(pretty2)
    print(combined)

    check_if_all(pretty1, pretty2, combined)


    x=''.join(combined)

    print(repr(x))


    pass

