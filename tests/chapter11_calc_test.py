import unittest

from typing import List, Any
from physics_TUI.chapters.chapter11 import Chapter11


class Testaccel_without_slipping(unittest.TestCase):
    """
    Tests the accel_without_slipping calculation method
    """

    def test_solving_for_accel(self) -> None:
        """
        Function tests solving for the acceleration (accel)
        """

        # Initial conditions

        mass: List[float] = [0.0, 2.0, 2.0, 2.0]
        moment_inertia: List[float] = [1.0, -1.0, 1.0, 1.0]
        radius: List[float] = [1.0, 1.0, 0.0, 1.0]
        theta: List[float] = [30.0, 30.0, 30.0, 30.0]

        expected: List[Any] = [
            ValueError(
                "We are operating with massive objects. \
                    Make sure all objects have a mass greater than zero."
            ),
            ValueError("The moment of inertia cannot be a negative value."),
            ValueError("Radius cannot be less than or equal to zero."),
            3.2733,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter11.Calculate.accel_without_slipping(
                        mass=mass[i],
                        moment_inertia=moment_inertia[i],
                        radius=radius[i],
                        theta=theta[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter11.Calculate.accel_without_slipping(
                    mass=mass[i],
                    moment_inertia=moment_inertia[i],
                    radius=radius[i],
                    theta=theta[i],
                )
                self.assertAlmostEqual(result, expected[i], places=3)

    def test_solving_for_mass(self) -> None:
        """
        Function tests solving for the mass (mass)
        """

        # Initial conditions

        accel: List[float] = [2.455]
        moment_inertia: List[float] = [3.0]
        radius: List[float] = [1.0]
        theta: List[float] = [30.0]

        expected: List[Any] = [3.0]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter11.Calculate.accel_without_slipping(
                        accel=accel[i],
                        moment_inertia=moment_inertia[i],
                        radius=radius[i],
                        theta=theta[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter11.Calculate.accel_without_slipping(
                    accel=accel[i],
                    moment_inertia=moment_inertia[i],
                    radius=radius[i],
                    theta=theta[i],
                )
                self.assertAlmostEqual(result, expected[i], places=3)

    def test_solving_for_moment_inertia(self) -> None:
        """
        Function tests solving for the moment of inertia (moment_inertia)
        """

        # Initial conditions

        accel: List[float] = [0.0, 2.455]
        mass: List[float] = [2.0, 2.0]
        radius: List[float] = [1.0, 1.0]
        theta: List[float] = [30.0, 30.0]

        expected: List[Any] = [
            ValueError("Division by zero is undefined."),
            2.0,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter11.Calculate.accel_without_slipping(
                        accel=accel[i],
                        mass=mass[i],
                        radius=radius[i],
                        theta=theta[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter11.Calculate.accel_without_slipping(
                    accel=accel[i],
                    mass=mass[i],
                    radius=radius[i],
                    theta=theta[i],
                )
                self.assertAlmostEqual(result, expected[i], places=3)

    def test_solving_for_radius(self) -> None:
        """
        Function tests solving for the radius (radius)
        """

        # Initial conditions

        accel: List[float] = [10.0, 2.455]
        mass: List[float] = [2.0, 2.0]
        moment_inertia: List[float] = [2.0, 2.0]
        theta: List[float] = [30.0, 30.0]

        expected: List[Any] = [
            ValueError(
                "Negative radicand yields an imaginary number. \
                        Check your values."
            ),
            1.0,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter11.Calculate.accel_without_slipping(
                        accel=accel[i],
                        mass=mass[i],
                        moment_inertia=moment_inertia[i],
                        theta=theta[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter11.Calculate.accel_without_slipping(
                    accel=accel[i],
                    mass=mass[i],
                    moment_inertia=moment_inertia[i],
                    theta=theta[i],
                )
                self.assertAlmostEqual(result, expected[i], places=3)

    def test_solving_for_theta(self) -> None:
        """
        Function tests solving for the angle (theta)
        """

        # Initial conditions

        accel: List[float] = [9.82, 2.455]
        mass: List[float] = [1.0, 2.0]
        moment_inertia: List[float] = [1.0, 2.0]
        radius: List[float] = [1.0, 1.0]

        expected: List[Any] = [
            ValueError("math domain error"),
            30.0,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter11.Calculate.accel_without_slipping(
                        accel=accel[i],
                        mass=mass[i],
                        moment_inertia=moment_inertia[i],
                        radius=radius[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter11.Calculate.accel_without_slipping(
                    accel=accel[i],
                    mass=mass[i],
                    moment_inertia=moment_inertia[i],
                    radius=radius[i],
                )
                self.assertAlmostEqual(result, expected[i], places=3)


class Testang_momentum_rigid_body(unittest.TestCase):
    """
    Tests the ang_momentum_rigid_body calculation method
    """

    def test_solving_for_angular_momentum(self) -> None:
        """
        Function tests solving for the angular momentum (angular_momentum)
        """

        # Initial conditions

        moment_interia: List[float] = [2.0]
        angular_vel: List[float] = [3.0]

        expected: List[Any] = [6.0]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter11.Calculate.ang_momentum_rigid_body(
                        moment_interia=moment_interia[i], angular_vel=angular_vel[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter11.Calculate.ang_momentum_rigid_body(
                    moment_interia=moment_interia[i], angular_vel=angular_vel[i]
                )
                self.assertAlmostEqual(result, expected[i], places=3)

    def test_solving_for_moment_interia(self) -> None:
        """
        Function tests solving for the moment of inertia (moment_interia)
        """

        # Initial conditions

        angular_momentum: List[float] = [6.0, 6.0]
        angular_vel: List[float] = [0.0, 3.0]

        expected: List[Any] = [
            ValueError("Division by zero is undefined."),
            2.0,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter11.Calculate.ang_momentum_rigid_body(
                        angular_momentum=angular_momentum[i], angular_vel=angular_vel[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter11.Calculate.ang_momentum_rigid_body(
                    angular_momentum=angular_momentum[i], angular_vel=angular_vel[i]
                )
                self.assertAlmostEqual(result, expected[i], places=3)

    def test_solving_for_angular_vel(self) -> None:
        """
        Function tests solving for the angular velocity (angular_vel)
        """

        # Initial conditions

        angular_momentum: List[float] = [6.0, 6.0, 6.0]
        moment_interia: List[float] = [0.0, -2.0, 2.0]

        expected: List[Any] = [
            ValueError("Divison by zero is undefined."),
            ValueError("The moment of inertia cannot be a negative value."),
            3.0,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter11.Calculate.ang_momentum_rigid_body(
                        angular_momentum=angular_momentum[i],
                        moment_interia=moment_interia[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter11.Calculate.ang_momentum_rigid_body(
                    angular_momentum=angular_momentum[i],
                    moment_interia=moment_interia[i],
                )
                self.assertAlmostEqual(result, expected[i], places=3)


class Testprocessional_ang_vel(unittest.TestCase):
    """
    Tests the processional_ang_vel calculation method
    """

    def test_solving_for_proccesional_ang_vel(self) -> None:
        """
        Function tests solving for the processional angular velocity (proccesional_ang_vel)
        """

        # Initial conditions

        radius: List[float] = [0.5, 0.5, -1.0, 0.5]
        mass: List[float] = [2.0, -1.0, 2.0, 2.0]
        moment_inertia: List[float] = [1.0, 1.0, 1.0, 1.0]
        angular_vel: List[float] = [0.0, 10.0, 10.0, 10.0]

        expected: List[Any] = [
            ValueError("Division by zero is undefined."),
            ValueError(
                "We are operating with massive objects. \
                    Make sure all objects have a mass greater than zero."
            ),
            ValueError("Radius cannot be less than or equal to zero."),
            0.982,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter11.Calculate.processional_ang_vel(
                        radius=radius[i],
                        mass=mass[i],
                        moment_inertia=moment_inertia[i],
                        angular_vel=angular_vel[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter11.Calculate.processional_ang_vel(
                    radius=radius[i],
                    mass=mass[i],
                    moment_inertia=moment_inertia[i],
                    angular_vel=angular_vel[i],
                )
                self.assertAlmostEqual(result, expected[i], places=3)

    def test_solving_for_radius(self) -> None:
        """
        Function tests solving for the radius (radius)
        """

        # Initial conditions

        proccesional_ang_vel: List[float] = [0.982]
        mass: List[float] = [2.0]
        moment_inertia: List[float] = [1.0]
        angular_vel: List[float] = [10.0]

        expected: List[Any] = [0.5]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter11.Calculate.processional_ang_vel(
                        proccesional_ang_vel=proccesional_ang_vel[i],
                        mass=mass[i],
                        moment_inertia=moment_inertia[i],
                        angular_vel=angular_vel[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter11.Calculate.processional_ang_vel(
                    proccesional_ang_vel=proccesional_ang_vel[i],
                    mass=mass[i],
                    moment_inertia=moment_inertia[i],
                    angular_vel=angular_vel[i],
                )
                self.assertAlmostEqual(result, expected[i], places=3)

    def test_solving_for_mass(self) -> None:
        """
        Function tests solving for the mass (mass)
        """

        # Initial conditions

        proccesional_ang_vel: List[float] = [0.982]
        radius: List[float] = [0.5]
        moment_inertia: List[float] = [1.0]
        angular_vel: List[float] = [10.0]

        expected: List[Any] = [2.0]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter11.Calculate.processional_ang_vel(
                        proccesional_ang_vel=proccesional_ang_vel[i],
                        radius=radius[i],
                        moment_inertia=moment_inertia[i],
                        angular_vel=angular_vel[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter11.Calculate.processional_ang_vel(
                    proccesional_ang_vel=proccesional_ang_vel[i],
                    radius=radius[i],
                    moment_inertia=moment_inertia[i],
                    angular_vel=angular_vel[i],
                )
                self.assertAlmostEqual(result, expected[i], places=3)

    def test_solving_for_moment_inertia(self) -> None:
        """
        Function tests solving for the moment of inertia (moment_inertia)
        """

        # Initial conditions

        proccesional_ang_vel: List[float] = [0.0, 0.982]
        radius: List[float] = [0.5, 0.5]
        mass: List[float] = [2.0, 2.0]
        angular_vel: List[float] = [10.0, 10.0]

        expected: List[Any] = [
            ValueError("Division by zero is undefined."),
            1.0,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter11.Calculate.processional_ang_vel(
                        proccesional_ang_vel=proccesional_ang_vel[i],
                        radius=radius[i],
                        mass=mass[i],
                        angular_vel=angular_vel[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter11.Calculate.processional_ang_vel(
                    proccesional_ang_vel=proccesional_ang_vel[i],
                    radius=radius[i],
                    mass=mass[i],
                    angular_vel=angular_vel[i],
                )
                self.assertAlmostEqual(result, expected[i], places=3)

    def test_solving_for_angular_vel(self) -> None:
        """
        Function tests solving for the angular velocity (angular_vel)
        """

        # Initial conditions

        proccesional_ang_vel: List[float] = [0.0, 0.982]
        radius: List[float] = [0.5, 0.5]
        mass: List[float] = [2.0, 2.0]
        moment_inertia: List[float] = [1.0, 1.0]

        expected: List[Any] = [
            ValueError("Division by zero is undefined."),
            10.0,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter11.Calculate.processional_ang_vel(
                        proccesional_ang_vel=proccesional_ang_vel[i],
                        radius=radius[i],
                        mass=mass[i],
                        moment_inertia=moment_inertia[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter11.Calculate.processional_ang_vel(
                    proccesional_ang_vel=proccesional_ang_vel[i],
                    radius=radius[i],
                    mass=mass[i],
                    moment_inertia=moment_inertia[i],
                )
                self.assertAlmostEqual(result, expected[i], places=3)
