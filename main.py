import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print("Activated")
    channel = client.get_channel(784519871857033239)
    await channel.send(f'Activated')


@client.command
async def clear(ctx, *, num):
    await ctx.channel.purge(limit=int(num) + 1)


@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason="Just for kicks")
    await ctx.send(f'{member.mention} was kicked.')

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason="idek")
    await ctx.send(f'{member.mention} was banned.')


client.run('Enter API key / token')
