
hours=float(input('Enter hours: '))
rate=float(input("Enter rate: "))
payment=hours*rate
if hours>45:
    payment+=(hours-45)*rate*1.5
 
print (payment)
big = max ('Heloo world')
print (big)


def greet(lang):
     if lang == 'es':
        print('Hola')
     elif lang == 'fr':
        print('Bonjour')
     else:
        print('hello')
 
greet('en')
greet('es')
greet('fr')
