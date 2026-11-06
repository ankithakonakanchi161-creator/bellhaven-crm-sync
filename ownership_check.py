import json

with open("accounts.json", "r", encoding="utf-8") as f:
    crm = json.load(f)["data"]

for a in crm:
    if a["name"] in [
        "Bellhaven Crossings of Lima",
        "Bellhaven of Marietta",
        "Bellhaven of Tiffin"
    ]:
        print("\n------------------")
        print("Name:", a["name"])
        print("Parent:", a["parent_name"])
        print("Revenue:", a["lifetime_revenue"])
        print("AR:", a["outstanding_ar"])