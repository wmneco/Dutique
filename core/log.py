"""Logging system of dutique"""
###############################################################################
# Imports

import logging
from colorama import Fore, Style


###############################################################################
# Logging Config

class LogFormatter(logging.Formatter):
    """Formate"""
    format_template = "%(levelname)s: [%(name)s]: %(message)s"

    FORMATS = {
        logging.DEBUG: format_template,
        logging.INFO: Fore.BLUE + format_template + Style.RESET_ALL,
        logging.WARNING: Fore.YELLOW + format_template + Style.RESET_ALL,
        logging.ERROR: Fore.RED + format_template + Style.RESET_ALL,
        logging.CRITICAL: Fore.LIGHTRED_EX + format_template + Style.RESET_ALL
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
