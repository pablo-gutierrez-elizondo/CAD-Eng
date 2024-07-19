from dotenv import load_dotenv
import anthropic
import streamlit as st

load_dotenv()

def get_response(user_content):
    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1024,
        system="Answer the following question. Keep it short and in simple terms. 1-2 sentences.",
        messages=[{"role":"user", "content":user_content}],
    )
    return response.content[0].text
