''' G-TASK (PYTHON): [2026년 4월 30일]
⭐️  Savol: Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin. 
MASALAN: get_highest_index([5, 21, 12, 21, 8]) return qiladi 1 sonini.
'''

# ⭐️  Masalaning yechimi:
# DEFINE


def get_highest_index(numb_list):
    highest_index = 0
    for number in numb_list:
        if (number > highest_index):
            highest_index = number
    return numb_list.index(highest_index)


# CALL
result = get_highest_index([5, 21, 12, 21, 8])
print(f"result: {result}")
