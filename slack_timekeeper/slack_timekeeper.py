# written on python 2.7.11
#
# Time keeping for slack for use in an appathon
#
# slacker: https://github.com/os/slacker
# slack api: https://api.slack.com/methods

import re, time
from slacker import Slacker

# read in the initialization variables
init_vars = {}

with open('ini.txt') as f:
    for L in f:
        if ":" in L:
            key, value = map(str.strip, L.split(" : ", 1))
            init_vars[key] = value
            
print init_vars

SLACK_TOKEN = init_vars.get('auth-token')
WORKSHOP_END = init_vars.get('ws-end-time')
SLACK_CHANNEL = init_vars.get('slack-channel')


slack = Slacker(SLACK_TOKEN)

# keep track of time

# build the message
message = 'This shit is going to end ' + \
            WORKSHOP_END + \
            ' :slightly_smiling_face:'

# Send a message to the SLACK_CHANNEL
slack.chat.post_message(SLACK_CHANNEL,
                        message,
                        username='timekeeper',
                        as_user=False,
                        icon_emoji=':stopwatch:')
