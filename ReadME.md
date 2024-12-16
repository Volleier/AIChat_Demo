# AI Chat Project

This is a simple AI chat project that uses Flask as the backend server, OpenAI's model to generate AI responses, and interacts with users through a simple front-end interface.

## Environment Setup

1. Install the required dependencies:

    ```sh
    pip install flask flask-cors openai
    ```

2. Set the OpenAI API key:
    In the `ai_processor.py` file, set `openai.api_key` to your OpenAI API key.

## How to Use

1. Start the Flask server:

    ```sh
    python backend_server.py
    ```

2. Open the `index.html` file:
    Open the `index.html` file in a browser and enter text in the chat box to chat with the AI.

## File Structure

- `backend_server.py`: Flask server code that handles front-end requests and returns responses.
- `ai_processor.py`: Handles interaction with the OpenAI API to generate AI responses.
- `keyword_detection.py`: Detects specific keywords in user input.
- `index.html`: Front-end HTML file that provides the user interface.
- `script.js`: Front-end JavaScript file that handles user input and interacts with the backend.
- `styles.css`: Front-end CSS file that defines the page styles.
