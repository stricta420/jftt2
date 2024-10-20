class DFA:
    def __init__(self, text, patern):
        self.text = text
        self.patern = patern
        self.alfabet = list(set(text))
        self.transition_table = self.crate_transition_table(patern, self.alfabet)

    def crate_transition_table(self, patern, alfabet):
        states = {}
        for i in range(len(patern) + 1):
            states[patern[:i]] = {}
        for state in states:
            slownik = states[state]
            for litera in alfabet:
                new_key = state + litera
                founded = False
                for i in range(len(new_key)):
                    if new_key[i:] in states:
                        slownik[new_key] = new_key[i:]
                        founded = True
                        break
                if not founded:
                    slownik[new_key] = ""

        return states

    def print_wlasciwosci(self):
        print("alfabet:")
        print(self.alfabet)
        print("\nstates:")
        for state in self.transition_table:
            print(state, end=", ")
        print()
        print("przejscia dla kazdego statu")
        for state in self.transition_table:
            print(f"{state}, przejscia: ")
            for trans in self.transition_table[state]:
                print(f"new char: {trans[-1]} -> {self.transition_table[state][trans]}")
    def check_whole(self):
        tekst = self.text
        patern = self.patern
        transiton_table = self.transition_table
        courrent_state = ""
        accept_state = patern
        indeks_list = []
        for i in range(len(tekst)):
            next_step = courrent_state + tekst[i]
            courrent_state = transiton_table[courrent_state][next_step]
            if courrent_state == accept_state:
                indeks_list.append(i - len(patern) + 1)
        return indeks_list
