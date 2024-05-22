import discord
import random
import wikipedia

from discord.ext import commands

# Botunuzu oluşturun
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Botun başlatıldığında çalışacak fonksiyon
@bot.event
async def on_ready():
    print(f'{bot.user.name} adlı bot giriş yaptı!')

# Rastgele şaka gönderen komut
@bot.command()
async def saka(ctx):
    sakalar = [
        "Neden kedinin dört ayağı vardır? İki ayağı olursa kedi yürüyemez.",
        "Adamın biri okula gitmiş, okul dağınık mış. Adam düşmüş, düşük mış.",
        "Temel sahilde yürüyormuş neden? Deniz ne demiş?",
        "Hangi dağda çiçek yetişmez? Yanardağ.",
        "Gece tacizcileri hangi saatte saldırıya geçer? İkinci iş çıkışı."
    ]
    saka = random.choice(sakalar)
    await ctx.send(saka)

# Wikipedia'da bir makale arayan komut
@bot.command()
async def wiki(ctx, *, aranan):
    wikipedia.set_lang("tr")
    try:
        arama = wikipedia.page(aranan)
        await ctx.send(f"Wikipedia'da {aranan} için bulduğum ilk paragraf:\n{arama.content.split('.')[0]}")
    except wikipedia.exceptions.DisambiguationError as e:
        await ctx.send(f"Aranan '{aranan}' için birden fazla sonuç bulundu. Lütfen daha spesifik bir arama yapın.")
    except wikipedia.exceptions.PageError:
        await ctx.send(f"Aranan '{aranan}' için Wikipedia'da makale bulunamadı.")

# Bildirim gönderen komutlar
@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel is not None:
        await channel.send(f'Hoş geldin {member.mention}!')

@bot.event
async def on_member_remove(member):
    channel = member.guild.system_channel
    if channel is not None:
        await channel.send(f'Güle güle {member.name}!')

# Botunuzu çalıştırın
bot.run('')
