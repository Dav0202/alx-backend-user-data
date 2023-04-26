#!/usr/bin/env python3
"""
Module for handling Personal Data
"""
import logging
import re
from typing import List
import logging
import mysql.connector
from os import environ


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Returns a log message obfuscated """
    for i in fields:
        message = re.sub(f'{i}=.*?{separator}',
                         f'{i}={redaction}{separator}', message)
    return message
