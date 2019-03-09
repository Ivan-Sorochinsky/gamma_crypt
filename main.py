
# T( i+1) = ( A * T( i ) + C ) mod M
# Метод  гаммирования с обратной связью b=7
# Пусть A=5; C=3; b=7; M=2^7=128; T(0)=7
# T(1)=(5*7+3) mod 128 = 38  (0100110)
# T(2)=(5*38+3) mod 128 = 65 (1000001)
# T(3)=(5*65+3) mod 128 = 72 (1001000)
# '{0:07b}'.format(72)
# Гамма шифра 0100110 1000001 1001000

def count_one_in_char(string):
    i=0
    answer = []
    for s in string:
        for c in '{0:07b}'.format(ord(s)):
            if c=="1":
                i+=1
        answer.append(i)
        i=0
    return answer

# T( i+1) = ( A * T( i ) + C ) mod M
def calculate_gamma(total):
    gamma = []
    for a in total:
        gamma.append('{0:07b}'.format((5 * a + 3) % 128))
    return gamma


def crypt(string, gamma):
    answer = ""
    string1=""
    gamma1=""
    for s, g in zip(string, gamma):
        string1 +='{0:07b}'.format(ord(s))
        gamma1 += g
    for s, g in zip(string1, gamma1):
        answer += str(int(s) ^ int(g))
    return answer

def decrypt(string, gamma):
    answer = ""
    ans = []
    ans2 = ""
    for s, g in zip(string, gamma):
        answer += str(int(s) ^ int(g))
    n = 7
    ans = [answer[i:i + n] for i in range(0, len(answer), n)]
    for s in ans:
        ans2 += chr(int(s, 2))
    return ans2


#def decrypt(str):

#print(count_one_in_char("аbcdef"))
#print(calculate_gamma([2,3,4,5]))

def main():

    print("Выберите требуемую операцию: 1 - crypt или 2 - decrypt ")
    answer = input()
    if answer=="1":
        print("Вы выбрали кодирование!")
        print("Введите строку котору требуется зашифровать: ")
        string = input()
        print("Количество единиц бинарного кода в каждом символе: ")
        total = count_one_in_char(string)
        print(total)
        print("Подсчет гамма шифра: ")
        gamma = calculate_gamma(total)
        print(gamma)
        print("Закодированние сообщение: ")
        print(crypt(string, gamma))
    else:
        print("Вы выбрали декодирование!")
        print("Введите строку котору требуется расшифровать: ")
        string = input()
        print("Введите гамма шифр: ")
        gamma = input()
        print("Исходное сообщение: ")
        print(decrypt(string, gamma))
main()

#ivan  1101001111011011000011101110
#Гамма шифр
#['0010111', '0011100', '0010010', '0011100']
#1111110110101011100111110010