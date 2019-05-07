def compare_contents(cons1, cons2):

    cons1 = list(filter(lambda el: el != '\n', cons1))
    cons2 = list(filter(lambda el: el != '\n', cons2))

    regex = ""
    combined = []


    for (idx, c1) in enumerate(cons1):
        if c1 in cons2 and cons2.index(c1) == idx:
            print("on same spot")

            addition = c1
            if hasattr(c1, 'prettify'):
                addition = addition.prettify()
            else:
                addition = "<!-- XYZ" + addition + " -->\n"
            regex += addition

            combined.append(addition)

        elif c1 in cons2:
            if idx < cons2.index(c1):
                print("v Cons2 je se nekaj vmes", idx, cons2.index(c1))  # cons2[idx]
                print(cons2[idx], "\n")

                addition = cons2[idx]
                if hasattr(cons2[idx], 'prettify'):
                    addition = addition.prettify()
                else:
                    addition = "(<!-- " + addition + " -->)?"
                regex += "(" + addition + ")?"

                combined.append("(" + addition + ")?")

                addition = c1
                if hasattr(c1, 'prettify'):
                    addition = addition.prettify()
                else:
                    addition = "<!-- " + addition + " -->"
                regex += addition

                combined.append(addition)

            if idx > cons2.index(c1):
                print("v Cons1 je se nekaj vmes", idx, cons2.index(c1))  # cons1[idx]
                print(cons1[idx], "\n")
                # regex += "(" + cons1[idx].prettify() + ")?"
                regex += "\nTODO"


        else:
            print("\nne obstaja v Cons2", c1, "\n")
            # primerjaj posebej v globino
            regex += "\nMISSING"


    # print("REGEX:")
    # print(regex)

    pretty1 = [x.prettify() if hasattr(x, 'prettify') else  "<!-- " + x + " -->\n" for x in cons1]
    pretty2 = [x.prettify() if hasattr(x, 'prettify') else  "<!-- " + x + " -->\n" for x in cons2]

    print(pretty1)
    print(pretty2)
    print(combined)

    pass

