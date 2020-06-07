import requests

def verify_and_add(word):
  url = f"https://remoteok.io/remote-{word}-jobs"
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
  result = requests.get(url, headers=headers, allow_redirects=False)
  if result.status_code != 404:
    return word
  else:
    return None