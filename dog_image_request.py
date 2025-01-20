import requests

def get_dog_image():

    url = "https://dog.ceo/api/breeds/image/random"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get("message", None)  # URL of the image
        else:
            return None
    except Exception as e:
        print(f"Error accessing the API: {str(e)}")
        return None
