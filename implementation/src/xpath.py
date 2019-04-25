from lxml import html

pages = {
    'rtvslo.si': {
        'Title': '//*[@id="main-container"]//h1/text()',
        'SubTitle': '//*[@id="main-container"]//*[@class="subtitle"]/text()',
        'Lead': '//*[@id="main-container"]//*[@class="lead"]/text()',
        'Content': '//*[@id="main-container"]//*[@class="article-body"]/text()',
        'Author': '//*[@id="main-container"]//*[@class="author-name"]/text()',
        'PublishedTime': '//*[@id="main-container"]//*[@class="publish-meta"]/text()'
    }
}


def get_to_xpath(tree, v):
    result = tree.xpath(v)
    if result is not None:
        return str(result[0])
    else:
        return 'Ni rezultata'


def process_file(content, page):
    print("XPATH")
    tree = html.fromstring(content)
    result = {}
    for k, v in pages[page].items():
        xpath = get_to_xpath(tree, v)
        print(k + ' is at: ' + v + ' with value: ' + xpath)
        result[k] = xpath

    """
    title = str(tree.xpath('//*[@id="main-container"]//h1/text()')[0])
    subtitle = str(tree.xpath('//*[@id="main-container"]//*[@class="subtitle"]/text()')[0])
    lead = str(tree.xpath('//*[@id="main-container"]//*[@class="lead"]/text()')[0])
    author_name = str(tree.xpath('//*[@id="main-container"]//*[@class="author-name"]/text()')[0])
    publish_meta = str(tree.xpath('//*[@id="main-container"]//*[@class="publish-meta"]/text()')[0])
    article_body = str(tree.xpath('//*[@id="main-container"]//*[@class="article-body"]/text()')[0])
    print("Found title: ", title)
    print("Found subtitle: ", subtitle)
    print("Found lead: ", lead)
    print("Found author name: ", author_name)
    print("Found publish meta: ", publish_meta)
    print("Found article body: ", article_body)
    """

    return result
