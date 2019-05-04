import json
import re

pages = {
    'rtvslo.si': {
        'Title': r"<h1[^>]*>(.*)<\/h1[^>]*>",
        'SubTitle': r'<div class="subtitle">(.*?)</div>',
        # 'SubTitle': r"<div[^>]*class=\"[^\"]*subtitle[^\"]*\"[^>]*>(.*)<\/div[^>]*>",
        'Lead': r'<p class="lead">(.*?)</p>',
        # 'Lead': r"<[^>]*class=\"[^\"]*lead[^\"]*\"[^>]*>(.*)<\/[^>]*>",
        'Content': r'<div class="article-body">(.*?)</div>',
        # 'Content': r"<[^>]*class=\"[^\"]*article-body[^\"]*\"[^>]*>(.*)<\/[^>]*>",
        'Author': r'<div class="author-name">(.*?)</div>',
        # 'Author': r"<[^>]*class=\"[^\"]*author-name[^\"]*\"[^>]*>(.*)<\/[^>]*>",
        'PublishedTime': r'<div class="publish-meta">(.*?)<br>',
        # 'PublishedTime': r"<[^>]*class=\"[^\"]*publish-meta[^\"]*\"[^>]*>(.*)<\/[^>]*>"
    },

    'overstock.com': {
        'Title': r'</table></td><td valign="top"> \n<a href="[^\"]*"><b>(.*?)</b>',
        'Content': '<span class="normal">([^<]*)<',
        'ListPrice': '<s>([^<]*)</s>',
        'Price': '<span class="bigred"><b>([^<]*)</b></span>',
        'Saving': r'<span class="littleorange">([^\s]*)\s[^<]*</span>',
        'SavingPercent': r'<span class="littleorange">[^\(]*\(([^<]*)\)</span>'
    },
    'bolha.com': {
        'Title': r"<h1[^>]*>(.*)<\/h1[^>]*>",
        'Price': '<div class="price">Cena: <span>([^<]*)</span></div>',
        'DaysUntilExpires': r'<p class="validTo">Oglas poteče čez ([^\s]*) dni </p>',
        'User': '<p><label>Uporabnik:</label><strong>([^<]*)</strong></p>',
        'Address': '<p><label>Naslov:</label><strong>([^<]*)<',
        'Phone': '<p><label>Telefon:</label><strong>([^<]*)<',
        'Mobile': '<p><label>Mobilna številka:</label><strong>([^<]*)<',
        'Content': '<div class="content">(.+?(?=</div))</div>',
        'MainImage': '<td class="imgHolder">.*<img src="([^"]*)"',
        'Images': '<td class="thumb">.+?(?=<img)<img src="([^"]*)"'
    }
}

no_result = 'Ni rezultata'


def execute_regex(content, regex, index, arr):
    result = re.findall(regex, content, re.DOTALL)
    # print(result)
    if arr:
        return result
    elif result and len(result) > index:
        return str(result[index])
    else:
        return no_result
    # print(matches)
    # pattern = re.compile(regex)
    # match = pattern.search(content)
    # print (match)
    # if match is not None:
    #     return match.group(1)
    # return "Ni rezultata"


def get_results(content, page, index):
    result = {}
    i = 0
    for k, v in pages[page].items():
        i += 1
        arr = False
        if k == 'Images':
            arr = True
        regular = execute_regex(content, v, index, arr)
        if i == 1 and regular == no_result:
            return None
        # print(k + ' is at: ' + v + ' with value: ' + str(regular))
        result[k] = regular
        # if k == 'Saving':
        #     exploded = regular.split(" ")
        #     result[k] = exploded[0]
        #     result['SavingPercent'] = exploded[1]
        # else:
        #     result[k] = regular

    return result


def process_file(content, page):
    # print("RE")

    if page == 'overstock.com':
        result = []
        for n in range(50):
            parsed = get_results(content, page, n)
            if parsed is None:
                break
            else:
                result.append(parsed)
    else:
        result = get_results(content, page, 0)

    # convert into JSON:
    y = json.dumps(result, ensure_ascii=False)

    # the result is a JSON string:
    print(y)
    return result


def process_file_old(content, page):
    print("RE")

    if page == 'overstock.com':
        result = []
        pattern = re.compile(r'<table[^>]*bgcolor=\"[^\"]*\"[^>]*>(.*)<\/table[^>]*>', re.MULTILINE)
        items = pattern.search(content)
        # print(items)
        for item in items:
            result.append(get_results(item, page))
    else:
        result = get_results(content, page)

    return result
