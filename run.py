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
print("{}".format(crayons.red('This is for educational purposes ONLY.\n')))

def send():
    webhook = DiscordWebhook(url=webhookurl, content="discord.gift/" + code) # Webhook url and message content
    response = webhook.execute()

# SETTINGS
webhookurl = 'Your webhook here!'

changewh = input("Do you want to change the web hook url, say Y if you haven't changed it in the file else say N. (Y/N) > ")
if changewh == "y":
    webhookurl = input("You have chosen to change the web hook url, paste it here and press enter. > ")

amount = 0
amount = input("How many codes would you like to be sent? ")
print("You have chose to send "+ amount +" codes.")


for x in range(1, int(amount) + 1):
    code = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
    send() # uses gay send def yes.
    print("Code Sent: " + code + "Code Number: %d" % (x))
    time.sleep(1.65) # waits 1.65 seconds due to ratelimits.

print('\nAll codes have been sent!')
time.sleep(5)
