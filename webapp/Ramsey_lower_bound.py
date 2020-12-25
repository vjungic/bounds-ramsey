import math


def nCr(n, r):
    # Implements the combinatorics n choose r
    r = min(r, n - r)
    numer = 1
    demon = 1
    while (r >= 1):
        numer *= (n - r + 1)
        demon *= r
        r -= 1
    return (int(numer / demon))


def lowerBound(s, t):
    # Inputs are integers s, t >= 3
    # Output is a integer n
    # n satisfies R(s,t) > n
    # m is a temp holder for min(s,t)

    m = min(s, t)
    L_cmp = 0
    L_usr = 0
    L_temp = 0

    # ------------------------------------------------------------#

    print("A lower bound on the diagonal Ramsey numbers R(s,s)\n"
          "was obtained by Paul Erdos using the probabilistic\n"
          "method. He showed that for K_n where n = 2^(s/2),\n"
          "any two-coloring on the edges of K_n will generate\n"
          "at least one K_s with a probability less than one.\n"
          "It is the same as saying the probability of having\n"
          "no monochromatic K_s in K_n is greater than 0, that\n"
          "it is certain that some colorings of K_n give no\n"
          "monochromatic K_s.\n"
          "\n"
          "Knowing R(s,s) < R(s,t) for s < t, we are certain\n"
          "that R(" + str(s) + "," + str(t) + ") < R(" + str(m) + ","
          + str(m) + ").\n"
                     "\n"
                     "Given the lower bound on the diagonal Ramsey numbers\n"
                     "is R(s,s) > 2^(s/2), lets find a lower bound for\n"
                     "R(" + str(m) + "," + str(m) + "), which also "
                                                    "bounds R(" + str(s) + "," + str(t) + ").\n")

    # L for lower bound
    L_cmp = math.floor(2 ** (m / 2))
    i = 0
    tempResult = (False, "ErrorType", i)
    while (not (tempResult[0])):
        L_usr = input("R(" + str(m) + "," + str(m) + ") > ")
        tempResult = usrInputCmp(L_cmp, L_usr, i)

        if (tempResult[1] == "tooLarge"):
            print("The entered value is larger than expected")
        elif (tempResult[1] == "tooSmall"):
            print("The entered value is smaller than expected")
        i = tempResult[2]
        if (i >= 10):
            print("The correct answer is " + str(L_cmp))
            break

    # ------------------------------------------------------------#

    print("A possible tighter lower bound than the Erdos'\n"
          "probabilistic method can be found here:\n"
          "https://jeremykun.com/2012/12/02/ramsey-number-lower-bound/\n"
          "It adopts the same probability idea and states\n"
          "that R(s,s) > n whenever s and n satisfy\n"
          "(n choose s)*2^(1-(s choose 2)) < 1.\n"
          "\n"
          "This lower bound is also only applicable to the\n"
          "diagonal Ramsey numbers. Given the above relation\n"
          "of s and n, what is the maximum n such that\n"
          "R(s,s) > n?\n")

    L_cmp = 0
    n = 0
    while (True):
        n += 1
        if (nCr(n, m) * 2 ** (1 - nCr(m, 2)) >= 1):
            L_cmp = n - 1
            break
    i = 0
    tempResult = (False, "ErrorType", i)
    while (not (tempResult[0])):
        L_usr = input("R(" + str(m) + "," + str(m) + ") > ")
        tempResult = usrInputCmp(L_cmp, L_usr, i)

        if (tempResult[1] == "tooLarge"):
            print("The entered value is larger than expected")
        elif (tempResult[1] == "tooSmall"):
            print("The entered value is smaller than expected")
        i = tempResult[2]
        if (i >= 10):
            print("The correct answer is " + str(L_cmp))
            break

    # usrInputCmp_old(s, t, m, L_cmp)

    print("However, I highly doubt the correctness of the\n"
          "above lower bound because in its proof, it is\n"
          "consciously fixing the location of K_s with respect\n"
          "to K_n, where a monochromatic K_s can appear\n"
          "elsewhere other than the location it is focusing\n"
          "on.\n")

    # ------------------------------------------------------------#

    # Constuctive lower bound:
    #   R(s,t+1) >= R(s,t)+2*s-2 for s >= 5, t >= 2

    print("A constructive lower bound on R(s,t) with distinct\n"
          "s and t can be found by applying the following\n"
          "formula iteratively:\n"
          "R(s,t+1) >= R(s,t)+2*s-2 for s >= 5, t >= 2\n"
          "which comes from this article:\n"
          "https://www.researchgate.net/publication/220533059\n"
          "_More_Constructive_Lower_Bounds_on_Classical_Ramsey_Numbers\n"
          "\n"
          "Recall that the given Ramsey number to be found is\n"
          "R(" + str(s) + "," + str(t) + ")\n")

    # Check if R(s,t) is one of the known Ramsey numbers
    L_temp = knownRst(min(s, t), max(s, t))
    if (L_temp != -1):
        print("R(" + str(s) + "," + str(t) + ") is known to be " + str(L_temp) + "\n")
        return (L_temp)

    # Select a known Ramsey number as base for iterations
    print("Now we need to select a known Ramsey number as a base\n"
          "for iterations. Remember that one of s and t needs to\n"
          "be greater than or equal to 5 while the other is greater\n"
          "than or equal to 2.\n")
    s_base = 0
    t_base = 0
    L_base = -1
    while (L_base == -1):
        s_base = int(input("s_base = "))  # Improvement: check input for robustness
        t_base = int(input("t_base = "))
        L_base = knownRst(min(s_base, t_base), max(s_base, t_base))
        if (L_base == -1):
            print("R(" + str(s_base) + "," + str(t_base) + ") is unknown\n"
                                                           "Try again\n")

    print("For convience, we will arrange R(s,t) in the form of\n"
          "R(min(s,t), max(s,t))\n")
    s_temp = s
    s = min(s, t)
    t = max(s_temp, t)
    s_baseTemp = s_base
    s_base = min(s_base, t_base)
    t_base = max(s_baseTemp, t_base)
    print("The lower bound we want to find for is R(" + str(s) + "," + str(t) + ")\n"
                                                                                "We know R(" + str(s_base) + "," + str(
        t_base) + ") = " + str(L_base) + "\n")

    iteList = ramseyLB_ite(s, t, s_base, t_base, L_base)
    L_cmp = iteList[-1][-1]

    return (L_cmp)


