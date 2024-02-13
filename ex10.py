from datetime import date

dt = int ( input ('Em que ano você nasceu? '))
idd = date.today().year - dt

if (idd < 18):
    print ('Novinho ainda, faltam {} ano(s) pra fazer 18!' .format (18 - idd))

elif (idd == 18):
    print ('Ta na hora de se alistar!!!')

elif (idd > 18):
    print ('Ja se passaram {} ano(s) desde que você tinha que se alistar' .format (idd - 18))