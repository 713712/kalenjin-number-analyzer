# Tugen number system converter
# Gideon kiplagat C026-01-1039/2021
# Rainner kimutai C026-01-1038/2021
def kalenjinToEnglish(number):
    kalenjinNumbers = {
        1: 'agenge',
        2: 'oeng',
        3: 'somok',
        4: 'angwan',
        5: 'mut',
        6: 'lo',
        7: 'tisab',
        8: 'sisit',
        9: 'sokol',
        10: 'taman',
        11: 'taman ak akenge',
        12: 'taman ak aeng',
        13: 'taman ak somok',
        14: 'taman ak angwan',
        15: 'taman ak mut',
        16: 'taman ak lo',
        17: 'taman ak tisab',
        18: 'taman ak sisit',
        19: 'taman ak sokol',
        20: 'tiptem',
        30: 'sosom',
        40: 'artam',
        50: 'konom',
        60: 'tomon nwokik lo',
        70: 'tomon nwokik tisab',
        80: 'tomon nwokik sisit',
        90: 'tomon nwokik sokol',
        100: 'bokol',

    }
    if number in kalenjinNumbers:
        return kalenjinNumbers[number]

    if number in kalenjinNumbers.values():
        return [eng for eng, kal in kalenjinNumbers.items() if kal == number][0]

    if number in kalenjinNumbers:
        return kalenjinNumbers[number]

    if 13 <= number <= 19:
        tens_digit = number % 10
        return f"{kalenjinNumbers[10]} ak {kalenjinNumbers[tens_digit]}"

    if 21 <= number <= 99:
        tens_digit = (number // 10) * 10
        ones_digit = number % 10
        return f"{kalenjinNumbers[tens_digit]} ak {kalenjinNumbers[ones_digit]}"

    if 101 <= number <= 999:
        hundreds_digit = number // 100
        remaining_number = number % 100

        if remaining_number == 0:
            return f"{kalenjinNumbers[hundreds_digit]} ak {kalenjinNumbers[100]}"
        else:
            return f"{kalenjinNumbers[hundreds_digit]} {kalenjinNumbers[100]} ak {kalenjinToEnglish(remaining_number)}"



def option1():
    if __name__ == "__main__":
        while True:
            number = int(input("Enter the number to be converted to tugen:\n"))
            print(f"{number}: {kalenjinToEnglish(number)}")
        while True:
            exxit = input("type 'exit' to exit")
            if exxit.lower() == 'exit':
                break


def option2():
    if __name__ == "__main__":
        while True:
            number = input("Enter a number in Kalenjin or type 'exit' to quit: ")
            if number.lower() == 'exit':
                break

            converted = kalenjinToEnglish(number)
            print(f"{number}: {converted}")
    return "Number not found in Kalenjin or out of range"


options = input("Hello What would you like to do:\n1. Convert integer to kalenjin\n2. Convert kalenjin to integer\n3. "
                "Exit application\n")

while True:
    if options == '1':
        option1()
    elif options == '2':
        option2()
    elif options == '3':
        break
    else:
        print("Please select!!!!!")
