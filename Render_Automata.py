from graphviz import Digraph

# DFA automata properties M =[Q,E,F,S,&]
# Q = states
# E = simbols
# F = Final State
# S = Inicial State
# & = Table

# Json&Images/NFA_Ɛ/NFAƐ.gv'


def render(path, Initicial_state: str, Final_state: list, Table_lists: list):
    # -------------------start rendering automata----------------
    f = Digraph(
        'Graph', filename='Json&Images/'+path)
    f.attr(rankdir='LR', size='8')
    # -----------------------Inicial state-------------------------------
    f.node('fake', style='invisible')
    f.edge('fake', Initicial_state, style='bold')
    if Initicial_state in Final_state:
        f.node(Initicial_state, root='true', shape='doublecircle')
    else:
        f.node(Initicial_state, root='true')
    # -----------------------final state-------------------------------
    f.attr('node', shape='doublecircle')
    for final_state in Final_state:
        f.node(final_state)
    # -----------------------Edge Linker-------------------------------
    print("-------------Automata_Linker---------------------")
    f.attr('node', shape='circle')
    for x in range(0, len(Table_lists)):
        if Table_lists[x] == ["", "", ""]:
            print(" ")
        else:
            f.edge(Table_lists[x][0], Table_lists[x]
                   [2], label=Table_lists[x][1])
    f.view()
