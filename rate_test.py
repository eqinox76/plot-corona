import unittest
from datetime import date

import rate


class TestRate(unittest.TestCase):

    def test_approximateGrowthLinear(self):
        self.assertEqual(
            [
                (date(2020, 6, 13), 1.),
                (date(2020, 6, 14), 1.),
            ],
            rate.approximateGrowth([
                (date(2020, 6, 12), 10),
                (date(2020, 6, 13), 20),
                (date(2020, 6, 14), 40)
            ])
        )

    def test_approximateGrowth1_0to0_5(self):
        self.assertEqual(
            [
                (date(2020, 6, 13), 1.),
                (date(2020, 6, 14), 0.75),
                (date(2020, 6, 15), 0.625),
            ],
            rate.approximateGrowth([
                (date(2020, 6, 12), 10),
                (date(2020, 6, 13), 20),
                (date(2020, 6, 14), 30),
                (date(2020, 6, 15), 45)
            ])
        )

    def test_approximateGrowth1_0to0_5withHole(self):
        self.assertEqual(
            [
                (date(2020, 6, 14), 1.),
                (date(2020, 6, 15), 0.75),
            ],
            rate.approximateGrowth([
                (date(2020, 6, 12), 10),
                (date(2020, 6, 14), 30),
                (date(2020, 6, 15), 45)
            ])
        )


if __name__ == '__main__':
    unittest.main()
