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

    }
}


def execute_regex(content, regex):
    pattern = re.compile(regex)
    match = pattern.search(content)
    if match != None:
        return match.group(1)
    return "Ni rezultata"


def process_file(content, page):
    print("RE")

    result = {}
    for k, v in pages[page].items():
        regular = execute_regex(content, v)
        print(k + ' is at: ' + v + ' with value: ' + regular)
        result[k] = regular

    """
        
    result = execute_regex(content, "<h1[^>]*>(.*)<\/h1[^>]*>")
    print("Found title: '{}'.".format(result))
    
    result = execute_regex(content, "<div[^>]*class=\"[^\"]*subtitle[^\"]*\"[^>]*>(.*)<\/div[^>]*>")
    print("Found subtitle: '{}'.".format(result))
    
    result = execute_regex(content, "<[^>]*class=\"[^\"]*lead[^\"]*\"[^>]*>(.*)<\/[^>]*>")
    print("Found lead: '{}'.".format(result))
    
    result = execute_regex(content, "<[^>]*class=\"[^\"]*author-name[^\"]*\"[^>]*>(.*)<\/[^>]*>")
    print("Found author name: '{}'.".format(result))
    
    result = execute_regex(content, "<[^>]*class=\"[^\"]*publish-meta[^\"]*\"[^>]*>(.*)<\/[^>]*>")
    print("Found publish meta: '{}'.".format(result))
    
    result = execute_regex(content, "<[^>]*class=\"[^\"]*article-body[^\"]*\"[^>]*>(.*)<\/[^>]*>")
    print("Found article body: '{}'.".format(result))
    """

    return result
