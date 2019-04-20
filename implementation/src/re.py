import re


def process_file(content):
    print("RE")
    # TODO refactor
    regex = "<h1[^>]*>(.*)<\/h1[^>]*>"
    pattern = re.compile(regex)
    match = pattern.search(content)
    print("Found title: '{}'.".format(match.group(1)))
    
    regex = "<div[^>]*class=\"[^\"]*subtitle[^\"]*\"[^>]*>(.*)<\/div[^>]*>"
    pattern = re.compile(regex)
    match = pattern.search(content)
    print("Found subtitle: '{}'.".format(match.group(1)))
    
    regex = "<[^>]*class=\"[^\"]*lead[^\"]*\"[^>]*>(.*)<\/[^>]*>"
    pattern = re.compile(regex)
    match = pattern.search(content)
    print("Found lead: '{}'.".format(match.group(1)))