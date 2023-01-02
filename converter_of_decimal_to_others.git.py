value = int(input('Type the decimal value: '))
base = int(input('type the base you wish to convert: '))
quotient = abs(value)
remainder = ""
while quotient > 0:
    remainder += str(quotient % base)
    quotient = quotient // base
if value > 0:
    print('({}) 10 = ({}) {}'.format(value, remainder[::-1], base))
else:
    print('({}) 10 = (-{}) {}'.format(value, remainder[::-1], base))