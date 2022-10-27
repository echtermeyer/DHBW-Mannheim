import json
from datetime import datetime
from pathlib import Path
from typing import Union, List, Optional, Dict

from vorlesung04.csv_read import DataReader

root = Path(__file__).parent


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

    @property
    def rows(self) -> int:
        """
        Anzahl der Zeilen
        :return:
        """
        return len(self.raw_data)


class CurrencyCsvRead(CsvRead):
    """
    Aufgabe
    dynamisch mehrere Währungen unterstützt:
    d = CurrencyCsvRead(...)
    currencies = {"EUR": 1.0, "USD": 1.05}
    setattr()
    d.sum_eur -> sum in Euro
    d.sum_usd -> sum in US Dollar
    d.sum_cad  -> sum in Kanadischen Dollar
    d.sum_gbp  -> sum in Brittischen Pfund Dollar

    Bonus:
    Währungskurse dynamisch ändern:
    d.usd = 1.10
    """

    def __init__(
        self,
        path: Union[str, Path],
        sep=",",
        date_pattern: str = "%m/%d/%y",
        currencies: Optional[Dict] = None,
    ):
        """

        :param path:
        :param sep:
        :param date_pattern:
        :param currencies: dict {"currency_code": wechselkurs zu EUR, ...}
        """
        super().__init__(path, sep, date_pattern)
        if not isinstance(currencies, dict):
            raise ValueError("provide a dict like {'currency code': rate}")
        self.currencies: Dict = {k.casefold(): v for k, v in currencies.items()}

        # für jede währung wir ein Klassenattribut mit value gesetzt
        for k, v in self.currencies.items():
            setattr(self, k, v)

    def __getattr__(self, item):
        """
        Diese Methode wird bei JEDEM Aufruf eines Attributes ausgeführt.
        So können auch "nicht existente" Attribute zurückgegeben werden
        :param item:
        :return:
        """
        print(item, "hi")
        # extra logik um unsere Konvention "sum_" + Währung zu bedienen:
        if str(item)[:4] == "sum_":
            try:
                item = str(item)[-3:]
                print(self.__dict__)
                return self.__dict__[item] * self.the_sum
            except AttributeError:
                print("Huh")
                pass
        # ab hier verhält sich __getattr__ wie gehabt

    def __setitem__(self, key, value):
        """
        Only currencies can be set, other attr are ignored
        :param key:
        :param value:
        :return:
        """
        print("Develeopedera")
        self.__dict__[key] = value
        print(self.__dict__)
        if key in self.currencies:
            setattr(self, key, value)

    @property
    def the_sum(self):
        """
        :return: Summe in EUR per default
        """
        # Demo hier würde statt range alle Werte der Spalte sum_column summiert
        return sum(range(1, 101))


if __name__ == "__main__":
    to_read = root / "../vorlesung04/APPLE-HistoricalPrices.csv"
    d = CurrencyCsvRead(to_read, currencies={"EUR": 1.0, "USD": 1.5, "GBP": 0.5})
    print("sugm_usd", d.sum_usd)
    print("deinemudder", d.usd)
    d.usd = 0.0
    print("sum_usd", d.sum_usd)
    a = 42
    d["dafasdf"] = 123
