import httplib2
from bs4 import BeautifulSoup, SoupStrainer

http = httplib2.Http()
status, response = http.request('https://lanceleonard.com')

print( "Status details:\n" )

import pprint
pp = pprint.PrettyPrinter(indent=3)
pp.pprint(status)

print( "\nLinks on page:\n" )

for link in BeautifulSoup(response, parse_only=SoupStrainer('a'), features="html.parser"):
    if link.has_attr('href'):
        print(link['href'])

# print( "Response: ", response, "\n" )


# print("Response headers:\n")
# 
# for header in response.headers:
#     
#     print( header, "/n" )
#
# print("HREFs:\n")
# 
# for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
#     if link.has_attr('href'):
#         print(link['href'])
