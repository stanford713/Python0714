def ctof(c)->float:
    return c*(9/5)+32
def ftoc(f)->float:
    return (f-32)*5/9

if __name__=="__main__":
    print(ctof(35),ftoc(108))

