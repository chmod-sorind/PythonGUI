import requests
from urllib.request import urlopen


uRl = "http://build02.broadsign.net/broadsign/suite/branches/release/11.1/bugfix/"

response = requests.get(uRl)
txt = response.text
print(txt)

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

html = urlopen(uRl)
print(html.read())

