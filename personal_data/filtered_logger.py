#!/usr/bin/env python3


"""
Filter
"""
import re
from typing import List
import logging
import os
import mysql.connector


PII_FIELDS = ("email", "password", "phone", "ssn", "ip")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    function called filter_datum that returns the log message obfuscated:
    """
    for field in fields:
        message = re.sub(f"{field}=[^;{separator}]*",
                         f"{field}={redaction}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Method to filter values in incoming log records
        """
        return (filter_datum(list(self.fields),
                             RedactingFormatter.REDACTION,
                             super().format(record),
                             RedactingFormatter.SEPARATOR))


def get_logger() -> logging.Logger:
    """
    Implement a get_logger function that takes
    no arguments and returns a logging.Logger object
    """
    logger = logging.getLogger("user_data")
    logger = logger.setLevel(logging.INFO)
    logger.propagate = False

    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    fuction connect to database
    """

    user = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME", "my_db")

    conn = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            db_name=db_name
    )

    return conn
