import re


def filter_datum(fields: list, redaction: str,
                 message: str, separator: str) -> str:
    """
    Retourne un message de journal obfusqué.

    Args:
        fields (list): Liste des champs à obfusquer.
        redaction (str): Valeur d'obfuscation.
        message (str): Ligne de journal.
        separator (str): Caractère séparant
        les champs dans la ligne de journal.

    Returns:
        str: Message de journal obfusqué.
    """
    for field in fields:
        message = re.sub(f"{field}=[^;{separator}]*",
                         f"{field}={redaction}", message)
    return message
