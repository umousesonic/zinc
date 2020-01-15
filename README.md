# CS-ia

It's my ia.
## What is this
It is a software bundle created to allow user 
to customize and create questions that can be 
accessed through a browser and interactively 
check the answers by applying intended inputs 
and outputs to check if the program functions as 
normal.

## For whom this is designed
Basically people who want to create their own 
"Codingbat questions".

## How to use
The software is divided into 2 parts. The first part is the **Creator**, which is a software with PyQt5 based GUI to allow users to create their question files. To run it, type in your console:
`python /path/to/gui.py`

After creating the question file, the question files need to be loaded into the server and configure the path in **Webapp**, which is a Flask based software, to allow it to be hosted online. Create a folder named `StudentResponse` in your questions folder first, then place your question files into the root directory of your questions folder. Go ahead and modify the `path` variable in the `webapp.py` to point to your path to question folder, and run in your counsole:`python /path/to/webapp.py`

Finally, the end users will be accessing it through their browser.

## How to install it
### Software requirements:
- Python 3
- Flask
- Flask_wtf
- PyQt5
- Requests
### Installation process
Clone the resporitry to your computer and the server. 
 
# Credits
- Flask
- Flask_wtf
- PyQt5
- Python
- Requests