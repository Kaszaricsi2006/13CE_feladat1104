import requests
import csv
import json
import base64

url = "https://github.com/Kaszaricsi2006/13CE_feladat1104/blob/main/konyvtar.txt"
response = requests.get(url)
data = response.text

lines = data.strip().splitlines()
reader = csv.DictReader(lines)
konyvtar_lista = [row for row in reader]

output_file = "konyvtar.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(konyvtar_lista, f, indent=4, ensure_ascii=False)

print(f"JSON adatok mentve ide: {output_file}")

# Feltöltés GitHub-ra (opcionális)
github_user = "<Kaszaricsi2006>"
github_repo = "<13CE_feladat1104>"
token = "<GITHUB_PERSONAL_ACCESS_TOKEN>"

with open(output_file, "rb") as f:
    content = f.read()

encoded_content = base64.b64encode(content).decode("utf-8")
api_url = f"https://api.github.com/repos/{github_user}/{github_repo}/contents/{output_file}"

payload = {
    "message": "Könyvtár JSON feltöltés",
    "content": encoded_content
}

headers = {"Authorization": f"token {token}"}
response = requests.put(api_url, headers=headers, json=payload)

if response.status_code in [200, 201]:
    print("JSON fájl sikeresen feltöltve a GitHub-ra!")
else:
    print(f"Hiba a feltöltés során: {response.status_code} - {response.text}")
