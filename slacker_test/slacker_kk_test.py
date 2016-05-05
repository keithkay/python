#! usr/bin/env python3
# 
# test of slacker Python-Slack integration
# slacker: https://github.com/os/slacker
# slack api: https://api.slack.com/methods

from slacker import Slacker

slack = Slacker('token')

# Send a message to #[channel/group]
slack.chat.post_message('#kks-python-test',
                        'test post:slightly_smiling_face:',
                        username='timekeeper',
                        as_user=False,
                        icon_emoji=':stopwatch:')

slack.chat.post_message('#kks-python-test',
                        '/topic test setting topic',
                        username='timekeeper',
                        as_user=False,
                        icon_emoji=':stopwatch:')

# Set the purpose to a group
#slack.groups.set_purpose("#kks-python-test", "test purpose")


# Get users list
#response = slack.users.list()
#users = response.body['members']

#for user in users:
#    print user
