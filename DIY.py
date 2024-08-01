import requests

API_TOKEN = "您的api令牌"
ZONE_ID = "区域ID"

baseUrl = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records"

headers = {
    'Authorization': f'Bearer {API_TOKEN}',
    'Content-Type': 'application/json'
}

listUrl = f"{baseUrl}?per_page=500"
print(listUrl)
response = requests.get(listUrl, headers=headers)
records = response.json()['result']

for record in records:
    name = record['name']
    content = record['content']

    print(f"Deleting {name} that points to {content}")

    deleteUrl = f"{baseUrl}/{record['id']}"
    requests.delete(deleteUrl, headers=headers)
    print(deleteUrl)
