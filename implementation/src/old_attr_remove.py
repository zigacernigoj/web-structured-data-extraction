# for a in parsed1.find_all("a"):
#     for attr in a.attrs:
#         a[attr] = ".*"
#
# for a in parsed2.find_all("a"):
#     for attr in a.attrs:
#         a[attr] = ".*"
#
# for a in parsed1.find_all("iframe"):
#     for attr in a.attrs:
#         a[attr] = ".*"
#
# for a in parsed2.find_all("iframe"):
#     for attr in a.attrs:
#         a[attr] = ".*"
#
# for a in parsed1.find_all("img"):
#     for attr in a.attrs:
#         a[attr] = ".*"
#
# for a in parsed2.find_all("img"):
#     for attr in a.attrs:
#         a[attr] = ".*"
#
# for a in parsed1.find_all("div"):
#     for attr in a.attrs:
#         a[attr] = ".*"
#
# for a in parsed2.find_all("div"):
#     for attr in a.attrs:
#         a[attr] = ".*"
#
# for a in parsed1.find_all("", onclick=True):
#     a["onclick"] = ".*"
#
# for a in parsed2.find_all("", onclick=True):
#     a["onclick"] = ".*"
#
# for a in parsed1.find_all("", {"class" : "active"}):
#     a.attrs["class"].remove("active")
#
# for a in parsed2.find_all("", {"class" : "active"}):
#     a.attrs["class"].remove("active")
#
# for a in parsed1.find_all("script"):
#     a.string="(.*\\n)*"
#     a.unwrap()
#
# for a in parsed2.find_all("script"):
#     a.string = "(.*\\n)*"
#     a.unwrap()
#
# for a in parsed1.find_all("style"):
#     a.string = "(.*\\n)*"
#     a.unwrap()
#
# for a in parsed2.find_all("style"):
#     a.string = "(.*\\n)*"
#     a.unwrap()
