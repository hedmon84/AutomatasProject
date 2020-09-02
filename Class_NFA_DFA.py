from Func_NFA_To_DFA import nfa_to_dfa


class NFATODFA:

    def __init__(self, path):
        self.path = path

    def NFA_To_DFA(self):
        nfa_to_dfa(self.path)
