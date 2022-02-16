#!/usr/bin/env python3
#Hold the code
lines = []

#Explanations
def cHelp():
    print("addCode(change)")
    print("   Adds code to your function. Use 3 quotation marks for multi-line things like for or while")
    print("")
    print("removeCode(index)")
    print("   Removes the code at the specied index. Index can be specified as an argument or after it's ran")
    print("")
    print("printCode()")
    print("   Prints all your code. No arguments")
    print("")
    print("changeCode(change, index)")
    print("   Changes the code at the specified index")
    print("")
    print("runCode()")
    print("   Runs your code")
    print("")
    print("cHelp()")
    print("   Prints this screen")
    print("")
    print("writeOut(fileName,AR)")
    print("   Writes your code in a seperate file. AR being an optional argument saying whether you want to append to a file or replace a file.")
    print("")
    print("Example:")
    print('addCode(\'Print("Put down that cookie!")\')')
cHelp()
#Add to the storage
def addCode(change):
    lines.append(change)
    for anyitem in lines:
        print(str(anyitem))
        
def removeCode(index="NaN"):
    codeCopy = line
    if index == "NaN":
        answer = input("Print current code? (y/n): ")
        if answer == "y":
            for printNum in range(len(codeCopy)):
                print(codeCopy[printNum],"| Index Number:", printNum)
        elif answer == "n":
            pass
        else:
            print("Invalid Input")
    if index == "NaN":
        index = int(input("Which index to remove? "))
    print("Line removed: ", lines[int(remNum)])
    lines.pop(int(remNum))

def printCode():
    for printNum in range(len(lines)):
        print(lines[printNum],"| Index Number:", printNum)
def changeCode(change, index):
    lines[index] = change
def runCode():
    for runLine in lines:
        exec(runLine)
def writeOut(fileName, AR="NaN"):
    if AR == "NaN":
        AR = input("Would you like to append (add to) an existing file or replace an existing file?\n(a/r): ")
    if AR.lower() == "a" or AR.lower == "append":
        try:
            output = open(fileName + ".py", "a")
        except:
            print("No file found to append to")
    elif AR.lower() == "r" or AR.lower == "replace":
        try:
            output = open(fileName + ".py", "w")
        except:
            print("An error occured")
    else:
        print("Invalid response")
        return
    for line in lines:
        output.write(line + "\n")
    output.close()
