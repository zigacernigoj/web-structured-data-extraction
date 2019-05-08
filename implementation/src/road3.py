from bs4 import BeautifulSoup
import numpy as np

def compare_by_line(cons1, cons2):

    cons1 = [x.strip() for x in cons1]
    cons2 = [x.strip() for x in cons2]

    max1 = len(cons1)
    i1 = 0

    max2 = len(cons2)
    i2 = 0

    regex_string = ""

    saved_repeaters = []
    saved_optionals = []

    while i1 < max1-1 or i2 < max2-1:
        # print(cons1[i1], cons2[i2])

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

        else:

            # string mismatch
            if type1 == "string" and type2 == "string":
                print("both strings:", repr(cons1[i1]), "|", repr(cons2[i2]))
                if cons1[i1]:
                    cons1[i1] = "#PCDATA"
                if cons2[i2]:
                    cons2[i2] = "#PCDATA"

            # tag mismatch
            if type1 == "tag" and type2 == "tag":

                # first check for iterations of same element
                last_tag1 = None
                last_tag2 = None

                for i in reversed(range(i1)):
                    print("rs1", i, cons1[i])
                    if cons1[i].startswith("</"):
                        last_tag1 = cons1[i]
                        break

                for i in reversed(range(i2)):
                    print("rs2", i, cons2[i])
                    if cons2[i].startswith("</"):
                        last_tag2 = cons2[i]
                        break

                last_tag = None
                if last_tag1 == last_tag2:
                    last_tag = last_tag1
                else:
                    print("too bad")
                    print(cons1[i1], last_tag1)
                    print(cons2[i2], last_tag2)
                    print("end too bad")

                # je ponavljanje
                if last_tag:

                    if cons1[i1].startswith("</"):
                        # more data in the cons2
                        print("more data in the cons2")

                    elif cons2[i2].startswith("</"):
                        # more data in the cons1
                        print("more data in the cons1")

                    found_tag_on_line1 = None
                    for additional1 in range(i1, len(cons1)):
                        print("add1", cons1[additional1])
                        if cons1[additional1] == last_tag:
                            found_tag_on_line1 = additional1
                            break

                    found_tag_on_line2 = None
                    for additional2 in range(i2, len(cons2)):
                        print("add2", cons2[additional2])
                        if cons2[additional2] == last_tag:
                            found_tag_on_line2 = additional2
                            break

                    print("lines", found_tag_on_line1, found_tag_on_line2)

                    # ZA 1
                    if found_tag_on_line1 and not found_tag_on_line2:
                        id1_prev_back = i1-1
                        print("i1", id1_prev_back, cons1[id1_prev_back])

                        id1_next_back = found_tag_on_line1
                        print("idn1", id1_next_back)

                        # go back to check
                        is_whole = True
                        for bi in reversed(range(i1, id1_next_back+1)):
                            print("go back", cons1[bi], cons1[id1_prev_back])
                            if cons1[id1_prev_back] == "#PCDATA":
                                cons1[bi] = "#PCDATA"
                            elif cons1[bi] != cons1[id1_prev_back]:
                                print("faila", cons1[bi], "|", cons1[id1_prev_back])
                                is_whole = False
                            id1_prev_back -= 1

                        print("is_whole 1", is_whole, cons1[i1:id1_next_back+1])
                        if is_whole:
                            rep_unit = cons1[i1:id1_next_back+1]
                            saved_repeaters.append(rep_unit)
                            i1 = id1_next_back+1


                    # ZA 2
                    if not found_tag_on_line1 and found_tag_on_line2:
                        id2_prev_back = i2-1
                        print("i2", id2_prev_back, cons2[id2_prev_back])

                        id2_next_back = found_tag_on_line2
                        print("idn2", id2_next_back)

                        # go back to check
                        is_whole = True
                        for bi in reversed(range(i2, id2_next_back+1)):
                            print("go back", cons2[bi], cons2[id2_prev_back])
                            if cons2[id2_prev_back] == "#PCDATA":
                                cons2[bi] = "#PCDATA"
                            elif cons2[bi] != cons2[id2_prev_back]:
                                print("faila", cons2[bi], "|", cons2[id2_prev_back])
                                is_whole = False
                            id2_prev_back -= 1

                        print("is_whole 2", is_whole, cons2[i2:id2_next_back+1])

                        if is_whole:
                            rep_unit = cons2[i2:id2_next_back+1]
                            saved_repeaters.append(rep_unit)
                            i2 = id2_next_back+1

                    print("last tag", last_tag, "diff", cons1[i1], cons2[i2])
                    print(cons1)
                    print(cons2)

                # ni ponavljanje
                else:
                    print("optional", cons1[i1], cons2[i2])

                    # najprej za 1
                    found_tag_on_line1 = None
                    for additional1 in range(i1, len(cons1)):
                        print("opt1", cons1[additional1])
                        if cons1[additional1] == cons2[i2]:
                            found_tag_on_line1 = additional1
                            break

                    # nato se za 2
                    found_tag_on_line2 = None
                    for additional2 in range(i2, len(cons2)):
                        print("opt2", cons2[additional2])
                        if cons2[additional2] == cons1[i1]:
                            found_tag_on_line2 = additional2
                            break

                    print("opt on line")
                    print(found_tag_on_line1) #, cons1[i1], cons1[found_tag_on_line1])
                    print(found_tag_on_line2) #, cons2[i2], cons2[found_tag_on_line2])
                    print("end of opt")

                    if found_tag_on_line1 and found_tag_on_line2 and found_tag_on_line1 is not None and found_tag_on_line2 is not None:
                        if cons1[i1].startswith("</"):
                            print("opt v 2 ...", cons2[i2:found_tag_on_line2+1])
                            must_add_opt = cons2[i2:found_tag_on_line2+1]
                            saved_optionals.append(must_add_opt)
                            o = 0
                            for x in range(i1, i1+len(must_add_opt)):
                                cons1.insert(x, must_add_opt[o])
                                o += 1
                            i1 = found_tag_on_line1+1
                            i2 = found_tag_on_line2+1

                        if cons2[i2].startswith("</"):
                            print("opt v 1 ...", cons1[i1:found_tag_on_line1+1])
                            saved_optionals.append(cons1[i1:found_tag_on_line1+1])
                            i1 = found_tag_on_line2+1


                    # ZA 1 - dodatni ele v 1
                    if found_tag_on_line1 and not found_tag_on_line2:
                        print("opt v 1", cons1[i1:found_tag_on_line1])
                        saved_optionals.append(cons1[i1:found_tag_on_line1])
                        i1 = found_tag_on_line1+1


                    # ZA 2 - dodatni ele v 2
                    if not found_tag_on_line1 and found_tag_on_line2:
                        print("opt v 2", cons2[i2:found_tag_on_line2])
                        must_add_opt = cons2[i2:found_tag_on_line2 + 1]
                        saved_optionals.append(must_add_opt)
                        o = 0
                        for x in range(i1, i1 + len(must_add_opt)):
                            cons1.insert(x, must_add_opt[o])
                            o += 1
                        i2 = found_tag_on_line2+1


        if i1 < max1-1:
            i1 += 1
        if i2 < max2-1:
            i2 += 1

    print("i1", i1, max1)
    print("i2", i2, max2)

    regex_string = "".join(cons1)

    for sr in saved_repeaters:
        if sr:
            sr_string = "".join(sr)
            first_oc = regex_string.find(sr_string)
            regex_string = regex_string.replace(sr_string, "")
            regex_string = regex_string[:first_oc] + "(" + sr_string + ")+" + regex_string[first_oc:]

    for so in saved_optionals:
        if so:
            so_string = "".join(so)
            first_oc = regex_string.find(so_string)
            regex_string = regex_string.replace(so_string, "")
            regex_string = regex_string[:first_oc] + "(" + so_string + ")?" + regex_string[first_oc:]


    print("saved rep", saved_repeaters)
    print("saved opt", saved_optionals)
    print("reg", regex_string)





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