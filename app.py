import streamlit as st
st.title("Qué pasó")
# Create file upload component
uploaded_file = st.file_uploader("Choose an audio file", type=["mp3", "wav", "opus", "m4a"])

# Check if a file is uploaded
if uploaded_file is not None:

    # Read file contents
    file_content = uploaded_file.read()
    
