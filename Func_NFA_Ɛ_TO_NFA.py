from tabulate import tabulate
import json
from Render_Automata import render
from Write_json import write_jason
import re


# listCƐ = []
# listcƐA = []
# print('Transitions')
# print(transitions)
# print('\nalphabet')
# print(alphabet)


def nfa_Ɛ_to_nfa(file_name: str):

    with open(file_name) as file:
        data = json.load(file)
        alphabet = data['alphabet']
        states = data['states']
        initalState = data['initial_state']
        acceptingStates = data['accepting_states']
        transitions = data['transitions']

    map_list = []
    lists2 = []
    # listspos = [a,b,Ɛ]
    print("\n")
    print("Default list ")
    for x in range(len(states)):
        lists2.append(states[x])
        for i in range(len(alphabet)):
            lists2.append("0")
        map_list.append(lists2)
        lists2 = []
    print(map_list)

    # listspos = [a,b,Ɛ]
    # lists = [['q0', '0', '0', '0'], [
    #     'q1', '0', '0', '0'], ['q2', '0', '0', '0'], ['q3', '0', '0', '0'], ['q4', '0', '0', '0']]
    # Print the default list

    print('\nTEST Transition')
    for x in range(len(transitions)):
        print(transitions[x])

    print('\nTransitions in order list')

    # list table 1
    # for x in range(len(transitions)):
    #     # print(transitions[x][0])
    #     i = 0
    #     pos = states.index(transitions[x][0])
    #     # print(pos)
    #     for a in range(1, len(alphabet)+1):

    #         if transitions[x][1] == alphabet[i]:
    #             map_list[pos][a] = transitions[x][2]
    #             i += 1
    #         else:
    #             i += 1
    # list table version 2
    for x in range(len(transitions)):
        # print(transitions[x][0])
        i = 0
        pos = states.index(transitions[x][0])
        # print(pos)
        for a in range(1, len(alphabet)+1):

            if transitions[x][1] == alphabet[i]:
                if map_list[pos][a] == "0":
                    map_list[pos][a] = [transitions[x][2]]
                    i += 1
                else:
                    map_list[pos][a].append(transitions[x][2])
                    i += 1
            else:
                i += 1
    # if transitions[x][1] == "a":
    #     lists[pos][1] = transitions[x][2]
    # if transitions[x][1] == "b":
    #     lists[pos][2] = transitions[x][2]
    # if transitions[x][1] == "Ɛ":
    #     lists[pos][3] = transitions[x][2]

    print(map_list)
    print("\n")
    alphabet.insert(0, 'Q')
    print("Rendering Transition table ")
    print(tabulate(map_list,
                   headers=alphabet, tablefmt='grid'))

    # ------------------- table header 2 CƐ(q)----------------------
    h_table3 = ['Q', 'CƐ(q)']
    i = 1
    for a in range(2, len(alphabet)):
        h_table3.append('d(CƐ(q),'+alphabet[i]+')')
        h_table3.append('CƐ(d(CƐ(q),'+alphabet[i]+'))')
        i += 1

    # -----------------------------C_Ɛ_map-------------------------

    print("\n")
    print("---C_Ɛ_table--")
    # print(map_list[0][3])
    print("\n")
    map_list2 = []
    print("Default list test")
    for x in range(len(states)):
        lists2.append(states[x])
        for i in range(1, len(h_table3)):
            lists2.append("0")
        map_list2.append(lists2)
        lists2 = []
    print(map_list2)
    print(tabulate(map_list2,
                   headers=h_table3, tablefmt='grid'))
    print("\n")
    # ------------------------ CƐ(q) -----------------------
    # print(alphabet.index("Ɛ"))  # epsilon position in list
    # print(map_list[0][3])
    Ɛ_pos = alphabet.index("Ɛ")

    for x in range(len(states)):
        # print(map_list[x][Ɛ_pos])
        # print(map_list[x][Ɛ_pos])
        map_list2[x][1] = [map_list[x][0]]

        if map_list[x][Ɛ_pos] == "0":
            print(" ")
        else:
            map_list2[x][1].extend(map_list[x][Ɛ_pos])  # add list together

        # print(map_list2[x][1].count(map_list[x][0]))
        # clear mutability
        cleanM = map_list2[x][1].count(map_list[x][0])
        if cleanM >= 2:
            map_list2[x][1].pop(0)

        # map_list2[x][1].pop(0)

    print(tabulate(map_list2,
                   headers=h_table3, tablefmt='grid'))

    # ------------------------ d(CƐ(q),a)  -----------------------
    print("\n")
    cicle = round(int((len(h_table3) / 2)))
    # print(cicle)
    g = 1  # count cea,ceb..
    for x in range(1, cicle):
        # print(x)
        # print("0")
        g += 1
        for i in range(len(states)):
            # print(len(map_list2[i][1]))
            # exit()
            is_zero = False
            for e in range(len(map_list2[i][1])):
                # print(map_list2[i][1][e])
                state_pos = states.index(map_list2[i][1][e])
                if map_list[state_pos][x] == '0':
                    print("")
                    is_zero = True
                else:
                    # print(map_list[state_pos][x])
                    # print(map_list2[i][g])
                    if e == 0 or is_zero == True:
                        map_list2[i][g] = []
                    map_list2[i][g].extend(map_list[state_pos][x])
                    print(map_list2[i][g])
                    is_zero = False  # test new change
                    print(tabulate(map_list2,
                                   headers=h_table3, tablefmt='grid'))

    # ------------------------ CƐ(d(CƐ(q),a)) -----------------------
        print("\n")
        print("\n")
        print("\n")
        g += 1
        for i in range(len(states)):
            is_zero = False
            if map_list2[i][g-1] == "0":
                print("")
            else:
                for e in range(len(map_list2[i][g-1])):
                    state_pos = states.index(map_list2[i][g-1][e])
                    if e == 0:
                        map_list2[i][g] = []
                    map_list2[i][g].extend(map_list2[state_pos][1])

    # ---------------------------Print NFA_TAble---------------------------
        print("\n")
        print("------------NFA_Table----------------")
        print(tabulate(map_list2,
                       headers=h_table3, tablefmt='grid'))

    # ---------------------------------create transitions--------------------------------------
    translist = []
    pos = 0
    move = 3
    cant = len(alphabet)-2
    for x in range(cant):

        if x > 0:
            move += 2

        for i in range(len(states)):

            for e in range(len(map_list2[i][move])):
                if map_list2[i][move] == "0":
                    print('')
                else:
                    translist.append([map_list2[i][0]])
                    translist[pos].append(alphabet[x+1])
                    translist[pos].append(map_list2[i][move][e])
                    pos += 1

        # print(map_list2)

    # ------------------------------------Render zone-------------------------------------------
    render("NFA/NFA.gv", initalState, acceptingStates, translist)

    # ---------------------------export DFA_Json-------------------------------------------------
    alphabet.remove("Q")
    alphabet.remove("Ɛ")
    print(alphabet)
    write_jason("NFA/NFA.json", alphabet, states,
                initalState, acceptingStates, translist)


# nfa_Ɛ_to_nfa(
#     "/media/hedmon/disk/Unitec/Q3_2020/Teoria_de_Computacion/project/project/Json&Images/test_automatas/NFA_E4.json")
