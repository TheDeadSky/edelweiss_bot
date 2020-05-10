import youtube_dl
import discord
from discord.ext import commands
import time, os

MAIN_ROLES = ["Dude3", "Dude2", "Magic Dude", "Dude Founder"]
YTDL_OPTS = {
    'format': 'bestaudio/best'
}
bot = commands.Bot(command_prefix='/')


@bot.command()
async def bc(ctx):
    roles = [x for x in ctx.guild.roles if x.name in MAIN_ROLES]

    await ctx.send(" ".join([x.mention for x in roles]))

@bot.command()
async def ruhelp(ctx, cmd = ''):
    author = ctx.message.author

    if cmd in [x.name for x in bot.commands if x.name != 'help']:
        help_msg = open(f"help/{cmd}.txt", encoding='utf-8').read()
    elif cmd != None and cmd != '':
        help_msg = u"Извините, такой команды нет в моих банках памяти." 
    else:
        help_msg = f"Приветствую, {author.mention}\n\n" + open("help/help.txt", encoding='utf-8').read()

    await ctx.send(help_msg)

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@bot.command()
async def play(ctx, url):
    voice_client = bot.voice_clients[0]
    
    ytdl = youtube_dl.YoutubeDL(YTDL_OPTS)
    info = ytdl.extract_info(url, download=False)
    
    asrc = discord.FFmpegOpusAudio(info['formats'][0]['url'])

    voice_client.play(asrc)


# @bot.command()
# async def playfile(ctx, url):
#     voice_client = bot.voice_clients[0]
    
#     #ytdl = youtube_dl.YoutubeDL(YTDL_OPTS)
#     #info = ytdl.extract_info(url, download=False)
    
#     asrc = discord.FFmpegPCMAudio(url)

#     voice_client.play(asrc)

@bot.command()
async def stop(ctx):
    voice_client = bot.voice_clients[0]
    voice_client.stop()

TOKEN = os.environ.get("BOT_TOKEN")
bot.run(str(TOKEN))
