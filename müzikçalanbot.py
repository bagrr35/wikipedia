import discord
from discord.ext import commands
import youtube_dl

# Botunuzu oluşturun
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# YouTube Downloader ayarları
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

# Botun başlatıldığında çalışacak fonksiyon
@bot.event
async def on_ready():
    print(f'{bot.user.name} adlı bot giriş yaptı!')

# Müzik çalma komutu
@bot.command()
async def play(ctx, url):
    voice_channel = ctx.author.voice.channel
    if voice_channel is None:
        await ctx.send("Lütfen bir ses kanalına katılın.")
        return
    try:
        await voice_channel.connect()
    except discord.errors.ClientException:
        pass

    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        voice_client.play(discord.FFmpegPCMAudio(url2))

# Botunuzu çalıştırın
bot.run('')
