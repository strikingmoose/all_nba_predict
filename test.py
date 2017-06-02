import pandas as pd

test = pd.read_html(
    'https://en.wikipedia.org/wiki/The_Godfather_(film_series)',
    header = 0
)

print test[test['Character'].contains('Michael')]