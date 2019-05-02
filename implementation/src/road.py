from bs4 import BeautifulSoup


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


def compare_nodes(node1, node2, generic_tree):

    print("node1", node1.name, node1.attrs)
    print("node2", node2.name, node2.attrs)

    children1 = get_next_level(node1)
    children2 = get_next_level(node2)

    print("len ch1", len(list(children1)))
    print("len ch2", len(list(children2)))

    generic_tree.append(generic_tree.new_tag(node1.name, node1.attrs))

    print("new", generic_tree)

    pass


def process_file(all_contents):
    print("roadrunner, num of contents", len(all_contents))

    content1 = all_contents[0]
    content2 = all_contents[1]

    # create trees from contents
    parsed1 = BeautifulSoup(content1, 'html.parser')
    parsed2 = BeautifulSoup(content2, 'html.parser')

    generic_tree = BeautifulSoup(features="lxml")

    # print("p1 body", parsed1.body)
    # tree_walker(parsed1.body)
    compare_nodes(parsed1.body, parsed2.body, generic_tree)

    # TODO:
    # - compare trees
    # - ...

    pass