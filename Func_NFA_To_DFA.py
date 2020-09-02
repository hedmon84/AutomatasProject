from tabulate import tabulate
import json
from Render_Automata import render
from Write_json import write_jason
import re

# nfa = {
#     'alphabet': ['0', '1'],
#     'states': ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8'],
#     'initial_state': 'q0',
#     'accepting_states': ['q8'],
#     'transitions': [
#         ['q0', '0', 'q0'],
#         ['q0', '0', 'q1'],
#         ['q0', '0', 'q2'],
#         ['q3', '0', 'q5'],
#         ['q7', '0', 'q7'],
#         ['q7', '0', 'q8'],
#         ['q0', '1', 'q1'],
#         ['q0', '1', 'q3'],
#         ['q0', '1', 'q4'],
#         ['q1', '1', 'q3'],
#         ['q2', '1', 'q4'],
#         ['q4', '1', 'q6'],
#         ['q4', '1', 'q8'],
#         ['q5', '1', 'q7'],
#         ['q5', '1', 'q8'],
#         ['q7', '1', 'q7'],
#         ['q7', '1', 'q8']
#     ]
# }


# nfa = {
#     'alphabet': ['a', 'b'],
#     'states': ['s0', 's1', 's2', 's3', 's4', 's5', 's6', 's7'],
#     'initial_state': 's0',
#     'accepting_states': ['s7'],
#     'transitions': [
#         ['s0', 'a', 's2'],
#         ['s1', 'a', 's2'],
#         ['s2', 'a', 's2'],
#         ['s2', 'a', 's3'],
#         ['s2', 'a', 's7'],
#         ['s5', 'a', 's5'],
#         ['s0', 'b', 's5'],
#         ['s2', 'b', 's2'],
#         ['s4', 'b', 's5'],
#         ['s5', 'b', 's5'],
#         ['s5', 'b', 's6'],
#         ['s5', 'b', 's7']
#     ]
# }


# nfa = {
#     'alphabet': ['a', 'b'],
#     'states': ['A', "B", "C"],
#     'initial_state': 'A',
#     'accepting_states': ['C'],
#     'transitions': [
#         ['A', 'a', 'A'],
#         ['A', 'a', 'B'],
#         ['A', 'b', 'C'],
#         ['B', 'a', 'A'],
#         ['B', 'b', 'B'],
#         ['C', 'b', 'A'],
#         ['C', 'b', 'B'],
#     ]
# }


# nfa = {
#     'alphabet': ['a', 'b'],
#     'states': ['q0', 'q1', 'q2', 'q3', 'q4', 'q5'],
#     'initial_state': 'q0',
#     'accepting_states': ['q2'],
#     'transitions': [
#         ['q0', 'a', 'q3'],
#         ['q0', 'a', 'q1'],
#         ['q0', 'a', 'q4'],
#         ['q0', 'a', 'q5'],
#         ['q1', 'a', 'q4'],
#         ['q1', 'a', 'q5'],
#         ['q3', 'a', 'q4'],
#         ['q3', 'a', 'q5'],
#         ['q0', 'b', 'q2'],
#         ['q1', 'b', 'q2'],
#         ['q3', 'b', 'q4'],
#         ['q3', 'b', 'q5'],
#         ['q3', 'b', 'q2']
#     ]
# }


