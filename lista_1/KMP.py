class KMP:
    def __init__(self, text, patern):
        self.text = text
        self.patern = patern
        self.lps = self.makeLPS(patern)

    def set_text(self, text):
        self.text = text

    def set_patern(self, patern):
        self.patern = patern
        self.lps = self.makeLPS(patern)

    def run(self):
        if self.patern == "" or self.text == "":
            return []  # Jeśli wzorzec lub tekst są puste, zwracamy pustą listę.
        if len(self.patern) > len(self.text):
            return []  # Jeśli wzorzec jest dłuższy niż tekst, nie ma dopasowania.
        return self.find_matching_indekses(self.patern, self.text, self.lps)
    def makeLPS(self, needle):
        if needle == "":
            return 0 #corner case, needle o dł 0 nie ma sensu
        lps = [0] * len(needle)

        prevLPS = 0
        i = 1 #zaczynamy od 1 bo na 1 miejscu zawsze jest 0
        while i < len(needle):
            if needle[i] == needle[prevLPS]: #jesli te elementy sa takie same to znaczy że mamy dłuższy prefix/sufix
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            else:
                if prevLPS == 0: #jesli nie mamy żadnego prefixu/sufixu i znaki nie sa rowne to dalej nie mamy zadnego prefixu/sufixu
                    lps[i] = 0
                    i += 1
                else:
                    prevLPS = lps[prevLPS - 1] #jesli znaki nie sa sobie rowne ale mamy jakis prefix/sufix to "cofamy" sie o 1
        return lps

    def find_matching_indekses(self, needle, haystack, lps):
        # print(needle)
        # print(haystack)
        # print(lps)
        i = 0 #indeks w haystack
        j = 0 #indeks w needle
        ans = []
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i+= 1
                j+= 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]
            if j == len(needle):
                ans.append(i - len(needle))
                j = lps[j-1]
        return ans