''' O-TASK (PYTHON): [2026년 5월 19일]
⭐️  Savol: Shunday function yozing, u har xil valuelardan iborat array qabul qilsin va List ichidagi sonlar yigindisini hisoblab chiqqan javobni qaytarsin. 
MASALAN: calculate_summary([10, "10", {son: 10}, true, 35]) return 45
'''

# ⭐️  Masalaning yechimi:
# DEFINE


def calculate_summary(array):
    summary = 0
    for ele in array:
        if type(ele) == type(summary):
             summary += ele
    return summary


# CALL
result = calculate_summary([10, "10", {"son": 10}, True, 35, False])
print(f"result: {result}")


# ==================================================================


''' M-TASK (PYTHON): [2026년 5월 14일]
⭐️  Savol: Shunday function yozing, u string qabul qilsin va string palindrom yani togri oqilganda ham, orqasidan oqilganda ham bir hil oqiladigan soz ekanligini aniqlab boolean qiymat qaytarsin. 
MASALAN: palindrom_check("dad") return True;  palindrom_check("son") return False;
'''

# ⭐️  Masalaning yechimi:
# DEFINE

'''
def palindrom_check(string):
    result = True if string == string[::-1] else False
    return result


# CALL
result = palindrom_check("dad")
print(f"result: {result}")
'''


# ==================================================================


''' K-TASK (PYTHON): [2026년 5월 11일]
⭐️  Savol: Shunday function yozing, u string qabul qilsin va string ichidagi eng uzun sozni qaytarsin. 
MASALAN: find_longest("I come from Uzbekistan") return "Uzbekistan"
'''

# ⭐️  Masalaning yechimi:
# DEFINE

'''
def find_longest(string):
    string_list = string.split()
    longest_word = string_list[0]
    for ele in string_list:
        if len(ele) > len(longest_word):
            longest_word = ele
    return longest_word


# CALL
result = find_longest("I come from Uzbekistan")
print(f"result: {result}")
'''


# ==================================================================


''' I-TASK (PYTHON): [2026년 5월 6일]
⭐️  Savol: Shunday function tuzing, unga string argument pass bolsin. Function ushbu agrumentdagi digitlarni yangi stringda return qilsin. 
MASALAN: get_digits("m14i1t") return qiladi "141"
'''

# ⭐️  Masalaning yechimi:
# DEFINE

'''
def get_digits(string):
    digits = ""
    for letter in string:
        if letter.isnumeric():
            digits += letter
    return digits


# CALL
result = get_digits("m14i1t")
print(f"result: {result}")
'''


# ==================================================================


''' G-TASK (PYTHON): [2026년 4월 30일]
⭐️  Savol: Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin. 
MASALAN: get_highest_index([5, 21, 12, 21, 8]) return qiladi 1 sonini.
'''

# ⭐️  Masalaning yechimi:
# DEFINE

'''
def get_highest_index(numb_list):
    highest_index = 0
    for number in numb_list:
        if (number > highest_index):
            highest_index = number
    return numb_list.index(highest_index)


# CALL
result = get_highest_index([5, 21, 12, 21, 8])
print(f"result: {result}")
'''
