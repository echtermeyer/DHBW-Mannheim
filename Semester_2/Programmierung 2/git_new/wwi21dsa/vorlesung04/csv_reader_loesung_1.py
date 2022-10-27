# Lösung von Amos Dinh, Ankit Gahi, Jan Mühlnikel und Jannik Völker DS21A

import json
from datetime import datetime
from pathlib import Path
from tokenize import String
from typing import Union, List, Optional

root = Path(__file__)


class OurDataFormat:
    """
    Date Store. Ermöglicht uns mit den eingelesenen, aufbereiteten Daten zu interagieren:
     - Zeile Auslesen
     - Spalte auslesen
     - Summe von Spalte
    """

    def __init__(self, the_data: List, columns: Optional[List] = None):
        self.data_columnbased = the_data
        self.data_rowbased = list(map(list, zip(*the_data)))
        self.columns = columns

    # def get_column(self, col: str | int) -> List:  - ab python 3.10
    def get_column(self, col: Union[str, int]) -> List:
        """
        Gibt die Werte einer Spalte zurück nach Namen oder Index
        :param col: Spaltenname ODER Spalten Index (int, 0-basiert)
        :return:
        """
        if isinstance(col, str) and col.strip() in self.columns:
            ind = self.columns.index(col.strip())
        elif isinstance(col, int) and len(self.columns) > col:
            ind = col
        else:
            raise IndexError("Index or name of column not found")

        return self.data_columnbased[ind]

    def get_row(self, row_index: int) -> List:
        """
        Gibt eine Zeile zurück
        - > Versuche es ohne for loop oder comprehension zu lösen
        :param row_index: Zeilennummer, 0-indiziert, 1. Zeile von self.data
        :return:
        """

        if len(self.data_rowbased) > row_index:
            return self.data_rowbased[row_index]
        else:
            raise IndexError("Index or name of column not found")

    def get_rows(self, rows_index: Union[range, List[int]]) -> List[List]:
        """
        Gibt Zeilen zurück:
        - range(3, 7) - > range funktion nutzen, mit Liste arbeiten
        :param rows_index: Zeilennummern als Liste oder slice, 0-indiziert, 1. Zeile von self.data
        :return: Ausgewählten Zeilen zurück als Liste
        """
        if isinstance(rows_index, list):
            return [self.get_row(ind) for ind in rows_index]
        elif isinstance(rows_index, range):
            return self.data_rowbased[
                rows_index.start : rows_index.stop : rows_index.step
            ]
        else:
            raise IndexError("Index not supported (Wrong type).")

    def sum_up_column(self, col: Union[str, int]):
        data_to_sum_up = self.get_column(col)

        if any([not isinstance(x, (int, float)) for x in data_to_sum_up]):
            raise ValueError("contains at least one value not being a number!")

        try:
            return sum(data_to_sum_up)  # assuming this a list
        except ValueError:
            raise  # custom exception? welche?


class DataReader:
    def __init__(self, path: Union[str, Path]):
        """
        Grundgedanke: Eine Klasse nur für das Einlesen von Daten zu schaffen.
        :param path: path to file to read, can be str or pathlib Path
        """
        self.path = path
        self.raw_data = None
        self.data: OurDataFormat = None  # eure Wahl -> designated data format
        # self.data.get_column(1)

    def read_file(self):
        with open(self.path) as f:
            self.raw_data = f.readlines()

    def pre_process_data(self):
        """
        Data mangling: process raw data to our designated format
        :return: None
        """
        raise NotImplementedError

    @classmethod
    def str_to_datetime(cls, str_date, pattern="%m/%d/%y"):
        """
        Helper method, to parse our standard date format month/day/year to datetime.
        :param str_date: In datetime zu umzuwandelnder String
        :param pattern: Datetime Direktiven
        :return:
        """
        try:
            return datetime.strptime(str_date, pattern)
        except ValueError:
            return str_date

    @classmethod
    def str_to_number(cls, str_data, float_notation="."):
        """
        Versucht Eingabewert in numerischen Wert zu verwandeln.
        Wenn nicht möglich wird der Eingabewert zurückgegeben.
        :param str_data:
        :param float_notation: Trennzeichen Floats, aktuelle nicht verwendet,
        wäre eine weitere Alternative Floats zu identifizieren.
        :return:
        """
        try:
            return int(str_data)
        except ValueError:
            pass
        try:
            return float(str_data)
        except ValueError:
            return str_data

    def optimistic_caster(self, data_str, date_pattern):
        """

        :param data_str:
        :param date_pattern:
        :return:
        """
        new_value = self.str_to_datetime(data_str, pattern=date_pattern)
        if isinstance(new_value, datetime):
            return new_value
        return self.str_to_number(data_str)


class CsvRead(DataReader):
    def __init__(
        self,
        path: Union[str, Path],
        sep=",",
        date_pattern: str = "%m/%d/%y",
    ):
        """

        :param path:
        :param sep:
        :param date_pattern:
        """
        super().__init__(path)
        self.sep = sep
        self.date_pattern = date_pattern
        self.processed_data: List[List] = [[]]
        self.columns: List = []

    def pre_process_data(self, header_row: Union[int, None] = None):
        """
        Data mangling: process raw CSV data to our designated format
        :return: None
        """
        data_index_row = 0  # erste Zeile mit Daten (nicht Spaltennamen)
        if header_row is not None:
            # Implementierung für max 1 Zeile mit Namen
            self.columns = [
                x.strip() for x in self.raw_data[header_row].split(self.sep)
            ]
            data_index_row = header_row + 1

        data = [
            [y.strip() for y in x.strip().split(self.sep)]
            for x in self.raw_data[data_index_row:]
        ]
        # Keinen Qualitätscheck, dass Struktur einheitlich ist.

        # transpose to columns
        data = list(map(list, zip(*data)))

        # brute force data parser
        for i, col in enumerate(data):
            processed_col = list(
                map(lambda x: self.optimistic_caster(x, self.date_pattern), col)
            )
            data[i] = processed_col

        self.data = data
        a = 42  # Hitchhikers Guide to the Galaxy


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


if __name__ == "__main__":
    d = CsvRead("APPLE-HistoricalPrices.csv")
    d.read_file()
    d.pre_process_data(header_row=0)
    data = OurDataFormat(the_data=d.data, columns=d.columns)
    # print(data.get_column(0))

    print(data.get_rows(range(0, 6, 2)))
    a = 42
