import requests
import json
class runner:
    def __init__(self):
        self._apiUrl = 'https://api.jdoodle.com/v1/execute'
        self._apiID = 'your id here'    # change it to your api id
        self._apiSecret = 'your secret here'    # change it to your api secret
        pass

    def sendCode(self, source_code, stdin):
        headers = {'content-type': 'application/json'}
        payload = json.dumps({'clientId': self._apiID,
                   'clientSecret': self._apiSecret,
                   'script': source_code,
                   'stdin': stdin,
                   'language': 'java',
                   'versionIndex': '3'})
        myPost = requests.post(self._apiUrl, headers=headers, data=payload)
        return myPost.json()

    def checkValue(self, source_code, myInput):
        # modify code to allow several pairs of input for the student program to run only once
        myModCode = 'public class main{' + \
                    source_code +\
                    'public static void main (String[] args){'
        # call multiple times of the student's function to get all results in single run
        for item in myInput:
            myModCode += 'System.out.println(StudentAnswer(\"' + item + '\"));'
            pass
        myModCode += '}}'

        # send code and return result
        return self.sendCode(myModCode, '')
        pass
