import xml.etree.ElementTree as et
import os

class Writer:

    def __init__(self):
        self._myName = '123'

        self._root = et.Element('root')     # the tree's root node
        self._question = et.SubElement(self._root, 'question')  # question node is a child node of tree.
        pass

    def SetQuestion(self, questionText):
        self._question.text = questionText
        pass

    def SetExpectedOutput(self, input, expectedOutput):
        et.SubElement(self._question, str(input)).text = expectedOutput  # storing input and output under question.
        pass

    def SetName(self, myName):
        self._myName = myName
        pass

    def Writeout(self, path):
        os.chdir(path)
        tree = et.ElementTree(self._root)
        tree.write(self._myName + '.xml', encoding='utf-8')
        pass