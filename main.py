import pandas as pd
import requests
from io import StringIO

url = "https://en.wikipedia.org/wiki/Telephone_numbers_in_Egypt"

# Fake a browser user-agent so Wikipedia serves full HTML with tables
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
html = requests.get(url, headers=headers).text

# Now Pandas can see the tables
tables = pd.read_html(StringIO(html), attrs={"class": "wikitable"})

print(f"Found {len(tables)} tables")

names = ["area_codes", "mobile_prefixes", "emergency_numbers", "hotlines"]

for i, name in enumerate(names):
    tables[i].to_csv(f"{name}.csv", index=False, encoding="utf-8-sig")
    print(f"Saved {name}.csv")
