import xml.etree.ElementTree as et
import os

class Writer:

    def __init__(self):
        # default value for name
        self._myName = '123'
        self._root = et.Element('root')     # the tree's root node
        #self._question = et.SubElement(self._root, 'question')  # question node is a child node of tree.
        pass

    def SetQuestion(self, questionText):
        # Set question description
        self._question = et.SubElement(self._root, 'question', {'questionText': questionText})
        pass

    def SetExpectedOutput(self, input, expectedOutput):
        # Append a subelement of pair of input and expected output to the tree
        et.SubElement(self._question, 'expectedOutput', {'input': str(input)}).text = expectedOutput  # storing input and output under question.
        pass

    def SetName(self, myName):
        # Set the question name
        self._myName = myName
        pass

    def Writeout(self, path):
        os.chdir(path)
        tree = et.ElementTree(self._root)
        tree.write(self._myName + '.xml', encoding='utf-8')
        pass