from lxml import html


def process_file(content):
    print("XPATH")
    tree = html.fromstring(content)
    title = str(tree.xpath('//*[@id="main-container"]//h1/text()')[0])
    subtitle = str(tree.xpath('//*[@id="main-container"]//*[@class="subtitle"]/text()')[0])
    lead = str(tree.xpath('//*[@id="main-container"]//*[@class="lead"]/text()')[0])
    print("Found title: ", title)
    print("Found subtitle: ", subtitle)
    print("Found lead: ", lead)

