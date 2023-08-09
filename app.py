from flask import Flask, request, jsonify
from chatgpt_bot import ChatGPTBotAPI

# Initialize Flask app
app = Flask(__name__)

# Create an instance of the ChatGPTBotAPI class
chatbot = ChatGPTBotAPI()

# Initialize the chatbot with the OpenAI API key
chatbot.initialize_gpt3('APIKey')  # replace with your API key

@app.route('/create_prompt', methods=['POST'])
def create_prompt():
    """Endpoint to create and store a new user prompt."""
    
    # Extract 'prompt' from the JSON request body
    prompt = request.json.get('prompt')
    
    # Store the prompt using the chatbot instance and retrieve its index
    index = chatbot.create_prompt(prompt)
    
    # Return a success message along with the index of the stored prompt
    return jsonify({"message": "Prompt added successfully", "index": index})

@app.route('/get_response/<int:prompt_index>', methods=['GET'])
def get_response(prompt_index):
    """Endpoint to retrieve a response for a stored prompt using its index."""
    
    # Fetch the response for the provided prompt index
    response = chatbot.get_response(prompt_index)
    
    # Return the generated response
    return jsonify({"response": response})

@app.route('/update_prompt/<int:prompt_index>', methods=['PUT'])
def update_prompt(prompt_index):
    """Endpoint to update a stored prompt using its index."""
    
    # Extract 'new_prompt' from the JSON request body
    new_prompt = request.json.get('new_prompt')
    
    # Update the prompt at the specified index and get the status message
    message = chatbot.update_prompt(prompt_index, new_prompt)
    
    # Return the status message
    return jsonify({"message": message})

# Run the Flask app when this script is executed
if __name__ == "__main__":
    app.run(debug=True)
