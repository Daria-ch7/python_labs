def format_record(rec: tuple[str, str, float]) -> str:
    """на вход подается кортеж, который инвертируется в строку"""

    if len(rec) != 3:
        return ValueError

    name = rec[0].strip()
    group = rec[1].strip()
    gpa = rec[2]

    if (
        (len(name) > 1)
        + ((len(group) != 0) and isinstance(group, str))
        + (isinstance(gpa, float))
    ) != 3:
        return ValueError
    """делаю проверку всех условий (если что-то неправильно, выводится ошибка)"""

    name = name.title().split()
    """с помощью метода title() делаю каждый элемент имени с заглавной буквой и разделяю их по пробелу"""
    if len(name) == 3:
        fio = f"{name[0]} {name[1][0]}.{name[2][0]}."

    if len(name) == 2:
        fio = f"{name[0]} {name[1][0]}."

    GPA = round(gpa, 2)
    """округляю балл до двух знаков"""

    return f"{fio}, гр. {group}, GPA {GPA: .2f}"


print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
