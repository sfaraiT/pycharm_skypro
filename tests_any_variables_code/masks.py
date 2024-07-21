def get_mask_card_number(info_card: str) -> str:
    """Receives the card number and returns a mask - the first six and last four digits of card"""
    card_list = [info_card[:4], info_card[4:6] + "**", "****", info_card[12:]]
    return "".join(card_list)


def get_mask_account(account_number: str) -> str:
    """Receives the card number and returns the mask - the last four digits"""
    return "**" + account_number[-4:]
