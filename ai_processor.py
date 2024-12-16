"""
    Generates a response from the OpenAI API based on the given prompt.
    This function uses the OpenAI Completion API to generate a response
    from a specified model (default is "gpt-3.5-turbo"). It handles the
    API call and returns the generated text.
    Parameters:
    prompt (str): The input text prompt to generate a response for.
    Returns:
    str: The generated response text from the OpenAI API, or an error message
         if the API call fails.
    Raises:
    Exception: If there is an issue with the API call, an error message is returned.
"""

import openai
import os

# Set OpenAI API key
openai.api_key = ''

# # Set proxy URL and port
# proxy_url = 'http://127.0.0.1'
# proxy_port = '7950'  # Replace this with your own port

# # Set http_proxy and https_proxy environment variables
# os.environ['http_proxy'] = f'{proxy_url}:{proxy_port}'
# os.environ['https_proxy'] = f'{proxy_url}:{proxy_port}'


def get_ai_response(prompt):
    try:
        # Use the new Completion API method
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # You can choose gpt-4 or other models
            prompt=prompt,           # User prompt
            max_tokens=150,          # Maximum number of tokens
            temperature=0.7,         # Controls the randomness of the text
        )

        # Return the generated content
        return response.choices[0].text.strip()

    except Exception as e:
        return f"Error: {str(e)}"


# Example: Call GPT-3.5 to answer a question
if __name__ == "__main__":
    prompt = "Explain the process of photosynthesis."
    response = get_ai_response(prompt)
    print("GPT-3.5 Response: ", response)
