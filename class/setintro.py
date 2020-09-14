import unittest

class TestTuple(unittest.TestCase):
    def test_tup(self):
        # How many unique characters are there in the following word?
        # 
        # supercalifragilisticexpialidocious
        #
        # Use the length of a set to figure it out.
        # Store the result in ``sflen``.
        # ===========================================


        self.assertEqual(sflen,  0xf)

        # The ``letters`` variable has all of the lowercase English
        # letters. Which letters are not in supercalifragilisticexpialidocious?
        # Store the result in a set called ``missing``
        # ===========================================
        letters = [chr(num) for num in range(ord('a'), ord('z')+1)]

        self.assertEqual(type(missing), set)
        self.assertEqual(''.join(sorted(missing)), 'bhjkmnqvwyz')

        # ``attendees`` contains the numeric ids of all students who
        # logged into a course.
        # Add user 17 to the course.
        # ===========================================
        attendees = set([0x42, 0o42, 420])

        self.assertEqual(attendees & {17}, {17})

        # Is user 42 logged in?
        # Store the result in ``found42``
        # ===========================================
        
        self.assertEqual(found42, False)

        # ``attendees2`` contains the numeric ids of all students who
        # logged into the course yesterday.
        # Find the students who only logged in yesterday and
        # store the results in the set ``yesterday_only``
        # ===========================================
        attendees2 = set([0x42, 402, 420, ])

        self.assertEqual(yesterday_only, {402})


        # Find the students who only logged both days and
        # store the results in the set ``both_days``
        # ===========================================

        self.assertEqual(both_days, {66, 420})


        



if __name__ == '__main__':
    unittest.main()

