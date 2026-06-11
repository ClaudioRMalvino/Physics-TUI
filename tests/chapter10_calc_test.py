import unittest

from typing import List, Any
from physics_TUI.chapters.chapter10 import Chapter10


class Testangular_position(unittest.TestCase):
    """
    Tests the angular_position calculation method
    """

    def test_solving_for_theta(self) -> None:
        """
        Function tests solving for the angular position (theta)
        """

        # Initial conditions

        arc_length: List[float] = [6.0, 6.0]
        radius: List[float] = [2.0, -2.0]

        expected: List[Any] = [
            3.0,
            ValueError(
                "Radius of rotational trajectory cannot be \
                    less than or equal to zero."
            ),
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter10.Calculate.angular_position(
                        arc_length=arc_length[i], radius=radius[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter10.Calculate.angular_position(
                    arc_length=arc_length[i], radius=radius[i]
                )
                self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_radius(self) -> None:
        """
        Function tests solving for the radius (radius)
        """

        # Initial conditions

        theta: List[float] = [0.0]
        arc_length: List[float] = [5.0]

        expected: List[Any] = [ValueError("Division by zero is undefined.")]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter10.Calculate.angular_position(
                        theta=theta[i], arc_length=arc_length[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter10.Calculate.angular_position(
                    theta=theta[i], arc_length=arc_length[i]
                )
                self.assertAlmostEqual(result, expected[i], places=4)


class Testtangential_speed(unittest.TestCase):
    """
    Tests the tangential_speed calculation method
    """

    def test_solving_for_tang_speed(self) -> None:
        """
        Function tests solving for the tangential speed (tang_speed)
        """

        # Initial conditions

        radius: List[float] = [2.0]
        angular_vel: List[float] = [3.0]

        expected: List[Any] = [6.0]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter10.Calculate.tangential_speed(
                        radius=radius[i], angular_vel=angular_vel[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter10.Calculate.tangential_speed(
                    radius=radius[i], angular_vel=angular_vel[i]
                )
                self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_angular_vel(self) -> None:
        """
        Function tests solving for the angular velocity (angular_vel)
        """

        # Initial conditions

        tang_speed: List[float] = [10.0]
        radius: List[float] = [4.0]

        expected: List[Any] = [2.5]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter10.Calculate.tangential_speed(
                        tang_speed=tang_speed[i], radius=radius[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter10.Calculate.tangential_speed(
                    tang_speed=tang_speed[i], radius=radius[i]
                )
                self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_radius(self) -> None:
        """
        Function tests solving for the radius (radius)
        """

        # Initial conditions

        tang_speed: List[float] = [5.0]
        angular_vel: List[float] = [0.0]

        expected: List[Any] = [ValueError("Divison by zero is undefined.")]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter10.Calculate.tangential_speed(
                        tang_speed=tang_speed[i], angular_vel=angular_vel[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter10.Calculate.tangential_speed(
                    tang_speed=tang_speed[i], angular_vel=angular_vel[i]
                )
                self.assertAlmostEqual(result, expected[i], places=4)


class Testaverage_angular_vel(unittest.TestCase):
    """
    Tests the average_angular_vel calculation method
    """

    def test_solving_for_ave_angular_vel(self) -> None:
        """
        Function tests solving for the average angular velocity (ave_angular_vel)
        """

        # Initial conditions

        init_angular_vel: List[float] = [10.0]
        final_angular_vel: List[float] = [20.0]

        expected: List[float] = [15.0]

        for i in range(len(expected)):
            result = Chapter10.Calculate.average_angular_vel(
                init_angular_vel=init_angular_vel[i],
                final_angular_vel=final_angular_vel[i],
            )
            self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_init_angular_vel(self) -> None:
        """
        Function tests solving for the initial angular velocity (init_angular_vel)
        """

        # Initial conditions

        ave_angular_vel: List[float] = [15.0]
        final_angular_vel: List[float] = [20.0]

        expected: List[float] = [10.0]

        for i in range(len(expected)):
            result = Chapter10.Calculate.average_angular_vel(
                ave_angular_vel=ave_angular_vel[i],
                final_angular_vel=final_angular_vel[i],
            )
            self.assertAlmostEqual(result, expected[i], places=4)


class Testangular_displacement(unittest.TestCase):
    """
    Tests the angular_displacement calculation method
    """

    def test_solving_for_theta_final(self) -> None:
        """
        Function tests solving for the final angular position (theta_final)
        """

        # Initial conditions

        theta_init: List[float] = [1.0, 1.0]
        ave_angular_vel: List[float] = [2.0, 2.0]
        time: List[float] = [3.0, -3.0]

        expected: List[Any] = [
            7.0,
            ValueError("Time cannot be a negative value."),
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter10.Calculate.angular_displacement(
                        theta_init=theta_init[i],
                        ave_angular_vel=ave_angular_vel[i],
                        time=time[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter10.Calculate.angular_displacement(
                    theta_init=theta_init[i],
                    ave_angular_vel=ave_angular_vel[i],
                    time=time[i],
                )
                self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_ave_angular_vel(self) -> None:
        """
        Function tests solving for the average angular velocity (ave_angular_vel)
        """

        # Initial conditions

        theta_final: List[float] = [5.0]
        theta_init: List[float] = [1.0]
        time: List[float] = [0.0]

        expected: List[Any] = [ValueError("Division by zero is undefined.")]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter10.Calculate.angular_displacement(
                        theta_final=theta_final[i],
                        theta_init=theta_init[i],
                        time=time[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter10.Calculate.angular_displacement(
                    theta_final=theta_final[i],
                    theta_init=theta_init[i],
                    time=time[i],
                )
                self.assertAlmostEqual(result, expected[i], places=4)


class Testangular_vel_const_accel(unittest.TestCase):
    """
    Tests the angular_vel_const_accel calculation method
    """

    def test_solving_for_final_angular_vel(self) -> None:
        """
        Function tests solving for the final angular velocity (final_angular_vel)
        """

        # Initial conditions

        init_angular_vel: List[float] = [2.0]
        const_angular_accel: List[float] = [3.0]
        time: List[float] = [4.0]

        expected: List[float] = [14.0]

        for i in range(len(expected)):
            result = Chapter10.Calculate.angular_vel_const_accel(
                init_angular_vel=init_angular_vel[i],
                const_angular_accel=const_angular_accel[i],
                time=time[i],
            )
            self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_time(self) -> None:
        """
        Function tests solving for the time (time)
        """

        # Initial conditions

        final_angular_vel: List[float] = [14.0]
        init_angular_vel: List[float] = [2.0]
        const_angular_accel: List[float] = [3.0]

        expected: List[float] = [4.0]

        for i in range(len(expected)):
            result = Chapter10.Calculate.angular_vel_const_accel(
                final_angular_vel=final_angular_vel[i],
                init_angular_vel=init_angular_vel[i],
                const_angular_accel=const_angular_accel[i],
            )
            self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_const_angular_accel(self) -> None:
        """
        Function tests solving for the constant angular acceleration (const_angular_accel)
        """

        # Initial conditions

        final_angular_vel: List[float] = [14.0]
        init_angular_vel: List[float] = [2.0]
        time: List[float] = [0.0]

        expected: List[Any] = [ValueError("Division by zero is undefined.")]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter10.Calculate.angular_vel_const_accel(
                        final_angular_vel=final_angular_vel[i],
                        init_angular_vel=init_angular_vel[i],
                        time=time[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter10.Calculate.angular_vel_const_accel(
                    final_angular_vel=final_angular_vel[i],
                    init_angular_vel=init_angular_vel[i],
                    time=time[i],
                )
                self.assertAlmostEqual(result, expected[i], places=4)


class Testangular_displacement_const_accel(unittest.TestCase):
    """
    Tests the angular_displacement_const_accel calculation method
    """

    def test_solving_for_theta_final(self) -> None:
        """
        Function tests solving for the final angular position (theta_final)
        """

        # Initial conditions

        theta_init: List[float] = [1.0]
        init_angular_vel: List[float] = [2.0]
        time: List[float] = [3.0]
        const_angular_accel: List[float] = [4.0]

        expected: List[float] = [25.0]

        for i in range(len(expected)):
            result = Chapter10.Calculate.angular_displacement_const_accel(
                theta_init=theta_init[i],
                init_angular_vel=init_angular_vel[i],
                time=time[i],
                const_angular_accel=const_angular_accel[i],
            )
            self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_time(self) -> None:
        """
        Function tests solving for the time (time)
        """

        # Initial conditions

        theta_final: List[float] = [9.0]
        theta_init: List[float] = [0.0]
        init_angular_vel: List[float] = [0.0]
        const_angular_accel: List[float] = [2.0]

        expected: List[float] = [3.0]

        for i in range(len(expected)):
            result = Chapter10.Calculate.angular_displacement_const_accel(
                theta_final=theta_final[i],
                theta_init=theta_init[i],
                init_angular_vel=init_angular_vel[i],
                const_angular_accel=const_angular_accel[i],
            )
            self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_init_angular_vel(self) -> None:
        """
        Function tests solving for the initial angular velocity (init_angular_vel)
        """

        # Initial conditions

        theta_final: List[float] = [9.0]
        theta_init: List[float] = [0.0]
        time: List[float] = [0.0]
        const_angular_accel: List[float] = [2.0]

        expected: List[Any] = [ValueError("Division by zero is undefined.")]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter10.Calculate.angular_displacement_const_accel(
                        theta_final=theta_final[i],
                        theta_init=theta_init[i],
                        time=time[i],
                        const_angular_accel=const_angular_accel[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter10.Calculate.angular_displacement_const_accel(
                    theta_final=theta_final[i],
                    theta_init=theta_init[i],
                    time=time[i],
                    const_angular_accel=const_angular_accel[i],
                )
                self.assertAlmostEqual(result, expected[i], places=4)


class Testchange_angular_velocity(unittest.TestCase):
    """
    Tests the change_angular_velocity calculation method
    """

    def test_solving_for_final_angular_vel(self) -> None:
        """
        Function tests solving for the final angular velocity (final_angular_vel)
        """

        # Initial conditions

        init_angular_vel: List[float] = [3.0, 1.0]
        const_angular_accel: List[float] = [2.0, -2.0]
        delta_theta: List[float] = [4.0, 4.0]

        expected: List[Any] = [
            5.0,
            ValueError(
                "A negative radicand yields an imaginary number.\
                        Check your values."
            ),
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter10.Calculate.change_angular_velocity(
                        init_angular_vel=init_angular_vel[i],
                        const_angular_accel=const_angular_accel[i],
                        delta_theta=delta_theta[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter10.Calculate.change_angular_velocity(
                    init_angular_vel=init_angular_vel[i],
                    const_angular_accel=const_angular_accel[i],
                    delta_theta=delta_theta[i],
                )
                self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_delta_theta(self) -> None:
        """
        Function tests solving for the change in angular position (delta_theta)
        """

        # Initial conditions

        final_angular_vel: List[float] = [5.0, 5.0]
        init_angular_vel: List[float] = [3.0, 3.0]
        const_angular_accel: List[float] = [2.0, 0.0]

        expected: List[Any] = [
            4.0,
            ValueError("Division by zero is undefined."),
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter10.Calculate.change_angular_velocity(
                        final_angular_vel=final_angular_vel[i],
                        init_angular_vel=init_angular_vel[i],
                        const_angular_accel=const_angular_accel[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter10.Calculate.change_angular_velocity(
                    final_angular_vel=final_angular_vel[i],
                    init_angular_vel=init_angular_vel[i],
                    const_angular_accel=const_angular_accel[i],
                )
                self.assertAlmostEqual(result, expected[i], places=4)


class Testrotational_ke(unittest.TestCase):
    """
    Tests the rotational_ke calculation method
    """

    def test_solving_for_kinetic_energy(self) -> None:
        """
        Function tests solving for the rotational kinetic energy (kinetic_energy)
        """

        # Initial conditions

        moment_inertia: List[float] = [2.0, -2.0]
        angular_vel: List[float] = [3.0, 3.0]

        expected: List[Any] = [
            9.0,
            ValueError("The moment of inertia cannot be a negative value."),
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter10.Calculate.rotational_ke(
                        moment_inertia=moment_inertia[i], angular_vel=angular_vel[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter10.Calculate.rotational_ke(
                    moment_inertia=moment_inertia[i], angular_vel=angular_vel[i]
                )
                self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_angular_vel(self) -> None:
        """
        Function tests solving for the angular velocity (angular_vel)
        """

        # Initial conditions

        kinetic_energy: List[float] = [9.0]
        moment_inertia: List[float] = [2.0]

        expected: List[float] = [3.0]

        for i in range(len(expected)):
            result = Chapter10.Calculate.rotational_ke(
                kinetic_energy=kinetic_energy[i], moment_inertia=moment_inertia[i]
            )
            self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_moment_inertia(self) -> None:
        """
        Function tests solving for the moment of inertia (moment_inertia)
        """

        # Initial conditions

        kinetic_energy: List[float] = [9.0]
        angular_vel: List[float] = [0.0]

        expected: List[Any] = [ValueError("Divison by zero is undefined.")]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter10.Calculate.rotational_ke(
                        kinetic_energy=kinetic_energy[i], angular_vel=angular_vel[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter10.Calculate.rotational_ke(
                    kinetic_energy=kinetic_energy[i], angular_vel=angular_vel[i]
                )
                self.assertAlmostEqual(result, expected[i], places=4)


class Testmagnitude_of_torque(unittest.TestCase):
    """
    Tests the magnitude_of_torque calculation method
    """

    def test_solving_for_torque(self) -> None:
        """
        Function tests solving for the magnitude of torque (torque)
        """

        # Initial conditions

        radius: List[float] = [2.0, 0.0]
        force: List[float] = [10.0, 10.0]
        theta: List[float] = [30.0, 30.0]

        expected: List[Any] = [
            10.0,
            ValueError(
                "The length of the center of axis to applied\
                    force cannot be less than or equal to zero."
            ),
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter10.Calculate.magnitude_of_torque(
                        radius=radius[i], force=force[i], theta=theta[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter10.Calculate.magnitude_of_torque(
                    radius=radius[i], force=force[i], theta=theta[i]
                )
                self.assertAlmostEqual(result, expected[i], places=4)

    def test_solving_for_theta(self) -> None:
        """
        Function tests solving for the angle of the applied force (theta)
        """

        # Initial conditions

        torque: List[float] = [10.0, 10.0, 30.0]
        radius: List[float] = [2.0, 2.0, 1.0]
        force: List[float] = [10.0, 0.0, 10.0]

        expected: List[Any] = [
            30.0,
            ValueError("Division by zero is undefined."),
            ValueError("math domain error"),
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter10.Calculate.magnitude_of_torque(
                        torque=torque[i], radius=radius[i], force=force[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter10.Calculate.magnitude_of_torque(
                    torque=torque[i], radius=radius[i], force=force[i]
                )
                self.assertAlmostEqual(result, expected[i], places=4)
