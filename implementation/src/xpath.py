from lxml import html

pages = {
    'rtvslo.si': {
        'Title': '//*[@id="main-container"]//h1/text()',
        'SubTitle': '//*[@id="main-container"]//*[@class="subtitle"]/text()',
        'Lead': '//*[@id="main-container"]//*[@class="lead"]/text()',
        'Content': '//*[@id="main-container"]//*[@class="article-body"]/text()',
        'Author': '//*[@id="main-container"]//*[@class="author-name"]/text()',
        'PublishedTime': '//*[@id="main-container"]//*[@class="publish-meta"]/text()'
    },
    'overstock.com': {
        'Title': './td[2]/a/b/text()',
        'Content': './td[2]/table//span[@class="normal"]/text()',
        'ListPrice': './td[2]/table//s/text()',
        'Price': './td[2]/table//span[@class="bigred"]/b/text()',
        'Saving': './td[2]/table//span[@class="littleorange"]/text()'
    }
}


def get_to_xpath(tree, v):
    result = tree.xpath(v)
    if result:
        return str(result[0])
    else:
        return 'Ni rezultata'


def get_results(tree, page):
    result = {}
    for k, v in pages[page].items():
        xpath = get_to_xpath(tree, v)
        print(k + ' is at: ' + v + ' with value: ' + xpath)
        if k == 'Saving':
            exploded = xpath.split(" ")
            result[k] = exploded[0]
            result['SavingPercent'] = exploded[1]
        else:
            result[k] = xpath

    return result


def process_file(content, page):
    print("XPATH")
    tree = html.fromstring(content)
    if page == 'overstock.com':
        result = []
        items = tree.xpath('//table[@cellpadding="2"]/tbody/tr[@bgcolor]')
        for item in items:
            result.append(get_results(item, page))
    else:
        result = get_results(tree, page)

    return result
