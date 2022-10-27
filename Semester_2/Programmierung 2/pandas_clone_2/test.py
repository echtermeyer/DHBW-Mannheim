from pathlib import Path
from data_reader import CSVReader, JSONReader

data_csv = Path("APPLE-HistoricalPrices.csv")
data_json = Path("APPLE-HistoricalPrices.json")

dtypes = ["date", float, float, float, float, int]
json_reader = JSONReader(data_json, dtypes, date_pattern="%Y-%m-%dT%H:%M:%S.%fZ")
print(json_reader.shape)
