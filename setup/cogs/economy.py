import asyncio
import json
import time

import datetime
import requests
import random

import discord
from discord import *
from discord.ext import commands

from discord_components import *

from main import get_bank, open_acc

class Economy(commands.Cog):

  def __init__(self, client):
    self.client = client


  @commands.command()
  async def balance(self, ctx, member: discord.Member=None):
    if member == None:
      member = ctx.author
    await open_acc(member)
    users = await get_bank()
    member_bank = users[str(member.id)]['wallet']
    e = discord.Embed(title=f'Текущий баланс — {member}', color=0x2f3136)
    e.add_field(name='<a:hdot:917704464520060938> Баланс:', value=f'```{member_bank}```')
    e.add_field(name='<a:hdot:917704464520060938> Звёзды:', value=f'```0```')
    e.set_thumbnail(url=member.avatar_url)
    await ctx.reply(embed=e, mention_author=False)

  @balance.error
  async def balance_error(self, ctx, error):
    if isinstance(error, commands.MemberNotFound):
      e = discord.Embed(description='Пользователь, которого вы указали не был найден.', color=0x2f3136)
      e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
      e.timestamp = datetime.datetime.utcnow()
      await ctx.reply(embed=e, mention_author=False)

  @commands.command(
    aliases = ['give', 'trade']
  )
  async def pay(self, ctx, member: discord.Member=None, amount: int=None):
    if member == None:
      e = discord.Embed(title=f'Передача баланса — {ctx.author}', description=f'{ctx.author.mention}, пожалуйста, **укажите пользователя** для передачи денег', color=0x2f3136)
      e.set_thumbnail(url=ctx.author.avatar_url)
      return await ctx.reply(embed=e, mention_author=False)
    if amount == None:
      e = discord.Embed(title=f'Передача баланса — {ctx.author}', description=f'{ctx.author.mention}, пожалуйста, укажите **колличество** денег для передачи', color=0x2f3136)
      e.set_thumbnail(url=ctx.author.avatar_url)
      return await ctx.reply(embed=e, mention_author=False)
    if amount <= 0:
      e = discord.Embed(title=f'Передача баланса — {ctx.author}', description=f'{ctx.author.mention}, вы **не можете** дать пользователю меньше **0**', color=0x2f3136)
      e.set_thumbnail(url=ctx.author.avatar_url)
      return await ctx.reply(embed=e, mention_author=False)
    await open_acc(ctx.author)
    await open_acc(member)
    users = await get_bank()
    author_bank = users[str(ctx.author.id)]['wallet']
    if author_bank < amount:
      e = discord.Embed(title=f'Передача баланса — {ctx.author}', description=f'{ctx.author.mention}, у вас недостаточно средств, для передачи денег', color=0x2f3136)
      e.set_thumbnail(url=ctx.author.avatar_url)
      return await ctx.reply(embed=e, mention_author=False)
    users[str(member.id)]['wallet'] += amount
    users[str(ctx.author.id)]['wallet'] -= amount
    with open('./jsons/bank.json', 'w') as f:
        json.dump(users, f)
    e = discord.Embed(title=f'Передача баланса — {ctx.author}', description=f'{ctx.author.mention}, вы **передали** пользователю {member.mention} `{amount}`<:money:918392208040792094>', color=0x2f3136)
    e.set_thumbnail(url=ctx.author.avatar_url)
    await ctx.reply(embed=e, mention_author=False)

  @pay.error
  async def pay_error(self, ctx, error):
    if isinstance(error, commands.MemberNotFound):
      e = discord.Embed(description='Пользователь, которого вы указали не был найден.', color=0x2f3136)
      e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
      e.timestamp = datetime.datetime.utcnow()
      await ctx.reply(embed=e, mention_author=False)

  @commands.command()
  async def timely(self, ctx):
    with open("./jsons/timely.json", "r") as f:
      timely = json.load(f)
      timely_member = str(ctx.author.id)
      if timely_member in timely:
        e = discord.Embed(title=f'Временная награда — {ctx.author}', description=f'{ctx.author.mention}, вы уже получили временную награду за сегодня', color=0x2f3136)
        e.set_thumbnail(url=ctx.author.avatar_url)
        return await ctx.reply(embed=e, mention_author=False)
      else:
        earned = random.randint(50, 300)
        await open_acc(ctx.author)
        users = await get_bank()
        users[str(ctx.author.id)]['wallet'] += earned
        with open('./jsons/bank.json', 'w') as f:
          json.dump(users, f)

        with open("./jsons/timely.json", "r") as f:
          timely = json.load(f)
        timely[str(ctx.author.id)] = 'taked'
        with open("./jsons/timely.json", "w") as f:
          json.dump(timely, f, indent=4)
        e = discord.Embed(title=f'Временная награда — {ctx.author}',description=f'{ctx.author.mention}, вы **получили** **{earned}** <:money:918392208040792094>. Возвращайтесь через 12 часов', color=0x2f3136)
        e.set_thumbnail(url=ctx.author.avatar_url)
        await ctx.reply(embed=e, mention_author=False)
        #43200
        time.sleep(5)
        with open("./jsons/timely.json", "r") as f:
          timely = json.load(f)
        timely.pop(str(ctx.author.id))
        with open("./jsons/timely.json", "w") as f:
          json.dump(timely, f, indent=4)



  @commands.command()
  @commands.has_permissions(administrator=True)
  async def add(self, ctx, member: discord.Member=None, count: int=None):
    if member == None:
      return await ctx.message.add_reaction("❌")
    if count == None:
      return await ctx.message.add_reaction("❌")
    if count <= 0:
      return await ctx.message.add_reaction("❌")
    else:
      await open_acc(member)
      users = await get_bank()
      users[str(member.id)]['wallet'] += count
      with open('./jsons/bank.json', 'w') as f:
        json.dump(users, f)
      await ctx.message.add_reaction("✅")

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def remove(self, ctx, member: Member=None, count: int=None):
    if member == None:
      return await ctx.message.add_reaction("❌")
    if count == None:
      return await ctx.message.add_reaction("❌")
    if count <= 0:
      return await ctx.message.add_reaction("❌")
    else:
      await open_acc(member)
      users = await get_bank()
      member_bank = users[str(member.id)]['wallet']
      if member_bank < count:
        return await ctx.message.add_reaction("❌")
      else:
        users[str(member.id)]['wallet'] -= count
        with open('./jsons/bank.json', 'w') as f:
          json.dump(users, f)
        await ctx.message.add_reaction("✅")

  @commands.command()
  async def coinflip(self, ctx, amount: int):
    if amount <= 0:
      e = discord.Embed(description='Ваша ставка должна быть больше **1**.', color=0x2f3136)
      e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
      e.timestamp = datetime.datetime.utcnow()
      return await ctx.reply(embed=e, mention_author=False)
    if amount == None:
      e = discord.Embed(description='Укажите количество монет для ставки.', color=0x2f3136)
      e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
      e.timestamp = datetime.datetime.utcnow()
      return await ctx.reply(embed=e, mention_author=False)
    await open_acc(ctx.author)
    users = await get_bank()
    author_bank = users[str(ctx.author.id)]['wallet']
    if amount > 100:
      e = discord.Embed(description='Ваша ставка не может быть более **100** <:money:918392208040792094>', color=0x2f3136)
      e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
      e.timestamp = datetime.datetime.utcnow()
      return await ctx.reply(embed=e, mention_author=False)
    if author_bank < amount:
      e = discord.Embed(description='У вас недостаточно средств для совершения операции.', color=0x2f3136)
      e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
      e.timestamp = datetime.datetime.utcnow()
      return await ctx.reply(embed=e, mention_author=False)
    else:
      flip = 'Орёл', 'Решка'
      stavka = random.choice(flip)
      if stavka == 'Орёл':
        users[str(ctx.author.id)]['wallet'] += amount
        with open('./jsons/bank.json', 'w') as f:
          json.dump(users, f)
        e = discord.Embed(description=f'Выпал **орёл**! Вы выйграли **{amount*2}** <:money:918392208040792094> ', color=0x2f3136)
        e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        e.timestamp = datetime.datetime.utcnow()
        return await ctx.reply(embed=e, mention_author=False)
      else:
        users[str(ctx.author.id)]['wallet'] += amount
        with open('./jsons/bank.json', 'w') as f:
          json.dump(users, f)
        e = discord.Embed(description=f'Выпала **решка**! Вы проиграли **{amount}** <:money:918392208040792094> ',color=0x2f3136)
        e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        e.timestamp = datetime.datetime.utcnow()
        return await ctx.reply(embed=e, mention_author=False)

















  @commands.command()
  async def status(self, ctx, *, msg=None):
    if msg == None:
      with open("./jsons/status.json", "r") as f:
        status = json.load(f)
        status_member = str(ctx.author.id)
        if status_member in status:
          e = discord.Embed(description='Вы уверены что хотите удалить свой статус?', color=0x2f3136)
          e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
          e.timestamp = datetime.datetime.utcnow()
          msg = await ctx.reply(embed=e, mention_author=False, components=[
            [
              Button(label="Да", style=ButtonStyle.green),
              Button(label="Нет", style=ButtonStyle.red)
            ]
          ])
          try:
            respone = await self.client.wait_for('button_click', timeout=30.0, check=lambda inter: inter.author.id == ctx.author.id)
            if respone.component.label == "Да":
              with open("./jsons/status.json", "r") as f:
                audit = json.load(f)
              audit.pop(str(ctx.author.id))
              with open("./jsons/status.json", "w") as f:
                json.dump(audit, f, indent=4)
              e = discord.Embed(description='Вы успешно удалили свой статус', color=0x2f3136)
              e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
              e.timestamp = datetime.datetime.utcnow()
              await msg.edit(embed=e, components=[])
            else:
              e = discord.Embed(description='Команда была отменена', color=0x2f3136)
              e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
              e.timestamp = datetime.datetime.utcnow()
              await msg.edit(embed=e, components=[])

          except asyncio.TimeoutError:
            e = discord.Embed(description='Время ожидания истекло. Команда была отменена', color=0x2f3136)
            e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            e.timestamp = datetime.datetime.utcnow()
            await msg.edit(embed=e, components=[])
        else:
          e = discord.Embed(description='Для добавления статуса напишите команду с аргументом', color=0x2f3136)
          e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
          e.timestamp = datetime.datetime.utcnow()
          await ctx.reply(embed=e, mention_author=False)
    if len(msg) > 30:
      e = discord.Embed(description='Ваш статус не может иметь более **30** символов', color=0x2f3136)
      e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
      e.timestamp = datetime.datetime.utcnow()
      return await ctx.reply(embed=e, mention_author=False)
    else:
      with open('./jsons/status.json', 'r') as f:
        status = json.load(f)
      status[str(ctx.author.id)] = msg
      with open('./jsons/status.json', 'w') as f:
        json.dump(status, f, indent=4)
      e = discord.Embed(description=f'Ваш статус был изменён на **{msg}**', color=0x2f3136)
      e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
      e.timestamp = datetime.datetime.utcnow()
      await ctx.reply(embed=e, mention_author=False)

  @commands.command()
  async def profile(self, ctx, member: discord.Member=None):
    if member == None:
      e = discord.Embed(title=f'Профиль — {ctx.author}', color=0x2f3136)
      with open('./jsons/status.json', 'r') as f:
        status = json.load(f)
        if str(ctx.author.id) in status:
          e.add_field(name='<a:hdot:917704464520060938> Статус:', value=f'```{status[str(ctx.author.id)]}```')
        else:
          e.add_field(name='<a:hdot:917704464520060938> Статус:', value=f'```Отсутствует```')
      await open_acc(ctx.author)
      users = await get_bank()
      author_bank = users[str(ctx.author.id)]['wallet']
      e.add_field(name='<a:hdot:917704464520060938> Баланс:', value=f'```{author_bank}```', inline=True)
      e.set_thumbnail(url=ctx.author.avatar_url)
      comp = [
        Button(style=ButtonStyle.grey, label='Изменить профиль')
      ]
      with open('./jsons/inst.json', 'r') as f:
        inst = json.load(f)
        if str(ctx.author.id) in inst:
          comp.append(Button(style=ButtonStyle.URL, label='Instagram', url=inst[str(ctx.author.id)]))
        else:
          pass
      with open('./jsons/vk.json', 'r') as f:
        vk = json.load(f)
        if str(ctx.author.id) in vk:
          comp.append(Button(style=ButtonStyle.URL, label='VK', url=vk[str(ctx.author.id)]))
        else:
          pass
      with open('./jsons/spotify.json', 'r') as f: '''не удивляйся, что профиль для осу, а файл спотифай XD. мне лень было переназывать'''
        spotify = json.load(f)
        if str(ctx.author.id) in spotify:
          comp.append(Button(style=ButtonStyle.URL, label='Osu', url=spotify[str(ctx.author.id)]))
        else:
          pass
      msg = await ctx.reply(embed=e, mention_author=False, components=[comp])
      try:
        respone = await self.client.wait_for('button_click', timeout=30.0, check=lambda inter: inter.author.id == ctx.author.id)
        if respone.component.label == 'Изменить профиль':
          e = discord.Embed(title=f'Управление профилем — {ctx.author}', color=0x2f3136)
          with open('./jsons/status.json', 'r') as f:
            status = json.load(f)
            if str(ctx.author.id) in status:
              e.add_field(name='<a:hdot:917704464520060938> Текущий статус:', value=f'```{status[str(ctx.author.id)]}```')
            else:
              e.add_field(name='<a:hdot:917704464520060938> Текущий статус:', value=f'```Не установлен```')
          with open('./jsons/vk.json', 'r') as f:
            vk = json.load(f)
            if str(ctx.author.id) in vk:
              vkon = vk[str(ctx.author.id)]
            else:
              vkon = 'Не установлен'
          with open('./jsons/inst.json', 'r') as f:
            inst = json.load(f)
            if str(ctx.author.id) in inst:
              inston = inst[str(ctx.author.id)]
            else:
              inston = 'Не установлен'
          with open('./jsons/spotify.json', 'r') as f:
            spotify = json.load(f)
            if str(ctx.author.id) in spotify:
              spotifon = spotify[str(ctx.author.id)]
            else:
              spotifon = 'Не установлен'
          e.add_field(name='<a:hdot:917704464520060938> Соцсети:', value=f'**Instagram**: {inston}\n**VK**: {vkon}\n**Osu**: {spotifon}', inline=False)
          e.set_thumbnail(url=ctx.author.avatar_url)
          await msg.edit(embed=e, mention_author=False, components=[
            [
              Button(style=ButtonStyle.grey, label='Установить статус'),
              Button(style=ButtonStyle.grey, label='Удалить статус')
            ],
            [
              Button(style=ButtonStyle.grey, label='Установить Instagram'),
              Button(style=ButtonStyle.grey, label='Установить VK'),
              Button(style=ButtonStyle.grey, label='Установить Osu')
            ],
            Button(style=ButtonStyle.grey, label='Назад')
          ])
          try:
            respone = await self.client.wait_for('button_click', timeout=50.0, check=lambda inter: inter.author.id == ctx.author.id)
            if respone.component.label == 'Установить статус':
              e = discord.Embed(title=f'Управление статусом — {ctx.author}', description='Для добавления статуса, отправьте его в чат в течении **50** секунд', color=0x2f3136)
              e.set_thumbnail(url=ctx.author.avatar_url)
              e.timestamp = datetime.datetime.utcnow()
              await msg.edit(embed=e, mention_author=False, components=[
                [
                  Button(style=ButtonStyle.grey, label='Назад')
                ]
              ])
              try:
                message = await self.client.wait_for('message', timeout=50.0,check=lambda inter: inter.author.id == ctx.author.id)
                with open('./jsons/status.json', 'r') as f:
                  status = json.load(f)
                status[str(ctx.author.id)] = message.content
                with open('./jsons/status.json', 'w') as f:
                  json.dump(status, f, indent=4)
                e = discord.Embed(title=f'Управление статусом — {ctx.author}', description='Вы успешно добавили новый статус ', color=0x2f3136)
                e.set_thumbnail(url=ctx.author.avatar_url)
                e.timestamp = datetime.datetime.utcnow()
                await msg.edit(embed=e, mention_author=False, components=[])
              except:
                e = discord.Embed(description='Время ожидания истекло. Команда была отменена', color=0x2f3136)
                e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
                e.timestamp = datetime.datetime.utcnow()
                await msg.edit(embed=e, mention_author=False, components=[])
              try:
                respone = await self.client.wait_for('button_click', timeout=30.0, check=lambda inter: inter.author.id == ctx.author.id)
                if respone.component.label == 'Назад':
                  return msg
              except:
                pass
          except asyncio.TimeoutError:
            e = discord.Embed(description='Время ожидания истекло. Команда была отменена', color=0x2f3136)
            e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            e.timestamp = datetime.datetime.utcnow()
            await msg.edit(embed=e, mention_author=False, components=[])
        if respone.component.label == 'Удалить статус':
          with open("./jsons/status.json", "r") as f:
            status = json.load(f)
            status_member = str(ctx.author.id)
            if status_member in status:
              with open("./jsons/status.json", "r") as f:
                audit = json.load(f)
              audit.pop(str(ctx.author.id))
              with open("./jsons/status.json", "w") as f:
                json.dump(audit, f, indent=4)
              e = discord.Embed(title=f'Управление статусом — {ctx.author}', description='Вы успешно удалили свой статус', color=0x2f3136)
              e.set_thumbnail(url=ctx.author.avatar_url)
              e.timestamp = datetime.datetime.utcnow()
              await msg.edit(embed=e, mention_author=False, components=[])
            else:
              e = discord.Embed(description='Нельзя удалить то, чего нет.', color=0x2f3136)
              e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
              e.timestamp = datetime.datetime.utcnow()
              await msg.edit(embed=e, mention_author=False, components=[])
        if respone.component.label == 'Установить Instagram':
          e = discord.Embed(title=f'Управление ссылками — {ctx.author}', description='Для добавления ссылки на профиль, отправьте его в течении **50** секунд.\nДля того, чтобы удалить ссылку, напишите: **Удалить**', color=0x2f3136)
          e.set_thumbnail(url=ctx.author.avatar_url)
          e.timestamp = datetime.datetime.utcnow()
          await msg.edit(embed=e, mention_author=False, components=[])
          try:
            message = await self.client.wait_for('message', timeout=50.0, check=lambda inter: inter.author.id == ctx.author.id)
            if message.content.startswith('https://www.instagram.com/' or 'https://instagram.com/'):
              r = requests.get(message.content)
              if r.status_code == 404:
                e = discord.Embed(description='Вы указали не рабочую ссылку на профиль. Проверьте написание', color=0x2f3136)
                e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
                e.timestamp = datetime.datetime.utcnow()
                return await msg.edit(embed=e, mention_author=False, components=[])
              else:
                with open('./jsons/inst.json', 'r') as f:
                  inst = json.load(f)
                inst[str(ctx.author.id)] = message.content
                with open('./jsons/inst.json', 'w') as f:
                  json.dump(inst, f, indent=4)
                e = discord.Embed(title=f'Управление ссылками — {ctx.author}', description='Вы успешно добавили ссылку на инстаграмм', color=0x2f3136)
                e.set_thumbnail(url=ctx.author.avatar_url)
                e.timestamp = datetime.datetime.utcnow()
                return await msg.edit(embed=e, mention_author=False, components=[])
            if message.content.startswith('Удалить' or 'удалить'):
              with open("./jsons/inst.json", "r") as f:
                inst = json.load(f)
                inst_member = str(ctx.author.id)
                if inst_member in inst:
                  with open("./jsons/inst.json", "r") as f:
                    inst = json.load(f)
                  inst.pop(str(ctx.author.id))
                  with open("./jsons/inst.json", "w") as f:
                    json.dump(inst, f, indent=4)
                  e = discord.Embed(title=f'Управление ссылками — {ctx.author}', description='Вы успешно удалили свою ссылку на **instagram**', color=0x2f3136)
                  e.set_thumbnail(url=ctx.author.avatar_url)
                  e.timestamp = datetime.datetime.utcnow()
                  return await msg.edit(embed=e, mention_author=False, components=[])
                else:
                  e = discord.Embed(description='Нельзя удалить то, чего нет.', color=0x2f3136)
                  e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
                  e.timestamp = datetime.datetime.utcnow()
                  await msg.edit(embed=e, mention_author=False, components=[])
            else:
              e = discord.Embed(description='Пожалуйста, укажите ссылку на профиль', color=0x2f3136)
              e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
              e.timestamp = datetime.datetime.utcnow()
              await msg.edit(embed=e, mention_author=False, components=[])
          except:
            e = discord.Embed(description='Время ожидания истекло. Команда была отменена', color=0x2f3136)
            e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            e.timestamp = datetime.datetime.utcnow()
            await msg.edit(embed=e, mention_author=False, components=[])
        if respone.component.label == 'Установить VK':
          e = discord.Embed(title=f'Управление ссылками — {ctx.author}', description='Для добавления ссылки на профиль, отправьте его в течении **50** секунд\nДля того, чтобы удалить ссылку, напишите: **Удалить**', color=0x2f3136)
          e.set_thumbnail(url=ctx.author.avatar_url)
          e.timestamp = datetime.datetime.utcnow()
          await msg.edit(embed=e, mention_author=False, components=[])
          try:
            message = await self.client.wait_for('message', timeout=50.0, check=lambda inter: inter.author.id == ctx.author.id)
            if message.content.startswith('https://vk.com/' or 'https://www.vk.com/'):
              r = requests.get(message.content)
              if r.status_code == 404:
                e = discord.Embed(description='Вы указали не рабочую ссылку на профиль. Проверьте написание', color=0x2f3136)
                e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
                e.timestamp = datetime.datetime.utcnow()
                return await msg.edit(embed=e, mention_author=False, components=[])
              else:
                with open('./jsons/vk.json', 'r') as f:
                  vk = json.load(f)
                vk[str(ctx.author.id)] = message.content
                with open('./jsons/vk.json', 'w') as f:
                  json.dump(vk, f, indent=4)
                e = discord.Embed(title=f'Управление ссылками — {ctx.author}', description='Вы успешно добавили ссылку на вконтакте', color=0x2f3136)
                e.set_thumbnail(url=ctx.author.avatar_url)
                e.timestamp = datetime.datetime.utcnow()
                return await msg.edit(embed=e, mention_author=False, components=[])
            if message.content.startswith('Удалить' or 'удалить'):
              with open("./jsons/vk.json", "r") as f:
                vk = json.load(f)
                vk_member = str(ctx.author.id)
                if vk_member in vk:
                  with open("./jsons/vk.json", "r") as f:
                    vk = json.load(f)
                  vk.pop(str(ctx.author.id))
                  with open("./jsons/vk.json", "w") as f:
                    json.dump(vk, f, indent=4)
                  e = discord.Embed(title=f'Управление ссылками — {ctx.author}', description='Вы успешно удалили свою ссылку на **vk**', color=0x2f3136)
                  e.set_thumbnail(url=ctx.author.avatar_url)
                  e.timestamp = datetime.datetime.utcnow()
                  return await msg.edit(embed=e, mention_author=False, components=[])
                else:
                  e = discord.Embed(description='Нельзя удалить то, чего нет.', color=0x2f3136)
                  e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
                  e.timestamp = datetime.datetime.utcnow()
                  await msg.edit(embed=e, mention_author=False, components=[])
            else:
              e = discord.Embed(description='Пожалуйста, укажите ссылку на профиль', color=0x2f3136)
              e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
              e.timestamp = datetime.datetime.utcnow()
              await msg.edit(embed=e, mention_author=False, components=[])
          except:
            e = discord.Embed(description='Время ожидания истекло. Команда была отменена', color=0x2f3136)
            e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            e.timestamp = datetime.datetime.utcnow()
            await msg.edit(embed=e, mention_author=False, components=[])
        if respone.component.label == 'Установить Osu':
          e = discord.Embed(title=f'Управление ссылками — {ctx.author}', description='Для добавления ссылки на профиль, отправьте его в течении **50** секунд\nДля того, чтобы удалить ссылку, напишите: **Удалить**', color=0x2f3136)
          e.set_thumbnail(url=ctx.author.avatar_url)
          e.timestamp = datetime.datetime.utcnow()
          await msg.edit(embed=e, mention_author=False, components=[])
          try:
            message = await self.client.wait_for('message', timeout=50.0, check=lambda inter: inter.author.id == ctx.author.id)
            if message.content.startswith('https://osu.ppy.sh/users/' or 'https://osu.ppy/users/'):
              r = requests.get(message.content)
              if r.status_code == 404:
                e = discord.Embed(description='Вы указали не рабочую ссылку на профиль. Проверьте написание', color=0x2f3136)
                e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
                e.timestamp = datetime.datetime.utcnow()
                return await msg.edit(embed=e, mention_author=False, components=[])
              else:
                with open('./jsons/spotify.json', 'r') as f:
                  spotify = json.load(f)
                spotify[str(ctx.author.id)] = message.content
                with open('./jsons/spotify.json', 'w') as f:
                  json.dump(spotify, f, indent=4)
                e = discord.Embed(title=f'Управление ссылками — {ctx.author}', description='Вы успешно добавили ссылку на **osu** профиль', color=0x2f3136)
                e.set_thumbnail(url=ctx.author.avatar_url)
                e.timestamp = datetime.datetime.utcnow()
                return await msg.edit(embed=e, mention_author=False, components=[])
            if message.content.startswith('Удалить' or 'удалить'):
              with open("./jsons/spotify.json", "r") as f:
                spotify = json.load(f)
                spotify_member = str(ctx.author.id)
                if spotify_member in spotify:
                  with open("./jsons/spotify.json", "r") as f:
                    spotify = json.load(f)
                  spotify.pop(str(ctx.author.id))
                  with open("./jsons/spotify.json", "w") as f:
                    json.dump(spotify, f, indent=4)
                  e = discord.Embed(title=f'Управление ссылками — {ctx.author}', description='Вы успешно удалили свою ссылку на **osu**', color=0x2f3136)
                  e.set_thumbnail(url=ctx.author.avatar_url)
                  e.timestamp = datetime.datetime.utcnow()
                  return await msg.edit(embed=e, mention_author=False, components=[])
                else:
                  e = discord.Embed(description='Нельзя удалить то, чего нет.', color=0x2f3136)
                  e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
                  e.timestamp = datetime.datetime.utcnow()
                  await msg.edit(embed=e, mention_author=False, components=[])
            else:
              e = discord.Embed(description='Пожалуйста, укажите ссылку на профиль', color=0x2f3136)
              e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
              e.timestamp = datetime.datetime.utcnow()
              await msg.edit(embed=e, mention_author=False, components=[])
          except:
            e = discord.Embed(description='Время ожидания истекло. Команда была отменена', color=0x2f3136)
            e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            e.timestamp = datetime.datetime.utcnow()
            await msg.edit(embed=e, mention_author=False, components=[])
        if respone.component.label == 'Назад':
          return msg

      except asyncio.TimeoutError:
        pass
    else:
      e = discord.Embed(title=f'Профиль — {member}', color=0x2f3136)
      await open_acc(member)
      users = await get_bank()
      member_bank = users[str(member.id)]['wallet']
      e.add_field(name='<a:hdot:917704464520060938> Баланс:', value=f'```{member_bank}```', inline=False)
      with open('./jsons/status.json', 'r') as f:
        status = json.load(f)
        if str(member.id) in status:
          e.add_field(name='<a:hdot:917704464520060938> Статус:', value=f'```{status[str(member.id)]}```')
        else:
          e.add_field(name='<a:hdot:917704464520060938> Статус:', value=f'```Отсутствует```')
      e.set_thumbnail(url=member.avatar_url)
      comp = []
      with open('./jsons/inst.json', 'r') as f:
        inst = json.load(f)
        if str(member.id) in inst:
          comp.append(Button(style=ButtonStyle.URL, label='Instagram', url=inst[str(member.id)]))
        else:
          pass
      with open('./jsons/vk.json', 'r') as f:
        vk = json.load(f)
        if str(member.id) in vk:
          comp.append(Button(style=ButtonStyle.URL, label='VK', url=vk[str(member.id)]))
        else:
          pass
      with open('./jsons/spotify.json', 'r') as f:
        spotify = json.load(f)
        if str(member.id) in spotify:
          comp.append(Button(style=ButtonStyle.URL, label='Osu', url=spotify[str(member.id)]))
        else:
          pass
      await ctx.reply(embed=e, mention_author=False, components=comp)








def setup(client):
  client.add_cog(Economy(client))