def usrInputCmp(L_cmp, L_usr, i):
    # Compares users result with cmpt result
    # Purpose is to let users try the calculation
    # Input L_cmp is computer result
    # Input L_usr is user result
    # Input i is a counter for wrongAnswers
    # Output is a tuple (boolean, errorType)

    try:
        L_usr = int(L_usr)
    except(ValueError):
        print("The bound should be a positive integer\n"
              "Try again")
        return (False, "ValueError", i)

    # Compare user ans with cmpt ans
    if (L_usr == L_cmp):
        print(str(L_usr) + " is correct\n")
        return (True, "NoError", i)

    else:
        i += 1
        print("Try again")
        if (L_usr > L_cmp):
            return (False, "tooLarge", i)
        else:
            return (False, "tooSmall", i)


def usrInputCmp_old(s, t, m, L_cmp, L_usr):
    # Compares users result with cmpt result
    # Purpose is to let users try the calculation
    # Input is cmpt result L_cmp
    # No output

    L_usr = 0
    i = 0
    while (True):
        # Let user input an int
        while (True):
            try:
                L_usr = int(input("R(" + str(m) + "," + str(m) + ") > "))
                break
            except(ValueError):
                print("The bound should be a positive integer\n"
                      "Try again")

        # Compare user ans with cmpt ans
        if (L_usr == L_cmp):
            print(str(L_usr) + " is correct\n")
            break

        i += 1
        print("Try again")

        # Show ans after 6 failures
        if (i == 6):
            print("The lower bound is " + str(L_cmp) + "\n")
            break

    return


def knownRst(s, t):
    # Input s is the smaller value min(s,t)
    # Input t is the larger value max(s,t)
    # Output -1 if unknown

    if (s == 1):
        return 1
    if (s == 2):
        return t

    if (s == 3 and t == 3):
        return 6
    if (s == 3 and t == 4):
        return 9
    if (s == 3 and t == 5):
        return 14
    if (s == 3 and t == 6):
        return 18
    if (s == 3 and t == 7):
        return 23
    if (s == 3 and t == 8):
        return 28
    if (s == 3 and t == 9):
        return 36

    if (s == 4 and t == 4):
        return 18
    if (s == 4 and t == 5):
        return 25

    return -1


def ramseyLB_ite(s, t, s_base, t_base, L_base):
    # Start the iteration here
    # Iterative condition:  s_base < s or t_base < t
    # Ending condition:     s_base = s and t_base = t
    # Incremental steps:
    #           if s < 5, increment s_base, update L_base
    #           for odd steps, increment s_base, update L_base
    #               if s_base == s, increment t_base, update L_base
    #           for even steps, increment t_base, update L_base
    #               if t_base == t, increment s_base, update L_base
    #   R(s,t+1) >= R(s,t)+2*s-2 for s >= 5, t >= 2s
    # Output is a two_dimensional list

    iteList = []
    loopNum = 0
    while ((s_base < s) or (t_base < t)):
        loopNum += 1
        if (s_base < 5):
            # increment s_base
            L_base = L_base + 2 * t_base - 2
            s_base += 1
            print(str(loopNum) + ": R(" + str(s_base) + "," + str(t_base) + ")>=" + str(L_base))
            iteList.append([loopNum, s_base, t_base, L_base])
            continue

        if (loopNum % 2 == 1):
            # odd steps
            if (s_base < s):
                # increment s_base
                L_base = L_base + 2 * t_base - 2
                s_base += 1

            else:
                # increment t_base
                L_base = L_base + 2 * s_base - 2
                t_base += 1

        else:
            # even steps
            if (t_base < t):
                # increment t_base
                L_base = L_base + 2 * s_base - 2
                t_base += 1

            else:
                # increment s_base
                L_base = L_base + 2 * t_base - 2
                s_base += 1

        print(str(loopNum) + ": R(" + str(s_base) + "," + str(t_base) + ")>=" + str(L_base))
        iteList.append([loopNum, s_base, t_base, L_base])

    return (iteList)


if __name__ == "__main__":
    print("Test on finding the lower bound of R(s,t)")
    s = 10
    t = 12
    L = 1
    L = lowerBound(s, t)
    print("Inputs are " + str(s) + " and " + str(t))
    print("Output is " + str(L))