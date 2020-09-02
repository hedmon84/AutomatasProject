from Func_NFA_Ɛ_TO_NFA import nfa_Ɛ_to_nfa


class NFAETONFA:

    def __init__(self, path):
        self.path = path

    def NFAE_TO_NFA(self):
        nfa_Ɛ_to_nfa(self.path)
