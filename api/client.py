import requests
import streamlit as st

def get_ollama_response(input_text, endpoint):
    try:
        # Make the POST request to the specified endpoint
        response = requests.post(
            f"http://localhost:8007/{endpoint}/invoke",
            json={'input': {'topic': input_text}}
        )
        
        # Raise an error if the request was unsuccessful
        response.raise_for_status()
        
        # Print raw response for debugging purposes
        data = response.json()
        st.write("Raw response data:", data)  # Temporary: Shows the full response for debugging
        
        # Check if 'output' is in the response data
        if 'output' in data:
            return data['output']
        else:
            return "No 'output' key in the response. Full response content: " + str(data)
            
    except requests.exceptions.RequestException as e:
        # Handle request issues
        st.error(f"Request failed: {e}")
    except ValueError:
        # Handle JSON decode errors
        st.error("Received invalid JSON from the server.")
    
    return "An error occurred or no output is available."

## Streamlit framework setup
st.title('Langchain Demo With LLAMA3.2 API')

# Input fields
input_text1 = st.text_input("Write a poem on")
input_text2 = st.text_input("Start a chat on")

# Display the response for each input
if input_text1:
    st.write(get_ollama_response(input_text1, endpoint="poem"))

if input_text2:
    st.write(get_ollama_response(input_text2, endpoint="chat"))
