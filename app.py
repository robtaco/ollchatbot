import streamlit as st
import ollama
import uuid

# Set the page title
st.set_page_config(page_title="Ollama Chat")

# Initialize session state for messages and chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = {}

# Sidebar for model selection and chat history
with st.sidebar:
    # Display a GIF in the sidebar

    # Tagline for the app
    # URL of the GIF
    gif_url = "https://i.makeagif.com/media/1-26-2025/hIx3id.gif"

    # Display the GIF
    st.image(gif_url)
    st.markdown("*Keep your prompt data private and secure*")

    # Model selection

    st.title("Model Selection")
    model = st.selectbox("Choose a model", ["llama3.2"])
    
    st.title("Chat History")
    if st.session_state["chat_history"]:
        selected_chat = st.radio(
            "Select a conversation",
            list(st.session_state["chat_history"].keys()),
            format_func=lambda x: st.session_state["chat_history"][x]["title"]
        )
        if st.button("Load Conversation"):
            st.session_state["messages"] = st.session_state["chat_history"][selected_chat]["messages"]

# Function to generate responses
def generate_response(prompt):
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        stream=False
    )
    return response["message"]["content"]

# Display chat messages
st.title("Ollama Chat")
st.markdown("*Ollama Chat, powered by Ollama*")
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input for user prompt
if prompt := st.chat_input("Enter your message:"):
    # Display user message
    st.chat_message("user").markdown(prompt)
    # Generate and display assistant response
    response = generate_response(prompt)
    st.chat_message("assistant").markdown(response)
    # Update chat history
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.session_state["messages"].append({"role": "assistant", "content": response})

    # Save to chat history with abbreviated title
    chat_id = str(uuid.uuid4())
    st.session_state["chat_history"][chat_id] = {
        "title": (prompt[:50] + '...') if len(prompt) > 50 else prompt,
        "messages": st.session_state["messages"][:]
    }
