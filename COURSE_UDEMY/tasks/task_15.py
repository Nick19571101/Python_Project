"""Module for processing data exchange.
Функції:
- get_data(): returns a list of exchange points and the markup factor.
- get_exchange_rate(): returns the exchange rate.
- get_percent_of(): calculates the percentage of a fraction of a value.
- get_procesed_data(): returns a list of interest rates and an updated list of exchange points.
"""


def get_data() -> list[list[str | float]]:
    """Returns a list of exchange points and the markup factor.
    Returns:
        list[list[str | float]]: list of exchange offices in the format [id, value]
    """
    return [
        ["44519", 0.91],
        ["96424", 0.9],
        ["345543", 0.9],
        ["44246", 0.92],
        ["64687", 0.91],
        ["86776", 0.91],
    ]


def get_exchange_rate() -> float:
    """Returns the currency exchange rate.
    Returns:
        float: currency exchange rate
    """
    return 0.89


def get_percent_of(value: float, part: float) -> float | bool:
    """Returns the percentage that is part of value.
    Args:
        value (float): base value (e.g. exchange rate)
        part (float): part (for example, exchange rate in exchange point)
    Returns:
        float: percentage rounded to two digits
        False: if the input data is not correct
    """
    if value <= 0 or part < 0:
        return False
    return round(part / value * 100, 2)


def get_processed_data() -> tuple[list[float], list[list[str | float]]]:
    """Processes a list of exchange points and adds a percentage of the base rate to each.
    Returns:
        tuple[list[float], list[list[str | float]]]:
            - list of procents (float),
            - updated list of exchange offices with added percent
    """
    percent_list = []
    exchangers = get_data()
    exchange_rate = get_exchange_rate()
    for exchanger in exchangers:
        percent = get_percent_of(exchange_rate, exchanger[1])
        if percent:
            percent_list.append(percent)
            exchanger.append(percent)
    return percent_list, exchangers


if __name__ == "__main__":
    x, y = get_processed_data()
    print(x)  # Підсумок: [102.25, 101.12, 101.12, 103.37, 102.25, 102.25]
