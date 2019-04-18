from lxml import html


def process_file(content):
    tree = html.fromstring(content)
    title = str(tree.xpath('//h1/text()')[0])
    print("Found title: '%s'." % title)

