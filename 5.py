#5) Escreva um programa que inverta os caracteres de um string.

#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

frase = str(input('Digite uma frase: '))
print(' Você digitou: {}'.format(frase))
string = frase[::-1]
print('A frase que você digitou invertida fica: {}'.format(string))