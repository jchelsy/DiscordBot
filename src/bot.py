import sys
import discord
from src import settings

# Set to remember if the bot is already running (since on_ready can be called more than once)
this = sys.modules[__name__]
this.running = False


######################################################################

def main():
    # Initialize the client
    print("Starting up...")
    client = discord.Client()

    # Define event handlers for the client
    # on_ready() may be called multiple times
    # (in the event of a reconnect). Hence, the 'running' flag.
    @client.event
    async def on_ready():
        if this.running:
            return

        this.running = True

        # Set the playing status
        if settings.NOW_PLAYING:
            print("Setting 'Now Playing' game...", flush=True)
            await client.change_presence(
                activity=discord.Game(name=settings.NOW_PLAYING))

        print("Logged in!", flush=True)

    # Run the bot
    client.run(settings.BOT_TOKEN)

######################################################################


if __name__ == "__main__":
    main()
