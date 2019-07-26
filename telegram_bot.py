import logging

import telegram
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters

logger = logging.getLogger('JS_BOT')


class TelegramBot:
    def __init__(self, name, token, uid):
        logger.debug('TelegramBot init')
        self.core = telegram.Bot(token)
        logger.debug('Got telegram.Bot')
        self.updater = Updater(token)
        logger.debug('Got Updater')
        self.uid = uid
        self.name = name

    def add_command_handler(self, cmd, func):
        self.updater.dispatcher.add_handler(CommandHandler(cmd, func))

    def add_message_handler(self, func):
        self.updater.dispatcher.add_handler(MessageHandler(Filters.text, func))

    def add_error_handler(self, func):
        self.updater.dispatcher.add_error_handler(func)

    def start(self):
        # self.send_message('Bot starting')
        logger.debug('Bot starting')
        self.updater.start_polling()
        self.updater.idle()

    def send_message(self, text):
        logger.debug('send_message: {}'.format(text))
        self.core.sendMessage(self.uid, text)
