import requests

def cat_curiosity():
    url = "https://catfact.ninja/fact"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get("fact", "No fact found.")
        else:
            return f"Error fetching fact: {response.status_code}"
    except Exception as e:
        print(f"Error accessing the API: {str(e)}")
        return "Error fetching the fact."
