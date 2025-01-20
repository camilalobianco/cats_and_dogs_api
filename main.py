import streamlit as st

from cat_gif_request import get_cat_gif
from cat_curiosity_request import cat_curiosity
from dog_curiosity_request import dog_curiosity
from dog_image_request import get_dog_image

if "selected" not in st.session_state:
    st.session_state["selected"] = "None"

st.title("GIFs and Facts About Cats and Dogs")

col1, col2 = st.columns(2)

with col1:
    if st.button("Cats", key="cats"):
        st.session_state["selected"] = "Cats"

with col2:
    if st.button("Dogs", key="dogs"):
        st.session_state["selected"] = "Dogs"

if st.session_state["selected"] == "Cats":
    cat_gif = get_cat_gif()
    cat_fact = cat_curiosity()
    
    if cat_gif:
        st.image(cat_gif, caption="A cat GIF for you!", use_container_width=True)

    if cat_fact:
        st.markdown("### Fact about Cats:")
        st.write(cat_fact)

elif st.session_state["selected"] == "Dogs":
    dog_gif = get_dog_image()
    dog_fact = dog_curiosity()
    
    if dog_gif:
        st.image(dog_gif, caption="A dog image for you!", use_container_width=True)

    if dog_fact:
        st.markdown("### Fact about Dogs:")
        st.write(dog_fact)
else:
    st.write("Click a button to see GIFs/images and facts about cats or dogs!")
