import os

from flask import Flask, request

from slack_bolt import App, Say, Ack
from slack_bolt.adapter.flask import SlackRequestHandler

from dotenv import load_dotenv

from pprint import pprint

load_dotenv()
app = Flask(__name__)
token = os.environ.get('CLIENT_TOKEN')
bolt_app = App(token=token, signing_secret=os.environ.get('SIGNING_SECRET'))

handler = SlackRequestHandler(bolt_app)

@app.route('/slack/events', methods=['POST'])
def handle_events():
        return handler.handle(request)

@bolt_app.command('/anon')
def anon(ack, respond, command):
    ack()
    respond(f'{command["text"]}', response_type='in_channel')

if __name__ == '__main__':
    app.run(threaded=True, port=5000)

