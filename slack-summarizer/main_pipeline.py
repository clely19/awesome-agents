# main_pipeline.py
import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from agents.summarizer_agent import summarize_thread
from agents.thread_fetcher_agent import ThreadFetcher

load_dotenv()
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")

# Initialize the app and thread fetcher
app = App(token=SLACK_BOT_TOKEN)
thread_fetcher = ThreadFetcher(SLACK_BOT_TOKEN)

@app.event("app_mention")
def handle_app_mention(body, say):
    text = body["event"].get("text", "")
    channel = body["event"].get("channel")
    thread_ts = body["event"].get("thread_ts") or body["event"].get("ts")

    if "summary" in text.lower():
        print(" Summary trigger detected")
        thread = thread_fetcher.get_thread_replies(channel, thread_ts)

        if "error" in thread:
            say(text=" Could not fetch thread.", thread_ts=thread_ts)
            return

        formatted_messages = [
            f'{thread_fetcher.get_user_display_name(m["user"])}: {m["text"]}' 
            for m in thread["messages"]
        ]

        summary = summarize_thread(formatted_messages)
        say(
            text=f"*Summary:*\n{summary}",
            thread_ts=thread_ts
        )

if __name__ == "__main__":
    print(" Running summarizer with Socket Mode...")
    SocketModeHandler(app, SLACK_APP_TOKEN).start()