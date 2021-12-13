import asyncio

import datetime
import random

import discord
from discord import *
from discord.ext import commands

from discord_components import *

class Ofter(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def avatar(self, ctx, member: discord.Member=None):
      if member == None:
          member = ctx.author
      e = discord.Embed(title=f'Аватарка {member.display_name}', description='_ _'
                                                                             f"[PNG]({member.avatar_url_as(static_format='png')}) | [WEBP]({member.avatar_url_as(static_format='webp')}) | [JPG]({member.avatar_url_as(static_format='jpg')})", color=0x2f3136)
      e.set_image(url=member.avatar_url)
      await ctx.send(embed=e)

  @avatar.error
  async def avatar_error(self, ctx, error):
      if isinstance(error, commands.MemberNotFound):
          e = discord.Embed(description='Пользователь, которого вы указали не был найден.', color=0x2f3136)
          e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
          e.timestamp = datetime.datetime.utcnow()
          await ctx.reply(embed=e, mention_author=False)

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def inrole(self, ctx, role: discord.Role=None):
      if role == None:
          return await ctx.message.add_reaction("❌")
      data = "\n".join(str(member)  for member in ctx.guild.members if role in member.roles)
      e = discord.Embed(description='**`                            Информация о ролях                            `**', color=0x2f3136)
      e.add_field(name='```                Роль                ```', value=f'```diff\n+ {role.name}\n```', inline=True)
      e.add_field(name='```                Люди                ```', value=f'```py\n{len(data)}\n```', inline=True)
      e.add_field(name='```                                    Люди                                  ```', value=f'```{data}```', inline=False)
      e.set_author(name=f'Роли • {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
      e.timestamp = datetime.datetime.utcnow()
      await ctx.send(embed=e)







def setup(client):
  client.add_cog(Ofter(client))
