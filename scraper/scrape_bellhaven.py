import requests
import urllib3
from bs4 import BeautifulSoup
import json
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://analyst-assessment-production.up.railway.app"

communities = []
community_links = []

# Get all community links
for page in range(1, 4):
    url = f"{BASE_URL}/communities?page={page}"

    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, "html.parser")

    for card in soup.select("div.card"):
        link = card.select_one("h3 a")

        if link:
            community_links.append(BASE_URL + link["href"])

print(f"Found {len(community_links)} community links")

# Visit each detail page
for idx, url in enumerate(community_links, start=1):

    print(f"Processing {idx}/{len(community_links)}")

    response = requests.get(url, verify=False)

    soup = BeautifulSoup(response.text, "html.parser")

    name = soup.find("h1").get_text(strip=True)

    page_text = soup.get_text("\n", strip=True)

    # Extract Address section
    address_match = re.search(
        r"Address\s+(.*?)\s+Care Offerings",
        page_text,
        re.DOTALL
    )

    address_block = address_match.group(1).strip() if address_match else ""

    lines = [x.strip() for x in address_block.split("\n") if x.strip()]

    street = ""
    city = ""
    state = ""
    zipcode = ""

    if len(lines) >= 2:
        street = lines[0]

        city_state_zip = lines[1]

        m = re.search(
            r"(.+?),\s*([A-Z]{2})\s*(\d{5})",
            city_state_zip
        )

        if m:
            city = m.group(1)
            state = m.group(2)
            zipcode = m.group(3)

    # Extract Care Offering
    care_match = re.search(
        r"Care Offerings\s+(.*?)\s+Administrator",
        page_text,
        re.DOTALL
    )

    care_type = care_match.group(1).strip() if care_match else ""

    communities.append({
        "name": name,
        "address": street,
        "city": city,
        "state": state,
        "zip": zipcode,
        "care_type": care_type,
        "url": url
    })

# Save results
with open("../data/website_locations.json", "w", encoding="utf-8") as f:
    json.dump(communities, f, indent=2)

print(f"\nSaved {len(communities)} communities")
print("Output: data/website_locations.json")