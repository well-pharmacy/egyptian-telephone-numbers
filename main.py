import pandas as pd
import requests
from io import StringIO
from typing import List, Optional, Dict

# --- Constants ---
URL = "https://en.wikipedia.org/wiki/Telephone_numbers_in_Egypt"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
TABLE_NAMES = ["area_codes", "mobile_prefixes", "emergency_numbers", "hotlines"]


def fetch_html(url: str, headers: Dict[str, str]) -> Optional[str]:
    """
    Fetches HTML content from a URL, handling potential network errors.
    """
    print(f"Fetching data from {url}...")
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        return response.text
    except requests.exceptions.RequestException as e:
        print(
            "Error: Failed to retrieve the webpage. Please check your connection or the URL."
        )
        print(f"Details: {e}")
        return None


def extract_tables(html: str) -> Optional[List[pd.DataFrame]]:
    """
    Extracts all tables with the 'wikitable' class from HTML content.
    """
    try:
        tables = pd.read_html(StringIO(html), attrs={"class": "wikitable"})
        print(f"Found {len(tables)} tables.")
        return tables
    except ValueError:
        print("Error: No tables with class 'wikitable' were found on the page.")
        print("The page structure may have changed.")
        return None


def save_tables_to_csv(tables: List[pd.DataFrame], names: List[str]) -> None:
    """
    Saves a list of DataFrames to correspondingly named CSV files.
    """
    if len(tables) < len(names):
        print(
            f"Error: Expected at least {len(names)} tables, but found only {len(tables)}."
        )
        print("The page structure may have changed.")
        return

    for i, name in enumerate(names):
        tables[i].to_csv(f"{name}.csv", index=False, encoding="utf-8-sig")
        print(f"Saved {name}.csv")


def main():
    """Main function to orchestrate the scraping and saving process."""
    html_content = fetch_html(URL, HEADERS)
    if html_content and (tables := extract_tables(html_content)):
        save_tables_to_csv(tables, TABLE_NAMES)


if __name__ == "__main__":
    main()
