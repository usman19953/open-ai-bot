# ChatGPT Flask API

A simple Flask API for interacting with OpenAI's GPT-3 model using CRUD operations. 

## Prerequisites

- Python 3.x
- Flask
- OpenAI Python library

## Getting Started

1. **Clone the Repository**:

git clone <repository-url>
cd <repository-name>

2. **Set Up a Virtual Environment** (Recommended):

python -m venv venv
source venv/bin/activate # On Windows use: venv\Scripts\activate

3. **Install Required Packages**:

pip install -r requirements.txt

4. **Set Your OpenAI API Key**:
- Open `app.py` and replace the placeholder API key with your actual OpenAI API key.
- For better security, consider using environment variables or secret management tools instead of hardcoding the API key.

5. **Run the Flask App**:

python app.py


## API Endpoints

1. **Create a new prompt**:
- **Endpoint**: `/create_prompt`
- **Method**: `POST`
- **Body**: 
  ```json
  {
    "prompt": "Your prompt here"
  }
  ```
- **Response**: The index of the stored prompt.

2. **Get a response for a prompt by its index**:
- **Endpoint**: `/get_response/<prompt_index>`
- **Method**: `GET`
- **Response**: The GPT-3 model's response.

3. **Update an existing prompt**:
- **Endpoint**: `/update_prompt/<prompt_index>`
- **Method**: `PUT`
- **Body**:
  ```json
  {
    "new_prompt": "Your updated prompt here"
  }
  ```
- **Response**: A success or error message.

