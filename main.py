# import urllib.request
# opener = urllib.request.build_opener()
# response = opener.open ("https://httpbin.org/get")
# print(response.read())

# import urllib.request
# import requests
# opener = urllib.request.build_opener()
# response = opener.open("https://httpbin.org/get")
# print(response.read())
# response = requests.get("https://httpbin.org/get")
# print(response.content)

# import requests
# response = requests.get("https://httpbin.org/get")
# print (response.content)
# print(f"Datatype - {type(response.content)}")

# import requests
# response = requests.get("https://httpbin.org/get")
# print(response.text)
# print(f"Datatype - {type(response.text)}")

# import requests
# response = requests.post("https://httpbin.org/post", data="Test data", headers={"h1": "Test title"})
# print(response. text)

# import requests
# response = requests.post("https://httpbin.org/post", data={"Test data":"ny_form"})
# print(response.text)

# import requests
# response = requests.get("https://coinmarketcap.com/")
# print(response.text)

# import requests
# response = requests.get("https://coinmarketcap.com/")
# response_text = response.text
# response_parse = response_text.split("<span>")
# for parse_elem_1 in response_parse:
#     if parse_elem_1.startswith("$"):
#         print(parse_elem_1)

# import requests
# response = requests.get("https://coinmarketcap.com/")
# response_text = response.text
# response_parse = response_text.split("<span>")
# for parse_elem_1 in response_parse:
#     if parse_elem_1.startswith("$"):
#         for parse_elem_2 in parse_elem_1.split("</span>"):
#             if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
#                 print(parse_elem_2)

# import requests
# res_parse_list = []
# response = requests.get("https://coinmarketcap.com/")
# response_text = response.text
# response_parse = response_text.split("<span>")
# for parse_elem_1 in response_parse:
#     if parse_elem_1.startswith("$"):
#         for parse_elem_2 in parse_elem_1.split("</span>"):
#             if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
#                 res_parse_list.append(parse_elem_2)
# bitcoin_exchange_rate = res_parse_list[8]
# print(bitcoin_exchange_rate)

# from bs4 import BeautifulSoup
# import requests
# response = requests.get("https://coinmarketcap.com/")
# if response.status_code == 200:
#     soup = BeautifulSoup (response.text, features="html.parser")
#     soup_list = soup.find_all("a", {"href":"/currencies/bitcoin/markets/"})
#     for elem in soup_list:
#         print(elem)