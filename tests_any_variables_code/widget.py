from masks import get_mask_account, get_mask_card_number


def mask_account_card(input_string: str) -> str | None:
    """Function disguise number card and invoice"""
    card_list = []
    name_and_number = []
    for number_and_name in input_string.split():
        if number_and_name.isalpha():
            name_and_number.append(number_and_name)
        elif number_and_name.isdigit():
            if len(number_and_name) == 16:
                mask_number_and_name = get_mask_card_number(number_and_name)
                name_and_number.append(mask_number_and_name)
                card_list.append(name_and_number)
                name_and_number = list()
            elif len(number_and_name) == 20:
                mask_number_account = get_mask_account(number_and_name)
                name_and_number.append(mask_number_account)
                card_list.append(name_and_number)
                name_and_number = list()
    return "\n".join(" ".join(values_cart) for values_cart in card_list)


def get_data(input_string: str) -> str | None:
    """Function convert date"""
    date = input_string.split("T")[0]
    formatted_date = f"{date[-2:]}.{date[5:7]}.{date[:4]}"
    return formatted_date


# Test our def and code ->
print(get_mask_account("Visa Platinum 8990922113665229"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Visa Platinum 5999414228426353"))
print(mask_account_card("Мир 5999414228426353"))
print(mask_account_card("Счет 35383033474447895560"))
print(get_mask_card_number("7000792289606361"))
print(get_data("2024-03-11T02:26:18.671407"))
