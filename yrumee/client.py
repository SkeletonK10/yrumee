import random

import discord


class YrumeeClient(discord.Client):
    is_active = False
    stack = []

    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))

    async def on_message(self, message: discord.Message):
        if message.author.id == self.user.id:
            return
        print("Message from {0.author}: {0.content}".format(message))

        if message.content.startswith("."):
            cp = message.content.split(" ", 1)
            if len(cp) == 1:
                command, payload = cp[0], ""
            else:
                command, payload = cp
            await self.on_command(command.lstrip("."), payload, message)
        else:
            cat_count = 0
            for cat in ["냥", "야옹", "고영", "고양"]:
                cat_count += message.content.count(cat)

            if self.is_active and cat_count > 0:
                await message.channel.send("냥" * cat_count)

    async def on_command(self, command, payload, message: discord.Message):
        if command == "로또":
            lotto_num = sorted([random.randint(1, 46) for _ in range(6)], reverse=False)
            lotto_num = " ".join([str(x) for x in lotto_num])
            await message.channel.send("여름이의 로또 픽: {}".format(lotto_num))

        if command == "냥바":
            if self.is_active is True:
                await message.channel.send("냥바 👋")
                self.is_active = False

        if command == "냥하":
            if self.is_active is False:
                await message.channel.send("냥하 🐈")
                self.is_active = True

        if command == "푸시":
            self.stack.append(payload)

        if command == "팝":
            if len(self.stack) > 0:
                await message.channel.send(self.stack.pop())
