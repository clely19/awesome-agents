# agents/thread_fetcher_agent.py
from slack_sdk import WebClient

class ThreadFetcher:
    def __init__(self, slack_token):
        self.client = WebClient(token=slack_token)

    def get_thread_replies(self, channel_id: str, thread_ts: str) -> dict:
        try:
            res = self.client.conversations_replies(channel=channel_id, ts=thread_ts)
            return {
                "thread_id": thread_ts,
                "messages": [{"user": m["user"], "text": m["text"], "ts": m["ts"]} for m in res["messages"]]
            }
        except Exception as e:
            return {"error": str(e)}

    def get_user_display_name(self, user_id):
        try:
            res = self.client.users_info(user=user_id)
            return res["user"]["real_name"] or res["user"]["name"]
        except Exception:
            return "Unknown User"