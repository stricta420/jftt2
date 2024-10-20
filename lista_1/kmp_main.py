import sys
import KMP
if len(sys.argv) != 3:
    print("Musisz podać 2 argumenty")
    sys.exit()

patern = sys.argv[1]
file = sys.argv[2]

print(f"Uruchomiles progrma dla paternu: {patern}\nOraz pliku: {file}")

plik = ""
try:
    with open(file, "r") as f:
        plik = f.read()
except FileNotFoundError:
    print("Podany plik nie istnieje!")
    sys.exit()

kmp = KMP.KMP(plik, patern)
print(kmp.run())
