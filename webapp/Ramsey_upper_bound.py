import math

def nCr(n, r):
    # Implements the combinatorics n choose r
    r = min(r, n-r)
    numer = 1
    demon = 1
    while(r >= 1):
        numer *= (n-r+1)
        demon *= r
        r -= 1
    return(int(numer/demon))

#try to help user to find upperbound by example
def upperBound(s, t):
    
    print("A upper bound on the Ramsey numbers R(s,t)\n"
          "was obtained by double induction on s and t.\n"
          "Since we have observed the relationship between R(s,t) and R(s-1,t), R(s, t-1).\n"
          "Such that: R(s,t) <= R(s-1,t) + R(s,t-1)\n"
          "Then apply the double induction\n"
          "assuming R(s,t) <= C(s+t-2, t-1) works for all s+t = n.\n"
          "Since R(s-1,t) <= C(s+t-2, t-1) = C(n-2, t-1)\n"
          "and R(s,t-1) <= C(s+t-2, t-2) = C(n-2, t-2).\n"
          "Applying Pascal's rule: C(n-2, t-1) + C(n-2, t-2) = C(n-1, t-1)\n"
          "which proves that R(s,t) <= R(s-1,t) + R(s,t-1)\n"
          "<= C(n-2, t-1) + C(n-2, t-2) = C(n-1, t-1).\n"
          "then it also works for s+t= n+1.\n"
          "\n"

          "Take R("+str(s)+","+str(t)+") for example.\n"
          "Given R(s,t) <= R(s-1,t) + R(s,t-1)\n"
          "To find upper bound of R(s,t)\n"
          "Which two Ramsey numbers should we use?\n"
          "A. R("+str(s)+","+str(t)+")\n"
          "B. R("+str(s-1)+","+str(t)+")\n"
          "C. R("+str(s)+","+str(t-1)+")\n"
          "D. R("+str(s-1)+","+str(t-1)+")\n")
    
    # user select the correct choice
    choiceSelection1()

    print("Then we take one step further\n"
        "Select combinations in order to calculate the upper bound of R("+str(s)+","+str(t)+")\n"
        "Which two combinations we should use?\n"
          "A. C("+str(s+t-1)+","+str(t-2)+") and C("+str(s+t-1)+","+str(t-1)+")\n"
          "B. C("+str(s+t-1)+","+str(t-2)+") and C("+str(s+t-1)+","+str(t-2)+")\n"
          "C. C("+str(s+t-2)+","+str(t-1)+") and C("+str(s+t-2)+","+str(t-1)+")\n"
          "D. C("+str(s+t-2)+","+str(t-1)+") and C("+str(s+t-2)+","+str(t-2)+")\n")

    # user select the correct choice
    choiceSelection2()

    print("Here we have known where to find the upper bound of R(s,t).\n"
          "Now to calculate the upper bound of R("+str(s)+","+str(t)+")\n"
          "Here are some results of combinations:\n"
          
          "C("+str(s+t-1)+","+str(t-3)+"): "+str(nCr(s+t-1, t-3))+"\n"
          "C("+str(s+t-2)+","+str(t-2)+"): "+str(nCr(s+t-2, t-2))+"\n"
          "C("+str(s+t-2)+","+str(t-3)+"): "+str(nCr(s+t-1, t-3))+"\n"
          "C("+str(s+t-2)+","+str(t-1)+"): "+str(nCr(s+t-2, t-1))+"\n"

          "Calculate the upper bound of R("+str(s)+","+str(t)+")\n"
          "And Write down your answer below:\n"
          )

    #user write the upper bound
    upperboundCalcualte(s, t)

    print("Thanks for your particpation.\n")

# To identify if user select the right choice 
# If user fail 6 times
# Then system automatically output thecorrect answer
def choiceSelection1():
    selection1 = " "
    selection2 = " "
    times1 = 0
    isFalse = True
    while(isFalse):

        while(isFalse):
            try:
                selection1,selection2 = map(str,input().split( ))
                break
            except(ValueError):
                print("Please select two choices from A,B,C,D\n"
                    "Remember seperating two choices by SPACE key\n"
                    "Try again\n")

        if (selection1 == "B") and (selection2 == "C"):
            print("Good job!\n")
            isFalse = False 
        elif (selection1 == "C") and (selection2 == "B"):
            print("Good job!\n")
            isFalse = False
        else:
            print("Sorry, try it again.\n")
            isFalse = True
        
        times1 = times1 + 1
        if (times1 == 6):
            print("The correct answer is B and C.\n")
            break
    return

# To identify if user select the right choice 
# If user fail 6 times
# Then system automatically output thecorrect answer
def choiceSelection2():
    selection3 = " "
    times2 = 0
    isFalse = True
    while(isFalse):

        while(isFalse):
            try:
                selection3 = str(input())
                break
            except(ValueError):
                print("Please select two choices from A,B,C,D\n"
                    "Try again\n")

        if (selection3 == "D"):
            print("Good job!\n")
            isFalse = False
        else:
            print("Sorry, try it again.\n")
            isFalse = True
        
        times2 = times2 + 1
        if (times2 == 6):
            print("The correct answer is D.\n")
            break
    return
    
# To identify if user write the correct upper bound 
# If user fail 6 times
# Then system automatically output thecorrect answer
def upperboundCalcualte(s, t):
    num = 0
    times3 = 0
    isFalse = True
    correct_answer = nCr(s+t-2, t-1) + nCr(s+t-2, t-2)
    while(isFalse):

        while(isFalse):
            try:
                num = int(input())
                break
            except(ValueError):
                print("Please write an intger\n"
                    "Try again\n")

        if (num == correct_answer):
            print("You have understood how to calculate upper bound of Ramsey Number.\n"
                    "Congradulations!\n")
            isFalse = False
        else:
            print("Sorry, try it again.\n")
            isFalse = True
        
        times3 = times3 + 1
        if (times3 == 6):
            print("The correct answer is: " + str(correct_answer))
            break
    return

if __name__ == "__main__":
    print("Test on finding the upper bound of R(s,t)")
    s = 10
    t = 12
    print("Inputs are "+str(s)+" and "+str(t))
    upperBound(s, t)