def nfa_to_dfa(file_name):

    with open(file_name) as file:
        data = json.load(file)
        alphabet = data['alphabet']
        states = data['states']
        initalState = data['initial_state']
        acceptingStates = data['accepting_states']
        transitions = data['transitions']

    nfa_table = []
    temp_list = []
    # listspos = [a,b,Ɛ]
    # ----------------- create default list--------------
    print("\n")
    print("Default list ")
    for x in range(len(states)):
        temp_list.append(states[x])
        for i in range(len(alphabet)):
            temp_list.append("0")
        nfa_table.append(temp_list)
        temp_list = []
    print(nfa_table)
    # ------------ set table transition------------------------------
    for x in range(len(transitions)):
        # print(transitions[x][0])
        i = 0
        pos = states.index(transitions[x][0])
        # print(pos)
        for a in range(1, len(alphabet)+1):

            if transitions[x][1] == alphabet[i]:
                if nfa_table[pos][a] == "0":
                    nfa_table[pos][a] = [transitions[x][2]]
                    i += 1
                else:
                    nfa_table[pos][a].append(transitions[x][2])
                    i += 1
            else:
                i += 1
    print("\n")
    alphabet.insert(0, 'Q')
    print("Rendering Transition table ")
    print(tabulate(nfa_table,
                   headers=alphabet, tablefmt='grid'))
    print("\n")

    # ------------ table_Nfa_to_Dfa version2---------------------

    dfa_table = []
    dfa_table.append(nfa_table[states.index(initalState)])
    new_states = [[initalState]]
    Nstates_pos = 1
    print(dfa_table)
    print("\n")
    end_loop = False
    is_newstate = False
    indexs = 0
    pos = 0
    count = 0
    states_pos = 0

    # exit()
    while end_loop != True:
        # ---------------- Searching new states---------------------------
        simbols_pos = 1
        is_newstate = False
        print(dfa_table)
        count = 0

        for i in range(1, len(dfa_table[indexs])):
            try:
                if new_states.index(dfa_table[pos][simbols_pos]):
                    print("is on list")
                    simbols_pos += 1
            except:
                try:
                    if dfa_table[pos][simbols_pos] == "0":
                        print("0 catch")
                        simbols_pos += 1
                    else:
                        print("is not on list")
                        new_states.append(dfa_table[pos][simbols_pos])
                        simbols_pos += 1
                        is_newstate = True
                        count += 1
                        print(new_states)

                except:
                    end_loop = True

         # ----------------------adding new states-------------------------------
        temp_list = []
        if is_newstate == True:

            for x in range(0, count):
                dfa_table.append([new_states[Nstates_pos]])
                states_pos += 1

                print(dfa_table)
                # exit()
                for i in range(1, len(alphabet)):
                    print("A")
                    for e in range(0, len(new_states[Nstates_pos])):
                        tempos = states.index(new_states[Nstates_pos][e])
                        # ----------------------Delete 0-------------------------------
                        unwanted_val = "0"
                        temp_list.extend(nfa_table[tempos][i])
                        temp_list = [
                            ele for ele in temp_list if ele not in unwanted_val]

                    # -------------delete duplications--------------------------
                    # remove duplicate numbers
                    temp_list = list(dict.fromkeys(temp_list))
                    # -------------------------------check table-------------------------------
                    print("\n")
                    if len(temp_list) == 0:
                        temp_list = "0"
                    print(temp_list)
                    dfa_table[states_pos].append(temp_list)
                    print(dfa_table)
                    print(tabulate(dfa_table,
                                   headers=alphabet, tablefmt='grid'))
                    temp_list = []
                Nstates_pos += 1
            pos += 1

        else:
            pos += 1
    # ------------------------print dfa_list----------------------
    print("\n")
    print("\n")
    print("\n")
    print("------------DFA_Table-------------------")
    print(tabulate(dfa_table,
                   headers=alphabet, tablefmt='grid'))

    # ----------------------Generate new States-----------------------------

    sates_new = []
    new_final_states = []

    for x in range(len(dfa_table)):
        # -------------------------new_final_states-------------
        try:

            for i in range(len(acceptingStates)):
                if dfa_table[x][0].index(acceptingStates[i]):
                    listToStr = ''.join(map(str, dfa_table[x][i]))
                    new_final_states.append(listToStr)

        except:
            pass

        # ------------------------new states----------
        listToStr = ''.join(map(str, dfa_table[x][0]))
        sates_new.append([listToStr])
        # print(dfa_table[x][0])

    # ----------------------------------Generate transitions---------------------
    translist = []
    cant = len(alphabet)-1
    poss = 0
    for x in range(len(dfa_table)):

        for i in range(cant):
            if dfa_table[x][i+1] == "0":
                print('')
            else:
                listToStr2 = ''.join(map(str, dfa_table[x][0]))
                translist.append([listToStr2])
                translist[poss].append(alphabet[i+1])
                listToStr3 = ''.join(map(str, dfa_table[x][i+1]))
                translist[poss].append(listToStr3)
                poss += 1

    # -------------------------------------render Dfa----------------------------------------
    render("DFA/DFA.gv", initalState, new_final_states, translist)
    # --------------------------------------creating json------------------------------------------
    alphabet.remove("Q")
    write_jason("DFA/DFA.json", alphabet, sates_new,
                initalState, new_final_states, translist)
    # print(dfa_table)
    exit()


# nfa_to_dfa("/media/hedmon/disk/Unitec/Q3_2020/Teoria_de_Computacion/project/project/Json&Images/test_/NFA4")
