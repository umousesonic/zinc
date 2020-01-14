# TODO: - Expected outputs use form
#       - add column button
#       - finish output function
#       - opening and edit function


from creatorWindow import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem
from PyQt5.Qt import Qt
from Writer import Writer as wt


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        self.ExpectedOutputTable.setColumnCount(3)
        self.ExpectedOutputTable.setHorizontalHeaderLabels(['checkbox', 'Input', 'Expected Output'])


        self.myQuestionFile = wt()
        pass

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
        for i in range(0, self.ExpectedOutputTable.rowCount()):
            if self.ExpectedOutputTable.item(i, 0).checkState() == Qt.Checked:
                self.ExpectedOutputTable.removeRow(i)
        pass

    def DoOutput(self):  # Finished entering information, Write into question XML
        outputPath = QFileDialog.getExistingDirectory(self, 'Select Folder', '')
        self.myQuestionFile.SetName(self.NameBox.text())
        self.myQuestionFile.SetQuestion(self.QuestionText.toPlainText())

        # Go through the form to put values into the answer branch.
        for i in range(0, self.ExpectedOutputTable.rowCount()):
            if self.ExpectedOutputTable.item(i, 1).text() != '' and self.ExpectedOutputTable.item(i, 2) != '':
                print(self.ExpectedOutputTable.item(i, 1).text()+','+ self.ExpectedOutputTable.item(i, 2).text())
                self.myQuestionFile.SetExpectedOutput(self.ExpectedOutputTable.item(i, 1).text(), self.ExpectedOutputTable.item(i, 2).text())
                pass
        self.myQuestionFile.Writeout(outputPath)
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
