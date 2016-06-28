import slackclient
import time
import os

slackClient = slackclient.SlackClient(os.environ["SLACK_TOKEN"])
slackClient.rtm_connect()
lastPingTime = 0
while True:
    for message in slackClient.rtm_read():
        if message["type"] == "team_join":
            username = message["user"]["name"]
            message = "Welcome to the New Ro-Bots Slack, @{}! Please make sure to download this on your phone so we can get your attention! The app is available on both iOS and Android.".format(username)
            slackClient.api_call("chat.postMessage", channel="#general",
                text=message, username="The New Ro-Bot", link_names = True)

    now = time.time()
    if now - lastPingTime >= 3:
        slackClient.server.ping()
        lastPingTime = now

    time.sleep(.1)
