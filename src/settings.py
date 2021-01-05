import os
from src import secrets

# The prefix that will be used to parse commands.
COMMAND_PREFIX = "!"

# The bot token. Located in the 'secrets.py' module.
BOT_TOKEN = secrets.BOT_TOKEN

# The 'now playing' message (None to disable).
NOW_PLAYING = COMMAND_PREFIX + "help"

# Base directory.
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
