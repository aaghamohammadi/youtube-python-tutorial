import pandas as pd

from tabulate import tabulate

data = pd.read_csv("data.csv", index_col=0)

print(tabulate(data, headers=data.columns, tablefmt="latex_booktabs", floatfmt=(".3f")))
