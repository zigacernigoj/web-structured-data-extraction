import re


def process_file(content):
    regex = "(\w+)"
    pattern = re.compile(regex)
    match = pattern.search(content)
    print("Found person: '{}'.".format(match.group(1)))