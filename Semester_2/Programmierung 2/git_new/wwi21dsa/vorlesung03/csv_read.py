import json
from datetime import datetime
from pathlib import Path
from typing import Union, List

root = Path(__file__)


class OurDataFormat:
    """
    data store
    - list of lists approach
    - dictionary approach
    """
    def __init__(self):
        self.data = None

    # def get_column(self, col: str | int) -> List:  - ab python 3.10
    def get_column(self, col: Union[str, int]) -> List:
        """
        :param col: colum name or index
        :return:
        """
        # TODO: Daten aus Datenstruktur holen
        raise NotImplementedError

    def get_row(self):
        """"""
        raise NotImplementedError


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


class DataReader:

    def __init__(self, path: Union[str, Path], date_pattern: str):
        """
        bla blubb
        :param path: path to file to read, can be str or pathlib Path
        :param date_pattern: pattern following datetime conventions
        """
        self.path = path
        self.raw_data = None
        self.data = []  # eure Wahl -> designated data format

    def read_file(self):
        with open(self.path) as f:
            self.raw_data = f.readlines()

    def pre_process_data(self):
        """
        Data mangling: process raw data to our designated format
        :return: None
        """
        # TODO: bitte lösen!
        raise NotImplementedError

    @classmethod
    def str_to_datetime(cls, str_date, pattern="%m/%d/%y"):
        """
        Helper method, to parse our standard date format month/day/year to datetime.
        """
        try:
            return datetime.strptime(str_date, pattern)
        except ValueError:
            print(f"{str_date} cannot be parsed!")


class CsvRead(DataReader):

    def pre_process_data(self):
        """
        Data mangling: process raw CSV data to our designated format
        :return: None
        """
        # TODO: bitte lösen!
        raise NotImplementedError


class JSONReader(DataReader):

    def read_file(self):
        with open(self.path) as f:
            self.raw_data = json.load(f)

    def pre_process_data(self):
        """
        Data mangling: process raw CSV data to our designated format
        :return: None
        """
        # TODO: bitte lösen!
        raise NotImplementedError

