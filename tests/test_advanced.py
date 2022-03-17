# -*- coding: utf-8 -*-

from .context import sample

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(print())
        """
        Write your test program entry
        """
        # corpus = ['this is the first document',
        #           'this is the second second document',
        #           'and the third one',
        #           'is this the first document']
        # self.assertIsNone(sample.run(corpus))

        path = './corpus/doc_one.txt'
        corpus = sample.read(path)
        print(corpus)
        self.assertIsNone(sample.run(corpus))


if __name__ == '__main__':
    unittest.main()
