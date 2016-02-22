# test of slacker Python-Slack integration
# slacker: https://github.com/os/slacker
# slack api: https://api.slack.com/methods

from slacker import Slacker

slack = Slacker('xoxp-2153792019-8313249396-20534467781-31e3a14fe0')

# Send a message to #[channel/group]
slack.chat.post_message('#kks-python-test', 'test post', username='appathon bot', as_user=False)

# Set the purpose to a group
#slack.groups.set_purpose("#kks-python-test", "test purpose")


# Get users list
#response = slack.users.list()
#users = response.body['members']

#for user in users:
#    print user
