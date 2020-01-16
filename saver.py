import os

def AppendStudentReport(content, path, filename):
    if os.path.exists(path):
        os.chdir(path)
        with open(filename+'.txt', 'a') as f:
            f.write('\n\n##### New Entry #####\n')
            f.write(content)
    else:
        os.mkdir(path)
        AppendStudentReport(content, path, filename)

