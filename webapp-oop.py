from flask import *
from flask_wtf import FlaskForm
from flask_login import LoginManager, login_required, logout_user, login_user, current_user
from ProgrammingForm import ProgrammingForm
from xmlreader import Reader as rd
import saver
import os
from runner import *
import Users


class webapp2:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'hard to guess string'
        self.path = ('/Users/apple/Desktop/questions')


        self.login_manager = LoginManager()
        self.login_manager.login_view = 'login'
        self.login_manager.login_message_category = 'info'
        self.login_manager.login_message = 'Access denied.'
        self.login_manager.init_app(self.app)

    def init_app(self):
        self.login_manager.user_loader(self.load_user)
        self.app.route('/favicon.ico')(self.favicon)
        self.app.route('/')(self.index)
        self.app.route('/questions/<questionName>', methods=['GET', 'POST'])(login_required(self.question))
        self.app.route('/login', methods=['GET', 'POST'])(self.login)
        self.app.route('/logout')(login_required(self.logout))

    def load_user(self, userId):
        if Users.getUser(userId) is not None:
            myUser = Users.User()
            myUser.id = userId
            return myUser


    def favicon(self):
        return send_from_directory(os.path.join(self.app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')


    def index(self):
        #return 'hello world'
        questionList = []
        for item in os.listdir(self.path):
            if item.split('.')[-1] == 'xml':
                questionList.append(item[:-4])
        return render_template('index-template.html', questions=questionList)


    def question(self, questionName):
        myRunner = runner()
        # get question text
        myQuestionFile = rd(self.path, questionName + '.xml')
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
            displayResult = ''
            processedMyResult = myResult['output'].split('\n')
            processedMyResult.pop()
            print("myresult: " + str(len(processedMyResult)))
            print ("myoutput length: " + str(len(myOutput)))
            flagAllCorrect = True
            if len(processedMyResult) == len(myOutput):
                for i in range(0, len(processedMyResult)):
                    displayResult += myInput[i] + ': '
                    if processedMyResult[i] == myOutput[i]:
                        displayResult += 'correct'
                    else:
                        displayResult += 'incorrect'
                        flagAllCorrect = False
                    displayResult += '|'
            else:
                displayResult = 'error:|'
                flagAllCorrect = False
                displayResult += myResult['output']
                pass
            # save student result
            if flagAllCorrect:
                saver.AppendStudentReport(programForm.programField.data + '\n\nResult:\n' + displayResult, self.path + '/StudentReports/' + questionName, current_user.get_id() + '.correct')
            else:
                saver.AppendStudentReport(programForm.programField.data + '\n\nResult:\n' + displayResult, self.path + '/StudentReports/' + questionName,
                                      current_user.get_id() + '.incorrect')

            #render result
            return render_template('question-template.html', questionName=questionName, questionText=myQuestionText, requirements=myRequirements,
                               form=programForm, result=displayResult)

        # render html
        return render_template('question-template.html', questionName=questionName, questionText=myQuestionText, requirements=myRequirements, form=programForm)


    def login(self):
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

    def logout(self):
        logout_user()
        return render_template('LoggedOut.html')

if __name__ == '__main__':
    myapp = webapp2()
    myapp.init_app()
    myapp.app.run(host='0.0.0.0', port=80)
    #myapp.app.run(debug=True)