import unittest

class TestSkilz(unittest.TestCase):
    def test_dict(self):
        #
        # Create a dictionary, ``company_bosses``,,
        # from ``companies`` and ``bosses`` mapping
        # the company name (key) to CEO name (value).
        # (Use ``dict`` and ``zip``)
        # ===========================================
        companies = 'Amazon, Apple, Facebook, Google, Netflix'.split(', ')
        bosses = ['Bezos', 'Cook', 'Zuck', 'Pichai', 'Hastings']


        self.assertEqual(company_bosses,
                         {'Amazon': 'Bezos',
                          'Apple': 'Cook',
                          'Facebook': 'Zuck',
                          'Google': 'Pichai',
                          'Netflix': 'Hastings'})

        #
        # Create a dictionary, ``bosses_salaries``,,
        # from ``bosses`` and ``salaries`` mapping
        # the CEO name (key) to salary (value).
        # (Use a dictionary comprehension)
        # ===========================================
        salaries = [81_840, 3_000_000, 1, 2_000_000, 700_000]


        
        self.assertEqual(bosses_salaries,
                         {'Bezos': 81840, 'Cook': 3000000, 'Zuck': 1, 'Pichai': 2000000, 'Hastings': 700000})

        #
        # Add Microsoft/Nadella to ``company_bosses``
        # ===========================================


        self.assertEqual(company_bosses['Microsoft'], 'Nadella')

        #
        # Check if 'Adobe' is in ``company_bosses``.
        # Store the result in ``found``.
        # ===========================================


        self.assertEqual(found, 'Adobe' in company_bosses)

        #
        # Get the boss for 'Adobe' from ``company_bosses``.
        # Return 'Missing' if not found.
        # Store the result in ``boss``.
        # ===========================================


        self.assertEqual(boss, 'Missing')

if __name__ == '__main__':
    unittest.main()
