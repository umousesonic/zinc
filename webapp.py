

from flask import *
from flask_wtf import FlaskForm
from ProgrammingForm import ProgrammingForm
from xmlreader import Reader as rd

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
path = ('/Users/apple/Desktop')

@app.route('/')
def index():
    return 'hello world'

@app.route('/questions/<questionName>', methods=['GET', 'POST'])
def question(questionName):
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
    # programForm.variable

    # render html
    return render_template('question-template.html', questionText=myQuestionText, requirements=myRequirements, form=programForm)


if __name__ == '__main__':
    app.run(debug=True)