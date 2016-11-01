from unittest import TestCase

from assess_composition.command_line import main


class TestCmd(TestCase):
    def test_basic(self):
        main()
