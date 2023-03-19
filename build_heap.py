# python3

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)
    for i in range(n, 1, -1):
        j = i
        while j > 1 and data[j-1] < data[parent(j)-1]:
            temp = data[parent(j)-1]
            data[parent(j)-1] = data[j-1]
            data[j-1] = temp
            swaps.append((parent(j)-1, j-1))
            
            j = parent(j)
    return swaps


def parent(child):
    if child % 2 == 0:
        return child // 2
    else:
        return (child - 1) // 2

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    text = input()
    if "I" == text[0]:
        n = int(input())
        data = list(map(int, input().split()))
    elif "F" == text[0]:
        #input from file
        filename = input()
        if "a" not in filename:
            with open('./tests/'+filename,'r') as file:
                n = int(file.readline())
                data = list(map(int, file.readline().split()))
                

    

    # input from keyboard
    #n = int(input())
    #data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    #for i, j in swaps:
    #    print(i, j)
    for i in swaps:
        print(i[0], i[1])

if __name__ == "__main__":
    main()
