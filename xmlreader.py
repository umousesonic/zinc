import xml.etree.ElementTree as et
import os

class Reader:
    def __init__(self, path, filename):
        # change working directory
        os.chdir(path)
        # parse xml file into a tree
        tree = et.parse(filename)
        # get the root of the tree
        self._root = tree.getroot()

    def getQuestion(self):
        # get question description
        myQuestionText = self._root[0].attrib['questionText']
        return myQuestionText

    def getExpectedOutputs(self):
        # loop to load all input and output pairs into a list
        myExpectedOutputs = []
        for child in self._root[0]:
            myExpectedOutputs.append([child.attrib['input'], child.text])
        return myExpectedOutputs

    def getExpectedOutput(self, input):
        # loop to find certain input and return the output of it.
        for child in self._root[0]:
            if child.attrib['input'] == input:
                return child.text
        return 'none'