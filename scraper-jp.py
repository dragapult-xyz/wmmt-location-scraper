# OS Library
import os

# Json library
import json

# Time Library
import time

# Web Scraping Library
import src.scraper as scraper

# Configuration
import config

# Base url for the query
BASE_URL = "https://wanganmaxi-official.com/wanganmaxi6rr/jp/locations/list"

# Output folder name
OUTPUT = "out_jp"

# This is the main process
if __name__ == '__main__':

    # Create the output directory if not present
    if (not os.path.exists(OUTPUT)):

        # Create the directory (recursive)
        os.makedirs(OUTPUT)

    # Loop over the countries
    # for country in countries:
    for i in range(1, 48):

        # Generate the name for the area
        area = f"JP-{str(i).zfill(2)}"

        try:

            print(f"Processing area: {area} ...")

            # Scrape the data from the country page
            stores = scraper.scrape_url(
                BASE_URL, {"area": area})

            # Generate the filename
            filename = f"Stores_{area}.json"

            # Generate the output filepath
            filepath = os.path.join(OUTPUT, filename)

            # Dump stores to json
            stores_json = json.dumps(stores, indent=config.INDENT, ensure_ascii=False)

            # Open the output file
            with open(filepath, "w+", encoding='utf8') as f:

                # Write the json data to the file
                f.write(stores_json)

            print(
                f"{len(stores)} stores written for area {area} to file {filepath} successfully."
            )

        except Exception as e:

            print(f"Failed for area {area}: {str(e)}")

        finally:  # Success or failure

            print(f"Sleeping for {config.DELAY} seconds ...")

            # Sleep for 'delay' seconds
            time.sleep(config.DELAY)
