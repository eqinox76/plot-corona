from datetime import date
from typing import List, Tuple

import plotly.graph_objects as go
import pywikibot

# pywikibot.config.verbose_output = 1
site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()


def main():
    data = {
        "india": extract("Q84055514"),
        "italy": extract("Q84104992"),
        "germany": extract("Q83889294"),
        "us": extract("Q83873577"),
        "russia": extract("Q84098939"),
        "spain": extract("Q84166704"),
        "japan": extract("Q83872291")
    }

    fig = go.Figure(
        data=[
            go.Scatter(x=[i[0] for i in data[country]],
                       y=[i[1] for i in data[country]],
                       mode='lines+markers',
                       name=country)
            for country in data
        ],
        layout=go.Layout(
            title=go.layout.Title(text="plot-corona"),
            yaxis_type="log"
        )
    )
    fig.show()


def extract(page: str) -> List[Tuple[date, int]]:
    item = pywikibot.ItemPage(repo, page)
    return sorted([
        (
            to_date(e.qualifiers['P585'][0].getTarget()),
            int(e.getTarget().amount),
        )
        for e in item.get()['claims']['P1603'] if 'P585' in e.qualifiers
    ],
        key=lambda a: a[0])


def to_date(data: pywikibot.WbTime) -> date:
    return date(data.year, data.month, data.day)


main()
