import asyncio

import datetime
import random

import discord
from discord import *
from discord.ext import commands

from discord_components import *

class Reactions(commands.Cog):

  def __init__(self, client):
    self.client = client

  #Парные реакции

  @commands.command()
  async def hug(self, ctx, member: discord.Member=None):
      gif = '''https://media.discordapp.net/attachments/668413046263250954/668425070041104394/image0.gif
      https://images-ext-2.discordapp.net/external/iYOTMwzM8SAFzhx4JoSFGRpSdSN75hF3454lyxc-wOw/https/cdn.weeb.sh/images/r1kC_dQPW.gif
      https://images-ext-1.discordapp.net/external/6nMBcWvxNn18TeWxxRK9v2ncDAJYRfKuhj47kMXhVuk/https/media.discordapp.net/attachments/697193976070930483/722084527975038996/image0.gif
      https://media.discordapp.net/attachments/668413046263250954/668425074927206410/image8.gif
      https://media.discordapp.net/attachments/722028202796777543/722141204036190278/image0.gif
      https://media.discordapp.net/attachments/722028202796777543/722141167533424660/image7.gif
      https://images-ext-1.discordapp.net/external/Ny2AMYgqsfPDd6LNWhzjhKITZK-8X0fX4r8hsxseKas/%3Fwidth%3D400%26height%3D210/https/images-ext-2.discordapp.net/external/t6cQwA4qveJLrr88EqzsPkTFLaJ1OGLIWAgnYb4yqgw/https/cdn.zerotwo.dev/HUG/d856f3fe-f220-41b6-b3c2-f0a2d956dd8a.gif
      https://images-ext-2.discordapp.net/external/XhFTQr-8ZCHD5xTHENZJVF7bVKQqaKoQnSleNnFoipw/%3Fwidth%3D384%26height%3D216/https/images-ext-2.discordapp.net/external/4dHLtCsOZq-rJoBAIhQwCTD5-MwyFV8dGzxq2tBJFnk/https/cdn.zerotwo.dev/HUG/fb248ca7-9e33-45e0-8b0a-c2d338eee707.gif
      https://images-ext-2.discordapp.net/external/__4EbiDsWB6pdMRMSsfxyAD3867fQU__XTb-arQ_VOQ/%3Fwidth%3D560%26height%3D315/https/images-ext-2.discordapp.net/external/PjmWjqSRHgZhHmw3g31TAuMeImYJwP8y1eYINZ-Oy9o/https/cdn.zerotwo.dev/HUG/f7d2556f-d556-4963-96d7-beeb308df970.gif
      https://media.discordapp.net/attachments/598817702383058944/598820602635091978/image2.gif
      https://media.discordapp.net/attachments/722028202796777543/722141810041946142/image1.gif
      '''
      if member == ctx.author:
          e = discord.Embed(title='Реакция: обнимашки', description=f'{ctx.author.mention} **обнимает себя**', color=0x2f3136)
          e.timestamp = datetime.datetime.utcnow()
          e.set_image(url=random.choice(gif.split("\n")))
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      if member == None:
          e = discord.Embed(title='Реакция: обнимашки', description=f'{ctx.author.mention} **обнимает всех**', color=0x2f3136)
          e.timestamp = datetime.datetime.utcnow()
          e.set_image(url=random.choice(gif.split("\n")))
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      else:
          e = discord.Embed(title='Реакция: обнимашки', description=f'{ctx.author.mention} **обнимает** {member.mention}', color=0x2f3136)
          e.timestamp = datetime.datetime.utcnow()
          e.set_image(url=random.choice(gif.split("\n")))
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          await ctx.send(embed=e)

  @commands.command()
  async def kiss(self, ctx, member: discord.Member=None):
      gif = '''https://images-ext-1.discordapp.net/external/TrIvQBPSADYWzwwhYdTae9mOOaNk3Pr29wL-oodAUa0/https/uploads.disquscdn.com/images/964bd0189d1674220997816c271470bf5f2c32860ee5bcf63d50031fbc82a0cd.gif
          https://media.discordapp.net/attachments/722028202796777543/722141266112020581/image1.gif
          https://media.discordapp.net/attachments/722028202796777543/722141268339064943/image6.gif
          https://images-ext-2.discordapp.net/external/YGeB_XtkuyD5tvCFbC59tKUstyDW59xQMIXaoQcrQS4/https/media.giphy.com/media/w62BhkdkxaCwE/giphy.gif
          https://media.discordapp.net/attachments/722028202796777543/722203507326713876/anime-kissin-8.gif
          https://media.discordapp.net/attachments/685868085588000805/685890000411557908/giphy_7.gif
          https://media.discordapp.net/attachments/722028202796777543/722141267848593448/image5.gif
          https://images-ext-1.discordapp.net/external/TrIvQBPSADYWzwwhYdTae9mOOaNk3Pr29wL-oodAUa0/https/uploads.disquscdn.com/images/964bd0189d1674220997816c271470bf5f2c32860ee5bcf63d50031fbc82a0cd.gif'''
      if member == ctx.author:
          e = discord.Embed(title='Реакция: поцелуйчик', description=f'{ctx.author.mention} **целует себя**', color=0x2f3136)
          e.timestamp = datetime.datetime.utcnow()
          e.set_image(url=random.choice(gif.split("\n")))
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      if member == None:
          e = discord.Embed(title='Реакция: поцелуйчик', description=f'{ctx.author.mention} **целует всех**', color=0x2f3136)
          e.timestamp = datetime.datetime.utcnow()
          e.set_image(url=random.choice(gif.split("\n")))
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      else:
          e = discord.Embed(title='Реакция: поцелуйчик', description=f'{member.mention}, вас хочет поцеловать {ctx.author.mention}. Что скажешь?', color=0x2f3136)
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          msg = await ctx.send(embed=e, components=[
              [
                  Button(label="Да", style=ButtonStyle.green),
                  Button(label="Нет", style=ButtonStyle.red)
              ]
          ])
          try:
              respone = await self.client.wait_for('button_click', timeout=30.0, check=lambda inter: inter.author.id == member.id)
              if respone.component.label == "Да":
                  e = discord.Embed(title='Реакция: поцелуйчик', description=f'{ctx.author.mention} **целует** {member.mention}', color=0x2f3136)
                  e.set_image(url=random.choice(gif.split("\n")))
                  e.timestamp = datetime.datetime.utcnow()
                  e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
                  await msg.edit(embed=e, components=[])
              if respone.component.label == "Нет":
                  e = discord.Embed(description=f'{ctx.author.mention}, вам отказали в поцелуйчике', color=0x2f3136)
                  e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
                  e.timestamp = datetime.datetime.utcnow()
                  await msg.edit(embed=e, components=[])

          except asyncio.TimeoutError:
              e = discord.Embed(description=f'{ctx.author.mention}, вам отказали в поцелуйчике', color=0x2f3136)
              e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
              e.timestamp = datetime.datetime.utcnow()
              await msg.edit(embed=e, components=[])

  @commands.command()
  async def bite(self, ctx, member: discord.Member=None):
      gif = '''https://media.discordapp.net/attachments/668413046263250954/668428870159958026/image0.gif
      https://media.discordapp.net/attachments/668413046263250954/668435026693718016/image1.gif
      https://images-ext-2.discordapp.net/external/_TfW8mZ6Jd3RH5IFRyanMClUL7YQ4U4eDqRFbCCZSeE/https/cdn.weeb.sh/images/HkutgeXob.gif
      https://media.discordapp.net/attachments/599641421472989190/599641468805840896/7b83c1b97c254cb8684e524adc638f9d8cfef3d5_hq.gif
      https://images-ext-1.discordapp.net/external/kDdKMawS8zwlqH31UZ3HyDH20yszXjYbaSqXvbfZNyE/https/images-ext-2.discordapp.net/external/ku7IMRa4mxqzQnmOMzGg4LFoFJ3EJlsNJvs1h425Afk/https/i.imgur.com/FPLaoam.gif'''
      if member == ctx.author:
          e = discord.Embed(title='Реакция: укус', description=f'{ctx.author.mention} **кусает себя**', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      if member == None:
          e = discord.Embed(title='Реакция: укус', description=f'{ctx.author.mention} **кусает всех**', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      else:
          e = discord.Embed(title='Реакция: укус', description=f'{ctx.author.mention} **кусает** {member.mention}', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          await ctx.send(embed=e)

  @commands.command()
  async def punch(self, ctx, member: discord.Member=None):
      gif = '''https://images-ext-1.discordapp.net/external/bRAQTSbWpS1ov6SicjJPxQjwJY6aTWim8d-JzuQ0_Ho/https/cdn.weeb.sh/images/S1yhZ8vuW.gif
      https://images-ext-1.discordapp.net/external/RkuVbGqqfdQnvvz5G6kccEkN3qQkWStkPDU8ghc1GL8/https/cdn.weeb.sh/images/H16aQJFvb.gif
      https://images-ext-2.discordapp.net/external/Li21rRdcGYkdtMIZzinOtvEXi9pTigNGHo5vZBDGHvw/%3Fitemid%3D8208759/https/media1.tenor.com/images/fb3e0b0f18188450bfded4a585de2b90/tenor.gif
      https://images-ext-2.discordapp.net/external/YCQ0rcC7kOPqFg6qmV9ouUjkD1Tc4JA02TTYv_O5g8Y/https/cdn.weeb.sh/images/Bk_oZUP_-.gif
      https://media.discordapp.net/attachments/686928099266265185/686995498657120270/Zayne_kickgif4.gif
      https://images-ext-1.discordapp.net/external/BEWTezzKyvjq_q8I6PCRpeBqq0HeZLK7fK_-SYjn2JQ/https/cdn.weeb.sh/images/ByIcZUPuZ.gif
      https://media.discordapp.net/attachments/599642600974319626/599643462630899722/OK6W_koKDTOqqqLDbIoPAhZR_h2JT0JePTKGFxyBArQ.gif'''
      if member == ctx.author:
          e = discord.Embed(title='Реакция: удар', description=f'{ctx.author.mention} **ударяет себя**', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      if member == None:
          e = discord.Embed(title='Реакция: удар', description=f'{ctx.author.mention} **ударяет всех**', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      else:
          e = discord.Embed(title='Реакция: удар', description=f'{ctx.author.mention} **ударяет** {member.mention}', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          await ctx.send(embed=e)

  @commands.command()
  async def pat(self, ctx, member: discord.Member=None):
      gif = '''https://media.discordapp.net/attachments/598817702383058944/598820228792713216/image2.gif
      https://images-ext-2.discordapp.net/external/g-wa_0tWijFjWlRC1aKm8sUxEo1EjP98cqzvvkyywos/https/cdn.weeb.sh/images/rkSN7g91M.gif
      https://media.discordapp.net/attachments/722028202796777543/722141813179416726/image9.gif
      https://media.discordapp.net/attachments/722028202796777543/722142384204283924/image3.gif
      https://images-ext-2.discordapp.net/external/HzsTrMFk29JcFITmJ0kWGh6TPUzF_L9eQ-SfGt54Cdk/https/cdn.weeb.sh/images/S1ja11KD-.gif
      https://images-ext-1.discordapp.net/external/yOicyNxjyB_y1Cf3hCgsePnL36oofd1qjsyFRjDWOzc/https/cdn.weeb.sh/images/SyFmqkFwW.gif
      https://images-ext-1.discordapp.net/external/RoXxD6xUGyWBM82Zkmc0o9IvmpZtppWwnAxO-G1WE3A/https/cdn.weeb.sh/images/rytzGAE0W.gif
      https://images-ext-2.discordapp.net/external/sGtTrJFXlehqXALALIM0pSRHQeRm35R7uoCmN5yknyU/https/media.tenor.co/images/f2c39ffd995ccd0f126df346d57d832e/tenor.gif'''
      if member == ctx.author:
          e = discord.Embed(title='Реакция: погладить', description=f'{ctx.author.mention} **гладит себя**', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      if member == None:
          e = discord.Embed(title='Реакция: погладить', description=f'{ctx.author.mention} **гладит всех**', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      else:
          e = discord.Embed(title='Реакция: погладить', description=f'{ctx.author.mention} **гладит** {member.mention}', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          await ctx.send(embed=e)

  @commands.command()
  async def love(self, ctx, member: discord.Member=None):
      gif = '''https://media.discordapp.net/attachments/776740212151287819/776812800034078777/image0.gif
      https://media.discordapp.net/attachments/776740212151287819/776811665798332426/image0.gif
      https://images-ext-2.discordapp.net/external/mDPXZL3Bo8ainBbNUvdHOVr4CHzE9IKLMzLbM9GIC1Y/https/i.pinimg.com/originals/07/a7/b2/07a7b2cbd3d9b084fdbbb773acfe4c5b.gif
      https://images-ext-1.discordapp.net/external/6liJfW5dFdC27dafvDkiIlUzchuSYnySS4sFfYl_bTw/https/i.pinimg.com/originals/78/99/32/78993211c012ac81720838b106e69ecd.gif
      https://images-ext-1.discordapp.net/external/HTVHvP0uPosEvJu6G9Qmx6Xlu49bn-lw6eyF0xmBEdM/https/i.pinimg.com/originals/bb/df/a3/bbdfa3edc21e1de194952a5c3ac6bd80.gif
      https://images-ext-1.discordapp.net/external/jJNEU3lv4oxLYiq5KjnDivpnN6ZDuADo4XMobtjo0O4/https/i.pinimg.com/originals/f9/07/c4/f907c4f26260f500c7ca11ae3bcf9bc0.gif
      https://media.discordapp.net/attachments/726198089328754738/813288898917826570/0738221a0721cd969a0ade60865fed80.gif'''
      if member == ctx.author:
          e = discord.Embed(title='Реакция: любовь', description=f'{ctx.author.mention} **любит себя**', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      if member == None:
          e = discord.Embed(title='Реакция: любовь', description=f'{ctx.author.mention} **любит всех**', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      else:
          e = discord.Embed(title='Реакция: любовь', description=f'{ctx.author.mention} **любит** {member.mention}', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          await ctx.send(embed=e)

  @commands.command()
  async def lick(self, ctx, member: discord.Member=None):
      gif = '''https://images-ext-2.discordapp.net/external/EWiWNWlRxXpK4c98xW9VxZyh6KfO4DUIFnuOMf7NpCQ/https/cdn.weeb.sh/images/rJ6hrQr6-.gif
      https://media.discordapp.net/attachments/722028202796777543/722204696235999388/1428932856_etotama-episode1-omake-3.gif
      https://media.discordapp.net/attachments/599641716491812893/599641763401039872/198881.gif
      https://images-ext-1.discordapp.net/external/r8JiD5lRAfxjdcNRHBqfjJw3dU31fkFGOnIrBwe94Fg/https/cdn.weeb.sh/images/ryGpGsnAZ.gif'''
      if member == ctx.author:
          e = discord.Embed(title='Реакция: лизнуть', description=f'{ctx.author.mention} **лижет себя**', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      if member == None:
          e = discord.Embed(title='Реакция: лизнуть', description=f'{ctx.author.mention} **лижет всех**', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      else:
          e = discord.Embed(title='Реакция: лизнуть', description=f'{ctx.author.mention} **лижет** {member.mention}', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          await ctx.send(embed=e)

  @commands.command()
  async def slap(self, ctx, member: discord.Member=None):
      gif = '''https://media.discordapp.net/attachments/722028202796777543/724028977177559040/image2.gif
      https://media.discordapp.net/attachments/686928201837969408/700038578910003298/K02.gif
      https://media.discordapp.net/attachments/686928201837969408/700038609138614453/UwmX.gif
      https://media.discordapp.net/attachments/686928201837969408/700038544395337778/73e.gif
      '''
      if member == ctx.author:
          e = discord.Embed(title='Реакция: дать лапаса', description=f'{ctx.author.mention} **бьёт себя**', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      if member == None:
          e = discord.Embed(title='Реакция: дать лапаса', description=f'{ctx.author.mention} **бьёт всех**', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      else:
          e = discord.Embed(title='Реакция: дать лапаса', description=f'{ctx.author.mention} **ебашит** {member.mention}', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          await ctx.send(embed=e)

  #Соло реакции

  @commands.command()
  async def cry(self, ctx, member: discord.Member=None):
      gif = '''https://media.discordapp.net/attachments/722028202796777543/724005388671909908/image0.gif
      https://media.discordapp.net/attachments/599646144515145778/600304602440663040/8735dd671fd1dc6514b58815f616e4b1ef20a666r1-540-304_hq.gif
      https://media.discordapp.net/attachments/722028202796777543/722141265570824273/image0.gif
      https://media.discordapp.net/attachments/599646144515145778/600304555061673993/e9706f956fabb465dd838967df57c2bd2bfe576er1-640-364_hq.gif
      https://media.discordapp.net/attachments/722028202796777543/722141208213848095/image8.gif
      https://images-ext-1.discordapp.net/external/oF67Cckx7VfXJb2lwP60XU1VjlbsMQ9aA6C97jBqX0I/https/cdn.weeb.sh/images/Hy4QmU7PZ.gif'''
      if member == ctx.author:
          e = discord.Embed(title='Реакция: плакать', description=f'{ctx.author.mention} **забился в себе**', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      if member == None:
          e = discord.Embed(title='Реакция: плакать', description=f'{ctx.author.mention} **плачет**', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      else:
          e = discord.Embed(title='Реакция: плакать', description=f'{ctx.author.mention} **плачет из-за** {member.mention}', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          await ctx.send(embed=e)

  @commands.command()
  async def sad(self, ctx, member: discord.Member=None):
      gif = '''https://media.discordapp.net/attachments/599644595135184896/600305533907369994/original.gif
      https://media.discordapp.net/attachments/668413046263250954/668544582379634688/image2.gif
      https://media.discordapp.net/attachments/599644595135184896/600445679973957642/69c634002f6a7e0a1d634cff0a753139a5bc096a_hq.gif
      https://media.discordapp.net/attachments/700040933588205579/700065799712407612/2019-05-19-15-09-03-1.gif
      https://media.discordapp.net/attachments/668413046263250954/668544070825672744/image1.gif
      https://media.discordapp.net/attachments/668413046263250954/668544070380945418/image0.gif
      '''
      if member == ctx.author:
          e = discord.Embed(title='Реакция: грусть', description=f'{ctx.author.mention} **забился в себе**', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      if member == None:
          e = discord.Embed(title='Реакция: грусть', description=f'{ctx.author.mention} **грустит**', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      else:
          e = discord.Embed(title='Реакция: грусть', description=f'{ctx.author.mention} **грустит из-за** {member.mention}', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          await ctx.send(embed=e)

  @commands.command()
  async def tea(self, ctx, member: discord.Member=None):
      gif = '''https://media.discordapp.net/attachments/686929201563303947/700044339950387210/6ce7c40dcaa6e1882d67d429b24f809c870d0e9br1-480-270_hq.gif
      https://media.discordapp.net/attachments/722028202796777543/722204314919239730/K1nG.gif
      https://media.discordapp.net/attachments/686929201563303947/700044300855148586/2ZzU.gif
      https://media.discordapp.net/attachments/686929201563303947/700044385726759015/decd7e3b56ec436bf57b02d0e2325ba6da1bad69r1-480-236_hq.gif
      https://media.discordapp.net/attachments/686929201563303947/700044456300249188/original_1.gif
      https://media.discordapp.net/attachments/686929201563303947/700044300855148586/2ZzU.gif'''
      if member == None:
          e = discord.Embed(title='Реакция: чаепитие', description=f'{ctx.author.mention} **наслаждается чаем**', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      else:
          e = discord.Embed(title='Реакция: чаепитие', description=f'{ctx.author.mention} **наслаждается чаем c** {member.mention}', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)

  @commands.command()
  async def snow(self, ctx, member: discord.Member=None):
      gif = '''https://images-ext-2.discordapp.net/external/E4mzQFlndDl8Vd27tPdjJcMPKBoeWxQjE-VojCHB9pI/https/media.discordapp.net/attachments/786908599045062666/807982731623137330/snow2.gif
      https://images-ext-1.discordapp.net/external/uGDwPShHIk42OJ9XY7gVucYyDSca4aLLcVtCRRUeJlg/https/media.discordapp.net/attachments/786908599045062666/807982735770779688/snow3.gif
      https://images-ext-1.discordapp.net/external/HX44GJ8sgMEuUQZ6mvJmzhMkgQjfZaxPNofFu_sGf-Q/https/media.discordapp.net/attachments/786908599045062666/807981468293922866/snow.gif
      https://images-ext-2.discordapp.net/external/79U6nUqNXZdd8fScMBprPy7CxA9JBdv4CI7T9Q2TD9U/https/media.discordapp.net/attachments/786908599045062666/807982733745061908/snow4.gif'''
      if member == None:
          e = discord.Embed(title='Реакция: снег', description=f'{ctx.author.mention} **смотрит на снег**', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      else:
          e = discord.Embed(title='Реакция: снег', description=f'{ctx.author.mention} **смотрит на снег c** {member.mention}', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)

  @commands.command()
  async def rain(self, ctx, member: discord.Member = None):
      gif = '''https://media.discordapp.net/attachments/726198089328754738/813290494452826112/d9e93f5ce187a25330775a0ba5aaf006.gif
      https://images-ext-1.discordapp.net/external/LUV8LAJFPV5JdzItuIKGnlKZ5sZ4wNBo8eYL_Gq3bdQ/https/i.pinimg.com/originals/65/29/c3/6529c3147d4e79e3722bf3c600f591ae.gif'''
      if member == None:
          e = discord.Embed(title='Реакция: дождь', description=f'{ctx.author.mention} **смотрит на дождь**', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      else:
          e = discord.Embed(title='Реакция: дождь', description=f'{ctx.author.mention} **смотрит на дождь c** {member.mention}', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)

  @commands.command()
  async def eat(self, ctx, member: discord.Member=None):
      gif = '''https://media.discordapp.net/attachments/700045908838187189/700046663863107634/5LYzTBVoS196gvYvw3zjwH23YP0vJ_aOPYGin-zQlaU.gif
      https://media.discordapp.net/attachments/722028202796777543/722141206137667644/image4.gif
      https://media.discordapp.net/attachments/700045908838187189/700046740778123378/OilyBeneficialFrigatebird-small.gif
      https://media.discordapp.net/attachments/700045908838187189/700046787322576936/orig_4.gif
      https://media.discordapp.net/attachments/722028202796777543/722175828271562792/1AF0.gif
      '''
      if member == None:
          e = discord.Embed(title='Реакция: кушать', description=f'{ctx.author.mention} **кушает**', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      else:
          e = discord.Embed(title='Реакция: кушать', description=f'{ctx.author.mention} **кушает** {member.mention}', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)

  @commands.command()
  async def dance(self, ctx, member: discord.Member=None):
      gif = '''https://media.discordapp.net/attachments/686929150837129245/700045628570599645/orig_3.gif
      https://media.discordapp.net/attachments/686929150837129245/700045634136440883/orig_2.gif
      https://media.discordapp.net/attachments/686929150837129245/700045688062345296/v77E7D-l5jQ69A_WX5nal_S-XzPy6VLH56E0YyWbskDAz7yWlGHrTND5UYMSXKBQd21ybuQh3v_-D6KZ7V0Cb09LRJVwphJUBvpx.gif?width=1202&height=676
      https://media.discordapp.net/attachments/686929150837129245/700045775081701568/tenor.gif
      https://images-ext-1.discordapp.net/external/8TxxOFspHbXkEeVzjf78HnivHzMC0KqhVAxT5pIIp6s/https/media.discordapp.net/attachments/686929150837129245/700045748783546389/orig.gif
      '''
      if member == None:
          e = discord.Embed(title='Реакция: танцы', description=f'{ctx.author.mention} **танцует**', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      else:
          e = discord.Embed(title='Реакция: танцы', description=f'{ctx.author.mention} **танцует с** {member.mention}', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)

  @commands.command()
  async def smoke(self, ctx, member: discord.Member=None):
      gif = '''https://media.discordapp.net/attachments/668413046263250954/668530195799605250/image5.gif
      https://media.discordapp.net/attachments/668413046263250954/668530194914476062/image4.gif
      https://media.discordapp.net/attachments/661896698926333952/668528160048152616/image0_1.gif'''
      if member == None:
          e = discord.Embed(title='Реакция: курение', description=f'{ctx.author.mention} **курит**', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      else:
          e = discord.Embed(title='Реакция: танцы', description=f'{ctx.author.mention} **курит с** {member.mention}', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)

  @commands.command()
  async def sleep(self, ctx, member: discord.Member = None):
      gif = '''https://media.discordapp.net/attachments/599643495807975434/603601825710604300/image2.gif
      https://media.discordapp.net/attachments/722028202796777543/722208660201275511/tenor_7.gif
      https://media.discordapp.net/attachments/599643495807975434/599646268079341588/1533723275_tumblr_n7sc9lGm2v1sn7u3jo1_500.gif'''
      if member == None:
          e = discord.Embed(title='Реакция: сон', description=f'{ctx.author.mention} **наелся и спит**', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      else:
          e = discord.Embed(title='Реакция: сон', description=f'{ctx.author.mention} **спит с** {member.mention}', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)

  @commands.command()
  async def read(self, ctx, member: discord.Member = None):
      gif = '''https://images-ext-2.discordapp.net/external/rtkLe3y9f5JQ8ODneVdzQIZUa0-wW9l_ic-SMExjcsY/https/media.discordapp.net/attachments/792746015567511587/812731033089998868/tenor_8.gif'''
      if member == None:
          e = discord.Embed(title='Реакция: чтение', description=f'{ctx.author.mention} **читает**', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      else:
          e = discord.Embed(title='Реакция: чтение', description=f'{ctx.author.mention} **читает вместе с** {member.mention}', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)

  @commands.command()
  async def chill(self, ctx, member: discord.Member = None):
      gif = '''https://images-ext-2.discordapp.net/external/huAY6c0NZkEAPmFZslBAhq81eKoik3IZ1mq_iLVOkBc/https/i.pinimg.com/originals/de/35/ad/de35ad0ea1dee5c4e3bc06fb0ddbcbb2.gif
      https://images-ext-2.discordapp.net/external/XyCMAwqFYQjW9yO_GAHA05_Yjf1MVl_BvvCli1pwEac/https/i.pinimg.com/originals/32/46/f8/3246f86fd3c8e39039a12029eb6cacd8.gif
      https://images-ext-2.discordapp.net/external/1jZxygg9j7hkv0yut2x-aSVLM-G9Wy5CwqlDQslhAf8/https/i.pinimg.com/originals/65/01/92/6501922ec790e2971e37d2c47a306cd7.gif
      https://images-ext-2.discordapp.net/external/SqonsAoqHicIxSm1-OU_sTJGHBWHmLlYDyvUKAqMyKU/https/i.pinimg.com/originals/25/26/1f/25261f171c5e8cb8e1f6987dd70c57b9.gif'''
      if member == None:
          e = discord.Embed(title='Реакция: отдых', description=f'{ctx.author.mention} **отдыхает**', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      else:
          e = discord.Embed(title='Реакция: чтение', description=f'{ctx.author.mention} **отдыхает вместе с** {member.mention}', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)

  @commands.command()
  async def kill(self, ctx, member: discord.Member = None):
      gif = '''https://images-ext-2.discordapp.net/external/ZllN79mQrpL1vwjU746_mtOEcEIhidXIUjC6pWxp-Vw/https/i.pinimg.com/originals/8e/22/2e/8e222e0175de9995669b54e6a14ee68d.gif
      https://images-ext-2.discordapp.net/external/AG_6BhqzuNlzNY9gj_HXrJEx7BJCVZQTafoY6zhoBpg/https/i.pinimg.com/originals/42/dd/88/42dd884acd74ab8c3755e17cebc5c1d2.gif
      https://images-ext-1.discordapp.net/external/aRyICVDY8sd_C4DozYpVuExzbc_W52IcsCgapBQe7fA/https/i.gifer.com/G9IM.gif
      https://images-ext-2.discordapp.net/external/KTWiXjl-5cDjsKYxDBllkcdr1uh_fjHEUUnilfZziCA/https/i.pinimg.com/originals/14/12/13/1412139a3d824a80996440c057068b24.gif'''
      if member == ctx.author:
          e = discord.Embed(title='Реакция: убийство', description=f'{ctx.author.mention} **убивает себя**', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      if member == None:
          e = discord.Embed(title='Реакция: убийство', description=f'{ctx.author.mention} **убивает всех**', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      else:
          e = discord.Embed(title='Реакция: чтение',
                            description=f'{ctx.author.mention} **убивает** {member.mention}', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)

  @commands.command()
  async def coffe(self, ctx, member: discord.Member=None):
      gif = '''https://media.discordapp.net/attachments/881088505051234317/917457977865285642/not_my_gif__made_a_little_colour_edit_on_We_Heart_It.gif
      https://media.discordapp.net/attachments/881088505051234317/917458081653338142/0763a933e9010f89.gif
      '''
      if member == None:
          e = discord.Embed(title='Реакция: кофеёк', description=f'{ctx.author.mention} **пьёт кофе**', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)
      else:
          e = discord.Embed(title='Реакция: чтение', description=f'{ctx.author.mention} **пьёт кофе с** {member.mention}', color=0x2f3136)
          e.set_image(url=random.choice(gif.split("\n")))
          e.timestamp = datetime.datetime.utcnow()
          e.set_footer(text=ctx.author.name + '\u200b', icon_url=ctx.author.avatar_url)
          return await ctx.send(embed=e)







def setup(client):
  client.add_cog(Reactions(client))
