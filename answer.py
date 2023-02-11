


def sumNums(numbers:[int])->int:
    total:int=0
    for num in numbers:
        if(int(num)==-999):
            break;
        elif(int(num)>=0):
            total=total+int(num)
    return total

def addNums(lines:list[int]):


    # if the first line that indicates the total nums is 0, the list is empty
    if len(lines) ==0:
        return "EMPTY"

    add:int = sumNums(lines[1:])
    return add


if __name__ == "__main__":
    filename = input()
    with open(filename) as data_file:
        lines: list[str]
        lines = data_file.readlines()
        addNums(lines)
        # Actually do the work

