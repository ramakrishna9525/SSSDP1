
k = int(input('Enter any number: '))

if k >= 0 and k <= 9:
    words = ['Zero', 'One', 'Two', 'Three', 'Four',
             'Five', 'Six', 'Seven', 'Eight', 'Nine']
    print(words[k])
else:
    print('Values must be from 0 to 9 only')
