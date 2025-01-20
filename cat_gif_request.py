import requests
from io import BytesIO

def get_cat_gif():

    url = "https://cataas.com/cat/gif"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return BytesIO(response.content)
        else:
            raise Exception(f"Error fetching GIF: {response.status_code}.")
    except Exception as e:
        print(f"Error accessing the API: {str(e)}")
        return None
