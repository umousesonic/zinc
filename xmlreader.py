import xml.etree.ElementTree as et
import os

class Reader:
    def __init__(self, path, filename):
        os.chdir(path)
        tree = et.parse(filename)
        self._root = tree.getroot()
        pass

    def getQuestion(self):
        myQuestionText = self._root[0].attrib['questionText']
        return myQuestionText

    def getExpectedOutputs(self):
        myExpectedOutputs = []
        for child in self._root[0]:
            myExpectedOutputs.append([child.attrib['input'], child.text])
        return myExpectedOutputs

    def getExpectedOutput(self, input):
        for child in self._root[0]:
            if child.attrib['input'] == input:
                return child.text
        return 'none'