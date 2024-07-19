import datetime
import re

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_string: str) -> str | None:
    """Function disguise number card and invoice"""
    if "Visa Platinum" in input_string or "Maestro" in input_string:
        return get_mask_account(input_string)
    elif "Счет" in input_string:
        return get_mask_account(input_string)
    return None


def get_data(input_string: str) -> str | None:
    """Function convert date"""
    date = input_string("T")[0]
    formatted_date = f"{date[-2:]}.{date[5:7]}.{date[:4]}"
    return formatted_date
