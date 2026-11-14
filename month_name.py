
o = int(input("Enter Month Number (1-12): "))

if o >= 1 and o <= 12:
    words = ['January', 'February', 'March',
             'April', 'May', 'June', 'July', 'August',
             'September', 'October', 'November', 'December']

    print(words[o-1])
else:
    print("Enter valid Month Number")
