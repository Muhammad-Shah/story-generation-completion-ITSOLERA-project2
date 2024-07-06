import streamlit as st

# Dummy functions for illustration


def generate_story(prompt, length, genre):
    # Replace with actual story generation logic
    return f"{prompt} ... (generated {genre} story of {length} words)"


def complete_story(partial_story, length, genre):
    # Replace with actual story completion logic
    return f"{partial_story} ... (completed {genre} story of {length} words)"


# Streamlit UI
st.title("Story Generation and Completion")

st.sidebar.title("Options")
task = st.sidebar.selectbox(
    "Choose Task", ["Generate a New Story", "Complete a Story"])

if task == "Generate a New Story":
    st.header("Enter your story prompt:")
    prompt = st.text_area("Prompt", "Once upon a time")

    st.sidebar.header("Generation Options")
    length = st.sidebar.slider("Select story length (words)", 100, 1000, 300)
    genre = st.sidebar.selectbox(
        "Select genre", ["Fantasy", "Sci-Fi", "Mystery", "Romance", "Horror"])

    if st.button("Generate Story"):
        if prompt.strip():
            story = generate_story(prompt, length, genre)
            st.subheader("Generated Story:")
            st.write(story)
        else:
            st.error("Please enter a story prompt.")

elif task == "Complete a Story":
    st.header("Enter your partial story:")
    partial_story = st.text_area("Partial Story", "The adventure began when")

    st.sidebar.header("Completion Options")
    length = st.sidebar.slider(
        "Select completion length (words)", 100, 1000, 300)
    genre = st.sidebar.selectbox(
        "Select genre", ["Fantasy", "Sci-Fi", "Mystery", "Romance", "Horror"])

    if st.button("Complete Story"):
        if partial_story.strip():
            completed_story = complete_story(partial_story, length, genre)
            st.subheader("Completed Story:")
            st.write(completed_story)
        else:
            st.error("Please enter a partial story.")
