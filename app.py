import streamlit as st
from PIL import Image


st.set_page_config(layout="wide")

# Sample dictionary with image file paths (you can replace these with actual paths)
image_dict = {
    'Image 1': '1.png',
    'Image 2': '2.png',
    'Image 3': '3.png',
}


# Initialize the session state for the current image index
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

# Function to go to the next image
def next_image():
    st.session_state.current_index = (st.session_state.current_index + 1) % len(image_dict)

# Function to go to the previous image
def prev_image():
    st.session_state.current_index = (st.session_state.current_index - 1) % len(image_dict)

# Display the current image
image_names = list(image_dict.keys())
current_image_name = image_names[st.session_state.current_index]
current_image_path = image_dict[current_image_name]

# Load and display the image as large as possible (fit the screen)
image = Image.open(current_image_path)
st.image(image, caption=current_image_name, use_container_width=True)

# Display next and back buttons
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button('Back'):
        prev_image()

with col3:
    if st.button('Next'):
        next_image()
