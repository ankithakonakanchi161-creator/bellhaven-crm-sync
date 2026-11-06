import json

with open("accounts.json", "r", encoding="utf-8") as f:
    crm = json.load(f)["data"]

for a in crm:
    if "Owosso" in a["name"]:
        print(a["account_id"], a["name"], a["billing_zip"])
