# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus
from tulo import tulo

logger("aloitetaan")

x = int(input("luku 1: "))
y = int(input("luku 2: "))
print(f"Lukujen {x} ja {y} summa on {summa(x, y)}")  # muutos bugikorjaus-branchissa
print(f"Lukujen {x} ja {y} erotus on {erotus(x, y)}")  # muutos bugikorjaus-branchissa
print(f"{x} * {y} = {tulo(x, y)}")

logger("lopetetaan ohjelma")
print("goodbye!") # lisäys bugikorjaus-branchissa
