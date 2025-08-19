# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types
import dotenv


dotenv.load_dotenv()


def generate_with_image(image_bytes, text_prompt, mime_type="image/png", chat_history=None):
    """
    Generate AI response based on image and text prompt with chat history
    
    Args:
        image_bytes (bytes): The image data as bytes
        text_prompt (str): The text prompt to send with the image
        mime_type (str): The MIME type of the image (default: image/png)
        chat_history (list): Previous chat messages in format [{"role": "user/assistant", "content": "text"}]
    
    Returns:
        str: The AI generated response
    """
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.5-flash"
    
    # Build conversation history
    contents = []
    
    # Add previous chat history
    if chat_history:
        for message in chat_history:
            role = "user" if message["role"] == "user" else "model"
            contents.append(
                types.Content(
                    role=role,
                    parts=[types.Part.from_text(text=message["content"])],
                )
            )
    
    # Add current user message with image
    contents.append(
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=text_prompt),
                types.Part.from_bytes(data=image_bytes, mime_type=mime_type),
            ],
        )
    )
    
    generate_content_config = types.GenerateContentConfig(
        thinking_config = types.ThinkingConfig(
            thinking_budget=-1,
        ),
    )

    response_text = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        response_text += chunk.text
    
    return response_text


def generate_text_only(text_prompt, chat_history=None):
    """
    Generate AI response based on text prompt only with chat history
    
    Args:
        text_prompt (str): The text prompt to send
        chat_history (list): Previous chat messages in format [{"role": "user/assistant", "content": "text"}]
    
    Returns:
        str: The AI generated response
    """
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.5-flash"
    
    # Build conversation history
    contents = []
    
    # Add previous chat history
    if chat_history:
        for message in chat_history:
            role = "user" if message["role"] == "user" else "model"
            contents.append(
                types.Content(
                    role=role,
                    parts=[types.Part.from_text(text=message["content"])],
                )
            )
    
    # Add current user message
    contents.append(
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=text_prompt)],
        )
    )
    
    generate_content_config = types.GenerateContentConfig(
        thinking_config = types.ThinkingConfig(
            thinking_budget=-1,
        ),
    )

    response_text = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        response_text += chunk.text
    
    return response_text


def generate():
    """Original function for backwards compatibility"""
    YOUR_IMAGE_PATH = '/Users/yugjindal/Desktop/Projects/AI Image Analysis/doraemon.png'
    with open(YOUR_IMAGE_PATH, 'rb') as f:
        image_bytes = f.read()
    
    response = generate_with_image(image_bytes, "What is this image about?")
    print(response)


if __name__ == "__main__":
    generate()
