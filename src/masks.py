def get_mask_card_number(card_number):
    """Принимает номер карты и возвращает маску - видны первые 6 и последние 4 цифры карты"""
    return f"{card_number[:6]} {card_number[6:10]:**} {card_number[10:16]} {card_number[16:]}".replace(
        " ", ""
    )


def get_mask_account(account_number):
    """Принимает номер карты и возвращает маску - последние 4 цифры карты"""
    return f"**{account_number[-4:]}".replace(" ", "")
