import discord

from discord.ext import commands

bot = commands.bot(command_prefix='!', self_bot=True)

@bot.command()

async def test(ctx):

  await ctx.send('$delete')

TOKEN = 'ODUyODEyNTIzOTk2ODM5OTc2.GuT-hp.cOFuE3Oqc6Wt3GsoFd-15LiZ-d6K-gXL70Kv_0'

bot.run(TOKEN)

