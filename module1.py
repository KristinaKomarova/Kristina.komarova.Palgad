from random import*
palk=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]
def lists()->list:
    """ listist teeme faili
    :rtype: list, list
    """
    palgad=[]
    with open("palgad.txt" "r") as p:
        palgad.append(p.strip())
    inimesed=[]
    with open ("inimesed.txt" "r") as i:
        inimesed.append(i.strip())
    return palgad,inimesed

def loe_failist_listisse(file:str)->list:
    """ loeme tekst failist ja salvestame seda järendisse
    """
    file=open(file,"r")
    list_=[]
    for stroka in file:
        list_.append(stroka.strip())
    file.close()
    return list

def lisa(palk,iminene):
    """ lisame inimest ja palgad
    :param list inimene: nimed
    :param list palk: palgad
    :rtype: list,list
    """
    a=input("sisesta nimi=>")
    inimesed.append(a)
    b=int(input("sisesta palk=>"))
    palk.append(b)
    return(palk,inimene)
def add_inimene():
    """lisame inimesei ja palk
    """
    nimi=input("sisesta nimi")
    palk=input("sisesta palk")
    with open ("inimesed.txt", "a") as inimesed:
        inimesed.write(nimi+"\n")
    with open ("palgad.txt", "a") as palgad:
        palgad.write(palk+"\n")

def sisesta_andmed(i,p): 
    """sisestame nimi ja palk
    """
    N=4
    for n in range(N):
        a=input("sisesta nimi:")
        i.append(a)
        palk=randint(100,10000)
        p.append(palk)
    return i,p

def andmed_ekranile(i,p):
    """näitame ekraanil nimi ja palk
    """
    N=len(i)
    for n in range(N):
        print(i[n],"-",p[n])

def kustutamine(i,p):
    """kustutame inimes ja tema palk
    :rtype: list,list
    """
    nimi=input("sisesta nimi et teda eemaldada:")
    n=i.count(nimi)
    abi_list=[]
    if n>0:
        t=0
        for e in range(len(i)):
            if i[e]==nimi:
                t+=1
                abi_list.append(int(e)) 
                print(t,". ",i[e],"-", p[e])
        jaar=int(input("järekorranumber:"))
        i.pop(abi_list[jaar-1])
        p.pop(abi_list[jaar-1])
        andmed_ekranile(i,p)
        return i,p

def otsing_nimi_jargi(inimesed:lost,palgad:list):
    """Tagastame järend või tekst
    :rtype var: tulemus
    """
    nimi=input("Keda otsime?")
    for inimene in inimesed:
        if inimene==nimi:
            n=inimesed.count(nimi)
            print("Inimene on olemas,selline nimi kohtume",n,"korda")
            b=0
            t=[]
            for i in range(n):
                k=inimesed.index(nimi)
                palk=palgad[k]
                b+=k+1
                t.append(nimi+str(palk))

        else:
            t="Ei ole nimikirjas"
    return t

