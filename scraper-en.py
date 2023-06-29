# OS Library
import os

# Json library
import json

# Time Library
import time

# Web Scraping Library
import src.scraper as scraper

# Countries list (EN Site)
countries = [
    "AUS",  # Australia
    "BRN",  # Brunei
    "HKG",  # Hong Kong
    "IDN",  # Indonesia
    "IND",  # India
    "KHM",  # Cambodia
    "KOR",  # Korea
    "LKA",  # Sri Lanka
    "MAC",  # Macau
    "MYS",  # Malaysia
    "NZL",  # New Zealand
    "PHL",  # Philippines
    "SGP",  # Singapore
    "THA",  # Thailand
    "TWN",  # Taiwan
    "VNM"  # Vietnam
]

# Base url for the query
BASE_URL = "https://wanganmaxi-official.com/wanganmaxi6rr/en/locations/list"

# Delay (In seconds) between queries
DELAY = 2

# Json output indent (spaces)
INDENT = 2

# Output folder name
OUTPUT = "out_en"

# This is the main process
if __name__ == '__main__':

    # Create the output directory if not present
    if (not os.path.exists(OUTPUT)):

        # Create the directory (recursive)
        os.makedirs(OUTPUT)

    # Loop over the countries
    for country in countries:

        try:

            print(f"Processing country: {country} ...")

            # Scrape the data from the country page
            stores = scraper.scrape_url(
                BASE_URL, {"country": country, 'lang': 'en'})

            # Generate the filename
            filename = f"Stores_{country}.json"

            # Generate the output filepath
            filepath = os.path.join(OUTPUT, filename)

            # Dump stores to json
            stores_json = json.dumps(stores, indent=INDENT)

            # Open the output file
            with open(filepath, "w+") as f:

                # Write the json data to the file
                f.write(stores_json)

            print(
                f"{len(stores)} stores written for country {country} to file {filepath} successfully."
            )

        except Exception as e:

            print(f"Failed for country {country}: {str(e)}")

        finally:  # Success or failure

            print(f"Sleeping for {DELAY} seconds ...")

            # Sleep for 'delay' seconds
            time.sleep(DELAY)
