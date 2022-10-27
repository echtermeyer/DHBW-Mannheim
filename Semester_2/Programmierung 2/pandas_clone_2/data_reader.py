import json
from datetime import datetime
from pathlib import Path
from typing import Union, List, Dict

root = Path(__file__)


class OurDataFormat:
    """
    data store
    - dictionary approach
    """

    def __init__(self, raw_data, dtypes, date_pattern):
        self.data = raw_data
        self.columns = list(self.data.keys())

        self.dtypes = dtypes
        self.date_pattern = date_pattern

        self.change_dtypes()

    def change_dtypes(self):
        """
        Converts initial string values to corresponding data types
        :return:
        """
        for idx, (key, value) in enumerate(self.data.items()):
            if self.dtypes[idx] == "date":
                self.data[key] = [OurDataFormat.str_to_datetime(i, self.date_pattern) for i in value]
            else:
                self.data[key] = list(map(self.dtypes[idx], self.data[key]))

    # def get_column(self, col: str | int) -> List:  - ab python 3.10
    def get_column(self, col: Union[str, int]) -> List:
        """
        :param col: colum name or index
        :return:
        """
        return self.data[col] if isinstance(col, str) else self.data[self.columns[col]]

    def get_row(self, row: int) -> List:
        """
        :param row: index of row
        :return: list with row
        """
        return [value[row] for value in self.data.values()]

    def sum_up_column(self, col: Union[str, int]):
        data_to_sum_up = self.get_column(col)

        if any(
                [not isinstance(x, (int, float)) for x in data_to_sum_up]
        ):
            raise ValueError("contains at least one value not being a number!")

        try:
            return sum(data_to_sum_up)  # assuming this a list
        except ValueError:
            raise  # custom exception? welche?

    @classmethod
    def str_to_datetime(cls, str_date, date_pattern):
        """
        Helper method, to parse our standard date format month/day/year to datetime.
        """
        try:
            return datetime.strptime(str_date, date_pattern)
        except ValueError:
            print(f"{str_date} cannot be parsed!")

    @property
    def shape(self):
        return len(self.columns), len(self.data[self.columns[0]])


class DataReader:

    def __init__(self, path: Union[str, Path], dtypes: List, date_pattern: str = "%d/%M/%y"):
        """
        bla blubb
        :param path: path to file to read, can be str or pathlib Path
        :param date_pattern: pattern following datetime conventions
        """
        self.path = path
        self.dtypes = dtypes

        self.raw_data = self.read_file()
        self.data: OurDataFormat = OurDataFormat(self.raw_data, self.dtypes, date_pattern)

        self.columns = None

    def read_file(self):
        """
        Data mangling: process raw data to our designated format
        :return: None
        """
        # TODO: bitte lösen!
        raise NotImplementedError

    def get_column(self, col: Union[str, int]) -> List:
        return self.data.get_column(col)

    def get_row(self, row: int) -> List:
        return self.data.get_row(row)

    def get_sum(self, col: Union[str, int]):
        return self.data.sum_up_column(col)

    @property
    def shape(self):
        return self.data.shape


class CSVReader(DataReader):

    def read_file(self):
        dataframe = {}
        with open(self.path, "r") as f:
            for idx, row in enumerate(f):
                words = row.strip("\n").split(", ")

                if idx == 0:
                    self.columns = words
                    for key in self.columns:
                        dataframe[key] = []
                else:
                    for key, value in list(zip(self.columns, words)):
                        dataframe[key].append(value)

            return dataframe


class JSONReader(DataReader):

    def read_file(self):
        with open(self.path) as f:
            data = json.load(f)

            dataframe = {}
            for idx, element in enumerate(data):
                if idx == 0:
                    self.columns = element.keys()
                    for key, value in element.items():
                        dataframe[key] = [value]
                else:
                    for key, value in element.items():
                        dataframe[key].append(value)

            return dataframe
