""" NewsCartSendgridAPI run file
    This file will start NewsCartSendgridAPI

    Example:
        $ python run.py
"""
import logging
from logging.handlers import RotatingFileHandler
from app import APP


if __name__ == '__main__':
    HANDLER = RotatingFileHandler('sengrid-api.log', maxBytes=10000, backupCount=2)
    HANDLER.setLevel(logging.DEBUG)
    APP.logger.addHandler(HANDLER)
    APP.run()
