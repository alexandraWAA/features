def filter_by_state(dictionary = [], state="EXECUTED") -> [dict]:
    """Функция формирования нового списка словарей по ключевому слову"""
    new_dictionary = []
    for el in dictionary:
        if state == None or state == "" or state == " ":
            print("Введите корректное state")
        elif el.get("state") == state:
            new_dictionary.append(el)

    return new_dictionary


def sort_by_date(dictionary: list[dict[str]], a=True) -> list[dict[str]]:
    """Функция формирования нового списка, отсортированных по дате"""
    sorted_dict = sorted(dictionary, key=lambda d: (d["date"].year, d["date"].month, d["date"].day), reverse=a)
    return sorted_dict
