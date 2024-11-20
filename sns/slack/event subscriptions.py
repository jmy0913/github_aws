import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


SLACK_BOT_TOKEN="xoxb-////"
SLACK_APP_TOKEN = "xapp-////"
SLACK_SIGNING_SECRET="////"

# Install the Slack app and get xoxb- token in advance
app = App(
    token=SLACK_BOT_TOKEN,
    signing_secret=SLACK_SIGNING_SECRET
)

@app.command("/hello-socket-mode")
def hello_command(ack, body):
    user_id = body["user_id"]
    ack(f"Hi, <@{user_id}>!")

@app.event("message")
def event_test(say):
    say("Hi")

@app.event("app_mention")
def event_test(say):
    say("Are you mention me?")


if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()