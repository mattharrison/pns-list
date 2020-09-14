import unittest

class TestTuple(unittest.TestCase):
    def test_tup(self):
        # Create a tuple, ``lego``, that has the following values:
        #
        # 2,2,'green'
        #
        # These represent:
        #  * width (2)
        #  * length (2)
        #  * color ('green')
        # ===========================================


        self.assertEqual(lego,  (2,2,'green'))

        # Fred used a list to store tuple data (bad Fred!), ``bad_lego``.
        # Create a tuple from Fred's data, ``lego2``, that uses
        # the ``tuple`` constructor
        # ===========================================
        bad_lego = [4,2,'blue']

        self.assertEqual(lego2,  (4,2,'blue'))

        # Unpack the values of ``lego2`` into these variables:
        # ``width``, ``length``, ``color``
        # ===========================================

        self.assertEqual((width, length, color), (4,2,'blue'))


        # Create a named tuple, ``Lego``.
        # Create a variable, ``lego3``, (using Lego) that has the following values:
        #
        # 1,2,'red'
        #
        # These represent: width, length, and color
        # ===========================================

        self.assertEqual(lego3.width, 1)
        self.assertEqual(lego3[-1], 'red')




if __name__ == '__main__':
    unittest.main()

