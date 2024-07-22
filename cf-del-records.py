import requests

API_TOKEN = "_gBdtqDf69R0RUG_3Mg4Y1rJf-22ChNBCW_5Y5J0"
ZONE_ID = "389ed7b7979aca66e05890b0fa7052e1"

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
