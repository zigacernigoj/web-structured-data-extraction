from lxml import html

pages = {
    'rtvslo.si': {
        'Title': '//*[@id="main-container"]//h1/text()',
        'SubTitle': '//*[@id="main-container"]//*[@class="subtitle"]/text()',
        'Lead': '//*[@id="main-container"]//*[@class="lead"]/text()',
        'Content': '//*[@id="main-container"]//*[@class="article-body"]//descendant::*/text()',
        'Author': '//*[@id="main-container"]//*[@class="author-name"]/text()',
        'PublishedTime': '//*[@id="main-container"]//*[@class="publish-meta"]/text()'
    },
    'overstock.com': {
        'Title': '//table[@cellpadding="2"]/tbody/tr[@bgcolor]/td[2]/a/b/text()',
        'Content': '//table[@cellpadding="2"]/tbody/tr[@bgcolor]/td[2]/table//span[@class="normal"]/text()',
        'ListPrice': '//table[@cellpadding="2"]/tbody/tr[@bgcolor]/td[2]/table//s/text()',
        'Price': '//table[@cellpadding="2"]/tbody/tr[@bgcolor]/td[2]/table//span[@class="bigred"]/b/text()',
        'Saving': '//table[@cellpadding="2"]/tbody/tr[@bgcolor]/td[2]/table//span[@class="littleorange"]/text()'
    },
    'bolha.com': {
        'Title': '//*[@id="adDetail"]/div[2]/h1/text()',
        'Price': '//*[@id="adDetail"]//div[@class="price"]/span/text()',
        'DaysUntilExpires': '//*[@id="adDetail"]/div[3]/div[1]/p[5]/text()',
        'User': '//*[@id="sellerInfo"]/div/p[1]/strong/text()',
        'Address': '//*[@id="sellerInfo"]/div/p[2]/strong/text()',
        'Phone': '//*[@id="sellerInfo"]/div/p[3]/strong/text()',
        'Mobile': '//*[@id="sellerInfo"]/div/p[4]/strong/text()',
        'Content': '//*[@id="adDetail"]//div[@class="content"]/descendant::*/text()',
        'MainImage': '//*[@id="gallery"]/table/tbody/tr/td/a/img/@src',
        'Images': '//*[@id="gal"]//td[@class="thumb"]/a/img/@src',
    }
}

no_result = 'Ni rezultata'


def get_to_xpath(tree, v, index, arr):
    result = tree.xpath(v)
    if arr:
        return result
    elif result and len(result) > index:
        return str(result[index])
    else:
        return no_result


def get_results(tree, page, index):
    result = {}
    i = 0
    for k, v in pages[page].items():
        i += 1
        arr = False
        if k == 'Images' or k == 'Content':
            arr = True
        xpath = get_to_xpath(tree, v, index, arr)
        if k == 'Content':
            xpath = ' '.join(xpath)
        if i == 1 and xpath == no_result:
            return None
        print(k + ' is at: ' + v + ' with value: ' + str(xpath))
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
        for n in range(50):
            parsed = get_results(tree, page, n)
            if parsed is None:
                break
            else:
                result.append(parsed)
    else:
        result = get_results(tree, page, 0)

    print(result)
    return result


def process_file_old(content, page):
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
