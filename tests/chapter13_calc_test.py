import unittest

from typing import List, Any
from physics_TUI.chapters.chapter13 import Chapter13


class Testlaw_of_gravitation(unittest.TestCase):
    """
    Tests the law_of_gravitation calculation method
    """

    def test_solving_for_force_12(self) -> None:
        """
        Function tests solving for the gravitational force (force_12)
        """

        # Initial conditions

        mass_1: List[float] = [-1.0, 1.0e10, 1.0e10]
        mass_2: List[float] = [2.0e10, 2.0e10, 2.0e10]
        distance: List[float] = [100.0, -100.0, 100.0]

        expected: List[Any] = [
            ValueError(
                "We are operating with massive objects. \
                    Make sure all objects have a mass greater than zero."
            ),
            ValueError("Distance cannot be a negative value."),
            1334800.0,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter13.Calculate.law_of_gravitation(
                        mass_1=mass_1[i], mass_2=mass_2[i], distance=distance[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter13.Calculate.law_of_gravitation(
                    mass_1=mass_1[i], mass_2=mass_2[i], distance=distance[i]
                )
                self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_mass_1(self) -> None:
        """
        Function tests solving for the mass of object 1 (mass_1)
        """

        # Initial conditions

        force_12: List[float] = [1334800.0]
        mass_2: List[float] = [2.0e10]
        distance: List[float] = [100.0]

        # Expected values in units of 1e10 kg
        expected: List[Any] = [1.0]

        for i in range(len(expected)):
            result = Chapter13.Calculate.law_of_gravitation(
                force_12=force_12[i], mass_2=mass_2[i], distance=distance[i]
            )
            self.assertAlmostEqual(result / 1.0e10, expected[i], places=4)

    def test_solving_for_mass_2(self) -> None:
        """
        Function tests solving for the mass of object 2 (mass_2)
        """

        # Initial conditions

        force_12: List[float] = [1334800.0]
        mass_1: List[float] = [1.0e10]
        distance: List[float] = [100.0]

        # Expected values in units of 1e10 kg
        expected: List[Any] = [2.0]

        for i in range(len(expected)):
            result = Chapter13.Calculate.law_of_gravitation(
                force_12=force_12[i], mass_1=mass_1[i], distance=distance[i]
            )
            self.assertAlmostEqual(result / 1.0e10, expected[i], places=4)

    def test_solving_for_distance(self) -> None:
        """
        Function tests solving for the distance between the two bodies (distance)
        """

        # Initial conditions

        force_12: List[float] = [1334800.0]
        mass_1: List[float] = [1.0e10]
        mass_2: List[float] = [2.0e10]

        expected: List[Any] = [100.0]

        for i in range(len(expected)):
            result = Chapter13.Calculate.law_of_gravitation(
                force_12=force_12[i], mass_1=mass_1[i], mass_2=mass_2[i]
            )
            self.assertAlmostEqual(result, expected[i], places=4)


class Testgravitational_acceleration(unittest.TestCase):
    """
    Tests the gravitational_acceleration calculation method
    """

    def test_solving_for_g(self) -> None:
        """
        Function tests solving for the acceleration due to gravity (g)
        """

        # Initial conditions

        mass_body: List[float] = [1.0e24, 1.0e24]
        distance: List[float] = [0.0, 1.0e6]

        expected: List[Any] = [
            ValueError(
                "Distance cannot be a value that is \
                    less than or equal to zero."
            ),
            66.74,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter13.Calculate.gravitational_acceleration(
                        mass_body=mass_body[i], distance=distance[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter13.Calculate.gravitational_acceleration(
                    mass_body=mass_body[i], distance=distance[i]
                )
                self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_mass_body(self) -> None:
        """
        Function tests solving for the mass of the stellar body (mass_body)
        """

        # Initial conditions

        g: List[float] = [66.74]
        distance: List[float] = [1.0e6]

        # Expected values in units of 1e24 kg
        expected: List[Any] = [1.0]

        for i in range(len(expected)):
            result = Chapter13.Calculate.gravitational_acceleration(
                g=g[i], distance=distance[i]
            )
            self.assertAlmostEqual(result / 1.0e24, expected[i], places=4)

    def test_solving_for_distance(self) -> None:
        """
        Function tests solving for the radius of the stellar body (distance)
        """

        # Initial conditions

        g: List[float] = [66.74]
        mass_body: List[float] = [1.0e24]

        expected: List[Any] = [1.0e6]

        for i in range(len(expected)):
            result = Chapter13.Calculate.gravitational_acceleration(
                g=g[i], mass_body=mass_body[i]
            )
            self.assertAlmostEqual(result, expected[i], places=4)


class Testgravitational_potential(unittest.TestCase):
    """
    Tests the gravitational_potential calculation method
    """

    def test_solving_for_potential_energy(self) -> None:
        """
        Function tests solving for the gravitational potential energy (potential_energy)
        """

        # Initial conditions

        mass_body: List[float] = [1.0e24, 1.0e24]
        mass_object: List[float] = [1000.0, 1000.0]
        distance: List[float] = [0.0, 1.0e6]

        # Numeric expected values in units of 1e10 J
        expected: List[Any] = [
            ValueError(
                "Distance between the two bodies must be \
                greater than zero."
            ),
            -6.674,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter13.Calculate.gravitational_potential(
                        mass_body=mass_body[i],
                        mass_object=mass_object[i],
                        distance=distance[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter13.Calculate.gravitational_potential(
                    mass_body=mass_body[i],
                    mass_object=mass_object[i],
                    distance=distance[i],
                )
                self.assertAlmostEqual(result / 1.0e10, expected[i], places=4)

    def test_solving_for_mass_body(self) -> None:
        """
        Function tests solving for the mass of the stellar body (mass_body)
        """

        # Initial conditions

        potential_energy: List[float] = [6.674e10, -6.674e10]
        mass_object: List[float] = [1000.0, 1000.0]
        distance: List[float] = [1.0e6, 1.0e6]

        # Numeric expected values in units of 1e24 kg
        expected: List[Any] = [
            ValueError("Mass cannot be negative. Check your values."),
            1.0,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter13.Calculate.gravitational_potential(
                        potential_energy=potential_energy[i],
                        mass_object=mass_object[i],
                        distance=distance[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter13.Calculate.gravitational_potential(
                    potential_energy=potential_energy[i],
                    mass_object=mass_object[i],
                    distance=distance[i],
                )
                self.assertAlmostEqual(result / 1.0e24, expected[i], places=4)

    def test_solving_for_mass_object(self) -> None:
        """
        Function tests solving for the mass of the orbiting object (mass_object)
        """

        # Initial conditions

        potential_energy: List[float] = [-6.674e10]
        mass_body: List[float] = [1.0e24]
        distance: List[float] = [1.0e6]

        expected: List[Any] = [1000.0]

        for i in range(len(expected)):
            result = Chapter13.Calculate.gravitational_potential(
                potential_energy=potential_energy[i],
                mass_body=mass_body[i],
                distance=distance[i],
            )
            self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_distance(self) -> None:
        """
        Function tests solving for the distance between the two bodies (distance)
        """

        # Initial conditions

        potential_energy: List[float] = [-6.674e10]
        mass_body: List[float] = [1.0e24]
        mass_object: List[float] = [1000.0]

        expected: List[Any] = [1.0e6]

        for i in range(len(expected)):
            result = Chapter13.Calculate.gravitational_potential(
                potential_energy=potential_energy[i],
                mass_body=mass_body[i],
                mass_object=mass_object[i],
            )
            self.assertAlmostEqual(result, expected[i], places=4)


class Testconservation_of_grav_energy(unittest.TestCase):
    """
    Tests the conservation_of_grav_energy calculation method
    """

    def test_solving_for_mass_body(self) -> None:
        """
        Function tests solving for the mass of the stellar body (mass_body)
        """

        # Initial conditions

        mass_object: List[float] = [100.0, 100.0]
        velocity_1: List[float] = [10000.0, 14000.0]
        velocity_2: List[float] = [10000.0, 10000.0]
        distance_1: List[float] = [-1.0, 1.0e6]
        distance_2: List[float] = [2.0e6, 2.0e6]

        # Numeric expected values in units of 1e24 kg
        expected: List[Any] = [
            ValueError("Distance cannot be a negative value."),
            1.4384177404854664,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter13.Calculate.conservation_of_grav_energy(
                        mass_object=mass_object[i],
                        velocity_1=velocity_1[i],
                        velocity_2=velocity_2[i],
                        distance_1=distance_1[i],
                        distance_2=distance_2[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter13.Calculate.conservation_of_grav_energy(
                    mass_object=mass_object[i],
                    velocity_1=velocity_1[i],
                    velocity_2=velocity_2[i],
                    distance_1=distance_1[i],
                    distance_2=distance_2[i],
                )
                self.assertAlmostEqual(result / 1.0e24, expected[i], places=4)

    def test_solving_for_mass_object(self) -> None:
        """
        Function tests solving for the mass of the orbiting object (mass_object)
        """

        # Initial conditions

        mass_body: List[float] = [1.0e24]
        velocity_1: List[float] = [10000.0]
        velocity_2: List[float] = [10000.0]
        distance_1: List[float] = [1.0e6]
        distance_2: List[float] = [2.0e6]

        expected: List[Any] = [
            ValueError(
                "Mass of orbiting body cancels out and \
                    cannot be determined."
            )
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter13.Calculate.conservation_of_grav_energy(
                        mass_body=mass_body[i],
                        velocity_1=velocity_1[i],
                        velocity_2=velocity_2[i],
                        distance_1=distance_1[i],
                        distance_2=distance_2[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter13.Calculate.conservation_of_grav_energy(
                    mass_body=mass_body[i],
                    velocity_1=velocity_1[i],
                    velocity_2=velocity_2[i],
                    distance_1=distance_1[i],
                    distance_2=distance_2[i],
                )
                self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_velocity_1(self) -> None:
        """
        Function tests solving for the velocity at moment 1 (velocity_1)
        """

        # Initial conditions

        mass_object: List[float] = [100.0]
        mass_body: List[float] = [1.0e24]
        velocity_2: List[float] = [5000.0]
        distance_1: List[float] = [1.0e6]
        distance_2: List[float] = [1.0e6]

        expected: List[Any] = [5000.0]

        for i in range(len(expected)):
            result = Chapter13.Calculate.conservation_of_grav_energy(
                mass_object=mass_object[i],
                mass_body=mass_body[i],
                velocity_2=velocity_2[i],
                distance_1=distance_1[i],
                distance_2=distance_2[i],
            )
            self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_velocity_2(self) -> None:
        """
        Function tests solving for the velocity at moment 2 (velocity_2)
        """

        # Initial conditions

        mass_object: List[float] = [100.0]
        mass_body: List[float] = [1.0e24]
        velocity_1: List[float] = [20000.0]
        distance_1: List[float] = [1.0e6]
        distance_2: List[float] = [2.0e6]

        expected: List[Any] = [18255.410156991817]

        for i in range(len(expected)):
            result = Chapter13.Calculate.conservation_of_grav_energy(
                mass_object=mass_object[i],
                mass_body=mass_body[i],
                velocity_1=velocity_1[i],
                distance_1=distance_1[i],
                distance_2=distance_2[i],
            )
            self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_distance_1(self) -> None:
        """
        Function tests solving for the distance at moment 1 (distance_1)
        """

        # Initial conditions

        mass_object: List[float] = [100.0]
        mass_body: List[float] = [1.0e24]
        velocity_1: List[float] = [10000.0]
        velocity_2: List[float] = [10000.0]
        distance_2: List[float] = [2.0e6]

        expected: List[Any] = [2.0e6]

        for i in range(len(expected)):
            result = Chapter13.Calculate.conservation_of_grav_energy(
                mass_object=mass_object[i],
                mass_body=mass_body[i],
                velocity_1=velocity_1[i],
                velocity_2=velocity_2[i],
                distance_2=distance_2[i],
            )
            self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_distance_2(self) -> None:
        """
        Function tests solving for the distance at moment 2 (distance_2)
        """

        # Initial conditions

        mass_object: List[float] = [100.0, 100.0]
        mass_body: List[float] = [1.0e24, 1.0e24]
        velocity_1: List[float] = [0.0, 10000.0]
        velocity_2: List[float] = [10000.0, 10000.0]
        distance_1: List[float] = [1.0e6, 1.0e6]

        expected: List[Any] = [
            ValueError("Division by zero is undefined."),
            1.0e6,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter13.Calculate.conservation_of_grav_energy(
                        mass_object=mass_object[i],
                        mass_body=mass_body[i],
                        velocity_1=velocity_1[i],
                        velocity_2=velocity_2[i],
                        distance_1=distance_1[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter13.Calculate.conservation_of_grav_energy(
                    mass_object=mass_object[i],
                    mass_body=mass_body[i],
                    velocity_1=velocity_1[i],
                    velocity_2=velocity_2[i],
                    distance_1=distance_1[i],
                )
                self.assertAlmostEqual(result, expected[i], places=4)

    def test_all_variables_known(self) -> None:
        """
        Function tests the fallthrough case where every variable is known
        and there is nothing left to solve for.
        """

        # Initial conditions

        mass_object: List[float] = [100.0]
        mass_body: List[float] = [1.0e24]
        velocity_1: List[float] = [10000.0]
        velocity_2: List[float] = [10000.0]
        distance_1: List[float] = [1.0e6]
        distance_2: List[float] = [1.0e6]

        expected: List[Any] = [0.0]

        for i in range(len(expected)):
            result = Chapter13.Calculate.conservation_of_grav_energy(
                mass_object=mass_object[i],
                mass_body=mass_body[i],
                velocity_1=velocity_1[i],
                velocity_2=velocity_2[i],
                distance_1=distance_1[i],
                distance_2=distance_2[i],
            )
            self.assertAlmostEqual(result, expected[i], places=4)


class Testescape_velocity(unittest.TestCase):
    """
    Tests the escape_velocity calculation method
    """

    def test_solving_for_escape_vel(self) -> None:
        """
        Function tests solving for the escape velocity (escape_vel)
        """

        # Initial conditions

        mass_body: List[float] = [1.0e24, 1.0e24]
        radius: List[float] = [0.0, 1.3348e6]

        expected: List[Any] = [
            ValueError("Radius of stellar body must be greater than zero."),
            10000.0,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter13.Calculate.escape_velocity(
                        mass_body=mass_body[i], radius=radius[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter13.Calculate.escape_velocity(
                    mass_body=mass_body[i], radius=radius[i]
                )
                self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_mass_body(self) -> None:
        """
        Function tests solving for the mass of the stellar body (mass_body)
        """

        # Initial conditions

        escape_vel: List[float] = [10000.0]
        radius: List[float] = [1.3348e6]

        # Expected values in units of 1e24 kg
        expected: List[Any] = [1.0]

        for i in range(len(expected)):
            result = Chapter13.Calculate.escape_velocity(
                escape_vel=escape_vel[i], radius=radius[i]
            )
            self.assertAlmostEqual(result / 1.0e24, expected[i], places=4)

    def test_solving_for_radius(self) -> None:
        """
        Function tests solving for the radius of the stellar body (radius)
        """

        # Initial conditions

        escape_vel: List[float] = [0.0, 10000.0]
        mass_body: List[float] = [1.0e24, 1.0e24]

        expected: List[Any] = [
            ValueError("Divison by zero is undefined."),
            1.3348e6,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter13.Calculate.escape_velocity(
                        escape_vel=escape_vel[i], mass_body=mass_body[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter13.Calculate.escape_velocity(
                    escape_vel=escape_vel[i], mass_body=mass_body[i]
                )
                self.assertAlmostEqual(result, expected[i], places=4)


class Testorbital_velocity(unittest.TestCase):
    """
    Tests the orbital_velocity calculation method
    """

    def test_solving_for_orbital_vel(self) -> None:
        """
        Function tests solving for the orbital velocity (orbital_vel)
        """

        # Initial conditions

        mass_body: List[float] = [1.0e24, 1.0e24]
        distance: List[float] = [-5.0, 6.674e5]

        expected: List[Any] = [
            ValueError("Radius of stellar body must be greater than zero."),
            10000.0,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter13.Calculate.orbital_velocity(
                        mass_body=mass_body[i], distance=distance[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter13.Calculate.orbital_velocity(
                    mass_body=mass_body[i], distance=distance[i]
                )
                self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_mass_body(self) -> None:
        """
        Function tests solving for the mass of the stellar body (mass_body)
        """

        # Initial conditions

        orbital_vel: List[float] = [10000.0]
        distance: List[float] = [6.674e5]

        # Expected values in units of 1e24 kg
        expected: List[Any] = [1.0]

        for i in range(len(expected)):
            result = Chapter13.Calculate.orbital_velocity(
                orbital_vel=orbital_vel[i], distance=distance[i]
            )
            self.assertAlmostEqual(result / 1.0e24, expected[i], places=4)

    def test_solving_for_distance(self) -> None:
        """
        Function tests solving for the distance from the stellar body (distance)
        """

        # Initial conditions

        orbital_vel: List[float] = [0.0, 10000.0]
        mass_body: List[float] = [1.0e24, 1.0e24]

        expected: List[Any] = [
            ValueError("Divison by zero is undefined."),
            6.674e5,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter13.Calculate.orbital_velocity(
                        orbital_vel=orbital_vel[i], mass_body=mass_body[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter13.Calculate.orbital_velocity(
                    orbital_vel=orbital_vel[i], mass_body=mass_body[i]
                )
                self.assertAlmostEqual(result, expected[i], places=4)


class Testorbital_period(unittest.TestCase):
    """
    Tests the orbital_period calculation method
    """

    def test_solving_for_period(self) -> None:
        """
        Function tests solving for the orbital period (period)
        """

        # Initial conditions

        distance: List[float] = [6.371e6]
        mass_body: List[float] = [5.972e24]

        expected: List[Any] = [5061.022584149725]

        for i in range(len(expected)):
            result = Chapter13.Calculate.orbital_period(
                distance=distance[i], mass_body=mass_body[i]
            )
            self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_distance(self) -> None:
        """
        Function tests solving for the altitude of the orbiting body (distance)
        """

        # Initial conditions

        period: List[float] = [5061.022584149725]
        mass_body: List[float] = [5.972e24]

        expected: List[Any] = [6.371e6]

        for i in range(len(expected)):
            result = Chapter13.Calculate.orbital_period(
                period=period[i], mass_body=mass_body[i]
            )
            self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_mass_body(self) -> None:
        """
        Function tests solving for the mass of the stellar body (mass_body)
        """

        # Initial conditions

        period: List[float] = [0.0, 5061.022584149725]
        distance: List[float] = [6.371e6, 6.371e6]

        # Numeric expected values in units of 1e24 kg
        expected: List[Any] = [
            ValueError("Division by zero is undefined."),
            5.972,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter13.Calculate.orbital_period(
                        period=period[i], distance=distance[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter13.Calculate.orbital_period(
                    period=period[i], distance=distance[i]
                )
                self.assertAlmostEqual(result / 1.0e24, expected[i], places=4)


class Testorbital_equation(unittest.TestCase):
    """
    Tests the orbital_equation calculation method
    """

    def test_solving_for_semi_latus_rectum(self) -> None:
        """
        Function tests solving for the semi-latus rectum (semi_latus_rectum)
        """

        # Initial conditions

        eccentricity: List[float] = [0.5, 0.5]
        distance: List[float] = [0.0, 2.0]
        theta: List[float] = [60.0, 60.0]

        expected: List[Any] = [
            ValueError("Distance cannot be less than or equal to zero."),
            2.5,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter13.Calculate.orbital_equation(
                        eccentricity=eccentricity[i],
                        distance=distance[i],
                        theta=theta[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter13.Calculate.orbital_equation(
                    eccentricity=eccentricity[i], distance=distance[i], theta=theta[i]
                )
                self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_eccentricity(self) -> None:
        """
        Function tests solving for the eccentricity of the orbit (eccentricity)
        """

        # Initial conditions

        semi_latus_rectum: List[float] = [2.5]
        distance: List[float] = [2.0]
        theta: List[float] = [60.0]

        expected: List[Any] = [0.5]

        for i in range(len(expected)):
            result = Chapter13.Calculate.orbital_equation(
                semi_latus_rectum=semi_latus_rectum[i],
                distance=distance[i],
                theta=theta[i],
            )
            self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_distance(self) -> None:
        """
        Function tests solving for the distance from the focus (distance)
        """

        # Initial conditions

        semi_latus_rectum: List[float] = [2.5, 2.5]
        eccentricity: List[float] = [1.0, 0.5]
        theta: List[float] = [180.0, 60.0]

        expected: List[Any] = [
            ValueError("Divison by zero is undefined."),
            2.0,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter13.Calculate.orbital_equation(
                        semi_latus_rectum=semi_latus_rectum[i],
                        eccentricity=eccentricity[i],
                        theta=theta[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter13.Calculate.orbital_equation(
                    semi_latus_rectum=semi_latus_rectum[i],
                    eccentricity=eccentricity[i],
                    theta=theta[i],
                )
                self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_theta(self) -> None:
        """
        Function tests solving for the angle from periapsis (theta)
        """

        # Initial conditions

        semi_latus_rectum: List[float] = [2.5, 2.5]
        eccentricity: List[float] = [0.0, 0.5]
        distance: List[float] = [2.0, 2.0]

        expected: List[Any] = [
            ValueError("Divison by zero is undefined."),
            60.0,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter13.Calculate.orbital_equation(
                        semi_latus_rectum=semi_latus_rectum[i],
                        eccentricity=eccentricity[i],
                        distance=distance[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter13.Calculate.orbital_equation(
                    semi_latus_rectum=semi_latus_rectum[i],
                    eccentricity=eccentricity[i],
                    distance=distance[i],
                )
                self.assertAlmostEqual(result, expected[i], places=4)


class Testkeplers_third_law(unittest.TestCase):
    """
    Tests the keplers_third_law calculation method
    """

    def test_solving_for_period(self) -> None:
        """
        Function tests solving for the orbital period (period)
        """

        # Initial conditions

        semi_major_axis: List[float] = [1.496e11]
        mass_body: List[float] = [1.989e30]

        expected: List[Any] = [31554896.928761967]

        for i in range(len(expected)):
            result = Chapter13.Calculate.keplers_third_law(
                semi_major_axis=semi_major_axis[i], mass_body=mass_body[i]
            )
            self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_semi_major_axis(self) -> None:
        """
        Function tests solving for the semi-major axis of the orbit (semi_major_axis)
        """

        # Initial conditions

        period: List[float] = [31554896.928761967]
        mass_body: List[float] = [1.989e30]

        # Expected values in units of 1e11 m
        expected: List[Any] = [1.496]

        for i in range(len(expected)):
            result = Chapter13.Calculate.keplers_third_law(
                period=period[i], mass_body=mass_body[i]
            )
            self.assertAlmostEqual(result / 1.0e11, expected[i], places=4)

    def test_solving_for_mass_body(self) -> None:
        """
        Function tests solving for the mass of the stellar body (mass_body)
        """

        # Initial conditions

        period: List[float] = [0.0, 31554896.928761967]
        semi_major_axis: List[float] = [1.496e11, 1.496e11]

        # Numeric expected values in units of 1e30 kg
        expected: List[Any] = [
            ValueError("Divison by zero is undefined."),
            1.989,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter13.Calculate.keplers_third_law(
                        period=period[i], semi_major_axis=semi_major_axis[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter13.Calculate.keplers_third_law(
                    period=period[i], semi_major_axis=semi_major_axis[i]
                )
                self.assertAlmostEqual(result / 1.0e30, expected[i], places=4)


class Testschwarzschild_radius(unittest.TestCase):
    """
    Tests the schwarzschild_radius calculation method
    """

    def test_solving_for_shwarz_radius(self) -> None:
        """
        Function tests solving for the Schwarzschild radius (shwarz_radius)
        """

        # Initial conditions

        mass_body: List[float] = [0.0, 1.989e30]

        expected: List[Any] = [
            ValueError(
                "We are operating with massive objects. \
                Make sure all objects have a mass greater than zero."
            ),
            2953.845147376436,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter13.Calculate.schwarzschild_radius(mass_body=mass_body[i])
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter13.Calculate.schwarzschild_radius(
                    mass_body=mass_body[i]
                )
                self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_mass_body(self) -> None:
        """
        Function tests solving for the mass of the stellar body (mass_body)
        """

        # Initial conditions

        shwarz_radius: List[float] = [2953.845147376436]

        # Expected values in units of 1e30 kg
        expected: List[Any] = [1.989]

        for i in range(len(expected)):
            result = Chapter13.Calculate.schwarzschild_radius(
                shwarz_radius=shwarz_radius[i]
            )
            self.assertAlmostEqual(result / 1.0e30, expected[i], places=4)
