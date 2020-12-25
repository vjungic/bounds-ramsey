import math
import time


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


def timeEstimate(U, L, s, t):
    # Inputs: U and L are bounds, s and t are for R(s,t)
    start = time.time()
    totCnt = 0  # exponent of total cnt with base 2
    stpCnt = 0  # exponent of step cnt with base 2
    n = U
    nextSig = True  # K_(n-1)'s time is significant
    while (n >= L):
        tempResult = operationCnt(n, s, t)
        print("The complete graph K_" + str(n) + " has " + str(tempResult[0]) + " edges.\n"
                                                                                "The number of 2-colorings is then 2^" + str(
            tempResult[0]) + ".\n"
                             "For each coloring, " + str(tempResult[1]) + " edge color comparisons\n"
                                                                          "are done to check if a monochromatic K_" + str(
            s) + " or K_" + str(t) +
              " exists.")
        stpCnt = tempResult[0] + math.log(tempResult[1], 2)
        if (totCnt == 0):
            totCnt = stpCnt
            print("Update total count")
            totCnt = stpCnt + math.log(2 ** (totCnt - stpCnt) + 1, 2)
            print("Current totCnt: 2^" + str(totCnt))
        else:
            # Assuming totCnt > stpCnt
            if (totCnt - stpCnt > 30):
                print("Total count is dominating the current step count\n"
                      "The ratio totCnt/stpCnt > 2^30\n"
                      "Total count is not updated\n"
                      "Current totCnt: 2^" + str(totCnt))
                nextSig = False
                print("All the rest step counts won't be significant.\n"
                      "Exiting the counting loop.\n")
                break
            else:
                print("Update total count")
                totCnt = stpCnt + math.log(2 ** (totCnt - stpCnt) + 1, 2)
                print("Current totCnt: 2^" + str(totCnt))
        n = n - 1
        print('')

    t_sec = cntToTime(totCnt)  # exponent with unit in seconds
    t_yrs = t_sec - 24.9  # exponent with unit in years

    print("Hence, the estimated time in seconds is 2^" + str(t_sec) + ",\n"
                                                                      "and that is equivalent to 2^" + str(
        t_yrs) + " years.")
    end = time.time()
    print("Hence the real process time for above example in the CPU is", str(end - start), "in seconds")
    return t_sec


def operationCnt(n, s, t):
    # Input: n for graph K_n
    # Input: s, t for subgraphs K_s and K_t
    # Output: (edgeNum,K_st_cnt), where the actual number count is
    #   2^edgeNum * K_st_cnt
    # The return is an estimation on the number of operation required
    #   to go through every coloring of K_n

    # Express the number of 2-colorings of K_n
    edgeNum = nCr(n, 2)

    # To check if a coloring of K_n has a monochromatic K_s, select s
    # vertices from K_n and check if all edges are of the same color.
    # The operation count here would be the number of K_s in K_n
    # times the edge number in each K_s
    K_s_cnt = nCr(n, s) * nCr(s, 2)
    K_t_cnt = nCr(n, t) * nCr(t, 2)
    K_st_cnt = K_s_cnt + K_t_cnt

    return (edgeNum, K_st_cnt)


def cntToTime(cnt):
    # Input: cnt for operation count
    # Output: t for time in seconds
    # Both are exponents of base 2
    K = 28.9
    # conversion factor: 2^K operations per second
    # Here, we are assuming 5*10^8 ops per second
    return (cnt - K)


if __name__ == "__main__":
    print("Test on doing a time estimation")
    # For example
    # U = 15
    # L = 6
    # s = 7
    # t = 4
    U = int(input("Please input your Upper bounds for R(s,t) : "))
    L = int(input("Please input your Lower bounds for R(s,t) : "))
    s = int(input("PLease input your s value for R(s,t) : "))
    t = int(input("Please input your t value for R(s,t) : "))
    estmT = timeEstimate(U, L, s, t)
    print("Inputs are U=" + str(U) + " and L=" + str(L))
    print("Output is estmT=2^" + str(estmT) + " in sec")