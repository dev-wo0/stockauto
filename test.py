from slacker import Slacker

slack = Slacker('xoxb-1638397409510-1651341107284-U6m83qi0cPGFapdHkbA7fWUv')

# Send a message to #general channel
slack.chat.post_message('#stock', 'Hello fellow slackers!')