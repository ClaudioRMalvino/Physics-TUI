import unittest

from typing import List, Any
from math import pi
from physics_TUI.chapters.chapter14 import Chapter14


class Testhydrostatic_pressure(unittest.TestCase):
    """
    Tests the hydrostatic_pressure calculation method
    """

    def test_solving_for_pressure(self) -> None:
        """
        Function tests solving for the hydrostatic pressure (pressure)
        """

        # Initial conditions
        pressure_atm: List[float] = [101325.0]
        density: List[float] = [1000.0]
        depth: List[float] = [10.0]

        expected: List[Any] = [199525.0]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter14.Calculate.hydrostatic_pressure(
                        pressure_atm=pressure_atm[i], density=density[i], depth=depth[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter14.Calculate.hydrostatic_pressure(
                    pressure_atm=pressure_atm[i], density=density[i], depth=depth[i]
                )
                self.assertAlmostEqual(result, expected[i], places=2)

    def test_solving_for_density(self) -> None:
        """
        Function tests solving for the density of the fluid (density)
        """

        # Initial conditions
        pressure: List[float] = [199525.0, 199525.0]
        pressure_atm: List[float] = [101325.0, 101325.0]
        depth: List[float] = [10.0, 0.0]

        expected: List[Any] = [
            1000.0,
            ValueError("Division by zero is undefined."),
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter14.Calculate.hydrostatic_pressure(
                        pressure=pressure[i], pressure_atm=pressure_atm[i], depth=depth[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter14.Calculate.hydrostatic_pressure(
                    pressure=pressure[i], pressure_atm=pressure_atm[i], depth=depth[i]
                )
                self.assertAlmostEqual(result, expected[i], places=2)

    def test_solving_for_depth(self) -> None:
        """
        Function tests solving for the depth (depth)
        """

        # Initial conditions
        pressure: List[float] = [-5.0]
        pressure_atm: List[float] = [101325.0]
        density: List[float] = [1000.0]

        expected: List[Any] = [
            ValueError("Hydrostatic or atmospheric pressure cannot be a negative value."),
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter14.Calculate.hydrostatic_pressure(
                        pressure=pressure[i],
                        pressure_atm=pressure_atm[i],
                        density=density[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter14.Calculate.hydrostatic_pressure(
                    pressure=pressure[i],
                    pressure_atm=pressure_atm[i],
                    density=density[i],
                )
                self.assertAlmostEqual(result, expected[i], places=2)


class Testpascals_principle(unittest.TestCase):
    """
    Tests the pascals_principle calculation method
    """

    def test_solving_for_force_2(self) -> None:
        """
        Function tests solving for the force applied by piston 2 (force_2)
        """

        # Initial conditions
        force_1: List[float] = [100.0]
        area_1: List[float] = [2.0]
        area_2: List[float] = [10.0]

        expected: List[Any] = [500.0]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter14.Calculate.pascals_principle(
                        force_1=force_1[i], area_1=area_1[i], area_2=area_2[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter14.Calculate.pascals_principle(
                    force_1=force_1[i], area_1=area_1[i], area_2=area_2[i]
                )
                self.assertAlmostEqual(result, expected[i], places=2)

    def test_solving_for_force_1(self) -> None:
        """
        Function tests solving for the force applied by piston 1 (force_1)
        """

        # Initial conditions
        area_1: List[float] = [2.0, 2.0]
        force_2: List[float] = [500.0, 500.0]
        area_2: List[float] = [10.0, 0.0]

        expected: List[Any] = [
            100.0,
            ValueError("Division by zero is undefined."),
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter14.Calculate.pascals_principle(
                        area_1=area_1[i], force_2=force_2[i], area_2=area_2[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter14.Calculate.pascals_principle(
                    area_1=area_1[i], force_2=force_2[i], area_2=area_2[i]
                )
                self.assertAlmostEqual(result, expected[i], places=2)


class Testcontinuity_const_density(unittest.TestCase):
    """
    Tests the continuity_const_density calculation method
    """

    def test_solving_for_velocity_2(self) -> None:
        """
        Function tests solving for the velocity of the fluid in nozzle 2 (velocity_2)
        """

        # Initial conditions
        area_1: List[float] = [2.0, -2.0]
        velocity_1: List[float] = [3.0, 3.0]
        area_2: List[float] = [1.5, 1.5]

        expected: List[Any] = [
            4.0,
            ValueError("Area cannot be less than or equal to zero."),
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter14.Calculate.continuity_const_density(
                        area_1=area_1[i], velocity_1=velocity_1[i], area_2=area_2[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter14.Calculate.continuity_const_density(
                    area_1=area_1[i], velocity_1=velocity_1[i], area_2=area_2[i]
                )
                self.assertAlmostEqual(result, expected[i], places=2)

    def test_solving_for_area_1(self) -> None:
        """
        Function tests solving for the area of nozzle 1 (area_1)
        """

        # Initial conditions
        velocity_1: List[float] = [0.0]
        area_2: List[float] = [1.5]
        velocity_2: List[float] = [4.0]

        expected: List[Any] = [
            ValueError("Divison by zero is undefined."),
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter14.Calculate.continuity_const_density(
                        velocity_1=velocity_1[i], area_2=area_2[i], velocity_2=velocity_2[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter14.Calculate.continuity_const_density(
                    velocity_1=velocity_1[i], area_2=area_2[i], velocity_2=velocity_2[i]
                )
                self.assertAlmostEqual(result, expected[i], places=2)


class Testcontinuity_const_general(unittest.TestCase):
    """
    Tests the continuity_const_general calculation method
    """

    def test_solving_for_velocity_2(self) -> None:
        """
        Function tests solving for the velocity of the fluid in nozzle 2 (velocity_2)
        """

        # Initial conditions
        density_1: List[float] = [1000.0, 0.0]
        area_1: List[float] = [2.0, 2.0]
        velocity_1: List[float] = [3.0, 3.0]
        density_2: List[float] = [500.0, 500.0]
        area_2: List[float] = [4.0, 4.0]

        expected: List[Any] = [
            3.0,
            ValueError("Density of a fluid cannot be less than or equal to zero."),
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter14.Calculate.continuity_const_general(
                        density_1=density_1[i],
                        area_1=area_1[i],
                        velocity_1=velocity_1[i],
                        density_2=density_2[i],
                        area_2=area_2[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter14.Calculate.continuity_const_general(
                    density_1=density_1[i],
                    area_1=area_1[i],
                    velocity_1=velocity_1[i],
                    density_2=density_2[i],
                    area_2=area_2[i],
                )
                self.assertAlmostEqual(result, expected[i], places=2)

    def test_solving_for_density_1(self) -> None:
        """
        Function tests solving for the density of the fluid in nozzle 1 (density_1)
        """

        # Initial conditions
        area_1: List[float] = [2.0, 2.0]
        velocity_1: List[float] = [3.0, 0.0]
        density_2: List[float] = [500.0, 500.0]
        area_2: List[float] = [4.0, 4.0]
        velocity_2: List[float] = [3.0, 3.0]

        expected: List[Any] = [
            1000.0,
            ValueError("Division by zero is undefined."),
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter14.Calculate.continuity_const_general(
                        area_1=area_1[i],
                        velocity_1=velocity_1[i],
                        density_2=density_2[i],
                        area_2=area_2[i],
                        velocity_2=velocity_2[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter14.Calculate.continuity_const_general(
                    area_1=area_1[i],
                    velocity_1=velocity_1[i],
                    density_2=density_2[i],
                    area_2=area_2[i],
                    velocity_2=velocity_2[i],
                )
                self.assertAlmostEqual(result, expected[i], places=2)


class Testbernoullis_equation(unittest.TestCase):
    """
    Tests the bernoullis_equation calculation method
    """

    def test_solving_for_pressure_2(self) -> None:
        """
        Function tests solving for the pressure of the fluid in moment 2 (pressure_2)
        """

        # Initial conditions
        density: List[float] = [1000.0, -1.0]
        pressure_1: List[float] = [200000.0, 200000.0]
        velocity_1: List[float] = [2.0, 2.0]
        height_1: List[float] = [10.0, 10.0]
        velocity_2: List[float] = [4.0, 4.0]
        height_2: List[float] = [2.0, 2.0]

        expected: List[Any] = [
            272560.0,
            ValueError("Density of a fluid cannot be less than or equal to zero."),
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter14.Calculate.bernoullis_equation(
                        density=density[i],
                        pressure_1=pressure_1[i],
                        velocity_1=velocity_1[i],
                        height_1=height_1[i],
                        velocity_2=velocity_2[i],
                        height_2=height_2[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter14.Calculate.bernoullis_equation(
                    density=density[i],
                    pressure_1=pressure_1[i],
                    velocity_1=velocity_1[i],
                    height_1=height_1[i],
                    velocity_2=velocity_2[i],
                    height_2=height_2[i],
                )
                self.assertAlmostEqual(result, expected[i], places=2)

    def test_solving_for_velocity_1(self) -> None:
        """
        Function tests solving for the velocity of the fluid in moment 1 (velocity_1)
        """

        # Initial conditions
        density: List[float] = [1000.0, 1000.0]
        pressure_1: List[float] = [200000.0, 300000.0]
        height_1: List[float] = [10.0, 0.0]
        pressure_2: List[float] = [272560.0, 200000.0]
        velocity_2: List[float] = [4.0, 0.0]
        height_2: List[float] = [2.0, 0.0]

        expected: List[Any] = [
            2.0,
            ValueError("Negative radicand yields an imaginary number"),
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter14.Calculate.bernoullis_equation(
                        density=density[i],
                        pressure_1=pressure_1[i],
                        height_1=height_1[i],
                        pressure_2=pressure_2[i],
                        velocity_2=velocity_2[i],
                        height_2=height_2[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter14.Calculate.bernoullis_equation(
                    density=density[i],
                    pressure_1=pressure_1[i],
                    height_1=height_1[i],
                    pressure_2=pressure_2[i],
                    velocity_2=velocity_2[i],
                    height_2=height_2[i],
                )
                self.assertAlmostEqual(result, expected[i], places=2)

    def test_solving_for_density(self) -> None:
        """
        Function tests solving for the density of the fluid (density)
        """

        # Initial conditions
        pressure_1: List[float] = [200000.0]
        velocity_1: List[float] = [2.0]
        height_1: List[float] = [10.0]
        pressure_2: List[float] = [272560.0]
        velocity_2: List[float] = [4.0]
        height_2: List[float] = [2.0]

        expected: List[Any] = [1000.0]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter14.Calculate.bernoullis_equation(
                        pressure_1=pressure_1[i],
                        velocity_1=velocity_1[i],
                        height_1=height_1[i],
                        pressure_2=pressure_2[i],
                        velocity_2=velocity_2[i],
                        height_2=height_2[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter14.Calculate.bernoullis_equation(
                    pressure_1=pressure_1[i],
                    velocity_1=velocity_1[i],
                    height_1=height_1[i],
                    pressure_2=pressure_2[i],
                    velocity_2=velocity_2[i],
                    height_2=height_2[i],
                )
                self.assertAlmostEqual(result, expected[i], places=2)


class Testviscocity(unittest.TestCase):
    """
    Tests the viscocity calculation method
    """

    def test_solving_for_viscocity(self) -> None:
        """
        Function tests solving for the viscocity of the fluid (viscocity)
        """

        # Initial conditions
        force: List[float] = [10.0, 10.0, 10.0]
        distance: List[float] = [2.0, 2.0, -1.0]
        area: List[float] = [5.0, 5.0, 5.0]
        velocity: List[float] = [4.0, 0.0, 4.0]

        expected: List[Any] = [
            1.0,
            ValueError("Division by zero is undefined."),
            ValueError(
                "Dimensions of length and area cannot be less than or equal to zero."
            ),
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter14.Calculate.viscocity(
                        force=force[i],
                        distance=distance[i],
                        area=area[i],
                        velocity=velocity[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter14.Calculate.viscocity(
                    force=force[i],
                    distance=distance[i],
                    area=area[i],
                    velocity=velocity[i],
                )
                self.assertAlmostEqual(result, expected[i], places=2)

    def test_solving_for_force(self) -> None:
        """
        Function tests solving for the force (force)
        """

        # Initial conditions
        viscocity: List[float] = [1.0]
        distance: List[float] = [2.0]
        area: List[float] = [5.0]
        velocity: List[float] = [4.0]

        expected: List[Any] = [10.0]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter14.Calculate.viscocity(
                        viscocity=viscocity[i],
                        distance=distance[i],
                        area=area[i],
                        velocity=velocity[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter14.Calculate.viscocity(
                    viscocity=viscocity[i],
                    distance=distance[i],
                    area=area[i],
                    velocity=velocity[i],
                )
                self.assertAlmostEqual(result, expected[i], places=2)


class Testpoiseuilles_law_resistance(unittest.TestCase):
    """
    Tests the poiseuilles_law_resistance calculation method
    """

    def test_solving_for_resistance(self) -> None:
        """
        Function tests solving for the resistance to laminar flow (resistance)
        """

        # Initial conditions
        viscocity: List[float] = [2.0, 2.0]
        length: List[float] = [3.0, 0.0]
        radius: List[float] = [1.0, 1.0]

        expected: List[Any] = [
            48.0 / pi,
            ValueError(
                "Dimensions of length and radius cannot be less than or equal to zero."
            ),
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter14.Calculate.poiseuilles_law_resistance(
                        viscocity=viscocity[i], length=length[i], radius=radius[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter14.Calculate.poiseuilles_law_resistance(
                    viscocity=viscocity[i], length=length[i], radius=radius[i]
                )
                self.assertAlmostEqual(result, expected[i], places=2)

    def test_solving_for_radius(self) -> None:
        """
        Function tests solving for the radius of the tube (radius)
        """

        # Initial conditions
        resistance: List[float] = [48.0 / pi, 0.0]
        viscocity: List[float] = [2.0, 2.0]
        length: List[float] = [3.0, 3.0]

        expected: List[Any] = [
            1.0,
            ValueError("Division by zero is undefined."),
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter14.Calculate.poiseuilles_law_resistance(
                        resistance=resistance[i], viscocity=viscocity[i], length=length[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter14.Calculate.poiseuilles_law_resistance(
                    resistance=resistance[i], viscocity=viscocity[i], length=length[i]
                )
                self.assertAlmostEqual(result, expected[i], places=2)


class Testpoiseuilles_law(unittest.TestCase):
    """
    Tests the poiseuilles_law calculation method
    """

    def test_solving_for_flow(self) -> None:
        """
        Function tests solving for the flow rate (flow)
        """

        # Initial conditions
        viscocity: List[float] = [2.0, 2.0]
        length: List[float] = [5.0, 5.0]
        radius: List[float] = [1.0, -1.0]
        pressure_1: List[float] = [1000.0, 1000.0]
        pressure_2: List[float] = [200.0, 200.0]

        expected: List[Any] = [
            10.0 * pi,
            ValueError(
                "Dimensions of length and radius cannot be less than or equal to zero."
            ),
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter14.Calculate.poiseuilles_law(
                        viscocity=viscocity[i],
                        length=length[i],
                        radius=radius[i],
                        pressure_1=pressure_1[i],
                        pressure_2=pressure_2[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter14.Calculate.poiseuilles_law(
                    viscocity=viscocity[i],
                    length=length[i],
                    radius=radius[i],
                    pressure_1=pressure_1[i],
                    pressure_2=pressure_2[i],
                )
                self.assertAlmostEqual(result, expected[i], places=2)

    def test_solving_for_pressure_1(self) -> None:
        """
        Function tests solving for the pressure at point 1 (pressure_1)
        """

        # Initial conditions
        flow: List[float] = [10.0 * pi]
        viscocity: List[float] = [2.0]
        length: List[float] = [5.0]
        radius: List[float] = [1.0]
        pressure_2: List[float] = [200.0]

        expected: List[Any] = [1000.0]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter14.Calculate.poiseuilles_law(
                        flow=flow[i],
                        viscocity=viscocity[i],
                        length=length[i],
                        radius=radius[i],
                        pressure_2=pressure_2[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter14.Calculate.poiseuilles_law(
                    flow=flow[i],
                    viscocity=viscocity[i],
                    length=length[i],
                    radius=radius[i],
                    pressure_2=pressure_2[i],
                )
                self.assertAlmostEqual(result, expected[i], places=2)

    def test_solving_for_pressure_2(self) -> None:
        """
        Function tests solving for the pressure at point 2 (pressure_2)
        """

        # Initial conditions
        flow: List[float] = [10.0 * pi]
        viscocity: List[float] = [2.0]
        length: List[float] = [5.0]
        radius: List[float] = [1.0]
        pressure_1: List[float] = [1000.0]

        expected: List[Any] = [200.0]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter14.Calculate.poiseuilles_law(
                        flow=flow[i],
                        viscocity=viscocity[i],
                        length=length[i],
                        radius=radius[i],
                        pressure_1=pressure_1[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter14.Calculate.poiseuilles_law(
                    flow=flow[i],
                    viscocity=viscocity[i],
                    length=length[i],
                    radius=radius[i],
                    pressure_1=pressure_1[i],
                )
                self.assertAlmostEqual(result, expected[i], places=2)

    def test_solving_for_viscocity(self) -> None:
        """
        Function tests solving for the viscocity of the fluid (viscocity)
        """

        # Initial conditions
        flow: List[float] = [0.0]
        length: List[float] = [5.0]
        radius: List[float] = [1.0]
        pressure_1: List[float] = [1000.0]
        pressure_2: List[float] = [200.0]

        expected: List[Any] = [
            ValueError("Division by zero is undefined."),
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter14.Calculate.poiseuilles_law(
                        flow=flow[i],
                        length=length[i],
                        radius=radius[i],
                        pressure_1=pressure_1[i],
                        pressure_2=pressure_2[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter14.Calculate.poiseuilles_law(
                    flow=flow[i],
                    length=length[i],
                    radius=radius[i],
                    pressure_1=pressure_1[i],
                    pressure_2=pressure_2[i],
                )
                self.assertAlmostEqual(result, expected[i], places=2)
