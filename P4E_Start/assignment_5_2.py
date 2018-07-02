# initialize variables
largest = None
smallest = None

while True:
    num = input('Enter a number: ')
    # check for done
    if num == 'done':
        break
    try:
        val = float(num)
    except:
        print('Invalid input')
        continue
    if largest is None:
        largest = val
    elif val > largest:
        largest = val
    if smallest is None:
        smallest = val
    elif val < smallest:
        smallest = val
print('Maximum is', int(largest))
print('Minimum is', int(smallest))
