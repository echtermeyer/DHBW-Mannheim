import unittest

from vorlesung05.csv_read import *

root = Path(__file__).parent
to_read = root / "test_data.csv"


class ReaderTest(unittest.TestCase):
    def test_currency_instance_creation(self):
        errors = []

        try:
            reader = CurrencyCsvRead(to_read, )
            reader.read_file()
        except BaseException as e:
            errors.append(e)

        self.assertEqual(errors, [])

    def test_currency_file_read(self):
        reader = CurrencyCsvRead(to_read, )
        reader.read_file()

        self.assertNotEqual(reader.raw_data, None)
        self.assertNotEqual(reader.raw_data, reader.processed_data)

    def test_row_property(self):
        reader = CurrencyCsvRead(to_read)
        reader.read_file()

        self.assertEqual(reader.rows, 5)



