from datetime import date
from pprint import pprint
from typing import List, Tuple

import pywikibot

# https://www.wikidata.org/wiki/Wikidata:Pywikibot_-_Python_3_Tutorial/Setting_up_Shop
site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()


def main():
    pprint(extract("Q84055514"))


def extract(page: str) -> List[Tuple[date, int]]:
    item = pywikibot.ItemPage(repo, page)
    return sorted([
        (
            to_date(e.qualifiers['P585'][0].getTarget()),
            int(e.getTarget().amount),
        )
        for e in item.get()['claims']['P1603']
    ],
        key=lambda a: a[0])


def to_date(data: pywikibot.WbTime) -> date:
    return date(data.year, data.month, data.day)


main()
