import requests

API_TOKEN = "L4kH3D67918f_oIsBe5Ua11p7ea4j-47KvCccW6T"
ZONE_ID = "0cbebb7d936c2d966f68edf637388f3e"

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
