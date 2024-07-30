from typing import Any
from masks import get_mask_account
from masks import get_mask_card_number

card_number = str(input())


def mask_account_card(arg: Any) -> str:
    """Функция обработки информации о картах и счетах"""
    cn = card_number.split(" ")
    if "счет" in cn[0].lower():
        b_number = get_mask_account(cn[-1])
        new_card = cn[0] + " " + b_number
    else:
        b_number = get_mask_card_number(cn[-1])
        cn = " ".join(cn[:-1])
        new_card = cn + " " + b_number
    return new_card


mask_account_card(card_number)
