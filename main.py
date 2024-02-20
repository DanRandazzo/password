import random
import json
import sys

# Define the range of characters for password generation
CHARACTERS = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
LOWER_CASE_CHARACTERS = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
UPPER_CASE_CHARACTERS = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '$', '%', '&', '*', '@']

# Define the password generation function
def generator_password(length):
    lower_case_password = number_password = strong_password = normal_password = simple_password = ''
    for i in range(length):
        strong_password += random.choice(CHARACTERS + NUMBERS + SYMBOLS)
        normal_password += random.choice(CHARACTERS + NUMBERS)
        simple_password += random.choice(CHARACTERS)
        number_password += random.choice(NUMBERS)
        lower_case_password += random.choice(LOWER_CASE_CHARACTERS)
    return lower_case_password, number_password, simple_password, normal_password, strong_password

# Define the password strength scoring function
def password_score(password):
    score = 0

    if len(password) < 6:
        return score

    score += 1
    has_sz = has_xx = has_dx = has_ts = False

    for c in password:
        if not has_sz and c in NUMBERS:
            score += 1
            has_sz = True
        if not has_xx and c in LOWER_CASE_CHARACTERS:
            score += 1
            has_xx = True
        if not has_dx and c in UPPER_CASE_CHARACTERS:
            score += 1
            has_dx = True
        if not has_ts and c in SYMBOLS:
            score += 1
            has_ts = True

    return score

# Determine if the password contains sequential characters
def isSeries(pwd, seriesCount=3):
    '''
    Check if the password contains sequential characters.
    pwd: The password
    seriesCount: The number of sequential characters to check for
    '''
    ascSeriesCount = descSeriesCount = 1
    for i in range(1, len(pwd)):
        if ord(pwd[i]) == ord(pwd[i - 1]) + 1:
            ascSeriesCount += 1
            if ascSeriesCount >= seriesCount:
                return True
        else:
            ascSeriesCount = 1

        if ord(pwd[i]) == ord(pwd[i - 1]) - 1:
            descSeriesCount += 1
            if descSeriesCount >= seriesCount:
                return True
        else:
            descSeriesCount = 1

    return False

# Get icon path based on password score
def get_icon_by_score(score):
    if score >= 5:
        return {'path': 'mima-4.png'}
    elif 4 >= score > 3:
        return {'path': 'mima-7.png'}
    elif 3 >= score > 2:
        return {'path': 'mima-5.png'}
    else:
        return {'path': 'mima-6.png'}

# Main function to generate and evaluate passwords
def main(length=16):
    lower_case_password, number_password, simple_password, normal_password, strong_password = generator_password(length)

    items = [
        {
            "title": strong_password,
            "subtitle": "Alphanumeric + special characters",
            "arg": strong_password,
            'icon': get_icon_by_score(password_score(strong_password)),
            "valid": "True"
        },
        {
            "title": normal_password,
            "subtitle": "Alphanumeric",
            "arg": normal_password,
            'icon': get_icon_by_score(password_score(normal_password)),
            "valid": "True"
        },
        {
            "title": simple_password,
            "subtitle": "Alphabetic only",
            "arg": simple_password,
            'icon': get_icon_by_score(password_score(simple_password)),
            "valid": "True"
        },
        {
            "title": lower_case_password,
            "subtitle": "Lowercase letters only",
            "arg": lower_case_password,
            'icon': get_icon_by_score(password_score(lower_case_password)),
            "valid": "True"
        },
        {
            "title": number_password,
            "subtitle": "Numbers only",
            "arg": number_password,
            'icon': get_icon_by_score(password_score(number_password)),
            "valid": "True"
        },
    ]

    return json.dumps({'items': items}, ensure_ascii=False)

if __name__ == '__main__':
    query = sys.argv[1] if len(sys.argv) > 1 else 14
    res = main(int(query))
    print(res)
