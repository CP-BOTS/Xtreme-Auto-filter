#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @neer_j

from pyrogram import Client, __version__

from . import API_HASH, APP_ID, GROUP_NAME, LOGGER, \
    USER_SESSION ,GP_LINK , BOT_NAME , GROUP_NAME,DEV_INFO


class User(Client):
    def __init__(self):
        super().__init__(
            USER_SESSION,
            api_hash=API_HASH,
            api_id=APP_ID,
            gp_link=GP_LINK,
            bot_name=BOT_NAME,
            group_name=GROUP_NAME,
            dev_info=DEV_INFO,
            workers=4
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        return (self, usr_bot_me.id)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
