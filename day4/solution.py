def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    count = 0
    for line in lines[:-1]:
        line = line.strip('\n')
        pairs = line.split(',')
        ranges = [x.split('-') for x in pairs]
        print(ranges)

        # Assume the first pair is contained in the second pair
        # Check if the left bound of the first pair is greater
        # or equal than the left boud of the second pair
        if int(ranges[0][0]) >= int(ranges[1][0]):
            
            # Check if the right bound of the first pair is lesser
            # than the right bound of second pair
            if int(ranges[0][1]) <= int(ranges[1][1]):
                count += 1
                print('yes')
            
            # Edge case - if the left bounds are equal
            # first pair may contain the second pair
            elif int(ranges[0][0]) == int(ranges[1][0]) and int(ranges[0][1]) >= int(ranges[1][1]):
                count += 1
                print('yes')
        else:
            
            # In that case the second pair might be contained in the first pair
            # Check if the left bound of the first pairs is greater or equal
            # thatn the left bound of the second pair
            if int(ranges[0][1]) >= int(ranges[1][1]):
                count += 1
                print('yes')
    print(count)
                

if __name__ == '__main__':
    main()
