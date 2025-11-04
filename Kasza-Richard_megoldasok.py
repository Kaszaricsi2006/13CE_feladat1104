
import json

with open("konyvtar.txt", "r", encoding="latin2") as f:
    tartalom = f.read()

adatok = []
sorok = tartalom.strip().split("\n")
fejlec = sorok[0].split(";")

for sor in sorok[1:]:
    ertekek = sor.split(";")
    rekord = dict(zip(fejlec, ertekek))
    adatok.append(rekord)

with open("konyvtar.json", "w", encoding="utf-8") as f:
    json.dump(adatok, f, ensure_ascii=False, indent=4)

print(" A JSON fájl elkészült: konyvtar.json")
