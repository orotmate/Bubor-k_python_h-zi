import random
from typing import List


szamok: List[int] = []
for i in range(10):
    szamok.append(random.randint(10, 99))

for i in range(len(szamok)-1):
    for j in range(i+1, len(szamok)):
        if szamok[i] > szamok[j]:
            szamok[i], szamok[j] = szamok[j], szamok[i]
print(szamok)