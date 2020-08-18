# Credits to iiLeafy for the majority of this project- https://github.com/iiLeafy
# This is very barebones, I will be improving on it in the future
# Any malicious use with this program will not be used against me.
# This is for educational purposes ONLY.

import string
import random
import time
import crayons
from discord_webhook import *

amount = 0

print("{}".format(crayons.red('Any malicious use with this program will not be used against me.')))
print("{}".format(crayons.red('This is for educational purposes ONLY.')))

amount = input("How many codes would you like to be sent? ")
print("You have chose to send "+ amount +" codes.")

def send():
    webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/745418383025111090/MvH8vMYZ6gweiVZoJmTyDpKJ-9BCR5kkEs4e7S291Ky3N0OyqULGJg8mhesIFZqU2FNT', content="discord.gift/" + code) # Webhook message and message content
    response = webhook.execute()


for x in range(1, int(amount) + 1):
    code = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
    send() # uses gay send def yes.
    print("Code Sent: " + code + "Code Number: %d" % (x))
    time.sleep(1.65) # waits 1.65 seconds due to ratelimits.

print('\nAll codes have been sent!')