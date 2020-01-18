from creatorWindow import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem
from PyQt5.Qt import Qt
from Writer import Writer as wt
from xmlreader import *


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        # Set up the expected output table, columns and labels.
        self.ExpectedOutputTable.setColumnCount(3)
        self.ExpectedOutputTable.setHorizontalHeaderLabels(['checkbox', 'Input', 'Expected Output'])

        # Instantiate a xml writer
        self.myQuestionFile = wt()
        pass

    def OpenButtonClicked(self):
        filePath, _filter = QFileDialog.getOpenFileName(self, "Select Question file...", '', "XML File (*.xml)")
        if not filePath == "":
            print(filePath)
            print(type(filePath))
            print(os.path.dirname(filePath))
            print(os.path.basename(filePath))
            myReader = Reader(os.path.dirname(filePath), os.path.basename(filePath))
            self.NameBox.setText(os.path.basename(filePath)[:-4])
            self.QuestionText.setText(myReader.getQuestion())
            myExpectedOutputs = myReader.getExpectedOutputs()
            self.ExpectedOutputTable.setRowCount(len(myExpectedOutputs))
            for i in range(0, len(myExpectedOutputs)):
                checkBox = QTableWidgetItem()
                checkBox.setCheckState(Qt.Unchecked)
                self.ExpectedOutputTable.setItem(i, 0, checkBox)
                self.ExpectedOutputTable.setItem(i, 1, QTableWidgetItem(myExpectedOutputs[i][0]))
                self.ExpectedOutputTable.setItem(i, 2, QTableWidgetItem(myExpectedOutputs[i][1]))


    def AddLine(self, table):
        row = table.rowCount()
        table.setRowCount(row + 1)
        checkBox = QTableWidgetItem()
        checkBox.setCheckState(Qt.Unchecked)

        table.setItem(row, 0, checkBox)

    def AddButtonClicked(self):
        self.AddLine(self.ExpectedOutputTable)
        pass

    def DeleteButtonClicked(self):
        myRow = -1
        for i in range(0, self.ExpectedOutputTable.rowCount()):
            if self.ExpectedOutputTable.item(i, 0).checkState() == Qt.Checked:
                myRow = i
        if not myRow == -1:
            self.ExpectedOutputTable.removeRow(myRow)
            self.DeleteButtonClicked()
        pass

    def DoOutput(self):  # Finished entering information, Write into question XML
        # Checking inputs
        if self.NameBox.text() == '':
            return ''
        if self.ExpectedOutputTable.rowCount() <= 0:
            return ''
        # Pop up window for saving directory
        outputPath = QFileDialog.getExistingDirectory(self, 'Select Folder', '')
        # if action cancelled
        if outputPath == '':
            return ''
        self.myQuestionFile.SetName(self.NameBox.text())
        self.myQuestionFile.SetQuestion(self.QuestionText.toPlainText())

        # Go through the form to put values into the answer branch.
        for i in range(0, self.ExpectedOutputTable.rowCount()):
            if str(self.ExpectedOutputTable.item(i, 1).text()) != '' and str(self.ExpectedOutputTable.item(i, 2).text()) != '':
                self.myQuestionFile.SetExpectedOutput(self.ExpectedOutputTable.item(i, 1).text(), self.ExpectedOutputTable.item(i, 2).text())
                pass
        self.myQuestionFile.Writeout(outputPath)
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
