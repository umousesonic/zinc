# TODO: - Expected outputs use form
#       - add column button
#       - finish output function
#       - opening and edit function


from creatorWindow import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import Writer.Writer as wt


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        self.myQuestionFile = wt()
        pass
    '''
    def BrowseButtonClicked(self):
        outputPath = QFileDialog.getExistingDirectory(self, 'Select Folder', '')
        self.OutfilePath.setText(outputPath)
        '''

    def DoOutput(self):
        outputPath = QFileDialog.getExistingDirectory(self, 'Select Folder', '')
        wt.SetName(self.NameBox.text())
        wt.SetQuestion(self.QuestionText.toPlainText())

        wt.Writeout()
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())