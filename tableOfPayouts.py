import pandas as pd

table = pd.read_csv("keno payout.csv")


def getPayout(spots, hits):
    rowNum = table[(table['Spots'] == spots) & (table['Hits'] == hits)].index[0]
    return table.iloc[rowNum]['Payout']
