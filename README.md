# Egypt Telephone Numbers Scraper

A Python script to scrape telephone number information for Egypt from Wikipedia and save it into CSV files.

## Description

This script fetches the Wikipedia page for "[Telephone numbers in Egypt](https://en.wikipedia.org/wiki/Telephone_numbers_in_Egypt)", finds all the data tables on the page, and saves the first four tables into separate CSV files.

The generated files are:
- `area_codes.csv`
- `mobile_prefixes.csv`
- `emergency_numbers.csv`
- `hotlines.csv`

## Requirements

- Python 3.6+
- `pandas`
- `requests`

## Installation

1.  Clone this repository or download the files.

2.  It is highly recommended to use a virtual environment to manage dependencies.

3.  Install the required packages from `requirements.txt`.

    **Using `uv`:**
    ```bash
    uv sync
    ```

## Usage

Run the script from your terminal:

```bash
python main.py
```

The script will print its progress as it saves each file:
```
Found 4 tables
Saved area_codes.csv
Saved mobile_prefixes.csv
Saved emergency_numbers.csv
Saved hotlines.csv
```

## Disclaimer

The data is sourced directly from Wikipedia. The accuracy of the data depends entirely on the source page. This script relies on the structure of the Wikipedia page (specifically, the presence and order of tables with the class `wikitable`). If the source page is updated in a way that changes this structure, the script may fail or produce incorrect output.