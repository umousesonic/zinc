from flask import *
from flask_wtf import FlaskForm
from flask_login import LoginManager, login_required, logout_user, login_user, current_user
from ProgrammingForm import ProgrammingForm
from xmlreader import Reader as rd
import saver
import os
from runner import *
import Users

# instantiate a flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'   # CSRF protection
path = ('/path/to/questions') # User's question directory

# instantiate LoginManager and set up
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.login_message = 'Access denied.'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userId):
    if Users.getUser(userId) is not None:
        myUser = Users.User()
        myUser.id = userId
        return myUser

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    # the index page
    # get and display question list by going over the files in user's question file path
    questionList = []
    for item in os.listdir(path):
        if item.split('.')[-1] == 'xml':
            # select only the xml files
            questionList.append(item[:-4])
    # render the website with Jinja2
    return render_template('index-template.html', questions=questionList)

@app.route('/questions/<questionName>', methods=['GET', 'POST'])
@login_required
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
        # get proper inputs and outputs
        myInput = []
        myOutput = []
        for item in myQuestionFile.getExpectedOutputs():
            myInput.append(item[0])
            myOutput.append(item[1])
        # send to online IDE
        myResult = myRunner.checkValue(programForm.programField.data, myInput)

        # check if correct and calculate result
        # structure all runs' result into a list
        displayResult = ''
        processedMyResult = myResult['output'].split('\n')
        processedMyResult.pop()

        # go through all the runs and compare the output with expected outputs
        flagAllCorrect = True
        # if the length mismatches, it means that the code generated error.
        if len(processedMyResult) == len(myOutput):
            for i in range(0, len(processedMyResult)):
                displayResult += myInput[i] + ': '
                if processedMyResult[i] == myOutput[i]:
                    # when match is correct.
                    displayResult += 'correct'
                else:
                    # when mismatches is incorrect.
                    # Also, one single correct makes it never all correct.
                    displayResult += 'incorrect'
                    flagAllCorrect = False
                displayResult += '|'
        else:
            # the student's code generated errors.
            displayResult = 'error:|'
            flagAllCorrect = False
            displayResult += myResult['output']
            pass
        # save student result
        if flagAllCorrect:
            saver.AppendStudentReport(programForm.programField.data + '\n\nResult:\n' + displayResult,
                                      path + '/StudentReports/' + questionName, current_user.get_id() + '.correct')
        else:
            saver.AppendStudentReport(programForm.programField.data + '\n\nResult:\n' + displayResult,
                                      path + '/StudentReports/' + questionName,
                                      current_user.get_id() + '.incorrect')

        #render result
        return render_template('question-template.html', questionName=questionName, questionText=myQuestionText, requirements=myRequirements,
                               form=programForm, result=displayResult)

    # render html
    return render_template('question-template.html', questionName=questionName, questionText=myQuestionText, requirements=myRequirements, form=programForm)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userId = request.form.get('userid')
        myUser = Users.getUser(userId)
        if myUser is not None and request.form['password'] == myUser['password']:
            currUser = Users.User()
            currUser.id = userId
            # login with flask-login
            login_user(currUser)
            return redirect(url_for('index'))
        # login fails
        flash('Wrong username or password!')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('LoggedOut.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    #app.run(debug=True, port=80)