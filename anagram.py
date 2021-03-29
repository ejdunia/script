# A Program to chech anagrams.

print("This program will tell you if the words you type are anagrams!\nAn example of an anagram is 'Live' and 'evil'.")
inp_1 = input("Enter a word: ").strip().lower()
inp_2 = input("Enter another word: ").strip().lower()

def check_angr(str_1, str_2):
    """ rearraanges arguments alphabetically then chechks if it's an anagram"""
    res_1 = ''.join(sorted(str_1))
    res_2 = ''.join(sorted(str_2))
# compare the strings
    if res_1 == res_2:
        print("This is an anagram!")
    else:
        print("This isn't an anagram")

check_angr(inp_1, inp_2)

