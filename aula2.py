a = int(input('Digite A: '))
b = int(input('Digite B: '))
soma = a+b
# print(soma)
subtracao = a - b
multiplicacao = a *b
divisao  = a/b
resto = float(a % b)
# print('soma: ' + str(soma))
resultado = ('soma: {soma} '
      '\nSubtração: {sub}'
      '\nmultiplicação: {mult}'
      '\ndivisão: {div}'
      '\nresto: {rest}'.format(soma=soma,
                               sub=subtracao,
                               mult=multiplicacao,
                               div=divisao,
                               rest=resto))
print(resultado)

# print(subtracao)
# print(multiplicacao)
# print(int(divisao))
# print(resto)
# print(type(divisao))
