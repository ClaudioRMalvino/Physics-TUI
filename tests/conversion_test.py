import unittest
from typing import List
from unittest.case import TestCase

from physics_TUI.unit_converter import Energy, Length, Time


class TestLengthUnitConversion(unittest.TestCase):
    """
    Tests the conversion method within the Length class for unit conversion
    """

    def setUp(self) -> None:
        """
        Set up the Length instance for testing
        """
        self.length_converter = Length()

    def test_converting_from_meter_to_kilometer(self) -> None:
        """
        Function testrs converting from meters to kilometer 
        """

        # Test cases
        scalar: List[float] = [1.0, 30.0, 1000.0, 1500.0]
        meters: List[str] = ["meter", "meter", "meter", "meter"]
        kilometers: List[str] = ["kilometer",
                                 "kilometer", "kilometer", "kilometer"]

        expected: List[float] = [0.001, 0.03, 1.0, 1.5]

        for i in range(len(expected)):
            result = self.length_converter.conversion(
                scalar=scalar[i],
                from_unit=meters[i],
                to_unit=kilometers[i]
            )
            self.assertEqual(result, expected[i],)

    def test_converting_from_kilometer_to_meter(self) -> None:
        """
        Function testrs converting from meters to kilometer 
        """

        # Test cases
        scalar: List[float] = [1.0, 30.0, 0.5, 0.1]
        meters: List[str] = ["meter", "meter", "meter", "meter"]
        kilometers: List[str] = ["kilometer",
                                 "kilometer", "kilometer", "kilometer"]

        expected: List[float] = [1000, 30000, 500, 100]

        for i in range(len(expected)):
            result = self.length_converter.conversion(
                scalar=scalar[i],
                from_unit=kilometers[i],
                to_unit=meters[i]
            )
            self.assertEqual(result, expected[i],)

    def test_converting_from_nanometer_to_millimeter(self) -> None:
        """
        Function tests converting from nanometers to millimeter
        """

        # Test cases
        scalar: List[float] = [1.0, 30.0, 0.01, 250.0]
        nanometers: List[float] = ["nanometer",
                                   "nanometer", "nanometer", "nanometer",]
        millimeters: list[float] = ["millimeter",
                                    "millimeter", "millimeter", "millimeter",]

        expected: List[float] = [1.0E-6, 3.0E-5, 1.0E-8, 2.5E-4]

        for i in range(len(expected)):
            result: float = self.length_converter.conversion(
                scalar=scalar[i],
                from_unit=nanometers[i],
                to_unit=millimeters[i]
            )
            self.assertAlmostEqual(result, expected[i], places=6)

    def test_converting_from_imperial_to_metric(self) -> None:
        """
        Function tests convering from inches to meters
        """

        # Test cases
        scalar: List[float] = [1.0, 1.0, 2.0, 30.0]
        from_unit: List[str] = ["inch", "foot", "yard", "mile"]
        to_unit: List[str] = ["centimeter", "meter", "meter", "kilometer"]

        expected: List[float] = [2.54, 0.3048, 1.8288, 48.2803]

        for i in range(len(expected)):
            result: float = self.length_converter.conversion(
                scalar=scalar[i],
                from_unit=from_unit[i],
                to_unit=to_unit[i]
            )
            self.assertAlmostEqual(result, expected[i], places=2)

    def test_converting_from_metric_to_imperial(self) -> None:
        """
        Function tests convering from inches to meters
        """

        # Test cases
        scalar: List[float] = [1.0, 1.0, 2.0, 30.0]
        from_unit: List[str] = ["centimeter", "meter", "meter", "kilometer"]
        to_unit: List[str] = ["inch", "foot", "yard", "mile"]

        expected: List[float] = [0.393701, 3.2808, 2.187, 18.64]

        for i in range(len(expected)):
            result: float = self.length_converter.conversion(
                scalar=scalar[i],
                from_unit=from_unit[i],
                to_unit=to_unit[i]
            )
            self.assertAlmostEqual(result, expected[i], places=2)


class TestTimeUnitConversion(unittest.TestCase):
    """
    Tests the conversion method within the Time class for unit conversion
    """

    def setUp(self) -> None:
        """
        Set up the Time instance for testing
        """
        self.time_converter = Time()

    def test_converting_from_day_to_hour(self) -> None:
        """
        Function tests converting from days to hours
        (regression pin for the fixed day factor)
        """

        # Test cases
        scalar: List[float] = [1.0]
        from_unit: List[str] = ["day"]
        to_unit: List[str] = ["hour"]

        expected: List[float] = [24.0]

        for i in range(len(expected)):
            result: float = self.time_converter.conversion(
                scalar=scalar[i],
                from_unit=from_unit[i],
                to_unit=to_unit[i]
            )
            self.assertAlmostEqual(result, expected[i], places=6)

    def test_converting_from_week_to_day(self) -> None:
        """
        Function tests converting from weeks to days
        """

        # Test cases
        scalar: List[float] = [1.0]
        from_unit: List[str] = ["week"]
        to_unit: List[str] = ["day"]

        expected: List[float] = [7.0]

        for i in range(len(expected)):
            result: float = self.time_converter.conversion(
                scalar=scalar[i],
                from_unit=from_unit[i],
                to_unit=to_unit[i]
            )
            self.assertAlmostEqual(result, expected[i], places=6)


class TestEnergyUnitConversion(unittest.TestCase):
    """
    Tests the conversion method within the Energy class for unit conversion
    """

    def setUp(self) -> None:
        """
        Set up the Energy instance for testing
        """
        self.energy_converter = Energy()

    def test_converting_from_megawatt_hour_to_kilowatt_hour(self) -> None:
        """
        Function tests converting from megawatt-hours to kilowatt-hours
        (regression pin for the fixed MWh factor)
        """

        # Test cases
        scalar: List[float] = [1.0]
        from_unit: List[str] = ["megawatt-hour"]
        to_unit: List[str] = ["kilowatt-hour"]

        expected: List[float] = [1000.0]

        for i in range(len(expected)):
            result: float = self.energy_converter.conversion(
                scalar=scalar[i],
                from_unit=from_unit[i],
                to_unit=to_unit[i]
            )
            self.assertAlmostEqual(result, expected[i], places=6)

    def test_converting_from_kilocalorie_to_calorie(self) -> None:
        """
        Function tests converting from kilocalories to calories
        """

        # Test cases
        scalar: List[float] = [1.0]
        from_unit: List[str] = ["kilocalorie"]
        to_unit: List[str] = ["calorie"]

        expected: List[float] = [1000.0]

        for i in range(len(expected)):
            result: float = self.energy_converter.conversion(
                scalar=scalar[i],
                from_unit=from_unit[i],
                to_unit=to_unit[i]
            )
            self.assertAlmostEqual(result, expected[i], places=6)
