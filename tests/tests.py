# -*- coding: utf-8 -*-
"""
created by YW
"""

import unittest

from translator import english_to_french, english_to_german

class TestEngFrench(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(english_to_french('Where is the library?'), 'Où est la bibliothèque?')

    def test2(self):
        self.assertEqual(english_to_french('Good morning. Would you like some coffee?'), 'Bonjour. Voudriez-vous du café?')
        
    def test3(self):
        self.assertEqual(english_to_french('Two birds with one stone is good luck'), 'Deux oiseaux avec une pierre est bonne chance')
    
    def test_none(self):
        self.assertEqual(english_to_french(None), None)
    
    def test_empty(self):
        self.assertEqual(english_to_french(''), '')
    
    def test_hw(self):
        self.assertEqual(english_to_french('Hello world'), 'Bonjour le monde')
        

class TestEngGer(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(english_to_german('Where is the library?'), 'Wo ist die Bibliothek?')

    def test2(self):
        self.assertEqual(english_to_german('Good morning. Would you like some coffee?'), 'Guten Morgen. Möchten Sie etwas Kaffee?')
        
    def test3(self):
        self.assertEqual(english_to_german('Two birds with one stone is good luck'), 'Zwei Vögel mit einem Stein sind viel Glück')
    
    def test_none(self):
        self.assertEqual(english_to_german(None), None)
    
    def test_empty(self):
        self.assertEqual(english_to_german(''), '')
    
    def test_hw(self):
        self.assertEqual(english_to_german('Hello world'), 'Hallo Welt')

unittest.main()