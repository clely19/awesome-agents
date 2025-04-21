# agents/summarizer_agent.py
import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini

load_dotenv()

def create_summarizer_agent():
    model = Gemini(
        id="gemini-2.0-flash-exp",
        api_key=os.getenv("GOOGLE_API_KEY")
    )
    return Agent(model=model, description="Summarizes Slack threads.", markdown=True)

def get_summary_prompt(formatted_messages):
    message_count = len(formatted_messages)
    
    # Determine number of sentences based on message count
    if message_count <= 3:
        max_sentences = 1
    elif message_count <= 6:
        max_sentences = 2
    else:
        max_sentences = 3

    formatted = "\n".join(formatted_messages)
    
    return f"""
Summarize the following Slack thread in a way that reflects the tone of the conversation.

Keep the summary natural and human-like — if the conversation is casual, keep the language light; if it's formal, use a professional tone.

Do not include usernames or timestamps. Summarize the thread in approximately {max_sentences} sentences, focusing on key takeaways, decisions, and questions.

Thread:
{formatted}
"""

def summarize_thread(formatted_messages):
    agent = create_summarizer_agent()
    prompt = get_summary_prompt(formatted_messages)
    result = agent.run(prompt)
    return result.content.strip()