# FredBot
## A Discord Bot to help with general server maintenance.

## Pre-requisites
Python Version
- Python >= 3.8

Libraries
- discord.py
- emoji

# Components

## Basic settings
The following parameters are located in the `settings.py` module:
- **COMMAND_PREFIX**: The prefix used for all commands. It is set to `!` by default, but it can be changed to anything else.
- **BOT_TOKEN**: The private Discord API [token](https://discordapp.com/developers/applications/me) for the Bot.
- **NOW_PLAYING**: The text that the bot displays as its 'now playing' status (to disable, set to `""`, `None`, or `False`).
- **BASE_DIR**: A variable to build relative paths inside the code. It points to the directory where the `settings.py` module is located.

## Additional utilities
The `utils.py` module contains a variety of useful methods.

### `get_rel_path()`
Returns the absolute path of a path relative to the base directory.

Parameters:
- **rel_path**: The relative path.

### `get_emoji()`
`discord.py` does not convert emoji aliases to their corresponding character when sending a message.

Therefore, this method uses the `emoji` library to return an emoji character, given its corresponding alias.

Parameters:
- **emoji_name**: The alias of the emoji to be sent, as defined in Discord (with or without colons).
- **fail_silently**: When `True`, if the emoji is not found, `emoji_name` is returned. Otherwise, (if `False`), `ValueError` will be raised. It defaults to `False`.

Example:
- `get_emoji(":ok_hand:")` returns `👌`.
- `get_emoji("ok_hand")` also returns `👌`.
- `get_emoji(":blabla:")` raises `ValueError`.
- `get_emoji(":blabla:", fail_silently=True)` returns `":blabla:"`.

### `get_channel()`
This method allows for a channel to be identified by one of its attributes.

For example, searching for a channel by name is easier than doing so by its ID.

If the specified channel is not found, `ValueError` is raised.

Parameters:
- **client**: The `discord.py` client of the bot.
- **value**: The desired value for the attribute to search for (e.g. channel name or ID).
- **attribute**: The name of the search attribute (e.g. `"name"` or `"id"`). Any attribute of a [discord.py Channel object](https://discordpy.readthedocs.io/en/latest/api.html#channel) can be used. It defaults to `"name"`.

### `send_in_channel()`
This method is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).

It quickly sends a message in a channel with a particular name.

Any positional arguments that would normally be passed to `client.send_message()` can be passed to it.

Since it utilizes `get_channel()`, it will raise `ValueError` if no such channel can be found.

Parameters:
- **client**: The `discord.py` client of the bot.
- **channel_name**: The name of the channel to send a message in.
- **\*args**: Any other positional arguments to pass to `client.send_message()`.

### `try_upload_file()`
This method is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).

It allows for a file to be uploaded into a particular channel with a single line of code. Upon failure, an error message is sent.

Parameters:
- **client**: The `discord.py` client of the bot.
- **channel**: The  `discord.py` [Channel object](https://discordpy.readthedocs.io/en/latest/api.html#channel) to send the file into.
- **file_path**: The absolute path of the file to be sent.
- **content**: The additional message string to send alongside the file. It defaults to `None`.
- **delete_after_send**: Whether or not to delete the file specified in `file_path` after it is sent. It will be deleted even if the file is not successfully sent. It defaults to `False`.
- **retries**: The number of times to retry sending the file if an error is encountered, before giving up and sending an error message. It defaults to `3`.

## Sensitive information
Any sensitive information is stored in the `secrets.py` module, which is located in the base directory.

This module is excluded from the repository, and must be added manually.
- **BOT_TOKEN**: imported into the `settings.py` module.

#### `BASE_DIR/secrets.py`
```python
BOT_TOKEN: ""
```
