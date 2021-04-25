from slack import WebClient
from slack.errors import SlackApiError


class SlackMessenger:
    def __init__(self, config):
        self.client = WebClient(token=config['slack_api_token'])

    def send_message(self, msg):
        try:
            response = self.client.chat_postMessage(
                channel='#competitive',
                text=msg)
            assert response["message"]["text"] == "Hello world!"
        except SlackApiError as e:
            assert e.response["ok"] is False
            assert e.response["error"]
            print(f"Got an error: {e.response['error']}")