import json
from Render_Automata import render


class Test_DFA:

    def readJSONEvaluate(self, automata):
        print('\n\nEVALUATE JSON')
        with open("/media/hedmon/disk/Unitec/Q3_2020/Teoria_de_Computacion/project/project/Json&Images/"+automata+".json") as file:
            data = json.load(file)
            # alphabet = data['alphabet']
            # states = data['states']
            initalState = data['initial_state']
            acceptingStates = data['accepting_states']
            transitions = data['transitions']

        # ------------------------ Render Automata-------------------------------------

        render("/media/hedmon/disk/Unitec/Q3_2020/Teoria_de_Computacion/project/project/Json&Images/" +
               automata+".json", initalState, acceptingStates, transitions)
        # print(data)

        # --------------------------------Enter expresion-------------------------------------
        expresion = input("Enter value to evaluate: ")

        inputData = expresion
        listInput = list(inputData)

        result = self.evaluateSymbol(
            listInput, transitions, acceptingStates, initalState)

        if(result == 'fail'):
            print('\nThe expresion is not part of the automata languaje')
        else:
            print('\nThe expresion is part of the automata languaje')

    def evaluateSymbol(self, listInput, transitions, acceptingStates, initalState):
        # counter = 0
        countList = 0
        currentN = initalState
        sz = len(listInput)

        while(1):
            currentS = listInput[countList]
            print('current->', currentN, '-', currentS)

            currentN = self.evaluationHelperTrans(
                currentN, currentS, transitions)

            if(currentN == 'fail'):
                return 'fail'

            if(countList != sz):
                countList = countList + 1
                if(countList == sz):
                    for xx in acceptingStates:
                        concat = ''
                        for yy in xx:
                            concat = concat + yy
                            print('-->', concat, currentN)
                        if(concat == currentN):

                            # print('Pass')
                            return 'pass'
                    return 'fail'
                currentS = listInput[countList]

    def evaluationHelperTrans(self, currentNode, exp, transitions):
        for x in transitions:
            orig = x[0]
            symb = x[1]
            dest = x[2]
            if(currentNode == orig):
                if(symb == exp):
                    print('enter', orig, symb, dest)
                    return dest

        return 'fail'


# p1 = Test_DFA()
# p1.readJSONEvaluate(
#     "aaabbaa", "DFA/DFA.json")

# p1 = Test_DFA()
# p1.readJSONEvaluate("DFA/DFA")
