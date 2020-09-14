import unittest

class TestSkilz(unittest.TestCase):
    def test_sort(self):
        #
        # Sort the ``faang`` list in place
        #
        # ===========================================
        faang = 'Netflix, Amazon, Facebook, Google, Apple'.split(', ')
        self.assertEqual(faang, ['Amazon', 'Apple', 'Facebook', 'Google', 'Netflix'])

        #
        # Sort the ``salaries`` list in place
        # from largest to smallest
        #
        # ===========================================
        bosses = ['Bezos', 'Cook', 'Zuck', 'Pichai', 'Hastings']
        salaries = [81_840, 3_000_000, 1, 2_000_000, 700_000]

        self.assertEqual(salaries, [3000000, 2000000, 700000, 81840, 1])

        #
        # Create a variable, ``by_name``, that
        # has a sorted list of ``people`` by name.
        #
        # ===========================================
        people = [{'name': 'Bezos', 'salary': 3000000},
         {'name': 'Cook', 'salary': 2000000},
         {'name': 'Zuck', 'salary': 700000},
         {'name': 'Pichai', 'salary': 81840},
         {'name': 'Hastings', 'salary': 1}]

        self.assertEqual([n['name'] for n in by_name], ['Bezos', 'Cook', 'Hastings', 'Pichai', 'Zuck'])


if __name__ == '__main__':
    unittest.main()
