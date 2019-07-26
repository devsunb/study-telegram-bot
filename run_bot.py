import logging

from js_bot import JSBot

logger = logging.getLogger('JS_BOT')


def proc_echo(bot, update):
    logger.debug('proc_echo: {}'.format(update.message.text))
    update.message.reply_text(update.message.text)


def proc_test(bot, update):
    logger.debug('proc_test')
    update.message.reply_text('TEST Done')


def proc_error(bot, update):
    logger.warning('Update "%s" caused error "%s"', update, update.error)


def setup_logger(log_level):
    logger.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] (%(filename)s:%(lineno)d) %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)


if __name__ == '__main__':
    setup_logger('DEBUG')
    js_bot = JSBot()
    js_bot.add_message_handler(proc_echo)
    js_bot.add_command_handler('test', proc_test)
    js_bot.add_error_handler(proc_error)
    logger.debug('Start JSBot')
    js_bot.start()
