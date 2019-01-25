import unittest
from ansiblelint import Runner, RulesCollection
from ansiblelint.rules.UseShellInsteadOfCommandRule import UseShellInsteadOfCommandRule


class TestUseShellInsteadOfCommandRule(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(UseShellInsteadOfCommandRule())

    def test_file_positive(self):
        success = 'test/shell-instead-of-command-success.yml'
        good_runner = Runner(self.collection, success, [], [], [])
        self.assertEqual([], good_runner.run())

    def test_file_negative(self):
        failure = 'test/shell-instead-of-command-failure.yml'
        bad_runner = Runner(self.collection, failure, [], [], [])
        errs = bad_runner.run()
        self.assertEqual(2, len(errs))
