T1 = int(0)
T2 = int(1)
T3 = int(0)
print('-' *40)
print(' ' *8, 'Sequência de Fibonacci')
print('-' *40)
n = int(input('Digite um número: '))
while n > T3:
    T3 = T1 + T2
    T1 = T2
    T2 = T3
if n == 0 or n == 1:
    print('O número informado pertence a sequência de Fibonacci.')
elif n == T3:
    print('O número informado pertence a sequência de Fibonacci.')
else:
    print('O número informado não faz parte da sequência de Fibonacci.')


