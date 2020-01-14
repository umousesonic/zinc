import xml.etree.ElementTree as et

class Writer:

    def __init__(self):
        self._name = '123'

        self._tree = et.Element('root')     # the tree's root node
        self._question = et.SubElement(self._tree, 'question')  # question node is a child node of tree.
        pass

    def SetQuestion(self, questionText):
        self._question.text = questionText
        pass

    def SetExpectedOutputs(self, expectedOutputs):
        # TODO: - format to accept proper inputs

        for item in expectedOutputs:
            et.SubElement(self._question, 'question' + expectedOutputs.index(item)).text = expectedOutputs  # the expected outputs are nodes under question.
        pass

    def SetName(self, name):
        self._name = name
        pass

    def Writeout(self):
        self._tree.write(self._name + '.xml', encoding='utf-8')
        pass

