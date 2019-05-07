from bs4 import BeautifulSoup
import numpy as np


def tree_walker(node):
    print("node name: " + str(node.name) + "| node type: " + str(type(node)))
    if node.name is not None:
        for child in node.children:
            # process node
            print(str(child.name) + ": " + str(type(child)))
            tree_walker(child)


def get_next_level(node):
    if node.name is not None:
        return node.children
    return None


def all_same(items):
    print(list(i for i in items))
    items = list(items)

    return all(x.name == items[0].name for x in items)


def compare_nodes(node1, node2, generic_tree):

    print("node1", node1.name, node1.attrs)
    print("node2", node2.name, node2.attrs)

    children1 = get_next_level(node1)
    num_of_c1 = len(list(children1))
    are_c1_a_list = all_same(children1)

    children2 = get_next_level(node2)
    num_of_c2 = len(list(children2))
    are_c2_a_list = all_same(children2)

    if num_of_c1 == num_of_c2:
        print("both have same amount of children")

    print("lst", are_c1_a_list, are_c2_a_list)
    if are_c1_a_list and are_c2_a_list:
        print("both are a list")

    generic_tree.append(generic_tree.new_tag(node1.name, node1.attrs))
    print("new", generic_tree)

    pass


def simple_tree_matching(tree1, tree2):

    if tree1.name is None or tree2.name is None:
        # print("isn't a valid DOM node")
        return 0

    if tree1.name != tree2.name:
        print("not same NAME:", tree1.name, tree1.attrs, "VS", tree2.name, tree2.attrs)
        return 0

    if tree1.attrs != tree2.attrs and tree1.name != "body" and tree2.name != "body":
        print("not same ATTRS:", tree1.name, tree1.attrs, "VS", tree2.name, tree2.attrs)
        return 0

    children1 = list(tree1.children)
    children2 = list(tree2.children)

    m = len(children1)
    n = len(children2)

    print("SAME", tree1.name, tree1.attrs, m, "VS", tree2.name, tree2.attrs, n)

    if m == 0:  # tree1 is a leaf
        print("m=0:\n", tree1, "\n", tree2)
    if n == 0:  # tree2 is a leaf
        print("n=0:\n", tree1, "\n", tree2)

    if m == 0 and n == 0:
        return 0

    big_m = np.empty([m, n])

    big_m[:, 0] = 0  # for i=0 to m do: M[i][0] = 0
    big_m[0, :] = 0  # for j=0 to n do: M[0][j] = 0

    for i in range(1, m):
        for j in range(1, n):
            w_ij = simple_tree_matching(children1[i-1], children2[j-1])
            big_m[i, j] = max(big_m[i, j-1], big_m[i-1, j], big_m[i-1, j-1] + w_ij)

    return big_m[m-1, n-1] + 1


def get_common(tree1, tree2):



    if tree1.name == tree1.name:
        if tree1.attrs == tree2.attrs:
            pass

        else:
            common_attrs = []

            for a in tree1.attrs:
                if a in tree2.attrs:
                    req_vals = []
                    opt_vals = []

                    for av in tree1[a]:
                        if av in tree2[a]:
                            req_vals.append(av)

                    for v in req_vals:
                        tree1[a].remove(v)
                        tree2[a].remove(v)

                    opt_vals += tree1[a]
                    opt_vals += tree2[a]

                    common_attrs.append({a: {"status": "required", "required_vals": req_vals, "optional_vals": opt_vals}})

            for a in tree1.attrs:
                if a not in tree2.attrs:
                    common_attrs.append({a: {"status": "optional", "required_vals": tree1[a]}})

            for a in tree2.attrs:
                if a not in tree1.attrs:
                    common_attrs.append({a: {"status": "required", "required_vals": tree2[a]}})

            print("common", common_attrs)

            # process children

            children = []

            for c1 in tree1.children:
                print("t1")
                for c2 in tree2.children:
                    print("t2")
                    if c1.name == c2.name:
                        print("same name", c1.name, c1 == c2)
                        if c1.name is None or c2.name is None:
                            pass
                        else:
                            if c1.attrs == c2.attrs:
                                print("same name and attrs", c1.name, c1.attrs)
                            else:
                                print("attrs", c1.attrs, "VS", c2.attrs)

                        break





                # print("c", c)


            return {tree1.name: {"attributes": common_attrs, "children": children}}


    pass


    wrapper_gen = []

def process_file(all_contents):
    print("roadrunner, num of contents", len(all_contents))

    content1 = all_contents[0]
    content2 = all_contents[1]

    # create trees from contents
    parsed1 = BeautifulSoup(content1, 'html.parser')
    parsed2 = BeautifulSoup(content2, 'html.parser')

    # SimpleTreeMatching
    # for script in parsed1.find_all("script"):
    #     script.decompose()
    # for script in parsed2.find_all("script"):
    #     script.decompose()
    #
    # for noscript in parsed1.find_all("noscript"):
    #     noscript.decompose()
    # for noscript in parsed2.find_all("noscript"):
    #     noscript.decompose()
    #
    # for link in parsed1.find_all("link"):
    #     link.decompose()
    # for link in parsed2.find_all("link"):
    #     link.decompose()
    #
    # for style in parsed1.find_all("style"):
    #     style.decompose()
    # for style in parsed2.find_all("style"):
    #     style.decompose()
    #
    # stm_res = simple_tree_matching(parsed1.body, parsed2.body)


    # generic_tree = BeautifulSoup(features="lxml")

    # print("p1 body", parsed1.body)
    # tree_walker(parsed1.body)
    # compare_nodes(parsed1.body, parsed2.body, generic_tree)


    cc = get_common(parsed1.body, parsed2.body)

    print("cc", cc)


    # TODO:
    # - compare trees
    # - ...

    pass


'''
se ena ideja
gres po enem beautifulsoup drevesu in za vsak element na x nivoju iščeš enak element v drugem drevesu
'''