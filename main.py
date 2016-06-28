import slackclient
import time
import os

slackClient = slackclient.SlackClient(os.environ["SLACK_TOKEN"])
slackClient.rtm_connect()

while True:
    print(slackClient.rtm_read())
    time.sleep(5)
