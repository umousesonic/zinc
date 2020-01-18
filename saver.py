import os

def AppendStudentReport(content, path, filename):
    # if the directory exists
    if os.path.exists(path):
        # if exists, write the results to a text file
        os.chdir(path)
        # in case the writing fails, close the file
        with open(filename+'.txt', 'a') as f:
            # seperate each run
            f.write('\n\n##### New Entry #####\n')
            f.write(content)
    else:
        # if not, make the directory then start over.
        os.makedirs(path)
        AppendStudentReport(content, path, filename)

