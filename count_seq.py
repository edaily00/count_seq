#Eric Daily
#Github Username: edaily00
#Date: 7/30/2022
#This program counts the numbers in a sting
def count_seq():
"""This functions runs forever and starts off by yielding the number to be counted"""
    num = "2"

    while 0 == 0:
        yield num
        new_num = ""
        i = 0
        while i < len(num):
            num_of = 0
            target = num[i]
            for x in num[i:]:
                if target == x:
                    num_of += 1
                    i += 1
                else:
                    break

            new_num += str(num_of)
            new_num += target
        num = new_num

