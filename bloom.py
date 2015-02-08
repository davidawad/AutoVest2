#!/usr/bin/python
import subprocess, sys
'''
This script will perform a series of headless web page console inspections while capturing and examining the STDOUT of those processes.
The script will then create JIRA issues for each error or warning given by based on the outputs of each of these subprocesses each time this script is run.

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--project',   required=True, help='JIRA project name')
parser.add_argument('-i', '--issueType', required=True, help='Jira IssueType')
parser.add_argument('-w', '--website',   required=True, help='Site to scrape' )
args = parser.parse_args()
'''

def fileParse(output):
        if not output:
                print "no console errors (apparently)"
                return
        with open('prices.txt','r') as f:
            inputS = f.read()
        inputStr = inputS.splitlines()
        for line in inputStr :
            return 

def runCommand(cmd):
    proc = subprocess.Popen( cmd, stdout = subprocess.PIPE)
    return proc.communicate()[0]

def testCommand():
    consoleOut = runCommand( ["nodejs", "bloom.js", "AAPL US Equity"] )
    print consoleOut
    fileParse()
