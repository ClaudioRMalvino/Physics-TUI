import unittest

from typing import List, Any
from physics_TUI.chapters.chapter12 import Chapter12


class Testyoung_modulus(unittest.TestCase):
    """
    Tests the young_modulus calculation method
    """

    def test_solving_for_young_mod(self) -> None:
        """
        Function tests solving for the Young modulus (young_mod)
        """

        # Initial conditions

        force: List[float] = [100.0, 100.0, 100.0]
        cross_section: List[float] = [0.5, 0.5, 0.5]
        init_length: List[float] = [0.0, 2.0, 2.0]
        delta_length: List[float] = [0.01, -0.01, 0.01]

        expected: List[Any] = [
            ValueError(
                "The initial length \
                    and cross section cannot be less than or equal to zero."
            ),
            ValueError("The change in length cannot be less than zero."),
            40000.0,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter12.Calculate.young_modulus(
                        force=force[i],
                        cross_section=cross_section[i],
                        init_length=init_length[i],
                        delta_length=delta_length[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter12.Calculate.young_modulus(
                    force=force[i],
                    cross_section=cross_section[i],
                    init_length=init_length[i],
                    delta_length=delta_length[i],
                )
                self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_force(self) -> None:
        """
        Function tests solving for the applied force (force)
        """

        # Initial conditions

        young_mod: List[float] = [40000.0]
        cross_section: List[float] = [0.5]
        init_length: List[float] = [2.0]
        delta_length: List[float] = [0.01]

        expected: List[Any] = [100.0]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter12.Calculate.young_modulus(
                        young_mod=young_mod[i],
                        cross_section=cross_section[i],
                        init_length=init_length[i],
                        delta_length=delta_length[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter12.Calculate.young_modulus(
                    young_mod=young_mod[i],
                    cross_section=cross_section[i],
                    init_length=init_length[i],
                    delta_length=delta_length[i],
                )
                self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_cross_section(self) -> None:
        """
        Function tests solving for the cross sectional area (cross_section)
        """

        # Initial conditions

        young_mod: List[float] = [0.0, 40000.0]
        force: List[float] = [100.0, 100.0]
        init_length: List[float] = [2.0, 2.0]
        delta_length: List[float] = [0.01, 0.01]

        expected: List[Any] = [
            ValueError("Division by zero is undefined."),
            0.5,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter12.Calculate.young_modulus(
                        young_mod=young_mod[i],
                        force=force[i],
                        init_length=init_length[i],
                        delta_length=delta_length[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter12.Calculate.young_modulus(
                    young_mod=young_mod[i],
                    force=force[i],
                    init_length=init_length[i],
                    delta_length=delta_length[i],
                )
                self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_init_length(self) -> None:
        """
        Function tests solving for the initial length (init_length)
        """

        # Initial conditions

        young_mod: List[float] = [40000.0, 40000.0]
        force: List[float] = [0.0, 100.0]
        cross_section: List[float] = [0.5, 0.5]
        delta_length: List[float] = [0.01, 0.01]

        expected: List[Any] = [
            ValueError("Division by zero is undefined."),
            2.0,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter12.Calculate.young_modulus(
                        young_mod=young_mod[i],
                        force=force[i],
                        cross_section=cross_section[i],
                        delta_length=delta_length[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter12.Calculate.young_modulus(
                    young_mod=young_mod[i],
                    force=force[i],
                    cross_section=cross_section[i],
                    delta_length=delta_length[i],
                )
                self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_delta_length(self) -> None:
        """
        Function tests solving for the change in length (delta_length)
        """

        # Initial conditions

        young_mod: List[float] = [0.0, 40000.0]
        force: List[float] = [100.0, 100.0]
        cross_section: List[float] = [0.5, 0.5]
        init_length: List[float] = [2.0, 2.0]

        expected: List[Any] = [
            ValueError("Divison by zero is undefined."),
            0.01,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter12.Calculate.young_modulus(
                        young_mod=young_mod[i],
                        force=force[i],
                        cross_section=cross_section[i],
                        init_length=init_length[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter12.Calculate.young_modulus(
                    young_mod=young_mod[i],
                    force=force[i],
                    cross_section=cross_section[i],
                    init_length=init_length[i],
                )
                self.assertAlmostEqual(result, expected[i], places=4)


class Testbulk_modulus(unittest.TestCase):
    """
    Tests the bulk_modulus calculation method
    """

    def test_solving_for_bulk_mod(self) -> None:
        """
        Function tests solving for the bulk modulus (bulk_mod)
        """

        # Initial conditions

        delta_pressure: List[float] = [100.0, 100.0]
        init_volume: List[float] = [2.0, 2.0]
        delta_volume: List[float] = [0.0, -0.01]

        expected: List[Any] = [
            ValueError("Division by zero is undefined."),
            20000.0,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter12.Calculate.bulk_modulus(
                        delta_pressure=delta_pressure[i],
                        init_volume=init_volume[i],
                        delta_volume=delta_volume[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter12.Calculate.bulk_modulus(
                    delta_pressure=delta_pressure[i],
                    init_volume=init_volume[i],
                    delta_volume=delta_volume[i],
                )
                self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_delta_pressure(self) -> None:
        """
        Function tests solving for the change in pressure (delta_pressure)
        """

        # Initial conditions

        bulk_mod: List[float] = [20000.0]
        init_volume: List[float] = [2.0]
        delta_volume: List[float] = [-0.01]

        expected: List[Any] = [100.0]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter12.Calculate.bulk_modulus(
                        bulk_mod=bulk_mod[i],
                        init_volume=init_volume[i],
                        delta_volume=delta_volume[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter12.Calculate.bulk_modulus(
                    bulk_mod=bulk_mod[i],
                    init_volume=init_volume[i],
                    delta_volume=delta_volume[i],
                )
                self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_init_volume(self) -> None:
        """
        Function tests solving for the initial volume (init_volume)
        """

        # Initial conditions

        bulk_mod: List[float] = [20000.0, 20000.0]
        delta_pressure: List[float] = [0.0, 100.0]
        delta_volume: List[float] = [-0.01, -0.01]

        expected: List[Any] = [
            ValueError("Division by zero is undefined."),
            2.0,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter12.Calculate.bulk_modulus(
                        bulk_mod=bulk_mod[i],
                        delta_pressure=delta_pressure[i],
                        delta_volume=delta_volume[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter12.Calculate.bulk_modulus(
                    bulk_mod=bulk_mod[i],
                    delta_pressure=delta_pressure[i],
                    delta_volume=delta_volume[i],
                )
                self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_delta_volume(self) -> None:
        """
        Function tests solving for the change in volume (delta_volume)
        """

        # Initial conditions

        bulk_mod: List[float] = [20000.0, 0.0, 20000.0]
        delta_pressure: List[float] = [100.0, 100.0, 100.0]
        init_volume: List[float] = [0.0, 2.0, 2.0]

        expected: List[Any] = [
            ValueError("The volume of the object must be greater than zero."),
            ValueError("Division by zero is undefined."),
            -0.01,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter12.Calculate.bulk_modulus(
                        bulk_mod=bulk_mod[i],
                        delta_pressure=delta_pressure[i],
                        init_volume=init_volume[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter12.Calculate.bulk_modulus(
                    bulk_mod=bulk_mod[i],
                    delta_pressure=delta_pressure[i],
                    init_volume=init_volume[i],
                )
                self.assertAlmostEqual(result, expected[i], places=4)


class Testshear_modulus(unittest.TestCase):
    """
    Tests the shear_modulus calculation method
    """

    def test_solving_for_shear_mod(self) -> None:
        """
        Function tests solving for the shear modulus (shear_mod)
        """

        # Initial conditions

        force: List[float] = [50.0, 50.0, 50.0]
        cross_section: List[float] = [0.25, 0.25, 0.25]
        init_length: List[float] = [-1.0, 4.0, 4.0]
        delta_layers: List[float] = [0.02, -0.02, 0.02]

        expected: List[Any] = [
            ValueError(
                "The initial length \
                    and cross section cannot be less than or equal to zero."
            ),
            ValueError("The change in length cannot be less than zero."),
            40000.0,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter12.Calculate.shear_modulus(
                        force=force[i],
                        cross_section=cross_section[i],
                        init_length=init_length[i],
                        delta_layers=delta_layers[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter12.Calculate.shear_modulus(
                    force=force[i],
                    cross_section=cross_section[i],
                    init_length=init_length[i],
                    delta_layers=delta_layers[i],
                )
                self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_force(self) -> None:
        """
        Function tests solving for the applied force (force)
        """

        # Initial conditions

        shear_mod: List[float] = [40000.0]
        cross_section: List[float] = [0.25]
        init_length: List[float] = [4.0]
        delta_layers: List[float] = [0.02]

        expected: List[Any] = [50.0]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter12.Calculate.shear_modulus(
                        shear_mod=shear_mod[i],
                        cross_section=cross_section[i],
                        init_length=init_length[i],
                        delta_layers=delta_layers[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter12.Calculate.shear_modulus(
                    shear_mod=shear_mod[i],
                    cross_section=cross_section[i],
                    init_length=init_length[i],
                    delta_layers=delta_layers[i],
                )
                self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_cross_section(self) -> None:
        """
        Function tests solving for the cross sectional area (cross_section)
        """

        # Initial conditions

        shear_mod: List[float] = [40000.0, 40000.0]
        force: List[float] = [50.0, 50.0]
        init_length: List[float] = [4.0, 4.0]
        delta_layers: List[float] = [0.0, 0.02]

        expected: List[Any] = [
            ValueError("Division by zero is undefined."),
            0.25,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter12.Calculate.shear_modulus(
                        shear_mod=shear_mod[i],
                        force=force[i],
                        init_length=init_length[i],
                        delta_layers=delta_layers[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter12.Calculate.shear_modulus(
                    shear_mod=shear_mod[i],
                    force=force[i],
                    init_length=init_length[i],
                    delta_layers=delta_layers[i],
                )
                self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_init_length(self) -> None:
        """
        Function tests solving for the initial length (init_length)
        """

        # Initial conditions

        shear_mod: List[float] = [40000.0, 40000.0]
        force: List[float] = [0.0, 50.0]
        cross_section: List[float] = [0.25, 0.25]
        delta_layers: List[float] = [0.02, 0.02]

        expected: List[Any] = [
            ValueError("Division by zero is undefined."),
            4.0,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter12.Calculate.shear_modulus(
                        shear_mod=shear_mod[i],
                        force=force[i],
                        cross_section=cross_section[i],
                        delta_layers=delta_layers[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter12.Calculate.shear_modulus(
                    shear_mod=shear_mod[i],
                    force=force[i],
                    cross_section=cross_section[i],
                    delta_layers=delta_layers[i],
                )
                self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_delta_layers(self) -> None:
        """
        Function tests solving for the shift of the layers (delta_layers)
        """

        # Initial conditions

        shear_mod: List[float] = [0.0, 40000.0]
        force: List[float] = [50.0, 50.0]
        cross_section: List[float] = [0.25, 0.25]
        init_length: List[float] = [4.0, 4.0]

        expected: List[Any] = [
            ValueError("Divison by zero is undefined."),
            0.02,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter12.Calculate.shear_modulus(
                        shear_mod=shear_mod[i],
                        force=force[i],
                        cross_section=cross_section[i],
                        init_length=init_length[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter12.Calculate.shear_modulus(
                    shear_mod=shear_mod[i],
                    force=force[i],
                    cross_section=cross_section[i],
                    init_length=init_length[i],
                )
                self.assertAlmostEqual(result, expected[i], places=4)
