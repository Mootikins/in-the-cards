import json
import os

CARDS_JSON = open("./json-against-humanity/cah-all-compact.json", "r", encoding="utf-8")

PARSED = json.load(CARDS_JSON)

CARDS_JSON.close()

try:
    os.mkdir("packs")
except FileExistsError as _e:
    print("'packs' directory already exists\nProceeding with existing directory")

for pack in PARSED["packs"]:
    PACK = {}

    PACK["name"] = pack["name"].replace('/', '+')
    PACK["official"] = pack["official"]
    PACK["white"] = []
    PACK["black"] = []

    for white_num in pack["white"]:
        card = {}
        card["text"] = PARSED["white"][white_num]
        PACK["white"].append(card)

    for black_num in pack["black"]:
        PACK["black"].append(PARSED["black"][black_num])

    with open("packs/" + PACK["name"] + ".json", "w", encoding="utf-8") as PACK_FILE:
        json.dump(PACK, PACK_FILE, ensure_ascii=False, indent="\t")
        PACK_FILE.close()
