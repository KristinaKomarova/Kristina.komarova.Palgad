from module1 import*
from keyboard import*
palgad=loe_failist_listisse("palk.txt")
inimesed=loe_failist_listisse("inimesed.txt")

while 1:
    print("*"*100, "\nkeskmine -A\nmimimum -B\nmaksimum -C\notsing -Gnlisa -V")
    print("vajutage nuppu==>")

    if read_key()=="A":
        kesk_palk,round(keskmine(palk),2)
        print ("keskmine palk on", kesk_palk)

    elif read_key()=="B"
    min_palk,kallel=minimum(palk,inimesed)
    print
