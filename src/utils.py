import os
from discord import HTTPException
from emoji import emojize
from src import settings


# Returns a path relative to the base directory
def get_rel_path(rel_path):
    return os.path.join(settings.BASE_DIR, rel_path)


# Returns an emoji to send in a message.
# The emoji alias can be passed with or without colons.
# If the emoji is not found, an exception will be returned.
# If fail_silently is True, the alias input will be returned, instead of an exception.
def get_emoji(emoji_name: str, fail_silently=False):
    # Ensure the emoji alias is in ":alias:" format
    alias = emoji_name if emoji_name[0] == emoji_name[-1] == ":" \
        else f":{emoji_name}:"
    the_emoji = emojize(alias, use_aliases=True)

    if the_emoji == alias and not fail_silently:
        raise ValueError(f"Emoji {alias} not found!")

    return the_emoji


# A shortcut to retrieve a Channel object with a particular attribute.
# By default, the channel name attribute is used.
# If multiple matching channels are found, the first one is returned.
def get_channel(client, value, attribute="name"):
    channel = next((c for c in client.get_all_channels()
                    if getattr(c, attribute).lower() == value.lower()), None)
    if not channel:
        raise ValueError("No such channel was found.")
    return channel


# A shortcut to send a message in a channel with a particular name.
# Additional positional arguments can be passed to send_message().
# Utilizes get_channel(), so it should be ensured that the bot only has access to a single channel by the given name.
async def send_in_channel(client, channel_name, *args):
    await client.send_message(get_channel(client, channel_name), *args)


# Attempts to upload a file to a particular channel.
# The 'content' parameter refers to the additional text that can be sent alongside the file.
# The 'delete_after_send' parameter can be set to True to delete the file afterwards.
async def try_upload_file(client, channel, file_path, content=None, delete_after_send=False, retries=3):
    used_retries = 0
    sent_msg = None

    while not sent_msg and used_retries < retries:
        try:
            sent_msg = await client.send_file(channel, file_path, content=content)
        except HTTPException:
            used_retries += 1

    if delete_after_send:
        os.remove(file_path)

    if not sent_msg:
        await client.send_message(channel, "Oops! Something went wrong. Please try again.")

    return sent_msg
