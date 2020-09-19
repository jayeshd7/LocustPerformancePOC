# encoding: utf-8

import logging
import datetime
import socket
import sys

from logging.handlers import TimedRotatingFileHandler

LOG_FILE = "result_{0}.log".format(datetime.datetime.now().strftime("%Y-%m-%d-%S"))
log_format = "%(asctime)s.%(msecs)03d000 [%(levelname)s] {0}/%(name)s : %(message)s".format(socket.gethostname())
FORMATTER = logging.Formatter(log_format, '%Y-%m-%d %H:%M:%S')


class Logger(object):
    def get_console_handler(self):
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(FORMATTER)
        return console_handler

    def get_file_handler(self, log_file=LOG_FILE):
        file_handler = TimedRotatingFileHandler(log_file)
        file_handler.setFormatter(FORMATTER)
        return file_handler

    def get_logger(self, logger_name, log_file=LOG_FILE):
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(self.get_console_handler())
        logger.addHandler(self.get_file_handler(log_file))
        return logger
