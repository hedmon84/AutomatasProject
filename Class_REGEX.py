from Func_RE_To_NFA_Ɛ import re_to_nfa_Ɛ
import re


class Regex:

    def __init__(self, regex):

        self.regex = regex

    def regex_to_nfa_Ɛ(self):
        re_to_nfa_Ɛ(self.regex)
