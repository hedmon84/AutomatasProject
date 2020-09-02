from Class_REGEX import Regex
from Class_NFA_Ɛ_NFA import NFAETONFA
from Class_NFA_DFA import NFATODFA
from Class_Test_DFA import Test_DFA
from Class_Draw_Automata import Draw
import os
import time

# a a*
# a a* | a b
# a a | b c
# a a | b c | a
# a (a | b )* c
# a ( a | b )* c | a ( a | b )+ a
# a a c | a b* c | a a | a b+ a
if __name__ == '__main__':

    # -------------------------Menu----------------------------------------
    exit = False

    while True != exit:
        # ----------------Awesome Automata-------------------
        print("\n\n\n\n")
        print("----------------Awesome Automata-------------------\n")
        print("       *----------Enter_Option-----------*")
        print("1.Draw your Automata")
        print("2.RE->NFA_Ɛ->NFA->DFA")
        print("3.RE->NFA_Ɛ")
        print("4.NAFA_Ɛ->NFA")
        print("5.NFA->DFA")
        print("6.Test_DFA")
        print("7.Exit/Quit")

        x = int(input())

        if x == 1:

            # DFA automata properties M =[Q,E,F,S,&]
            # Q = states
            # E = simbols
            # F = Final State
            # S = Inicial State
            states: input("Enter states: ")
            simbols: input("Enter Simbols: ")
            final_states: input("Enter Final_state: ")
            Inicial_state: input("Enter Initial_State: ")

            paint1 = Draw(states, simbols, final_states, Inicial_state)

        elif x == 2:
            # -------------------------regex to NFAE--------------------
            regex = input("Enter Regular Expresion: ")
            automata = Regex(regex)
            automata.regex_to_nfa_Ɛ()
            print("--Press Enter  key for NFA_Ɛ->NFA Conversion--")
            a = input()
            print(a)
            # -------------------------NFAE to NFA-------------------------------
            automata2 = NFAETONFA(
                "/media/hedmon/disk/Unitec/Q3_2020/Teoria_de_Computacion/project/project/Json&Images/NFA_Ɛ/NFAƐ.json")
            automata2.NFAE_TO_NFA()
            print("--Press Enter  key for NFA_DFA Conversion--")
            a = input()
            print(a)

            automata3 = NFATODFA(
                "/media/hedmon/disk/Unitec/Q3_2020/Teoria_de_Computacion/project/project/Json&Images/NFA/NFA.json")
            automata3.NFA_To_DFA()
            print("--Back to menu press Enter--")
            a = input()
            print(a)

            # -----------------------NFA to DFA------------------------------------

        elif x == 3:
            # -------------------------regex to NFAE--------------------
            regex = input("Enter Regular Expresion: ")
            automata4 = Regex(regex)
            automata4.regex_to_nfa_Ɛ()
            print("*--Back to menu press Enter--*")
            a = input()
            print(a)

        elif x == 4:
            # -------------------------NFAE to NFA-------------------------------
            json_name = input(
                "Enter the json FIle Nam from the test_automata_folder: ")
            automata5 = NFAETONFA(
                "/media/hedmon/disk/Unitec/Q3_2020/Teoria_de_Computacion/project/project/Json&Images/test_automatas/"+json_name+".json")
            automata5.NFAE_TO_NFA()
            print("--Press Enter  key for NFA_DFA Conversion--")
            a = input()
            print(a)
        elif x == 5:
            # -------------------------NFA to DFA-------------------------------
            json_name = input(
                "Enter the json FIle Name from the test_automata_folder: ")
            automata6 = NFATODFA(
                "/media/hedmon/disk/Unitec/Q3_2020/Teoria_de_Computacion/project/project/Json&Images/test_automatas/"+json_name+".json")
            automata6.NFA_To_DFA()
            print("--Press Enter  key for NFA_DFA Conversion--")
            a = input()
            print(a)
        elif x == 6:
            exits = 1
            json_name = input("Enter the json  path name and file name: ")
            test = Test_DFA()
            while(exits != "0"):

                test.readJSONEvaluate(json_name)
                print("--Press Enter to continue evaluating or 0 to exit-")
                exits = input()
        elif x == 7:
            print("Good Bye")
            exit = True
