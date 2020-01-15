from flask import *
from flask_wtf import FlaskForm
from ProgrammingForm import ProgrammingForm
from xmlreader import Reader as rd
import saver
import os
from runner import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
path = ('C:/Users/WIN10/Desktop/questions')

@app.route('/')
def index():
    #return 'hello world'
    questionList = []
    for item in os.listdir(path):
        if item.split('.')[-1] == 'xml':
            questionList.append(item[:-4])
    return render_template('index-template.html', questions=questionList)

@app.route('/questions/<questionName>', methods=['GET', 'POST'])
def question(questionName):
    myRunner = runner()
    # get question text
    myQuestionFile = rd(path, questionName + '.xml')
    myQuestionText = myQuestionFile.getQuestion()

    # get requirements
    myRequirements = ''
    for item in myQuestionFile.getExpectedOutputs():
        myRequirements += item[0]
        myRequirements += ' ---> '
        myRequirements += item[1]
        myRequirements += '|'

    # programming field as form
    programForm = ProgrammingForm()

    # handle incoming data
    if request.method == 'POST':
        # save student result
        saver.AppendStudentReport(programForm.programField.data, path+'/StudentReports', 'student-name')
        # get proper inputs and outputs
        myInput = []
        myOutput = []
        for item in myQuestionFile.getExpectedOutputs():
            myInput.append(item[0])
            myOutput.append(item[1])
        # send to online IDE
        myResult = myRunner.checkValue(programForm.programField.data, myInput)

        # check if correct and calculate result
        displayResult = ''
        processedMyResult = myResult['output'].split('\n')
        processedMyResult.pop()
        print("myresult: " + str(len(processedMyResult)))
        print ("myoutput length: " + str(len(myOutput)))
        if len(processedMyResult) == len(myOutput):
            for i in range(0, len(processedMyResult)):
                displayResult += myInput[i] + ': '
                if processedMyResult[i] == myOutput[i]:
                    displayResult += 'correct'
                else:
                    displayResult += 'incorrect'
                displayResult += '|'
        else:
            displayResult = 'error:|'
            displayResult += myResult['output']
            pass

        #render result
        return render_template('question-template.html', questionName=questionName, questionText=myQuestionText, requirements=myRequirements,
                               form=programForm, result=displayResult)

    # render html
    return render_template('question-template.html', questionName=questionName, questionText=myQuestionText, requirements=myRequirements, form=programForm)



if __name__ == '__main__':
    app.run(debug=True)