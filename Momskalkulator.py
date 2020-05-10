def momsUtenTotal(momsProsent, sumVerdi):
    momsVerdi = sumVerdi*(momsProsent/100)
    return momsVerdi

def momsTotalSum(momsProsent, sumVerdi):
    momsVerdi = sumVerdi-sumVerdi/(1+(momsProsent/100))
    return momsVerdi

brukerValg = 0
print('Tast 1 for å regne ut moms fra en sum eks. moms. \n\
Tast 2 for å regne ut moms fra en totalsum.')
brukerValg = int(input())


if brukerValg == 1:
    print('Skriv inn momsen du ønsker\
 å regne med (for eskempel 25 for 25%)')
    brukerProsent = int(input())
    print('Skriv inn summen du skal regne ut momsen for.')
    brukerSum = int(input())
    svarMoms = momsUtenTotal(brukerProsent, brukerSum)
    print('Av ' + str(brukerSum) + 'kr blir momsen ' +\
 str(float("{:.2f}".format(svarMoms)))\
 + 'kr.')
    totalSum = brukerSum + svarMoms
    print('Totalsummen blir ' + str(totalSum) + 'kr.')
elif brukerValg == 2:
    print('Skriv inn momsen du ønsker\
 å regne med (for eskempel 25 for 25%)')
    brukerProsent = int(input())
    print('Skriv inn summen du skal regne momsen fra.')
    brukerSum = int(input())
    svarMoms = momsTotalSum(brukerProsent, brukerSum)
    print('Av totalsum på ' + str(brukerSum) +  'kr, utgjør momsen '\
 + str(float("{:.2f}".format(svarMoms))) + 'kr.')
    sumUtenMoms = brukerSum - svarMoms
    print('Sum eks. moms blir ' + str(sumUtenMoms) + 'kr.')
else:
    print('Du har ikke valgt 1 eller 2.')
