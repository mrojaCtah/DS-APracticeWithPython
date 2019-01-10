from pythonds.basic.stack import Stack

def myParChecker(mySymbolString):
    
    stack = Stack()
    
    charSpot = 0
    balanced = True
    
    while(balanced and charSpot<len(mySymbolString)):
        
        if(mySymbolString[charSpot] == '('):
            stack.push('(')
        if(mySymbolString[charSpot] == ')'):
            if(stack.isEmpty()):
                balanced = false
                return balanced
            stack.pop()
        if(charSpot == len(mySymbolString) - 1):
            if(not stack.isEmpty()):
                balanced = False
                return balanced
            return balanced
        charSpot += 1
        
    
    
print(myParChecker('((()))'))
print(myParChecker('(()')) 
