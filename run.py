# Credits to iiLeafy for the majority of this project- https://github.com/iiLeafy
# This is very barebones, I will be improving on it in the future
# Any malicious use with this program will not be used against me.
# This is for educational purposes ONLY.

import string
import random
import time
import crayons
from discord_webhook import *

print("{}".format(crayons.red('Any malicious use with this program will not be used against me.')))
print("{}".format(crayons.red('This is for educational purposes ONLY.')))

def send():
    webhook = DiscordWebhook(url='https://discordbhookhere.gl', content="discord.gift/" + code) # Webhook message and message content
    response = webhook.execute()


for x in range(1, 1001):
    code = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
    send() # uses gay send def yes.
    print("Code Sent: " + code + "Code Number: %d" % (x))
    time.sleep(1.65) # waits 1.65 seconds due to ratelimits.

print('\nAll codes have been sent!')