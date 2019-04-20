from lxml import html


def process_file(content):
    print("XPATH")
    tree = html.fromstring(content)
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

