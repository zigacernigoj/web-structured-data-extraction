from bs4 import BeautifulSoup
import numpy as np
import math

def get_similarity(tree1, tree2):
    pass


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

def simple_tree_matching(tree1, tree2):

    if tree1.name is None or tree2.name is None:
        # print("isn't a valid DOM node", tree1, tree2)
        if tree1 == tree2:
            return 1
        else:
            return 0

    if tree1.name != tree2.name:
        # print("not same NAME:", tree1.name, "VS", tree2.name)
        return 0

    children1 = list(tree1.children)
    children2 = list(tree2.children)

    m = len(children1)
    n = len(children2)

    # print("SAME", tree1.name, tree1.attrs, m, "VS", tree2.name, tree2.attrs, n)

    # if m == 0:  # tree1 is a leaf
        # print("m=0:\n", tree1, "\n", tree2)
    # if n == 0:  # tree2 is a leaf
        # print("n=0:\n", tree1, "\n", tree2)

    if m == 0 or n == 0:
        if tree1.name == tree2.name:
            return 1
        else:
            return 0

    big_m = np.empty([m, n])

    big_m[:, 0] = 0  # for i=0 to m do: M[i][0] = 0
    big_m[0, :] = 0  # for j=0 to n do: M[0][j] = 0

    for i in range(1, m):
        for j in range(1, n):
            w_ij = simple_tree_matching(children1[i-1], children2[j-1])
            big_m[i, j] = max(big_m[i, j-1], big_m[i-1, j], big_m[i-1, j-1] + w_ij)

    return big_m[m-1, n-1] + 1


def string_distance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]




def compare_contents(cons1, cons2):

    cons1 = list(filter(lambda el: el != '\n', cons1))
    cons2 = list(filter(lambda el: el != '\n', cons2))

    print("STRANI:")
    print(list(enumerate(cons1)))
    print("||||||")
    print(list(enumerate(cons2)))
    print("STRANI:")

    pretty1 = [x.prettify() if hasattr(x, 'prettify') else "<!--" + x + "-->\n" for x in cons1]
    pretty2 = [x.prettify() if hasattr(x, 'prettify') else "<!--" + x + "-->\n" for x in cons2]

    regex = ""
    combined = []

    potential_pairs = []
    already_used1 = []
    already_used2 = []

    for (idx1, c1) in enumerate(cons1):
        if c1 in cons2:
            if idx1 not in already_used1 and cons2.index(c1) not in already_used2:
                potential_pairs.append({ (idx1, cons2.index(c1)): 100 })
                already_used1.append(idx1)
                already_used2.append(cons2.index(c1))
        else:
            max_match = math.inf
            id1 = idx1
            id2 = 0
            for (idx2, c2) in enumerate(cons2):
                temp = string_distance(c1, c2)
                if temp < max_match:
                    id2 = idx2
                    max_match = temp

            if id1 not in already_used1 and id2 not in already_used2:
                potential_pairs.append({ (id1, id2): max_match })
                already_used1.append(id1)
                already_used2.append(id2)

    for (idx2, c2) in enumerate(cons2):
        if c2 in cons1:
            if cons1.index(c2) not in already_used1 and idx2 not in already_used2:
                potential_pairs.append({ (cons1.index(c2), idx2): 100 })
                already_used1.append(cons1.index(c2))
                already_used2.append(idx2)
        else:
            max_match = math.inf
            id2 = idx2
            id1 = 0
            for (idx1, c1) in enumerate(cons1):
                temp = string_distance(c2, c1)
                if temp < max_match:
                    id1 = idx1
                    max_match = temp

            if id1 not in already_used1 and id2 not in already_used2:
                potential_pairs.append({ (id1, id2): max_match })
                already_used1.append(id1)
                already_used2.append(id2)


    print("POTENTIAL PAIRS")
    print(potential_pairs)
    print(already_used1)
    print(already_used2)
    print("------------------")


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





def process_file(all_contents):
    print("roadrunner, num of contents", len(all_contents))

    content1 = all_contents[0]
    content2 = all_contents[1]

    # create trees from contents
    parsed1 = BeautifulSoup(content1, 'html.parser')
    parsed2 = BeautifulSoup(content2, 'html.parser')

    print("prettify")
    print(parsed1.body.prettify())
    print("------------")

    for tag in parsed1.recursiveChildGenerator():
        if hasattr(tag, 'attrs'):
            tag.attrs = None

    for tag in parsed2.recursiveChildGenerator():
        if hasattr(tag, 'attrs'):
            tag.attrs = None

    prepared1 = parsed1.body.contents
    prepared2 = parsed2.body.contents

    # print(parsed1.body)
    # print("----------------")
    # print(parsed2.body)
    # print("----------------")


    compare_contents(prepared1, prepared2)


'''
pojdi za vsak el cez contents in primerjaj med sabo

'''