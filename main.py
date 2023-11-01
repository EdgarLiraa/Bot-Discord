import discord
import asyncio
from discord.ext import commands
from meu_cog import Greetings

intentss = discord.Intents.default()
intentss.members = True
intentss.message_content = True

bot = commands.Bot(command_prefix='-', intents = intentss, help_command=None)

async def load():
    await bot.add_cog(Greetings(bot))

async def main():
    await load()
    await bot.start("")

asyncio.run(main())