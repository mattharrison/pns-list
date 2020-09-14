import unittest

class TestSkilz(unittest.TestCase):
    def test_dict(self):
        #
        # Create a dictionary, ``bosses_company``,,
        # from ``companies`` and ``bosses`` mapping
        # the CEO name (key) to company name (value).
        # (Use ``dict`` and ``zip``)
        # ===========================================
        companies = 'Amazon, Apple, Facebook, Google, Netflix'.split(', ')
        bosses = ['Bezos', 'Cook', 'Zuck', 'Pichai', 'Hastings']


        self.assertEqual(bosses_company,
                         {'Bezos': 'Amazon',
                          'Cook': 'Apple',
                          'Hastings': 'Netflix',
                          'Pichai': 'Google',
                          'Zuck': 'Facebook'})

        # Create an inverted index for ``bosses_company``
        # in ``company_bosses``.
        # ===========================================

        self.assertEqual(company_bosses,
                         {'Amazon': 'Bezos',
                          'Apple': 'Cook',
                          'Facebook': 'Zuck',
                          'Google': 'Pichai',
                          'Netflix': 'Hastings'})

        #
        # Add 'Sarandos' to ``bosses_company``.
        # Use 'Netflix' as a value.
        # ===========================================

        self.assertEqual(bosses_company['Sarandos'],
                         'Netflix')

        # Create an inverted index for ``bosses_company``
        # in ``company_bosses2``. Because ``bosses_company``
        # now has non-unique values map the keys to a list
        # ===========================================


        self.assertEqual(company_bosses2['Netflix'],  ['Hastings', 'Sarandos'])


if __name__ == '__main__':
    unittest.main()
