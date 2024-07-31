def get_mask_card_number(card_number: str) -> str:
    """Receives the card number and returns a mask - the first six and last four digits of card"""

    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:]}"
    else:
        return ""


def get_mask_account(account: str) -> str:
    """Receives the card number and returns the mask - the last four digits"""
    if account.isdigit() and len(account) == 20:
        return f"{'*' * 2}{account[16:]}"
    else:
        return ""
