# The  conclusion of Ramsey Theorem
def conclusion():
    print("Great! You have got the basic idea of Ramsey's Theorem.\n"
          "\n"
          "Since we have learned how to calculate\n"
          "the upper bound and lower bound of Ramsey Number\n"
          "and the time estimation of calculating bounds in 2-colour case.\n"
          "Nowadays, there are still many Ramsey numbers that human can not calculate\n"
          "due to limited computational ability.\n"
          "For example, as for a K100 complete graph, there are C(100, 2) = 4950 edges.\n"
          "In 2-color case, each edge has two choices of coloring.\n"
          "We need to calculate 2^4950 possible ways to find it.\n"
          "It is a really huge number compared to approximate 10^78 to 10^82 atoms in the universe.\n"
          "\n")

    print("Actually, Ramsey's Theorem is not formed by Ramsey himself.\n"
          "British mathematician Frank Ramsey pubulished his paper 'On a Problem of Formal Logic'\n"
          "presenting the initial version: 'Given any r, n, and mu we can find an m0 such that,\n"
          "if m >= m0 and the r-combinations of any gamma(m) are divided\n"
          "in any manner into mu mutually exclusive classes Ci (i = 1, 2, ... ,mu),\n"
          "then gamma(m) must contain a sub-class delta(n) such that\n"
          "all the r-combinations of members of delta(n) belong to the same Ci.'\n"
          "\n"

          "After that, Ramsey's Theory has been shaping throughout the 1970s\n"
          "from new results and two surveys by Graham and Rothschild.\n"
          "In 1980, the book 'Ramsey Theory'\n"
          "by Graham, Rothschild, and Spencer assured the name of theorem.\n"
          "The Ramsey's Theory finally completed in 1972\n"
          "at the Combinatorial Conference at Balatonfüred, Hungary, 1973\n"
          "with the great work of Paul Erdos and other mathematicians.\n")

    print("Ramsey's Theorem does not only focus on 2-color case,\n"
          "Ramsey's Theorem also works in infinite graphs.\n"
          "When it applies to infinite graphs, it also named as 'Infinite Ramsey theorem'.\n"
          "The theorem states as follows:\n"
          "Let X be some infinite set and colour the elements of X(n) (the subsets of X of size n) in c different colours.\n"
          "Then there exists some infinite subset M of X such that the size n subsets of M all have the same colour.\n"
          "\n.")


if __name__ == "__main__":
    conclusion()