import random
import requests
import time

while True:
    n = random.randint(10000000, 99999999)
    r = requests.get(f"https://www.stundenplan24.de/{str(n)}/mobil")
    if r.status_code == 200:
        print("[+] " + str(n))
        open('hits.txt','a+').write("{}\n".format(str(n)))
    elif r.status_code == 404:
        print("[-] " + str(n))
    else:
        print("[-] Error")
    time.sleep(2)
