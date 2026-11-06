import json

# Load website locations
with open("data/website_locations.json", "r", encoding="utf-8") as f:
    website = json.load(f)

# Load CRM accounts
with open("accounts.json", "r", encoding="utf-8") as f:
    crm = json.load(f)["data"]

website_names = {x["name"].lower() for x in website}

crm_names = {
    x["name"].lower()
    for x in crm
    if "parent account" not in x["name"].lower()
}

print("Website communities:", len(website_names))
print("CRM accounts:", len(crm_names))

print("\n=== Missing from CRM ===")
for name in sorted(website_names - crm_names):
    print(name)

print("\n=== Exists in CRM but not on Website ===")
for name in sorted(crm_names - website_names):
    print(name)
    print("\n=== ZIP Matches ===")

website_zip = {
    (x["zip"], x["name"])
    for x in website
}

crm_zip = {
    (x["billing_zip"], x["name"])
    for x in crm
    if "Parent Account" not in x["name"]
}

for w_zip, w_name in website_zip:
    for c_zip, c_name in crm_zip:
        if w_zip == c_zip and w_name.lower() != c_name.lower():
            print()
            print("Website:", w_name)
            print("CRM    :", c_name)
            print("ZIP    :", w_zip)
