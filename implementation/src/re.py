import re

pages = {
    'rtvslo.si': {
        'Title': r"<h1[^>]*>(.*)<\/h1[^>]*>",
        'SubTitle': r"<div[^>]*class=\"[^\"]*subtitle[^\"]*\"[^>]*>(.*)<\/div[^>]*>",
        'Lead': r"<[^>]*class=\"[^\"]*lead[^\"]*\"[^>]*>(.*)<\/[^>]*>",
        'Content': r"<[^>]*class=\"[^\"]*article-body[^\"]*\"[^>]*>(.*)<\/[^>]*>",
        'Author': r"<[^>]*class=\"[^\"]*author-name[^\"]*\"[^>]*>(.*)<\/[^>]*>",
        'PublishedTime': r"<[^>]*class=\"[^\"]*publish-meta[^\"]*\"[^>]*>(.*)<\/[^>]*>"
    },

    'overstock.com': {
        'Title': '',
        'Content': '',
        'ListPrice': '',
        'Price': '',
        'Saving': ''
    }
}


def execute_regex(content, regex):
    pattern = re.compile(regex)
    match = pattern.search(content)
    if match is not None:
        return match.group(1)
    return "Ni rezultata"


def get_results(content, page):
    result = {}
    for k, v in pages[page].items():
        regular = execute_regex(content, v)
        print(k + ' is at: ' + v + ' with value: ' + regular)
        if k == 'Saving':
            exploded = regular.split(" ")
            result[k] = exploded[0]
            result['SavingPercent'] = exploded[1]
        else:
            result[k] = regular

    return result


def process_file(content, page):
    print("RE")

    if page == 'overstock.com':
        result = []
        pattern = re.compile(r'<table[^>]*bgcolor=\"[^\"]*\"[^>]*>(.*)<\/table[^>]*>', re.MULTILINE)
        items = pattern.search(content)
        print (items)
        for item in items:
            result.append(get_results(item, page))
    else:
        result = get_results(content, page)

    return result
