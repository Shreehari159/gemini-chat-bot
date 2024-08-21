import streamlit as st
import google.generativeai as genai

# Set up the Streamlit app
st.title("Welcome to Gemini Chat")

# Configure the Google Generative AI with your API key
genai.configure(api_key="AIzaSyAf4lE0j4NsLAHUICbQjD3WIS8etmeirOY")

# Get user input from Streamlit
user_input = st.text_input("Enter your message:")

# Only proceed if the user has entered some input
if user_input:
    # Initialize the generative model
    model = genai.GenerativeModel('gemini-pro')
    
    # Start a chat session
    chat = model.start_chat(history=[])
    
    # Send the message and get a response
    response = chat.send_message(user_input)
    
    # Display the response in the Streamlit app
    st.write(response.text)
