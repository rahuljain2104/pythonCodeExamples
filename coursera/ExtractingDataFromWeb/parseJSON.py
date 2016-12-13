import json

'''

#
# '''
# data = '''{
#         "person" : {
#              "name" : {
#                 "firstname":"rahul",
#                 "lastname":"jain"
#             },
#             "email":"rahuljain2104@gmail.com"
#         }
#         }'''


import urllib

sample_data = "http://python-data.dr-chuck.net/comments_42.json"  # (Sum=2553)
actual_data = "http://python-data.dr-chuck.net/comments_340272.json"  # (Sum ends with 36)
# "http://python-data.dr-chuck.net/known_by_Fikret.html"

data = urllib.urlopen(actual_data).read()

info = json.loads(data)

s = 0
comments = info['comments']

for i in range(len(comments)):
    s += int(info['comments'][i]['count'])

print s
