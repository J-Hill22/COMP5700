'''
Created on Jan 19, 2023

@author: Jarrett
'''
import unittest
import app

class sbomTest(unittest.TestCase):


    def test_sbom_100_ShouldReturnAuthorName(self):
        myName = 'jwh0100'
        result = app._getAuthor('../../')
        resultingAuthorName = result['author']
        self.assertEqual(resultingAuthorName, myName)
