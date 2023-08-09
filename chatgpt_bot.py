import openai

class ChatGPTBotAPI:
    def __init__(self):
        # Initialize lists to store prompts and their corresponding responses
        self.prompts = []
        self.responses = []

    def initialize_gpt3(self, api_key):
        # Set the OpenAI API key for future requests
        openai.api_key = api_key

    def create_prompt(self, prompt):
        """Store a user prompt and return its index."""
        self.prompts.append(prompt)
        return len(self.prompts) - 1  # Return the index of the stored prompt

    def get_response(self, prompt_index):
        """Retrieve the response for a stored prompt using its index."""
        
        # Check for invalid index
        if prompt_index >= len(self.prompts) or prompt_index < 0:
            return "Invalid prompt index"

        # Check if a response for the given index already exists
        if len(self.responses) > prompt_index:
            return self.responses[prompt_index]
        
        # If no cached response, get one from OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use the specified engine for generating responses
            prompt=self.prompts[prompt_index]
        ).choices[0].text.strip()  # Extract the response text from API's reply

        # Cache the generated response and return it
        self.responses.append(response)
        return response

    def update_prompt(self, prompt_index, new_prompt):
        """Update a stored prompt using its index and remove its cached response if it exists."""
        
        # Check for invalid index
        if prompt_index >= len(self.prompts) or prompt_index < 0:
            return "Invalid prompt index"
        
        # Update the prompt at the specified index
        self.prompts[prompt_index] = new_prompt
        
        # If a response exists for this prompt, remove it to ensure freshness for the next call
        if len(self.responses) > prompt_index:
            del self.responses[prompt_index]  # Remove cached response
            
        return "Prompt updated successfully"
