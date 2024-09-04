import streamlit as st
import replicate
import os

# Configure Replicate API
os.environ['REPLICATE_API_TOKEN'] = 'r8_OWqDkv1kf49OW6lPcBdxB4HimMMBjzq4c1AA7'

# Streamlit app
st.title('Chatbot with Replicate')

user_input = st.text_input("You:", "")

if st.button('Send'):
    if user_input:
        try:
            response = replicate.run(
                "your-model-id",
                input={"text": user_input}
            )
            st.text_area("Chatbot:", response, height=200)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter a message.")
