import fileinput

# Enter your code here. Read input from STDIN. Print output to STDOUT
def fixDoubleQuotes(string):
    return string.replace("\"\"", "*")

def fixCommas(string):
    stringList = list(string)
    for i in range(len(stringList)):
        if stringList[i] == ",":
            if stringList[:i].count("\"") % 2 == 1:
                stringList[i] = "#"
    return "".join(stringList)

def stripApostrophies(string):
    return string.replace("\"", "")

def fixOutputString(stringList):
    output = []
    for word in stringList:
        word = word.replace("#", ",")
        word = word.replace("*", "\"")
        output.append(word)
    return "".join(output)

for line in fileinput.input():
    fixedLine = stripApostrophies(fixCommas(fixDoubleQuotes(line)))
    # print(fixedLine)
    first_name, last_name, email, interests, notes, city, age = fixedLine.split(",")
    outputList = [first_name, ", ", age[:-1], " years old, is from ", city, " and is interested in ", interests, "."]
    fixedOutputString = fixOutputString(outputList)
    print(fixedOutputString)
