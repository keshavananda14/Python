#!/usr/bin/python

import sys
FileName = sys.argv[1]
print "FileName: ",FileName,",NoOfArguments: ",len(sys.argv),",CommandLineArguments: ",str(sys.argv)
EndOfFile = "Quit"
print "EndOfFile: ",EndOfFile
FileText = ""
try:
    file1 = open(FileName,"w")
except IOError:
    print "File ",FileName," Opening Error in Write Mode"
    sys.exit()
print FileName," Opened Succesfully"

while FileText != EndOfFile: 
    FileText = raw_input("Enter The Text:")
    if FileText == EndOfFile:
        file1.close();
        break;
    file1.write(FileText)
    file1.write('\n')
file1.close()


with open(FileName,"r") as file3:
    for line in file3:
        print line

try:
    file2 = open(FileName,"r")
except IOError:
    print "File ",FileName,"Opening Fialed in Read Mode"
print '\n',FileName,"Opend successfully\n"

for line in file2.readlines():
    print line
    
file2.close()
