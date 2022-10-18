import pandas as pd

table = pd.read_csv("keno payout.csv")

nytable = pd.read_csv("NYLottery Payouts.csv")


def getPayout(spots, hits):
    rowNum = table[(table['Spots'] == spots) & (table['Hits'] == hits)].index[0]
    return table.iloc[rowNum]['Payout']

def getPayoutNY(spots, hits):
    rowNum = nytable[(nytable['Spots'] == spots) & (nytable['Hits'] == hits)].index[0]
    return nytable.iloc[rowNum]['Payout']