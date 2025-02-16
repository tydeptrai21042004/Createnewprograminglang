import sys,os,traceback
sys.path.append('./test/')
import subprocess
import unittest
from antlr4 import *

#Make sure that ANTLR_JAR is set to antlr-4.9.2-complete.jar
ANTLR_JAR = os.environ.get('ANTLR_JAR')
TARGET = '../target/main/minigo/parser' if os.name == 'posix' else os.path.normpath('../target/')

def main(argv):
    global ANTLR_JAR, TARGET
    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'gen':
        subprocess.run(["java","-jar",ANTLR_JAR,"-o","../target","-no-listener","-visitor","main/minigo/parser/MiniGo.g4"])
    elif argv[0] == 'clean':
        subprocess.run(["rm","-rf","../target/main"])
    elif argv[0] == '-assign1':
        from TestUtils import TestLexer,TestParser
        lexstart = int(argv[1])
        lexend = int(argv[2]) + 1
        lextestdir = argv[3]
        lexsoldir = argv[4]
        recstart = int(argv[5])
        recend = int(argv[6]) + 1
        rectestdir = argv[7]
        recsoldir = argv[8]
        for i in range(lexstart,lexend):
            try: 
                TestLexer.test(lextestdir,lexsoldir,i)
            except:
                trace = traceback.format_exc()
                print ("Test " + str(i) + " catches unexpected error:" + trace + "\n")
        for i in range(recstart,recend):
            try:
                TestParser.test(rectestdir,recsoldir,i)
            except:
                trace = traceback.format_exc()
                print ("Test " + str(i) + " catches unexpected error:" + trace + "\n")
    elif argv[0] == 'test':
        if not './main/minigo/parser/' in sys.path:
            sys.path.append('./main/minigo/parser/')
        if os.path.isdir(TARGET) and not TARGET in sys.path:
            sys.path.append(TARGET)
        if len(argv) < 2:
            printUsage()
        elif argv[1] == 'LexerSuite':
            from LexerSuite import LexerSuite
            suite = unittest.makeSuite(LexerSuite)
            test(suite)
        elif argv[1] == 'ParserSuite':
            from ParserSuite import ParserSuite
            suite = unittest.makeSuite(ParserSuite)
            test(suite)
        else:
            printUsage()
    else:
        printUsage()
    

def test(suite):
    from pprint import pprint
    from io import StringIO
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream)
    result = runner.run(suite)
    print('Tests run ', result.testsRun)
    print('Errors ', result.errors)
    pprint(result.failures)
    stream.seek(0)
    print('Test output\n', stream.read())

def printUsage():
    print("python run.py gen")
    print("python run.py test LexerSuite")
    print("python run.py test ParserSuite")

if __name__ == "__main__":
   main(sys.argv[1:])
