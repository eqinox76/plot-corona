from datetime import date
from typing import List, Tuple


def approximateGrowth(data: List[Tuple[date, int]]) -> List[Tuple[date, float]]:
    # filter low values
    data = list(filter(lambda x: x[1] >= 10, data))
    result = []
    approx = None

    for i, j in zip(data[:-1], data[1:]):
        diff = j[1] / float(i[1])
        diff = diff - 1

        days = (j[0] - i[0]).days
        diff = diff / days
        # linear approximation for a exponential growth will be very wrong
        for _ in range(days):
            if approx:
                approx = (approx + diff) / 2.
            else:
                approx = diff
        result.append((j[0], approx))

    return result
