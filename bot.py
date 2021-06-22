import discord, os, json, asyncio
from feed import Feed

guilds = None
with open("guilds.json", 'r') as file:
  guilds = json.load(file)
  file.close()

class Bot(discord.Client):
  async def on_ready(self):
    print(f"[LOG] ({self.user}): Logged in!")
    await schedule()

async def schedule():
  await fetch()
  await asyncio.sleep(60 * 30)
  await schedule()

async def fetch():
  feed = Feed("https://www.omgubuntu.co.uk/feed")
  item = feed.fetch()

  if item != None:
    for guild in guilds['guilds']:
      try:
        channelObj = await client.fetch_channel(guild['channel'])
        guildObj = await client.fetch_guild(guild['id'])

        embed = discord.Embed()
        embed.title = item.get_title()
        embed.url = item.get_link()
        embed.timestamp = item.get_datetime()
        embed.set_image(url = item.get_image())
        embed.description = item.get_summary()

        if guild['role']:
          roles = await guildObj.fetch_roles()
          role = [r for r in roles if r.id == guild['role']]
          
          if len(role): 
            await channelObj.send(role[0].mention, embed = embed)
          else:
            await channelObj.send(embed = embed)
        else:
          await channelObj.send(embed = embed)

        print(f"[LOG] ({guild['channel']}): Successfully sent message.")

      except Exception as e:
        print(f"[ERR] ({guild['channel']}): {e}")
        continue

client = Bot()
client.run(os.environ.get("BOT_TOKEN"))