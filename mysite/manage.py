import random, re

BIG_SIGN = list('QWERTYUIOPASDFGHJKLZXCVBNM')
LOW_SIGN = list('qwertyuiopasdfghjklzxcvbnm')
NUMS = list('1234567890')
LETTER_RANDOM = list('1234567')
NUMBER_RANDOM = list('123')
key_num = ''
key_num2 = ''
key_num3 = ''
keyA = ""
key_big = ''
key_big2 = ''
key_big3 = ''
keyA2 = ''
keyA3 = ''
with open('steam-keys.txt', 'w', encoding='utf-8') as file_keys:
    for i in range(50):
        letter_big = random.randint(6, 20)
        for i in range(letter_big):
            value = random.randrange(len(BIG_SIGN))
            value2 = random.randrange(len(BIG_SIGN))
            value3 = random.randrange(len(BIG_SIGN))
            key_big += BIG_SIGN[value]
            key_big2 += BIG_SIGN[value2]
            key_big3 += BIG_SIGN[value3]

        nums = random.randint(6, 9)
        for i in range(nums):
            value = random.randrange(len(NUMS))
            value2 = random.randrange(len(NUMS))
            value3 = random.randrange(len(NUMS))
            key_num += NUMS[value]
            key_num2 += NUMS[value2]
            key_num3 += NUMS[value3]

        keyA = key_num + key_big
        keyA2 = key_num2 + key_big2
        keyA3 = key_num3 + key_big3
        list_of_keys = list(keyA)
        list_of_keys2 = list(keyA2)
        list_of_keys3 = list(keyA3)
        random.shuffle(list_of_keys)
        random.shuffle(list_of_keys2)
        random.shuffle(list_of_keys3)
        append_string = ""
        append_string2 = ""
        append_string3 = ""

        for i in range(5):
            append_string += list_of_keys[i]
        for i in range(5):
            append_string2 += list_of_keys2[i]
        for i in range(5):
            append_string3 += list_of_keys3[i]
        l = re.findall('\d+', append_string)

        wow = ""
        wow += append_string
        wow += '-'
        wow += append_string2
        wow += '-'
        wow += append_string3
        #wow += ':'
        wow += '\n'



        file_keys.write(wow)


        print(wow)




#print(append_string)
