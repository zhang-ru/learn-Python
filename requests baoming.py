import requests
res = requests.get("http://baoming4.ntce.cn/apply")
print(res.text)