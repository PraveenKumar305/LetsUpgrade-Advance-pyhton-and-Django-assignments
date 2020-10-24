import requests, re
url = "https://study-ccna.com/classes-of-ip-addresses/"

r = requests.get(url)

data = r.text
ip = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

list1_ip = re.findall(ip, data)
list1_ip = list(set(list1_ip))
for each in list1_ip:
	print(each)
	
