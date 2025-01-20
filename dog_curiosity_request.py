import requests

def dog_curiosity():
    """
    Fetches a random dog fact from the Dog Facts API.
    """
    url = "https://dog-api.kinduff.com/api/facts"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            facts = data.get("facts", [])
            return facts[0] if facts else "No fact found."
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        print(f"Error accessing the API: {str(e)}")
        return "Error fetching the fact."
