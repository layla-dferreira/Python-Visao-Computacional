# Salário com bônus(beecrowd) - Fazer o calculo do salario com bonus a patir dos dados informado pelo usuario
nome = input('');
salario = float(input(''));
vendas = float(input(''));

total = (vendas * 0.15) + salario;

print('TOTAL = R$', "%.2f" % total);


# Esfera(beecrowd) - Calcular o valor da esfera a partir do raio informado pelo usuario
raio = int(input(''));

volume = (4/3.0) * 3.14159 * (raio ** 3);

print('VOLUME =', "%.3f" % volume); 


# Área(beecrowd) - Fazer o calculo da area de algumas figuras
A = float(input(''));
B = float(input(''));
C = float(input(''));

trianguloRetangulo = (1/2.0) * A * C;
circulo = 3.14159 * (C ** 2);
trapezio = ((A + B) * C) / 2;
quadrado = B ** 2;
retangulo = A * B;

print('TRIANGULO:', '%.3f' % trianguloRetangulo);
print('CIRCULO:', '%.3f' % circulo);
print('TRAPEZIO:', '%.3f' % trapezio);
print('QUADRADO:', '%.3f' % quadrado);
print('RETANGULO:', '%.3f' % retangulo);


# Notas e Moedas(beecrowd) - Produzir um codigo para fazer a contagem de notas e moedas de acordo com o valor informado pelo usuario
valor = float(input(''));

print('NOTAS:');
if valor >= 100:
    cem = valor // 100;
    cem1 = int(cem);
    print(f'{cem1} nota(s) de R$ 100.00');
    rest1 = valor - (cem1 * 100);
else:
    print('0 nota(s) de R$ 100.00');
    rest1 = valor;
 
if rest1 >= 50:
    cinquenta = rest1 // 50;
    cinquenta1 = int(cinquenta);
    print(f'{cinquenta1} nota(s) de R$ 50.00');
    rest2 = rest1 - (cinquenta1 * 50);
else:
    print('0 nota(s) de R$ 50.00');
    rest2 = rest1;

if rest2 >= 20: 
    vinte = rest2 // 20;
    vinte1 = int(vinte);
    print(f'{vinte1} nota(s) de R$ 20.00');
    rest3 = rest2 - (vinte1 * 20);
else:
    print('0 nota(s) de R$ 20.00');
    rest3 = rest2

if rest3 >= 10: 
    dez = rest3 // 10;
    dez1 = int(dez);
    print(f'{dez1} nota(s) de R$ 10.00');
    rest4 = rest3 - (dez1 * 10);
else:
    print('0 nota(s) de R$ 10.00');
    rest4 = rest3;

if rest4 >= 5: 
    cinco = rest4 // 5;
    cinco1 = int(cinco);
    print(f'{cinco1} nota(s) de R$ 5.00');
    rest5 = rest4 - (cinco1 * 5);
else:
    print('0 nota(s) de R$ 5.00');
    rest5 = rest4;

if rest5 >= 2: 
    dois = rest5 // 2;
    dois1 = int(dois);
    print(f'{dois1} nota(s) de R$ 2.00');
    rest6 = rest5 - (dois1 * 2);
else:
    print('0 nota(s) de R$ 2.00');
    rest6 = rest5;

print('MOEDAS:');
if rest6 >= 1:
    um = rest6 // 1;
    um1 = int(um);
    print(f'{um1} moeda(s) de R$ 1.00');
    rest7 = rest6 - (um1 * 1);
else:
    print('0 moeda(s) de R$ 1.00');
    rest7 = rest6;

if rest7 >= 0.50:
    cinquentaCents = rest7 // 0.5;
    cinquentaCents1 = int(cinquentaCents);
    print(f'{cinquentaCents1} moeda(s) de R$ 0.50');
    rest8 = rest7 - (cinquentaCents1 * 0.5);
else:
    print('0 moeda(s) de R$ 0.50');
    rest8 = rest7;

if rest8 >= 0.25:
    vinteCinco = rest8 // 0.25;
    vinteCinco1 = int(vinteCinco);
    print(f'{vinteCinco1} moeda(s) de R$ 0.25');
    rest9 = rest8 - (vinteCinco1 * 0.25);
else:
    print('0 moeda(s) de R$ 0.25');
    rest9 = rest8;

if rest9 >= 0.10:
    dezCents = rest9 // 0.10;
    dezCents1 = int(dezCents);
    print(f'{dezCents1} moeda(s) de R$ 0.10');
    rest01 = rest9 - (dezCents1 * 0.10);
else:
    print('0 moeda(s) de R$ 0.10');
    rest01 = rest9;

if rest01 >= 0.05:
    cincoCents = rest01 // 0.05;
    cincoCents1 = int(cincoCents);
    print(f'{cincoCents1} moeda(s) de R$ 0.05');
    rest02 = rest01 - (cincoCents1 * 0.05);
else:
    print('0 moeda(s) de R$ 0.05');
    rest02 = rest01;

if rest02 >= 0.01:
    umCents = rest02 // 0.01;
    umCents1 = int(umCents);
    print(f'{umCents1} moeda(s) de R$ 0.01');
    rest03 = rest02 - (umCents1 * 0.01);
else:
    print('0 moeda(s) de R$ 0.01');
    rest03 = rest02;


# A conversão de graus Farenheit para Celsius é obtida por C = 5 (F-32)/9 Fazer um programa para calcular e mostrar uma tabela de graus Celsius em função de graus 
# Farenheit, que variem de 50 a 150, de 1 em 1.
for fareheit in range(50, 151):
    celcius = (5 * (fareheit-32)) / 9;
    print('Fareheit: ', '%.2f' % fareheit, 'Celcius: ' '%.2f' % celcius);


# Fazer um programa para gerar e mostrar os N primeiros termos da série a seguir. N é informado pelo usuário. 0 - 5 - 6 - 11 - 12 - 17 - 18 - 23 - 24 ...
num = int(input('Digite a quantidade de numeros: '));

# Feito com While
i = 0
while i <= num:
    print(i)
    if i % 2 != 0 and i < num:
        i += 1
        print(i)
    i += 5

# Feito com For
i = 0;
for _ in range(num):
    print(i);

    if i % 2 != 0 and i < num:
        i += 1;
        print(i);
    i += 5;