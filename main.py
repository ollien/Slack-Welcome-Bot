import slackclient
import time
import os

slackClient = slackclient.SlackClient(os.environ["SLACK_TOKEN"])
slackClient.rtm_connect()
slackClient.api_call("channels.join", name="#electrical")
while True:
    for message in slackClient.rtm_read():
        print(message)
        if message["type"] == "team_join":
            username = message["user"]["name"]
            print(username)
            message = "Welcome to the New Ro-Bots Slack, @{}! Please make sure to download this on your phone so we can get your attention! The app is available on both iOS and Android.".format(username)
            slackClient.api_call("chat.postMessage", channel="#general",
                text=message, username="The New Ro-Bot", link_names = True)
    time.sleep(.1)
