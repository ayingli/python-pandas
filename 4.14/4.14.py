import pandas

data = pandas.read_csv(
    'D:\\PDA\\4.14\\data.csv'
)

data['scale'] = round(
    (
        data.score-data.score.min()
    )/(
        data.score.max()-data.score.min()
    )
    , 2
)
