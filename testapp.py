import ollama

# Install Ollama on your Windows machine by following the instructions on the Ollama website: https://ollama.com/docs/install/windows

# Run the Ollama client with the default URL and port (localhost:11434) on your Windows machine
# Open a browser and go to http://localhost:11434 to access the Ollama web interface
# If you see Ollama is running, you can proceed with the following code
# If you don't see Ollama is running, you can try to run the following command in your terminal
# ollama run llama3.2
# If you see Ollama is running, you can proceed with the following code:

# excecute the following code in your terminal to run this test app:
# py .\testapp.py

# Define the prompt
prompt = "What is the capital of France?"

# Generate a response
response = ollama.chat(model='llama3.2', messages=[{'role': 'user', 'content': prompt}])

# Print the response
print(response['message']['content'])
