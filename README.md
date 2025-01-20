### README for Cat and Dog App

---

## **Overview**
This project is a simple **Streamlit** app that fetches and displays random facts and images/GIFs about cats and dogs. The app uses multiple APIs to provide engaging content for animal lovers.

---

## **Features**
1. Displays random **cat facts** and **cat GIFs**.
2. Displays random **dog facts** and **dog images**.
3. Simple and interactive interface using **Streamlit**.
4. Dynamic selection between cats and dogs, showing corresponding content.

---

## **APIs Used**
### 1. [Dog CEO API](https://dog.ceo/dog-api/documentation/random)
- Provides random images of dogs.
- Endpoint used: `https://dog.ceo/api/breeds/image/random`

### 2. [Dog Facts API](https://kinduff.github.io/dog-api/)
- Provides random facts about dogs.
- Endpoint used: `https://dog-api.kinduff.com/api/facts`

### 3. [Cat Facts API](https://catfact.ninja/)
- Provides random facts about cats.
- Endpoint used: `https://catfact.ninja/fact`

### 4. [Cataas API](https://cataas.com/)
- Provides random GIFs of cats.
- Endpoint used: `https://cataas.com/cat/gif`

---

## **Running the App**
1. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```
2. Open the app in your browser (usually at `http://localhost:8501`).

---

## **Project Structure**
```
├── cat_curiosity_request.py   # Fetches cat facts
├── cat_gif_request.py         # Fetches cat GIFs
├── dog_curiosity_request.py   # Fetches dog facts
├── dog_image_request.py       # Fetches random dog images
├── main.py                    # Streamlit app logic
├── requirements.txt           # List of dependencies
├── README.md                  # Documentation
```

---

## **How to Use the App**
1. Open the app in your browser after running it.
2. Choose between "Cats" and "Dogs" by clicking the respective button.
3. The app will display:
   - A random **GIF** (for cats) or **image** (for dogs).
   - A random fact about the selected animal.

---

## **Error Handling**
- Displays meaningful error messages for API call failures.
- Handles missing or empty responses gracefully.

---

## **License**
This project is licensed under the MIT License. See the LICENSE file for details.

---

## **Contributors**
- [Your Name](https://github.com/your-profile)

Feel free to contribute by submitting pull requests or reporting issues! 🐾✨