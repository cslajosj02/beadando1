import sys
from phone import model

def main()->None:

    try:
        tartomany = int(sys.argv[1])
    except:
        print("HIBA, nem ért. az arg.!, -> A program futása véget ért! Kérem javítsa ki a hibát!")
        return

    if len(sys.argv)<2:
        print( "HIBA, nincs arg.! -> A program futása véget ért! Kérem javítsa ki a hibát!")
        return
    if tartomany==1:
        print("Az argumentumok rendben vannak! Kérem kezdje el begépelni az adatsort!")
    else:
        print("Az argumentumok rendben vannak! Kérem kezdje el begépelni az adatsorokat!")



    devices=[]
    for n in range(tartomany):
        line= input()
        tokens=line.split(';')
        if len(tokens)==4:
            device=model.sphone(tokens[0],tokens[1],int(tokens[2]),tokens[3])
            devices.append(device)

    devices.sort()
    for dv in devices:
        print(dv)






if __name__=="__main__":
    main()