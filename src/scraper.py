# Web Requests
import requests

# Beautiful soup
from bs4 import BeautifulSoup as bs


def remove_whitespace(name: str):

    # Strip any whitespace from the url
    return name.strip()


def get_store_id(url: str):

    # Remove url section, strip all whitespace
    return url.split("=")[-1].strip()


def scrape_url(url: str, params: object):

    # Store Data
    stores = []

    try:

        # Store Address
        addresses = []

        # Store Name
        names = []

        # Store ID
        ids = []

        # Request the page for the country
        response = requests.get(url, params=params)

        # Success status code is retrieved
        if (response.status_code == 200):

            # Get the raw text from the response
            text = response.text

            # Get the object from the html body
            body = bs(text, 'html.parser')

            # Find the list of stores
            dl = body.find('dl')

            # Loop over all of the 'dt' elements
            for dt in dl.find_all('dt'):

                # Get the 'a' element
                a = dt.find('a')

                # Get the name for the store
                name = remove_whitespace(a.get_text())

                # Get the store id from the url
                id = get_store_id(a.get('href'))

                # Add name to list
                names.append(name)

                # Add id to list
                ids.append(id)

            # Loop over all of the 'dd' elements
            for dd in dl.find_all('dd'):

                # Get the address for the store
                address = remove_whitespace(dd.get_text())

                # Add the address to the list
                addresses.append(address)

            # Ensure all of the lists have the same length
            if len(names) == len(ids) == len(addresses):

                # Derefence the store count
                count = len(names)

                # Loop over the stores
                for i in range(count):
                    stores.append({
                        "id": ids[i],
                        "name": names[i],
                        "address": addresses[i],
                    })

            else:  # Uneven array length

                raise Exception(
                    f"Number of store names, ids and addresses does not match!")

        else:  # Failure status code
            raise Exception(f"Bad status code {response.status_code}!")

        print("Data scraped successfully.")

    except Exception as e:  # Failed to scrape data
        print(f"Failed to scrape data! {str(e)}")

    # Return stores array
    return stores
