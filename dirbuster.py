import requests
import threading

target = "http://192.168.133.129"
wordlist = "/usr/share/wordlists/dirb/common.txt"

def check_dir(word):
    url = f"{target}/{word}"
    try:
        response = requests.get(url, timeout=2)
        if response.status_code == 200:
            print(f"[200] FOUND: {url}")
        elif response.status_code == 403:
            print(f"[403] FORBIDDEN: {url}")
    except:
        pass

print(f"Scanning {target} for directories...\n")

threads = []
with open(wordlist, "r") as f:
    for word in f:
        word = word.strip()
        t = threading.Thread(target=check_dir, args=(word,))
        threads.append(t)
        t.start()

for t in threads:
    t.join()

print("\nScan complete.")
