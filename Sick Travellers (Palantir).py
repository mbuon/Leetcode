# Complete the traceDisease function below.
# initialStates is an array of strings, each string a line of input. 
# Your return value should also be a list of strings (see the prompt for the expected output format)
# Content sent to stdout (i.e. any print statements) will be sent to a separate output that is ignored by the test checker.
def everyoneHealthy(officeState):
    everyoneHealthy = True
    for office in officeState:
        for person in officeState[office]:
            if person[1] != "HEALTHY":
                everyoneHealthy = False
                break
    return everyoneHealthy

def printStates(officeState):
    # Print the states, sorted by the name to the print buffer
    result = []
    output = []
    for office in officeState:
        for personState in officeState[office]:
            result.append([personState[0], [personState[1]]])
    result = sorted(result, key = lambda x: x[0])
    for personState in result:
        output.append(personState[1][0])
    return(" ".join(output))
    
def printNames(officeState):
    # Print names in sorted order to the print buffer
    result = []
    for office in officeState:
        for personState in officeState[office]:
            result.append(personState[0])
    result = sorted(result)
    return(" ".join(result))

def traceDisease(initialStates):
    # allOutput is out print buffer, and officeState maintains the state of each person in each office
    allOutput = []
    officeState = {}
    # Determine and print the names, and initial states to the print buffer
    for initialState in initialStates:
        values = initialState.split(" ")
        name = values[0]
        state = values[1]
        offices = values[2:]
        firstOffice = offices[0]
        if firstOffice in officeState:
            officeState[firstOffice].append((name, state, offices))
        else:
            officeState[firstOffice] = []
            officeState[firstOffice].append((name, state, offices))
    allOutput.append(printNames(officeState))
    allOutput.append(printStates(officeState))
    # All people initialized to an office
    # Now, for each day, 1) move people to their next office, and change state
    for day in range(1, 365):
        if everyoneHealthy(officeState):
            break
        newOfficeState = {}
        for office in officeState:
            # In each office, just check if there is at least one exposer
            exposerPresent = False
            for person in officeState[office]:
                if person[1] == "SICK" or person[1] == "RECOVERING":
                    exposerPresent = True
                    break
            # Change states of all the people based on if exposerPresent (SICK and RECOVERING anyway go to better state)
            for person in officeState[office]:
                nextOffice = person[2][day % len(person[2])]
                if person[1] == "HEALTHY":
                    if exposerPresent:
                        newPersonState = (person[0], "SICK", person[2])
                    else:
                        newPersonState = (person[0], person[1], person[2])
                elif person[1] == "RECOVERING":
                    newPersonState = (person[0], "HEALTHY", person[2])
                else:
                    newPersonState = (person[0], "RECOVERING", person[2])
                # We have the updates state, store it in a new map
                if nextOffice in newOfficeState:
                    newOfficeState[nextOffice].append(newPersonState)
                else:
                    newOfficeState[nextOffice] = []
                    newOfficeState[nextOffice].append(newPersonState)
        # Add the current state to print buffer and update officeState with the newOfficeState
        allOutput.append(printStates(newOfficeState))
        officeState = newOfficeState
    # Finally, check if everyone was not healthy by the last iteration
    if everyoneHealthy(officeState):
        allOutput.append(str(day))
    else:
        allOutput.append(str(365))
    return allOutput