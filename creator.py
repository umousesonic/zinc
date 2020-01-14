# this creator creates the question xml based on user inputs.
import Writer.Writer as wt


# gui

if __name__=='__main__':
    myFileName = input('Question name: ')
    myQuestionFile = wt(myFileName)

    myQuestion = input('Question Text: ')
    myQuestionFile.SetQuestion(myQuestion)

    myExpectedOutputs = input('Expected outputs: ')
    pass