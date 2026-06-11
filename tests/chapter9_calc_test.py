import unittest
from typing import Any, List
from unittest.case import TestCase

from physics_TUI.chapters.chapter9 import Chapter9


class TestInelasticCollisionMomentum(unittest.TestCase):
    """
    Tests the main use cases of calculations for the inelastic collision of
    two bodies.
    """

    def test_solving_for_mass_1(self) -> None:
        """
        Function tests solving for the mass of the first object (mass_1)
        """

        # Initial conditions
        mass_2: List[float] = [
            -10.0,
            10.0,
            10.0,
        ]
        velocity_1: List[float] = [
            10.0,
            0.0,
            10.0,
        ]
        velocity_2: List[float] = [
            30.0,
            30.0,
            30.0,
        ]
        velocity_f: List[float] = [20.0, 20.0, 20.0]
        mass_f: List[float] = [10.0, 20.0, 20.0]

        expected: List[Any] = [
            ValueError(
                "We are operating with massive objects. Make sure all objects have a mass greater than zero."
            ),
            ValueError("Division by zero is undefined."),
            10.0,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter9.Calculate.inelastic_collision_momentum(
                        mass_2=mass_2[i],
                        velocity_1=velocity_1[i],
                        velocity_2=velocity_2[i],
                        velocity_f=velocity_f[i],
                        mass_f=mass_f[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter9.Calculate.inelastic_collision_momentum(
                    mass_2=mass_2[i],
                    velocity_1=velocity_1[i],
                    velocity_2=velocity_2[i],
                    velocity_f=velocity_f[i],
                    mass_f=mass_f[i],
                )
                self.assertAlmostEqual(result, expected[i], places=2)

    def test_solving_for_mass_2(self) -> None:
        """
        Function tests solving for the mass of the second object (mass_2)
        """

        # Initial conditions

        mass_1: List[float] = [
            -10.0,
            10.0,
            10.0,
        ]
        velocity_1: List[float] = [
            10.0,
            0.0,
            10.0,
        ]
        velocity_2: List[float] = [
            30.0,
            30.0,
            30.0,
        ]
        velocity_f: List[float] = [20.0, 20.0, 20.0]
        mass_f: List[float] = [10.0, 20.0, 20.0]

        expected: List[float] = []

    def test_solving_for_mass_2_smoke(self) -> None:
        """
        Function tests solving for the mass of the second object (mass_2),
        covering the error branches and the value branch.
        """

        # Initial conditions
        mass_1: List[float] = [
            -10.0,
            10.0,
            10.0,
        ]
        velocity_1: List[float] = [
            10.0,
            10.0,
            10.0,
        ]
        velocity_2: List[float] = [
            30.0,
            0.0,
            30.0,
        ]
        velocity_f: List[float] = [20.0, 20.0, 20.0]
        mass_f: List[float] = [10.0, 20.0, 20.0]

        expected: List[Any] = [
            ValueError(
                "We are operating with massive objects. Make sure all objects have a mass greater than zero."
            ),
            ValueError("Division by zero is undefined."),
            10.0,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter9.Calculate.inelastic_collision_momentum(
                        mass_1=mass_1[i],
                        velocity_1=velocity_1[i],
                        velocity_2=velocity_2[i],
                        velocity_f=velocity_f[i],
                        mass_f=mass_f[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter9.Calculate.inelastic_collision_momentum(
                    mass_1=mass_1[i],
                    velocity_1=velocity_1[i],
                    velocity_2=velocity_2[i],
                    velocity_f=velocity_f[i],
                    mass_f=mass_f[i],
                )
                self.assertAlmostEqual(result, expected[i], places=2)

    def test_solving_for_velocity_1(self) -> None:
        """
        Function tests solving for the velocity of the first object (velocity_1)
        """

        # Initial conditions
        mass_1: List[float] = [10.0]
        mass_2: List[float] = [10.0]
        velocity_2: List[float] = [30.0]
        velocity_f: List[float] = [20.0]
        mass_f: List[float] = [20.0]

        expected: List[Any] = [10.0]

        for i in range(len(expected)):
            result = Chapter9.Calculate.inelastic_collision_momentum(
                mass_1=mass_1[i],
                mass_2=mass_2[i],
                velocity_2=velocity_2[i],
                velocity_f=velocity_f[i],
                mass_f=mass_f[i],
            )
            self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_velocity_2(self) -> None:
        """
        Function tests solving for the velocity of the second object (velocity_2)
        """

        # Initial conditions
        mass_1: List[float] = [10.0]
        mass_2: List[float] = [10.0]
        velocity_1: List[float] = [10.0]
        velocity_f: List[float] = [20.0]
        mass_f: List[float] = [20.0]

        expected: List[Any] = [30.0]

        for i in range(len(expected)):
            result = Chapter9.Calculate.inelastic_collision_momentum(
                mass_1=mass_1[i],
                mass_2=mass_2[i],
                velocity_1=velocity_1[i],
                velocity_f=velocity_f[i],
                mass_f=mass_f[i],
            )
            self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_mass_f(self) -> None:
        """
        Function tests solving for the mass after the collision (mass_f)
        """

        # Initial conditions
        mass_1: List[float] = [10.0, 10.0]
        mass_2: List[float] = [10.0, 10.0]
        velocity_1: List[float] = [10.0, 10.0]
        velocity_2: List[float] = [30.0, 30.0]
        velocity_f: List[float] = [0.0, 20.0]

        expected: List[Any] = [
            ValueError("Division by zero is undefined."),
            20.0,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter9.Calculate.inelastic_collision_momentum(
                        mass_1=mass_1[i],
                        mass_2=mass_2[i],
                        velocity_1=velocity_1[i],
                        velocity_2=velocity_2[i],
                        velocity_f=velocity_f[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter9.Calculate.inelastic_collision_momentum(
                    mass_1=mass_1[i],
                    mass_2=mass_2[i],
                    velocity_1=velocity_1[i],
                    velocity_2=velocity_2[i],
                    velocity_f=velocity_f[i],
                )
                self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_velocity_f(self) -> None:
        """
        Function tests solving for the velocity after the collision (velocity_f)
        """

        # Initial conditions
        mass_1: List[float] = [10.0]
        mass_2: List[float] = [10.0]
        velocity_1: List[float] = [10.0]
        velocity_2: List[float] = [30.0]
        mass_f: List[float] = [20.0]

        expected: List[Any] = [20.0]

        for i in range(len(expected)):
            result = Chapter9.Calculate.inelastic_collision_momentum(
                mass_1=mass_1[i],
                mass_2=mass_2[i],
                velocity_1=velocity_1[i],
                velocity_2=velocity_2[i],
                mass_f=mass_f[i],
            )
            self.assertAlmostEqual(result, expected[i], places=4)


class TestElasticCollisionMomentum(unittest.TestCase):
    """
    Tests the main use cases of calculations for the elastic collision of
    two bodies.

    Consistent 1D elastic data set: m1=2, m2=4, v_i1=6, v_i2=0 gives
    v_f1 = (m1-m2)/(m1+m2)*v_i1 = -2 and v_f2 = 2m1/(m1+m2)*v_i1 = 4.
    Momentum check: 2*6 + 4*0 = 12 = 2*(-2) + 4*4.
    """

    def test_solving_for_mass_1(self) -> None:
        """
        Function tests solving for the mass of the first object (mass_1)
        """

        # Initial conditions
        mass_2: List[float] = [4.0, 4.0]
        velocity_i1: List[float] = [6.0, 6.0]
        velocity_i2: List[float] = [0.0, 0.0]
        velocity_f1: List[float] = [6.0, -2.0]
        velocity_f2: List[float] = [4.0, 4.0]

        expected: List[Any] = [
            ValueError("Divison by zero is undefined."),
            2.0,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter9.Calculate.elastic_collision_momentum(
                        mass_2=mass_2[i],
                        velocity_i1=velocity_i1[i],
                        velocity_i2=velocity_i2[i],
                        velocity_f1=velocity_f1[i],
                        velocity_f2=velocity_f2[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter9.Calculate.elastic_collision_momentum(
                    mass_2=mass_2[i],
                    velocity_i1=velocity_i1[i],
                    velocity_i2=velocity_i2[i],
                    velocity_f1=velocity_f1[i],
                    velocity_f2=velocity_f2[i],
                )
                self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_mass_2(self) -> None:
        """
        Function tests solving for the mass of the second object (mass_2)
        """

        # Initial conditions
        mass_1: List[float] = [-1.0, 2.0, 2.0]
        velocity_i1: List[float] = [6.0, 6.0, 6.0]
        velocity_i2: List[float] = [0.0, 4.0, 0.0]
        velocity_f1: List[float] = [-2.0, -2.0, -2.0]
        velocity_f2: List[float] = [4.0, 4.0, 4.0]

        expected: List[Any] = [
            ValueError(
                "We are operating with massive objects.                     Make sure all objects have a mass greater than zero."
            ),
            ValueError("Divison by zero is undefined."),
            4.0,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter9.Calculate.elastic_collision_momentum(
                        mass_1=mass_1[i],
                        velocity_i1=velocity_i1[i],
                        velocity_i2=velocity_i2[i],
                        velocity_f1=velocity_f1[i],
                        velocity_f2=velocity_f2[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter9.Calculate.elastic_collision_momentum(
                    mass_1=mass_1[i],
                    velocity_i1=velocity_i1[i],
                    velocity_i2=velocity_i2[i],
                    velocity_f1=velocity_f1[i],
                    velocity_f2=velocity_f2[i],
                )
                self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_velocity_i1(self) -> None:
        """
        Function tests solving for the initial velocity of the first object (velocity_i1)
        """

        # Initial conditions
        mass_1: List[float] = [2.0]
        mass_2: List[float] = [4.0]
        velocity_i2: List[float] = [0.0]
        velocity_f1: List[float] = [-2.0]
        velocity_f2: List[float] = [4.0]

        expected: List[Any] = [6.0]

        for i in range(len(expected)):
            result = Chapter9.Calculate.elastic_collision_momentum(
                mass_1=mass_1[i],
                mass_2=mass_2[i],
                velocity_i2=velocity_i2[i],
                velocity_f1=velocity_f1[i],
                velocity_f2=velocity_f2[i],
            )
            self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_velocity_i2(self) -> None:
        """
        Function tests solving for the initial velocity of the second object (velocity_i2)
        """

        # Initial conditions
        mass_1: List[float] = [2.0]
        mass_2: List[float] = [4.0]
        velocity_i1: List[float] = [6.0]
        velocity_f1: List[float] = [-2.0]
        velocity_f2: List[float] = [4.0]

        expected: List[Any] = [0.0]

        for i in range(len(expected)):
            result = Chapter9.Calculate.elastic_collision_momentum(
                mass_1=mass_1[i],
                mass_2=mass_2[i],
                velocity_i1=velocity_i1[i],
                velocity_f1=velocity_f1[i],
                velocity_f2=velocity_f2[i],
            )
            self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_velocity_f1(self) -> None:
        """
        Function tests solving for the final velocity of the first object (velocity_f1)
        """

        # Initial conditions
        mass_1: List[float] = [2.0]
        mass_2: List[float] = [4.0]
        velocity_i1: List[float] = [6.0]
        velocity_i2: List[float] = [0.0]
        velocity_f2: List[float] = [4.0]

        expected: List[Any] = [-2.0]

        for i in range(len(expected)):
            result = Chapter9.Calculate.elastic_collision_momentum(
                mass_1=mass_1[i],
                mass_2=mass_2[i],
                velocity_i1=velocity_i1[i],
                velocity_i2=velocity_i2[i],
                velocity_f2=velocity_f2[i],
            )
            self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_velocity_f2(self) -> None:
        """
        Function tests solving for the final velocity of the second object (velocity_f2)
        """

        # Initial conditions
        mass_1: List[float] = [2.0]
        mass_2: List[float] = [4.0]
        velocity_i1: List[float] = [6.0]
        velocity_i2: List[float] = [0.0]
        velocity_f1: List[float] = [-2.0]

        expected: List[Any] = [4.0]

        for i in range(len(expected)):
            result = Chapter9.Calculate.elastic_collision_momentum(
                mass_1=mass_1[i],
                mass_2=mass_2[i],
                velocity_i1=velocity_i1[i],
                velocity_i2=velocity_i2[i],
                velocity_f1=velocity_f1[i],
            )
            self.assertAlmostEqual(result, expected[i], places=4)


class TestRocketEquation(unittest.TestCase):
    """
    Tests the main use cases of calculations for the rocket equation.

    Data set: u=100, m(i)=200, m=100 => Δv = 100*ln(2) = 69.31471805599453.
    The inverse solves feed Δv = 69.3147 back in, so the expected values are
    only exact to about 4 decimal places.
    """

    def test_solving_for_delta_v(self) -> None:
        """
        Function tests solving for the change in velocity (delta_v)
        """

        # Initial conditions
        vel_exhaust: List[float] = [100.0, 100.0]
        initial_mass: List[float] = [200.0, 200.0]
        final_mass: List[float] = [-5.0, 100.0]

        expected: List[Any] = [
            ValueError(
                "We are operating with massive objects.                     Mass must be greater than zero."
            ),
            69.3147,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter9.Calculate.rocket_equation(
                        vel_exhaust=vel_exhaust[i],
                        initial_mass=initial_mass[i],
                        final_mass=final_mass[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter9.Calculate.rocket_equation(
                    vel_exhaust=vel_exhaust[i],
                    initial_mass=initial_mass[i],
                    final_mass=final_mass[i],
                )
                self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_vel_exhaust(self) -> None:
        """
        Function tests solving for the velocity of the exhaust (vel_exhaust)
        """

        # Initial conditions
        delta_v: List[float] = [69.3147]
        initial_mass: List[float] = [200.0]
        final_mass: List[float] = [100.0]

        expected: List[Any] = [100.0]

        for i in range(len(expected)):
            result = Chapter9.Calculate.rocket_equation(
                delta_v=delta_v[i],
                initial_mass=initial_mass[i],
                final_mass=final_mass[i],
            )
            self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_initial_mass(self) -> None:
        """
        Function tests solving for the initial mass of the rocket (initial_mass)
        """

        # Initial conditions
        delta_v: List[float] = [69.3147]
        vel_exhaust: List[float] = [100.0]
        final_mass: List[float] = [100.0]

        expected: List[Any] = [200.0]

        for i in range(len(expected)):
            result = Chapter9.Calculate.rocket_equation(
                delta_v=delta_v[i],
                vel_exhaust=vel_exhaust[i],
                final_mass=final_mass[i],
            )
            self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_final_mass(self) -> None:
        """
        Function tests solving for the final mass of the rocket (final_mass)
        """

        # Initial conditions
        delta_v: List[float] = [69.3147]
        vel_exhaust: List[float] = [100.0]
        initial_mass: List[float] = [200.0]

        expected: List[Any] = [100.0]

        for i in range(len(expected)):
            result = Chapter9.Calculate.rocket_equation(
                delta_v=delta_v[i],
                vel_exhaust=vel_exhaust[i],
                initial_mass=initial_mass[i],
            )
            self.assertAlmostEqual(result, expected[i], places=4)
