"""
    This is a program that goes to a website and finds the occurance of every word
    This program will write to a csv file about every words in the in the heading and its frequency
    We get a dictionary that we write to a csv file
"""

__author__ = "Aman Nagpal", "bucky"
__email__ = "amannagpal4@gmail.com"

import requests
from bs4 import BeautifulSoup
import operator
from pathlib import Path


ENVIOURMENT = "TEST"

class FrequencyCounter():

    url = "https://thenewboston.com/videos.php"
    words = []

    def __init__(self):
        if (ENVIOURMENT == "TEST"):
            file = Path('soup.txt')
            if (file.is_file() and (len(self.readSoup())) > 1):
                soup = self.readSoup()
            else:
                soup = self.makeSoup()
                self.saveSoup(soup)
        self.getWords(soup)
        self.cleanList(self.words)
        word_count = self.makeDictionary(self.words)
        self.sortDictionary(word_count)

    def makeSoup(self):
        """
        This function gets the text from the url provided and converts it into a soup object
        :return: soup object
        """
        try:
            # gets the text from the url
            html = requests.get(self.url).text
            # converts it into a soup
            soup = BeautifulSoup(html, 'html.parser')
            return soup

        except Exception as e:
            print(str(e))


    def getWords(self, soup):
        """
        This function gets the data from the url and converts it into a soup
        :return: populates the variable words with the words on the website
        """
        try:
            # gets all the words from the soup - loops through the sentences and breaks it down to words
            descriptions = soup.findAll('p', {'class': "top-course-details"})
            # for word in description description is an array that has all the descriptions we loop through it to get a single description
            for description in descriptions:
                # a loop to itterate through every word in the description
                for word in description.get_text().split():
                    self.words.append(word)  # we then add the words to self.words array
            return

        except Exception as e:
            print(str(e))

    def saveSoup(self, soup):
        """
        This function gets the soup object and saves it on a file
        :param soup: The soup object to save
        :return: True if file is succesfully create
        """
        try:
            fw = open("soup.txt", "w")
            fw.write(str(soup))
            fw.close()
            return True

        except Exception as e:
            print(str(e))

    def readSoup(self):
        """
        This function reads the soup from the text file
        :return: soup object
        """
        try:
            fw = open("soup.txt", "r")
            soup = fw.read()
            fw.close()
            return BeautifulSoup(soup, "html.parser")
        except Exception as e:
            print(str(e))

    def cleanList(self, list = []):
        """
        This function cleans the list of the word "videos" and any number
        :return: count of the number of elements removed
        """
        try:
            count = 0
            if(len(list) < 1):
                raise Exception("The word list was not properly populated and is empty")
            else:
                newList = []
                for word in list:
                    if (word.lower() == "videos" or word.isdigit()):
                        count = count + 1
                    else:
                        newList.append(word)
                self.words = newList
                return count

        except Exception as e:
            print(str(e))


    def makeDictionary(self, list = []):
        """
        This function creates a dictionary with the word as a key and its frequency as the value
        :param list: the list of words that need to be sorted
        :return: A dictionary created out of lists
        """
        word_count = {}
        for word in list:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        return word_count

    def sortDictionary(self, dict):
        """
        Sorts the dictionary provided based on its value
        :param dict: The dictionary that needs to be sorted
        :return: A sorted dictionary
        """
        sorted_dict = {}
        for key, value in sorted(dict.items(), key=operator.itemgetter(1)):
            sorted_dict[key] = value
            print(key, value)
        return sorted_dict

f = FrequencyCounter()


