import requests

with open("validips.txt", "r") as f:
    proxies = f.read().split("\n")


counter = 0
for x in proxies:
    try:
        res = requests.get("http://ipinfo.io/json", proxies={"http":proxies[counter], "https":proxies[counter]})
        print(res.status_code)
        print(res.text)

    except:
        print("Failed")
    finally:
        counter += 1
        counter % len(proxies)
