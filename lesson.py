# 1---------------------------------------
def convert_to_kg(number, key_in_massa, **massa):
    m = massa.get(key_in_massa)
    print(m)
    if m == 'kg':
        return number
    if m == 'mgr':
        return (float(number)*float(1/1000000))
    if m == 'gr':
        return (float(number)*float(1/1000))
    if m == 't':
        n = int(number * 1000)
        return n
    if m == 'cent':
        n = int(number * 100)
        return n




massa = {'1': 'kg', '2': 'gr', '3': 't', '4': 'cent', '5': 'mgr'}

number = input('Введите массу ')
key_in_massa = input("Выберите ключ своей массы \n"
                        "1: 'kg'\n"
                        "2: 'gr'\n"
                        "3: 't'\n"
                        "4: 'cent'\n"
                        "5: 'mgr'")

if __name__ == "__main__":
    print(convert_to_kg(number, str(key_in_massa), **massa))

# 2-----------------------------
def rekur(n):
    print(pow(n,2))
    rekur(n)

if __name__ == "__main__":
    rekur(2)