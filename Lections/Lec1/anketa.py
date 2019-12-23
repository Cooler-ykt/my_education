print('Как тебя зовут?')
name = input()
print('Рад позвакомиться, ', name, '!', sep = '')
age = int(input("Сколько тебе лет, " + name + "?\n"))
x = age + 1
#if 11 <= x and x <= 19:
if x in range(11,20,1):
    x = 'лет!...'
elif 1 == x % 10:
    x = 'год!...'
#elif 2 <= x % 10 and x % 10 <= 4:
elif x % 10 in range(2,5,1):
    x = 'года!...'
else:
    x = 'лет!...'

print('А я думал, тебе', age + 1, x)
           
