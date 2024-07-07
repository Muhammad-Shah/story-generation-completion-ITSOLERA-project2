import streamlit as st
from generation import generate, complete


# Streamlit UI
st.title("Story Generation and Completion")

st.sidebar.title("Options")
task = st.sidebar.selectbox(
    "Choose Task", ["Generate a New Story", "Complete a Story"])

if task == "Generate a New Story":
    st.header("Enter your story prompt:")
    prompt = st.text_input(
        "Sory Title", placeholder="Dog and Cat", label_visibility='hidden')

    st.sidebar.header("Generation Options")

    # Creating the slider
    creative = st.sidebar.slider(
        label="Realistic Creative", min_value=0.0, max_value=1.0, value=0.7,)
    length = st.sidebar.selectbox(
        "Select length", ["Small", "Medium", "Large"])
    if length == "Small":
        length = 100
    elif length == "Medium":
        length = 300
    else:
        length = 500
    genre = st.sidebar.selectbox(
        "Select genre", ["Fantasy", "Sci-Fi", "Mystery", "Romance", "Horror"])

    if st.button("Generate Story"):
        if prompt.strip():
            story = generate(prompt, length, genre, )
            st.subheader("Generated Story:")
            st.write(story)
        else:
            st.error("Please enter a story prompt.")

elif task == "Complete a Story":
    st.header("Enter your partial story:")
    partial_story = st.text_area(
        "Partial Story", placeholder="The adventure began when", label_visibility='hidden')

    st.sidebar.header("Completion Options")
    length = st.sidebar.slider(
        "Select completion length (words)", 100, 1000, 300)
    genre = st.sidebar.selectbox(
        "Select genre", ["Fantasy", "Sci-Fi", "Mystery", "Romance", "Horror"])

    if st.button("Complete Story"):
        if partial_story.strip():
            completed_story = complete(partial_story, length, genre)
            st.subheader("Completed Story:")
            st.write(completed_story)
        else:
            st.error("Please enter a partial story.")
