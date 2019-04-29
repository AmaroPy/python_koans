# Rockanroladas de python

## Mostrar un diccionario como un json

textodesalida | python -m json.tool

## Namedtupled (clases baratas)
Convierte un diccionario a objeto.


## Sets en python

Son como arrays pero en vez [] va con {}

{"banana","platano", "whatever"}

Un set se parece mucho en un array, hasta ahora la única vez que lo he visto en producción es para usar:

`intersection` que sirve para encontrar elementos en común entre 2 `set` y ejemplo tenemos debajo:

## Elementos en comun entre 2 arrays

```
b1 = [1,2,3,4,5,9,11,15]
b2 = [4,5,6,7,8]
set(b1).intersection(b2)
set([4, 5])
```
## Comprenhension lists

Creo que lo mejor es pasar un bucle for a comprehension y practicarlo:

```
numbers = [1,2,11,14,16,0,3]
```

```
higher_than_ten = []                                                # 1
for number in numbers                                               # 2
    if number > 10:                                                 # 3
        higher_than_ten.append(str(number) + ' is higher than ten') # 4
```

```
higher_than_ten = [str(number) + ' is higher than ten' for number in numbers if number > 10]
#[     #1      ]  [             #4                   ][        #2           ][     #3      ] 
   Nombre variable           Lo que se ejecuta         for number in numbers    la condicion
```


Nested comprehension: (a mi no me gustan pero bueno)

```
flattened = []
for row in matrix:
    for n in row:
        flattened.append(n)
```

```
flattened = [n for row in matrix for n in row]
```

mejor escrito parece que tiene algo mas de sentido:

```
flattened = [
    n 
    for row in matrix 
    for n in row
    ]
```



## Decoradores

## @Properties

## enumerate

## *args y **kwargs

## Bucle con indice

```
names = ['Bob', 'Alice', 'Guido']
for index, value in enumerate(names):
    print(f'{index}: {value}')


######
# 0: Bob
# 1: Alice
# 2: Guido
```

## Magia de clases:

https://github.com/RafeKettler/magicmethods

## DATETIME TIME STRPTIME

Como convertir un string en un objeto de tiempo:

<table class="tg"><tbody><tr><th class="tg-xldj">Directive</th><th class="tg-xldj">Description</th><th class="tg-xldj">Example Output</th></tr><tr><td class="tg-c51l">%a</td><td class="tg-c51l">Weekday as locale’s abbreviated name.</td><td class="tg-c51l">Sun, Mon, …, Sat (en_US)<br>So, Mo, …, Sa (de_DE)</td></tr><tr><td class="tg-xldj">%A</td><td class="tg-xldj">Weekday as locale’s full name.</td><td class="tg-xldj">Sunday, Monday, …, Saturday (en_US)<br>Sonntag, Montag, …, Samstag (de_DE)</td></tr><tr><td class="tg-c51l">%w</td><td class="tg-c51l">Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.</td><td class="tg-c51l">0, 1, 2, 3, 4, 5, 6</td></tr><tr><td class="tg-xldj">%d</td><td class="tg-xldj">Day of the month as a zero-padded decimal number.</td><td class="tg-xldj">01, 02, …, 31</td></tr><tr><td class="tg-c51l">%b</td><td class="tg-c51l">Month as locale’s abbreviated name.</td><td class="tg-c51l">Jan, Feb, …, Dec (en_US)<br>Jan, Feb, …, Dez (de_DE)</td></tr><tr><td class="tg-xldj">%B</td><td class="tg-xldj">Month as locale’s full name.</td><td class="tg-xldj">January, February, …, December (en_US)<br>Januar, Februar, …, Dezember (de_DE)</td></tr><tr><td class="tg-c51l">%m</td><td class="tg-c51l">Month as a zero-padded decimal number.</td><td class="tg-c51l">01, 02 … 12</td></tr><tr><td class="tg-xldj">%y</td><td class="tg-xldj">Year without century as a zero-padded decimal number.</td><td class="tg-xldj">01, 02, … 99</td></tr><tr><td class="tg-c51l">%Y</td><td class="tg-c51l">Year with century as a decimal number.</td><td class="tg-c51l">0001, 0002, … , 9999</td></tr><tr><td class="tg-xldj">%H</td><td class="tg-xldj">Hour (24-hour clock) as a zero-padded decimal number.</td><td class="tg-xldj">01, 02, … , 23</td></tr><tr><td class="tg-c51l">%I</td><td class="tg-c51l">Hour (12-hour clock) as a zero-padded decimal number.</td><td class="tg-c51l">01, 02, … , 12</td></tr><tr><td class="tg-xldj">%p</td><td class="tg-xldj">Locale’s equivalent of either AM or PM.</td><td class="tg-xldj">AM, PM (en_US)<br>am, pm (de_DE)</td></tr><tr><td class="tg-c51l">%M</td><td class="tg-c51l">Minute as a zero-padded decimal number.</td><td class="tg-c51l">01, 02, … , 59</td></tr><tr><td class="tg-0pky">%S</td><td class="tg-0pky">Second as a zero-padded decimal number.</td><td class="tg-0pky">01, 02, … , 59</td></tr><tr><td class="tg-phtq">%f</td><td class="tg-phtq">Microsecond as a decimal number, zero-padded on the left.</td><td class="tg-phtq">000000, 000001, …, 999999<br>Not applicable with time module.</td></tr><tr><td class="tg-0pky">%z</td><td class="tg-0pky">UTC offset in the form ±HHMM[SS] (empty string if the object is naive).</td><td class="tg-0pky">(empty), +0000, -0400, +1030</td></tr><tr><td class="tg-phtq">%Z</td><td class="tg-phtq">Time zone name (empty string if the object is naive).</td><td class="tg-phtq">(empty), UTC, IST, CST</td></tr><tr><td class="tg-0pky">%j</td><td class="tg-0pky">Day of the year as a zero-padded decimal number.</td><td class="tg-0pky">001, 002, …, 366</td></tr><tr><td class="tg-phtq">%U</td><td class="tg-phtq">Week number of the year (Sunday as the first day of the week) as a zero padded decimal number. <br>All days in a new year preceding the first Sunday are considered to be in week 0.</td><td class="tg-phtq">00, 01, …, 53</td></tr><tr><td class="tg-0pky">%W</td><td class="tg-0pky">Week number of the year (Monday as the first day of the week) as a decimal number. <br>All days in a new year preceding the first Monday are considered to be in week 0.</td><td class="tg-0pky">00, 01, …, 53</td></tr><tr><td class="tg-phtq">%c</td><td class="tg-phtq">Locale’s appropriate date and time representation.</td><td class="tg-phtq">Tue Aug 16 21:30:00 1988 (en_US)<br>Di 16 Aug 21:30:00 1988 (de_DE)</td></tr><tr><td class="tg-0pky">%x</td><td class="tg-0pky">Locale’s appropriate date representation.</td><td class="tg-0pky">08/16/88 (None)<br>08/16/1988 (en_US)<br>16.08.1988 (de_DE)</td></tr><tr><td class="tg-phtq">%X</td><td class="tg-phtq">Locale’s appropriate time representation.</td><td class="tg-phtq">21:30:00 (en_US)<br>21:30:00 (de_DE)</td></tr><tr><td class="tg-0pky">%%</td><td class="tg-0pky">A literal ‘%’ character.</td><td class="tg-0pky">%</td></tr></tbody></table>