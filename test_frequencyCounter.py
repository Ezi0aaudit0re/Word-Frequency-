from unittest import TestCase
from frequencyCounter import FrequencyCounter
from pathlib import Path

class TestFrequencyCounter(TestCase):
    instance = None
    soup = None

    def setUp(self):
        self.instance = FrequencyCounter()
        # this code block checks if there is a file soup.txt and if there is gets the soup from that place
        path = Path("soup.txt")
        if (path.is_file()):
            self.soup = self.instance.readSoup()
        else:
           self.soup = self.instance.makeSoup()
        # to check that __init__ method is working properly we can use this method as it initializes a new class
        # we check the length of the words variable inside the class to figure out weather the method has worked properly
        self.assertGreaterEqual(len(self.instance.words), 1, {"There was some problem in the init method"})

    def test_makeSoup(self):
        length = len(self.soup.findAll('div'))
        self.assertGreaterEqual(length, 1, {"There was some problem in makeSoup method"})

    def test_getWords(self):
        self.instance.getWords(self.soup)
        self.assertGreaterEqual(len(self.instance.words), 1, {"There was some problem in the getWords method"})  # we do self.assertGreaterEqual because its a part of the TestCase class


    def test_saveSoup(self):
        self.assertEquals(self.instance.saveSoup(self.soup), True, {"There was some problem with the saveSoup method"})

    def test_readSoup(self):
        path = Path("soup.txt")
        if(path.is_file()):
            soup = self.instance.readSoup()
            length = len(soup.findAll('div'))
            self.assertGreaterEqual(length, 1, {"There was some problem in makeSoup method"})

    def test_cleanList(self):
        try:
            length = self.instance.cleanList["Aman", "83", "Videos", "Programmer"]
            self.assertEquals(length, 2, {"The function cleanList is not working as expected"})
        except TypeError as e:
            print(str(e))

    def test_makeDictionary(self):
        self.assertEquals(self.instance.makeDictionary(["aman", "fat", "aman", "fat"]), {"aman": 2, "fat": 2}, {"There is some problem with the makeDictionary method"})


    def test_sortDictionary(self):
        sorted_dictionary = self.instance.sortDictionary({"aman": 10, "fat": 4})
        val = sorted_dictionary["fat"]
        if val != 4:
           self.assertEqual(1, 10, {"THere is something wrong with the method sortDictionary"})
