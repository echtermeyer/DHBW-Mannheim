from pathlib import Path
from datetime import datetime

class PandasClone:
    def __init__(self):
        """
        
        """
        self.dataframe = {}
        self.columns = None

    def read_csv(self, path):
        with open(path, "r") as f:
            for idx, row in enumerate(f):
                words = row.strip("\n").split(", ")

                if idx == 0:
                    self.columns = words
                    for key in self.columns:
                        self.dataframe[key] = []
                else:
                    for key, value in list(zip(self.columns, words)):
                        self.dataframe[key].append(value)

    def get_sum(self, key):
        return sum(list(map(float, self.dataframe[key])))

    def weekly_aggregates_sum(self, key):
        aggregated_sums = []

        for date_r in self.dataframe[key]:
            date_f = datetime.strptime(date, "%d/%M/%y")

    def head(self):
        print(self.dataframe["Open"])


df = PandasClone()
df.read_csv(Path("data/APPLE-HistoricalPrices.csv"))

# print(df.get_sum("Close"))
print(df.weekly_aggregates_sum("Date"))
# df.head()
