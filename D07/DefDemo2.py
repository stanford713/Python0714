def calc(*score)-> int:# *=多個參數
    print(type(score))
    sum=0;
    for s in score:
        sum+=s
    return sum


if __name__ == "__main__":
    sum=calc(10,20,30,40)
    print(sum)
    sum=calc()
    print(sum)