import unittest

from typing import List
from physics_TUI.base_chapter import Equation
from physics_TUI.chapters.chapter8 import Chapter8


class TestChapter8Content(unittest.TestCase):
    """
    Content sanity tests for Chapter 8 (reference-only chapter,
    no calculation functions).
    """

    def setUp(self) -> None:
        """
        Set up the Chapter8 instance for testing
        """
        self.chapter = Chapter8()

    def test_equation_and_definition_counts(self) -> None:
        """
        Function tests that the chapter contains the expected number
        of equations and definitions
        """
        self.assertEqual(len(self.chapter.equations), 5)
        self.assertEqual(len(self.chapter.definitions), 13)

    def test_no_calculable_equations(self) -> None:
        """
        Function tests that the chapter has no calculable equations
        """
        calculable: List[Equation] = self.chapter.get_calculable_equations()
        self.assertEqual(calculable, [])

    def test_equations_have_name_and_formula(self) -> None:
        """
        Function tests that every equation has a non-empty name and formula
        """
        for equation in self.chapter.equations:
            self.assertTrue(equation.name)
            self.assertTrue(equation.formula)
