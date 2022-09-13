Table = ["", "", "abc", "def", "ghi", "jkl","mno", "pqrs", "tuv", "wxyz"]
def printWord(number, c, out, n):
    if(c == n):
        print(out)
        return
    for i in range(len(Table[number[c]])):
        out.append(Table[number[c]][i])
        printWord(number, c + 1, out, n)
        out.pop()
        if(number[c] == 0 or number[c] == 1):
            return
def printWords(number, n):
    printWord(number, 0, [], n)
  
  
if __name__ == '__main__':
    number =[]
    a=int(input("enter the limit:"))
    for j in range(0,a):
        b=int(input("enter the element"))
        number.append(b)
    n = len(number)
printWords(number, n)
