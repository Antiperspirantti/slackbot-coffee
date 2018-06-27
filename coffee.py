import keyboard

import time

from slackclient import SlackClient

#Replace 'X' with you'r slack token
slack_token = "xxxxxxxxxxxxxxxx"
sc = SlackClient(slack_token)

# Variables used in Slack messages.
channel = "coffee"
icon = ":coffee:"
user = "CoffeeBot"

while True:
        if keyboard.is_pressed('enter'):
                print('Enter key pressed!')
                sc.api_call(
                "chat.postMessage",
                #channel="xxxxxx",
                channel = channel,
                username = user,
                icon_emoji = icon,
                text="A kind person started brewing coffee! Ready in 10 minutes.")

                # Sleep for 10 minutes when the button is pressed.
                time.sleep(600)

                sc.api_call(
                "chat.postMessage",
                #channel="xxxxxx",
                channel = channel,
                username = user,
                icon_emoji = icon,
                text="@channel Fresh coffee ready! :coffee:")