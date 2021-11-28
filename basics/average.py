"""
this is a program that gets numbers as input
and shows the average
"""

a = []
count = 0
while True:
    m = input ("inter you number: ")
    try: # avoid non-numerical inputs
        m = int(m)
        if m == -1: #avoid zero devision error
            if count == 0:
                print ("ziro")
                break
            average = sum (a)/ count
            print (average)
            print("over")
            break
        a.append(m)
        count = count+1
    except ValueError:
        a.append(2)
        count = count+1