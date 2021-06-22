import discord, os, threading
from feed import Feed
from feed_item import FeedItem

channels = [
  "856631760132505604"
]

class Bot(discord.Client):
  async def on_ready(self):
    print("Logged on as {0}!".format(self.user))
    await schedule()

async def schedule():
  await fetch()
  threading.Timer(60, schedule).start()

async def fetch():
  feed = Feed("https://www.omgubuntu.co.uk/feed")
  item = feed.fetch()

  if item != None:
    for id in channels:
      try:
        channel = await client.fetch_channel(id)
        
        embed = discord.Embed()
        embed.title = item.get_title()
        embed.url = item.get_link()
        embed.timestamp = item.get_datetime()
        embed.set_image(url = item.get_image())
        embed.description = item.get_summary()

        await channel.send("<@&856667771446493225>", embed = embed)

      except (discord.HTTPException, discord.NotFound):
        print(f"[ERROR] ({id}): {str(e)}")
      except (discord.Forbidden) as e:
        print(f"[ERROR] ({id}): {str(e)}")
      except (AttributeError) as e:
        print(f"[ERROR] ({id}): {str(e)}")

client = Bot()
client.run(os.environ.get("BOT_TOKEN"))