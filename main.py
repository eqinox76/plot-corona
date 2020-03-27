from datetime import date
from typing import List, Tuple

import plotly.graph_objects as go
import plotly.subplots as subplots
import pywikibot
import rate

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
        "japan": extract("Q83872291"),
        "china": extract("Q83872271"),
        "france": extract("Q83873593")
    }

    fig = subplots.make_subplots(rows=1, cols=2, shared_yaxes=True)

    for country in data:
        fig.add_trace(
            go.Scatter(x=[i[0] for i in data[country]],
                       y=[i[1] for i in data[country]],
                       mode='lines+markers',
                       name=country),
            row=1,
            col=1
        )

    growth = {c: rate.approximateGrowth(data[c]) for c in data}

    for country in data:
        fig.add_trace(
            go.Scatter(x=[i[0] for i in growth[country]],
                       y=[i[1] * 100 for i in growth[country]],
                       mode='lines+markers',
                       name=country),
            row=1,
            col=2
        )
    fig.update_layout(
        title_text="plot-corona",
        yaxis_type="log"
    )
    fig.show()


def extract(page: str) -> List[Tuple[date, int]]:
    item = pywikibot.ItemPage(repo, page)
    result = {}
    for e in item.get()['claims']['P1603']:
        if 'P585' in e.qualifiers:
            k = to_date(e.qualifiers['P585'][0].getTarget())
            v = int(e.getTarget().amount)
            # need to deduplicate
            if k not in result or result[k] < v:
                result[k] = v

    return sorted([(k, result[k]) for k in result.keys()], key= lambda a: a[0])


def to_date(data: pywikibot.WbTime) -> date:
    return date(data.year, data.month, data.day)

main()
