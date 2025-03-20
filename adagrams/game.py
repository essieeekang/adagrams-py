from random import randint

# constants declaration
LETTER_POOL = [
    {"letter": "A", "count": 9, "value": 1},
    {"letter": "B", "count": 2, "value": 3},
    {"letter": "C", "count": 2, "value": 3},
    {"letter": "D", "count": 4, "value": 2},
    {"letter": "E", "count": 12, "value": 1},
    {"letter": "F", "count": 2, "value": 4},
    {"letter": "G", "count": 3, "value": 2},
    {"letter": "H", "count": 2, "value": 4},
    {"letter": "I", "count": 9, "value": 1},
    {"letter": "J", "count": 1, "value": 8},
    {"letter": "K", "count": 1, "value": 5},
    {"letter": "L", "count": 4, "value": 1},
    {"letter": "M", "count": 2, "value": 3},
    {"letter": "N", "count": 6, "value": 1},
    {"letter": "O", "count": 8, "value": 1},
    {"letter": "P", "count": 2, "value": 3},
    {"letter": "Q", "count": 1, "value": 10},
    {"letter": "R", "count": 6, "value": 1},
    {"letter": "S", "count": 4, "value": 1},
    {"letter": "T", "count": 6, "value": 1},
    {"letter": "U", "count": 4, "value": 1},
    {"letter": "V", "count": 2, "value": 4},
    {"letter": "W", "count": 2, "value": 4},
    {"letter": "X", "count": 1, "value": 8},
    {"letter": "Y", "count": 2, "value": 4},
    {"letter": "Z", "count": 1, "value": 10}
    ]

# function takes no parameters and returns array of ten strings representing 10 tiles of letters
def draw_letters():
    tile_count = []
    hand = []
    
    for letter in LETTER_POOL:
        tile_count.append(letter["count"])

    while len(hand) < 10:
        letter_id = randint(0, 25)
        if tile_count[letter_id]:
            hand.append(LETTER_POOL[letter_id]["letter"])
            tile_count[letter_id] -= 1
        else:
            continue

    return hand

def uses_available_letters(word, letter_bank):
    letter_bank = letter_bank.copy()
    for letter in word.upper():
        if letter in letter_bank:
            letter_bank.remove(letter)
        else:
            return False

    return True

def score_word(word):
    score = 0
    if not word:
        return 0
    if len(word) > 6:
        score += 8
    for letter in word.upper():
        index = get_index_from_letter(letter)
        score += LETTER_POOL[index]["value"]
    
    return score

def get_highest_word_score(word_list):
    pass

# helper functions
def get_index_from_letter(letter):
    index_map = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, 
                "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11,
                "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17,
                "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23,
                "Y": 24, "Z": 25}
    return index_map[letter]