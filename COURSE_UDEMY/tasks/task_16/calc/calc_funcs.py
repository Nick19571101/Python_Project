
def block_volume(
    length: int | float, width: int | float, /, *, height: int | float
) -> int | float:
    """Повертає об'єм прямокутного паралелипіпеду."""
    area = block_area(length, width)
    volume = area * height
    return volume
def block_area(length: int | float, width: int | float) -> int | float:
    area = abs(length) * abs(width)
    return area
def with_gap(
    size: tuple, gap: int | float, *, minus_gap: bool = False
) -> tuple[int | float, ...]:
    new_size = []
    gap = abs(gap)
    if minus_gap:
        gap = -gap
    for side in size:
        new = abs(side) + gap
        new_size.append(new)
    return tuple(new_size)
def count_item_in_total_v(a, b):
    """Скільки об'ємів складової частини в об'ємі загальному.
    Приймає параметри сторін в форматі (довжина, ширина, висота)
    """
    one = block_volume(*a[:2], height=a[2])
    two = block_volume(*b[:2], height=b[2])
    if two > one:
        one, two = two, one
    return one // two
