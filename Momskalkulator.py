def momsUtenTotal(momsProsent, sumVerdi):
    momsVerdi = sumVerdi*(momsProsent/100)
    return momsVerdi

def momsTotalSum(momsProsent, sumVerdi):
    momsVerdi = sumVerdi-sumVerdi/(1+(momsProsent/100))
    return momsVerdi

brukerValg = 0
print('Tast 1 for å regne ut moms fra totalsum,\
 tast 2 for å regne ut moms fra sum eks moms.')
brukerValg = int(input())


if brukerValg == 1:
    print('Skriv inn momsen du ønsker\
 å regne med (for eskempel 25 for 25%)')
    brukerProsent = int(input())
    print('Skriv inn summen du skal regne momsen fra.')
    brukerSum = int(input())
    svarMoms = momsUtenTotal(brukerProsent, brukerSum)
    print(float("{:.2f}".format(svarMoms)))
elif brukerValg == 2:
    print('Skriv inn momsen du ønsker\
 å regne med (for eskempel 25 for 25%)')
    brukerProsent = int(input())
    print('Skriv inn summen du skal regne momsen fra.')
    brukerSum = int(input())
    svarMoms = momsTotalSum(brukerProsent, brukerSum)
    print(float("{:.2f}".format(svarMoms)))
else:
    print('Du har ikke valgt 1 eller 2.')
