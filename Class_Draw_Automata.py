from graphviz import Digraph


class Draw:

    # DFA automata properties M =[Q,E,F,S,&]
    # Q = states
    # E = simbols
    # F = Final State
    # S = Inicial State
    # & = Table

    def __init__(self, Q, E, F, S):
        self.Q = Q.split(",")

        self.E = E.split(",")
        self.F = F.split(",")
        self.S = S

    def stat_list(self):
        print(self.Q)

    def dfa_export(self):

        # -------------------Automata Parameters---------------------
        print("--Automata bnf Formula--\n  M=[Q, E, F, S]\n")
        print("--M Current States--\n", self.Q)
        print("--E Current Simbols--\n", self.E)
        print("--F Final States--\n", self.F)
        print("--S Inicial States--\n", "  " + self.S)
        print("Link your automata current states, Example = q1->q2")

        # -------------------start rendering automata----------------
        f = Digraph('Graph', filename='DFA/XDFA.gv')
        f.attr(rankdir='LR', size='8,5')

        # -----------------------Inicial state-------------------------------
        f.node('fake', style='invisible')
        f.edge('fake', self.S, style='bold')
        if self.S in self.F:
            f.node(self.S, root='true', shape='doublecircle')
        else:
            f.node(self.S, root='true')

        # -----------------------final state-------------------------------
        f.attr('node', shape='doublecircle')
        for final_state in self.F:
            f.node(final_state)

        # -----------------------Edge Linker-------------------------------
        print("-------------Automata_Linker---------------------")

        exits = "1"
        f.attr('node', shape='circle')
        while(exits != "0"):
            # -------------------Automata Linker input---------------------
            input_states = input("Link : ")
            inputs = input_states.split("->")
            input_label = input("Enter edge value : ")
            check = all(item in self.Q for item in inputs)
            if check is True and input_label in self.E:
                f.edge(inputs[0], inputs[1], label=input_label)
                exits = input(
                    "submit press 0, continue linking press any key:  ")
            else:
                print("Incorrect Q(\"state\") or E(\"Simbols\")")
                exits = input(
                    "exit press 0, continue linking press any key:  ")

        f.view()

    # final state

    # f.attr('node', shape='circle')
    # for states in self.Q:
    #     f.node(states)

    # f.view()
