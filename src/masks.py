import re
def get_mask_card_number(info_card: str) -> str:
    """Receives the card number and returns a mask - the first six and last four digits of card"""
    # return f"{card_number[:6]} {card_number[6:10]:**} {card_number[10:16]} {card_number[16:]}".replace(
    #     " ", ""
    # )
    info_card = info_card.replace("", "")
    enumeration = None
    for m, char in enumerate(info_card):
        if char.isdigit():
            enumeration = m
            break

    if enumeration is None:
        return "Incorrect input data"

    type_card, number_card = info_card[:enumeration], info_card[enumeration:]
    if len(info_card) != 16:
        return "Incorrect input data"

    type_card_with_empty = re.sub(r"([A-Z])", r"\1", type_card).strip()
    number_mask = number_card[0:4] + " " + number_card[4:6] + "** ****" + number_card[-4:]
    return f"{type_card_with_empty} {number_mask}"


def get_mask_account(account_number):
    """Receives the card number and returns the mask - the last four digits"""
    return "Счет **" + account_number[-4:]

#return f"**{account_number[-4:]}".replace(" ", "")
