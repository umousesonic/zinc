import os

def AppendStudentReport(content, path, filename):
    os.chdir(path)
    with open(filename+'.txt', 'a') as f:
        f.write('\n\n###New Entry###\n')
        f.write(content)

