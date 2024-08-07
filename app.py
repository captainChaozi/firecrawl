import requests

url = "https://fire.qingyingda.com/v0/scrape"

payload = {
    "url": "https://suno.com/song/100690f6-3545-4bec-a97c-2f8c18dc6318",
    "pageOptions": {
        "waitFor": 50000
    }

}
headers = {
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)
