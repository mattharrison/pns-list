import unittest

class TestSkilz(unittest.TestCase):
    def test_creation(self):
        #
        # Create a list, ``faang``, with the names of:
        # Netflix, Amazon, Facebook, Google, and Apple
        #
        # ===========================================

        self.assertEqual(faang, ['Netflix', 'Amazon', 'Facebook', 'Google', 'Apple'])

        # Use the list constructor to create a
        # list, ``vals``, with the numbers in
        # the ``vals_range`` variable.
        #
        # ===========================================
        vals_range = range(len(faang))
        
        self.assertEqual(vals, [0,1,2,3,4])
        copy_f = faang
        # Remove Netflix from ``faang``
        #
        # ===========================================
        
        self.assertEqual(faang, ['Amazon', 'Facebook', 'Google', 'Apple'])
        self.assertEqual(faang, copy_f, 'You probably forgot to use .remove')
        
        # Append Microsoft to ``faang``
        #
        # ===========================================
        
        self.assertEqual(faang, ['Amazon', 'Facebook', 'Google', 'Apple', 'Microsoft'])
        self.assertEqual(faang, copy_f, 'You probably used + instead of .append')
        


if __name__ == '__main__':
    unittest.main()
