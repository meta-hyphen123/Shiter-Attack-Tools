import requests
from urllib.parse import quote, urlsplit, urlunsplit
h ="""
 __  __             _   _   _             _    
 \ \/ /___ ___     / \ | |_| |_ __ _  ___| | __
  \  // __/ __|   / _ \| __| __/ _` |/ __| |/ /
  /  \\\__ \__ \  / ___ \ |_| || (_| | (__|   < 
 /_/\_\___/___/ /_/   \_\__|\__\__,_|\___|_|\_\\


"""
print(h)



content = """
FUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHITFUCKYOUSHIT
"""

# 移除每行末尾的换行符等空白字符
payloads = [x.strip() for x in content]

url = input("URL: ")

vuln = []

# 定义代理为None
proxies = None

for payload in payloads:
    encoded_payload = quote(payload)
    url_parts = list(urlsplit(url))
    url_parts[2] = quote(url_parts[2])  # 编码路径部分
    url_parts[3] = f"{url_parts[3]}{encoded_payload}"  # 在查询部分追加编码后的payload
    xss_url = urlunsplit(url_parts)
    try:
        r = requests.get(xss_url, proxies=proxies)
        # 使用小写进行大小写不敏感的比较
        if payload.lower() in r.text.lower():
            print("Vulnerable: " + payload)
            if payload not in vuln:
                vuln.append(payload)
        else:
            print("Not vulnerable!")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

print("--------------------\nAvailable Payloads:")
print('\n'.join(vuln))
