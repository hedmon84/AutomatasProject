from Render_Automata import render
from Write_json import write_jason
import re
# ------------test------------
# a pass
# aa pass
# a | b cpass
# a | b c | d pass
# a a | b | a pass
# a a a | b a a | c d d pass
# a | b | a pass
# a a | b pass
# a* pass
# a* b* c* pass
# a b* pass
# a* b pass
# a* | b* b* | c* pass
# b* a | a c* a | b* a
# a | b* pass
# a* b | a pass
# a a | b b b b | a a a a | b b b b pass
# a b* | a c pass
# a b+ pass
# a b | b+ c pass
# a+ | b+ b+ | c* pass
# ( a )* pass
# ( a a )* pass
# ( a | b )* pass
# ( a a | b b | c c )* pass
# "( a | b )* c" pass
# "a ( a | b )*" pass
# "c ( a | b )* d" pass
# a ( a | b )* c | a pass
# # (a | b )* c | a ( a | b )* c pass
# a(a|b) pass
# a(a|b)* pass
# a(a|b)+
# a(a|b) pass
# a ( a | b )* c | a ( a | b )* c | d ( a | b )* h
# a(a|b*) falta
# a(a|b+)* falta
# a(a|b*)+ falta
# a(a|b) falta


def re_to_nfa_Ɛ(input: str) -> str:

    initial_state = ""
    final_states = []
    multiple_final_states = []
    count_finals = 0
    previews_state = ""
    state = "q"
    position = 0
    count = 0
    is_first = False
    open_par = False
    next_inpar = False
    new_or_final = False
    count_states = 0
    is_last_concat = False
    is_or = False
    comesfrom_par = False
    is_final = True
    nfa_Ɛ_table = []

    # ----------------------------------Generating alpha------------------------
    res1 = " ".join(re.split("[^a-zA-Z]*", input))
    clean_string = " "

    alphabets = list(res1)
    alphabets = [
        ele for ele in alphabets if ele not in clean_string]

    res = []
    [res.append(x) for x in alphabets if x not in res]

    # ----------------------------------Split the input--------------------------

    regex = input.split(" ")
    print(regex)

    for x in range(0, len(regex)):

        if "(" in regex[x]:
            open_par = True

        # --------------------------------- (a)* zone ----------------------------

        if open_par == True:
            print("enter")

            if x == 0 or next_inpar == True:

                if x == 0:
                    state += str(count_states)
                    nfa_Ɛ_table.append([state])
                    initial_state = state
                    state = "q"
                    count_states += 1
                    is_first = True

                    # -------------adding epsilon --------------
                    nfa_Ɛ_table[position].append("Ɛ")

                    # --------------adding last state---
                    state += str(count_states)
                    nfa_Ɛ_table[position].append(state)
                    previews_state = state
                    Epsilon_Initial = state
                    state = "q"
                    count_states += 1
                # adding initial to final epsilon
                if next_inpar == True:
                    nfa_Ɛ_table.append([previews_state])
                    Epsilon_Initial = previews_state
                    next_inpar = False
                    is_first = True
                else:
                    nfa_Ɛ_table.append([Epsilon_Initial])

                position += 1

                val = re.findall(r'\d+', previews_state)
                temp2 = int(val[0])
                nfa_Ɛ_table[position].append("Ɛ")
                state += str(temp2+3)
                nfa_Ɛ_table[position].append(state)
                Epsilon_Final = state
                state = "q"
                # -------------------------------copy list alpha--------------------
                temp_list = nfa_Ɛ_table[position]

            if is_or == True:
                previews_state = Epsilon_Initial
                count += 1
                is_first = True

             # adding 0------->a------------>0
            if regex[x].isalpha() and len(regex[x]) == 1:

                if is_first == True:
                    # adding 0------->a------------>0
                    nfa_Ɛ_table.append([previews_state])
                    position += 1
                    # -------------adding head epsilon --------------
                    nfa_Ɛ_table[position].append("Ɛ")
                    # --------------adding last state---
                    state += str(count_states)
                    nfa_Ɛ_table[position].append(state)
                    previews_state = state
                    state = "q"
                    count_states += 1
                    is_first = False

                # ------adding alpha-----------------
                nfa_Ɛ_table.append([previews_state])
                position += 1
                nfa_Ɛ_table[position].append(regex[x])
                # --------------adding last state---
                state += str(count_states)
                nfa_Ɛ_table[position].append(state)
                previews_state = state
                state = "q"
                count_states += 1
                # --------------- tail epsilon------------------
                nfa_Ɛ_table.append([previews_state])
                position += 1
                nfa_Ɛ_table[position].append("Ɛ")
                # --------------adding last state of epsilon---
                if is_final == False and regex[x+1] == ")*" or regex[x+1] == ")+" or regex[x+1] == "|" and count >= 1:
                    nfa_Ɛ_table[position].append(Epsilon_Final)
                    count_states += 1
                    is_or = False
                else:
                    state += str(count_states)
                    nfa_Ɛ_table[position].append(state)
                    previews_state = state
                    if is_final == True:
                        Epsilon_Final = state
                    state = "q"
                    count_states += 1
                is_or = False

            if ")*" in regex[x] or ")+" in regex[x]:

                # ------------------epsilon final to initial-----------
                nfa_Ɛ_table.append([Epsilon_Final])
                position += 1
                nfa_Ɛ_table[position].append("Ɛ")
                nfa_Ɛ_table[position].append(Epsilon_Initial)
               # -----------final estate closing parentesis----------
                nfa_Ɛ_table.append([Epsilon_Final])
                position += 1
                nfa_Ɛ_table[position].append("Ɛ")
                state += str(count_states)
                nfa_Ɛ_table[position].append(state)
                previews_state = state
                if x+1 == len(regex):
                    final_states = state
                state = "q"
                count_states += 1

                # ------------------reset values---------------
                count = 0

                # --------------------calibraring Intial epsilon ------------------
                if ")+" in regex[x]:

                    nfa_Ɛ_table[nfa_Ɛ_table.index(
                        temp_list)] = ["", "", ""]
                    state = "q"

                else:
                    nfa_Ɛ_table[nfa_Ɛ_table.index(
                        temp_list)][2] = Epsilon_Final
                    state = "q"

                # print(nfa_Ɛ_table)
                # exit()

                # ------------------------if is a--------------------
        if regex[x].isalpha() and len(regex[x]) == 1 and open_par == False:
            # if is the first state
            if x == 0 or is_or == True:

                if x == 0:
                    state += str(count_states)
                    nfa_Ɛ_table.append([state])
                    initial_state = state
                    state = "q"
                    count_states += 1
                if is_or == True:
                    nfa_Ɛ_table.append([initial_state])
                    count += 1
                    position += 1

                # -------------adding epsilon --------------
                nfa_Ɛ_table[position].append("Ɛ")

                # --------------adding last state---
                state += str(count_states)
                nfa_Ɛ_table[position].append(state)
                previews_state = state
                state = "q"
                count_states += 1

            # --------adding previews state node-------------
            nfa_Ɛ_table.append([previews_state])
            position += 1

            # ----adding alphabet transition-----------
            nfa_Ɛ_table[position].append(regex[x])

            try:
                if regex[x+1] == "|" and count > 0:
                    is_last_concat = True

            except:
                pass

            # ----adding  next state----------
            state += str(count_states)
            nfa_Ɛ_table[position].append(state)
            previews_state = state
            state = "q"
            count_states += 1

            # -----------------final epsilon transition ------------
            nfa_Ɛ_table.append([previews_state])
            position += 1
            nfa_Ɛ_table[position].append("Ɛ")
            if is_or == True and x+1 == len(regex) and new_or_final == False:
                nfa_Ɛ_table[position].append(final_states)
            elif x+1 == len(regex) and is_final == False and comesfrom_par == False or is_last_concat == True:
                is_last_concat = False
                nfa_Ɛ_table[position].append(final_states)
            else:
                state += str(count_states)
                nfa_Ɛ_table[position].append(state)
                previews_state = state
                if is_final == True and x+1 == len(regex) or comesfrom_par == True and x+1 == len(regex) or regex[x+1] == "|":
                    final_states = state
                    count_finals += 1
                    multiple_final_states.append(state)
                # elif new_or_final == True:
                #     final_states.append(state)
                state = "q"
                count_states += 1
                try:
                    if regex[x+1] == "(":
                        next_inpar = True
                except:
                    pass

            is_or = False

        # -----------------------zone a*---------------------------------
        if "*" in regex[x] and len(regex[x]) == 2 and open_par == False or "+" in regex[x] and len(regex[x]) == 2 and open_par == False:

            if x == 0 or is_or == True:
                # ------adding  0-->e--0- ---------

                if x == 0:
                    state += str(count_states)
                    nfa_Ɛ_table.append([state])
                    initial_state = state
                    state = "q"
                    count_states += 1
                if is_or == True:
                    nfa_Ɛ_table.append([initial_state])
                    count += 1
                    position += 1

                # -------------adding epsilon --------------
                nfa_Ɛ_table[position].append("Ɛ")
                # --------------adding last state----------
                state += str(count_states)
                nfa_Ɛ_table[position].append(state)
                previews_state = state
                Epsilon_Initial = state
                state = "q"
                count_states += 1

            # -----------------------adding Initial->e--final--------------

            if "*" in regex[x]:
                nfa_Ɛ_table.append([previews_state])
                if x > 0:
                    Epsilon_Initial = previews_state
                position += 1
                nfa_Ɛ_table[position].append("Ɛ")
                temp = count_states
                state += str(temp + 2)
                nfa_Ɛ_table[position].append(state)
                state = "q"
            else:
                Epsilon_Initial = previews_state

            # -------------adding 0-->e--0--------------
            nfa_Ɛ_table.append([previews_state])
            position += 1
            nfa_Ɛ_table[position].append("Ɛ")
            state += str(count_states)
            nfa_Ɛ_table[position].append(state)
            previews_state = state
            state = "q"
            count_states += 1
            # -------------adding 0-->alphabet--0--------------
            nfa_Ɛ_table.append([previews_state])
            position += 1
            nfa_Ɛ_table[position].append(regex[x][0])

            try:
                if regex[x+1] == "|" and count > 0:
                    is_last_concat = True

            except:
                pass

            state += str(count_states)
            nfa_Ɛ_table[position].append(state)
            previews_state = state
            state = "q"
            count_states += 1

            # -----------------------adding 0->e--0--------------
            nfa_Ɛ_table.append([previews_state])
            position += 1
            nfa_Ɛ_table[position].append("Ɛ")
            state += str(count_states)
            nfa_Ɛ_table[position].append(state)
            Epsilon_Final = state
            previews_state = state
            state = "q"
            count_states += 1
            # -----------------------adding 0->e--0--------------
            nfa_Ɛ_table.append([previews_state])
            position += 1
            nfa_Ɛ_table[position].append("Ɛ")
            if is_or == True and x+1 == len(regex):
                nfa_Ɛ_table[position].append(final_states)
            elif x+1 == len(regex) and is_final == False or is_last_concat == True:
                is_last_concat = False
                nfa_Ɛ_table[position].append(final_states)
            else:
                state += str(count_states)
                nfa_Ɛ_table[position].append(state)
                previews_state = state
                if is_final == True:
                    final_states = state
                state = "q"
                count_states += 1
            is_or = False
            # -----------------------adding Final--->e--Intitial--------------
            nfa_Ɛ_table.append([Epsilon_Final])
            position += 1
            nfa_Ɛ_table[position].append("Ɛ")
            nfa_Ɛ_table[position].append(Epsilon_Initial)

            # --------------------- is | ------------------------------------
        if regex[x] == "|":
            is_final = False
            is_or = True

        # ---------------closing parentesis--------------------
        if ")*" in regex[x] or ")+" in regex[x]:
            open_par = False
            comesfrom_par = True
            new_or_final = True

    if count_finals > 1:
        final_states = []
        final_states = multiple_final_states
    else:
        value = final_states
        final_states = []
        final_states.append(value)

    # -------------------------getting states---------------------
    lists2 = []
    for x in range(0, len(nfa_Ɛ_table)):

        lists2.append(nfa_Ɛ_table[x][0])
        lists2.append(nfa_Ɛ_table[x][2])

    res2 = []
    [res2.append(x) for x in lists2 if x not in res2]

    print(nfa_Ɛ_table)
    print("inital state " + initial_state)
    print("final state")
    print(final_states)
    print("---------Loading Automata--------")
    render("NFA_Ɛ/NFAƐ.gv", initial_state, final_states, nfa_Ɛ_table)

    # res alphabet
    # res2 states
    res.append("Ɛ")
    # ----------creating json--------------------
    write_jason("NFA_Ɛ/NFAƐ.json", res, res2,
                initial_state, final_states, nfa_Ɛ_table)


# re_to_nfa_Ɛ("( a | b )* c | a ( a | b )* c")


# (a | b )* c | a ( a | b )+ c pass

# a+ ( a+ | b* )* c | a ( a+ | b* )* c*
