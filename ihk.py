def prozent_berechnen(value: int, max_value: int) -> int:
    if type(value) is not int or type(max_value) is not int:
        raise TypeError("")

    if value > max_value or value < 0 or max_value < 6:
        raise ValueError("")

    return int((value / max_value) * 100)


def note_berechnen(value: int) -> str:
    if type(value) is not int:
        raise TypeError("")

    if value > 100 or value < 0:
        raise ValueError("")

    if value >= 92:
        return "sehr gut"

    if value >= 81:
        return "gut"

    if value >= 67:
        return "befriedigend"

    if value >= 50:
        return "ausreichend"

    if value >= 30:
        return "mangelhaft"

    if value >= 0:
        return "ungenügend"
