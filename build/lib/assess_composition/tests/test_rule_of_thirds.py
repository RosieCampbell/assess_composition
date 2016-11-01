from unittest import TestCase

import assess_composition.rule_of_thirds

class TestRuleOfThirds(TestCase):
    def test_calculate_thirds(self):
        s = assess_composition.calculate_thirds(999)
        self.assertEquals(s, (333, 666))
