import re


def filter_datum(fields: list, redaction: str,
                 message: str, separator: str) -> str:
    """ function fileter_datume """
    for field in fields:
        message = re.sub(f"{field}=[^;{separator}]*",
                         f"{field}={redaction}", message)
    return message
