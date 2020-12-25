# import Ramsey_upper_bound
import Ramsey_lower_bound
import Ramsey_Conclusion
import math

def sectionTrans(sectionNum):
    # Increment sectionNum with <n> for next
    # Decrement sectionNum with <p> for previous

    transChr = "a"

    print("Please enter <n> for next and <p> for previous\n"
          "Then follow your entry with <Enter>")

    while ((transChr != "n") and (transChr != "p")):
        transChr = input("Entry: ")

        if ((transChr != "n") and (transChr != "p")):
            print("Please enter <n> for next and <p> for previous\n"
                  "Try again")

    if (transChr == "n"):
        sectionNum += 1
    else:
        sectionNum -= 1

    return sectionNum


if __name__ == "__main__":
    # The main function needs to implement the following feature
    # Pressing a key <n> goes to the next section
    # Pressing a key <p> goes to the previous section

    print("Start of the main function")

    s = 0  # User provided s as part of R(s,t)
    t = 0  # User provided t as part of R(s,t)
    U = 0  # Calculated upper bound
    L = 0  # Calculated lower bound

    sectionNum = 1

    while (sectionNum < 10):
        if (sectionNum < 1):
            sectionNum = 1
            continue

        elif (sectionNum == 1):
            # Introduction
            print("Introduction section")

            # values for s and t are updated, below are tentative
            s = 7
            t = 9

            sectionNum = sectionTrans(sectionNum)
            continue

        elif (sectionNum == 2):
            # Section for Upper Bound
            print("Section for Upper Bound")

            sectionNum = sectionTrans(sectionNum)
            continue

        elif (sectionNum == 3):
            # Section for Lower Bound
            print("Section for Lower Bound")

            L = Ramsey_lower_bound.lowerBound(s, t)

            sectionNum = sectionTrans(sectionNum)
            continue

        elif (sectionNum == 4):
            # Section for Time Estimation
            print("Section for Time Estimation")

            sectionNum = sectionTrans(sectionNum)
            continue

        elif (sectionNum == 5):
            # Conclusion
            print("Conclusion")

            Ramsey_Conclusion.conclusion()

            sectionNum = sectionTrans(sectionNum)
            continue

        else:
            print("End of program")
            break
