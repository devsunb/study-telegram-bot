import logging

from telegram_bot import TelegramBot

logger = logging.getLogger('JS_BOT')


class JSBot(TelegramBot):
    def __init__(self):
        logger.debug('JSBot init')
        self.token = ''
        self.id = 0
        TelegramBot.__init__(self, 'JS Bot', self.token, self.id)
