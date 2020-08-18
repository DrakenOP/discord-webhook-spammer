# Discord Webhook Spammer
This is a Discord Webhook spammer written in Python 3.8

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies.

```bash
pip install discord_webhooks
pip install crayons # not necessary
```

## Usage

```python
# This example is a fake Discord Nitro generator
import discord_webhook
import string
import random
import time

def send():
    webhook = DiscordWebhook(url='https://discordbhookhere.gl', content="discord.gift/" + code)
    response = webhook.execute()

for x in range(1, 1001):
    code = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
    send()
    print("Code Sent: " + code + "Code Number: %d" % (x))
    time.sleep(1.65)

print('\nAll codes have been sent!')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## I am not liable for any misuse of this program