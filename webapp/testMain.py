from flask import Flask, render_template, request
import Ramsey_lower_bound as RL
import Ramsey_upper_bound as RU
import math
app = Flask(__name__, static_folder='./styles')
s = 10
m = 10
t = 10
trial_times = 0
max_times = 3

paragraphs = ["Welcome to the journey of Ramsey theorem!\r\n"
"What is Ramsey theorem?"]

titles = ["Introduction", "Finding the Lowerbound", "Finding the Upperbound", "Conclusion"]
functionnames = ["/intro","/pigeon", "/introfin","/function1", "/function2", "/function3", "/function4", "/function5", "/function6", "/function7", "/function8", "/function9"]
comments = ["a12", "2", "3", "4"]

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

pagenum = 0


@app.route("/")
@app.route("/index")
@app.route("/back_to_home", methods=['POST'])
def home():
    global pagenum
    pagenum = 0
    options = ["The mathematics of coloring", "The study of the preservation of properties under set partitions"
               , "The order in chaos", "A science of the stubbornness of patterns"]
    titles = ["Introduction", "Finding the Lowerbound", "Finding the Upperbound", "Conclusion"]
    functionnames = ["/intro", "/pigeon", "/introfin", "/function1", "/function2", "/function3", "/function4",
                     "/function5", "/function6", "/function7", "/function8", "/function9"]
    return render_template("ramsey.html", functionname = functionnames[pagenum], pagenum = pagenum,
                           paragraph = paragraphs[pagenum], title = titles[0], options=options)

@app.route('/intro', methods=['POST'])
def intro():
    result = request.form
    global pagenum;
    pagenum = pagenum + 1
    paragraphs.append("ALL! To understand Ramsey theorem Let us focus on some basic concepts of Ramsey theorem: If we have 3 pigeonholes and 4 pigeons,can we just have at most one pigeon in each pigeonhole?"+"\r\n")
    options = ["YES", "NO"]
    return render_template("ramsey.html", functionname = functionnames[pagenum], pagenum = pagenum,
                           paragraph = paragraphs[pagenum], title = titles[0], options=options)

@app.route('/pigeon', methods=['POST'])
def pigeon():
    result = request.form
    global pagenum, trial_times, max_times;
    if result["option"] == "B":
        paragraphs.append("Now, let us come to the Pigeonhole Princle:"+
"For k pigeonholes and n pigeons,"+
"if n > k, then at least one pigeonhole contains at least two pigeons."+
"As for the complete graph"+
"It is a simple undirected graph"+
"every pair of distinct vertices is connected by a unique edge."+
"In short, every two distinct points are connected by an edge in complete graph."+
"For example, the flag of England is the complete graph of K4"+"\r\r\n"+
"Now we comes to A Dinner Party Problem."+
"uppose that six people are gathered at a dinner party."+
"Then there is a group of three people at the party"+
"who are either all mutual acquaintances or all mutual strangers."+
"Magic? That is the magic of Ramsey Theorem!"+
"The Ramsey number, in this party problem, shows the minimum number of guests"+
"either m mutual acquaintances or n mutual strangers in this party"+
"denoted as R(m,n)."+
"From the example we know that R(3,3) is 6."+"\r\r\n"+
"Then we focus on Ramsey Theorem in 2-coloring,"+
"take blue and red color for example,"+
"Let r and s be any two positive integers"+
"Ramsey theorem states that there exists a least positive integer R(r, s)"+
"for which every blue-red edge colouring of the complete graph on R(r, s) vertices"+
"contains a blue clique on r vertices or a red clique on s vertices"+
"That is a brief introduction of Ramsey Theorem")
        pagenum = pagenum + 1
        trial_times = 0
        return render_template("ramsey.html", functionname = functionnames[pagenum], pagenum = pagenum,
                           paragraph = paragraphs[pagenum], title = titles[0])
    elif trial_times < max_times:
        trial_times += 1
        return render_template("ramsey.html", functionname=functionnames[pagenum], pagenum=pagenum,
                               paragraph=paragraphs[pagenum], title=titles[0],
                               comment="Your answer is incorrect, please try again", options = ["YES", "NO"])
    else:
        trial_times = 0
        return render_template("ramsey.html", functionname=functionnames[pagenum], pagenum=pagenum,
                               paragraph=paragraphs[pagenum], title=titles[0],
                               comment="Correct answer is B", options=["YES", "NO"])

@app.route('/introfin', methods=['POST'])
def introfin():
    global pagenum;
    pagenum = pagenum + 1
    paragraphs.append("Now you can write two intergers s an t, and start your journey of the Ramsey Theorem!")

    return render_template("ramsey.html", functionname = functionnames[pagenum], pagenum = pagenum,
                           paragraph = paragraphs[pagenum], title = titles[1], labels=["s = ", "t = "])


@app.route('/function1', methods=['POST'])
def function1():
    result = request.form
    global pagenum, s, t, m;
    s = int(result["fillbox1"])
    t = int(result["fillbox2"])
    m = min(s,t)
    pagenum = pagenum + 1
    paragraphs.append("A lower bound on the diagonal Ramsey numbers R(s,s) was obtained by Paul Erdos using the probabilistic method. He showed that for K_n where" +
                      " n = 2^(s/2), any two-coloring on the edges of K_n will generate at least one K_s with a probability less than one. It is the same as saying the probability of having no monochromatic K_s in K_n is greater than 0, that it is certain that some colorings of K_n give no monochromatic K_s."+"\r\n"+
                      "Knowing R(s,s) < R(s,t) for s < t, we are certain that R(" + str(s) + "," + str(t) + ") < R(" + str(m) + ","+ str(m) + "). "
                      +"Given the lower bound on the diagonal Ramsey numbers is R(s,s) > 2^(s/2), lets find a lower bound for R(" + str(m) + "," + str(m) + "), which also bounds R(" + str(s) + "," + str(t) + ")."+"\r\n")

    return render_template("ramsey.html", functionname = functionnames[pagenum], pagenum = pagenum,
                           paragraph = paragraphs[pagenum], title = titles[1], s=s, t=t, m=m, labels=["lowerbound="])

@app.route('/function2', methods=['POST'])
def function2():
    result = request.form
    userResult = int(result["fillbox1"])
    global pagenum,m, trial_times, max_times
    L_cmp = math.floor(2 ** (m / 2))
    print(L_cmp)
    if (userResult != L_cmp):
        if trial_times < max_times:
            trial_times += 1
            if userResult < L_cmp:
                return render_template("ramsey.html", functionname=functionnames[pagenum], pagenum=pagenum,
                                       paragraph=paragraphs[pagenum], title=titles[1],
                                       comment="Your answer is too small, please try again", labels=["lowerbound="])
            else:
                return render_template("ramsey.html", functionname=functionnames[pagenum], pagenum=pagenum,
                                       paragraph=paragraphs[pagenum], title=titles[1],
                                       comment="Your answer is too big, please try again", labels=["lowerbound="])
        else:
            trial_times = 0
            return render_template("ramsey.html", functionname=functionnames[pagenum], pagenum=pagenum,
                                   paragraph=paragraphs[pagenum], title=titles[1],
                                   comment="Correct answer is " + str(L_cmp) + ", please try again", labels=["lowerbound="])
    else:
        pagenum = pagenum + 1
        trial_times = 0
        print(pagenum)
        paragraphs.append("A possible tighter lower bound than the Erdos' probabilistic method can be found here: https://jeremykun.com/2012/12/02/ramsey-number-lower-bound/"+"\n"+
          "It adopts the same probability idea and states that R(s,s) > n whenever s and n satisfy "+"\r\n"+
          "(n choose s)*2^(1-(s choose 2)) < 1."+"\n"+
          "This lower bound is also only applicable to the diagonal Ramsey numbers. Given the above relation of s and n, what is the maximum n such that"+"\n"+
          "R(s,s) > n?"+"\r\n")
        return render_template("ramsey.html", functionname=functionnames[pagenum], pagenum=pagenum,
                               paragraph=paragraphs[pagenum], title=titles[1], labels=["n ="])

@app.route('/function3', methods=['POST'])
def function3():
    global pagenum, m, trial_times, max_times
    result = request.form
    userResult = int(result["fillbox1"])
    L_cmp = 0
    n = 0
    while (True):
        n += 1
        if (nCr(n, m) * 2 ** (1 - nCr(m, 2)) >= 1):
            L_cmp = n - 1
            break

    print(L_cmp)
    if (userResult != L_cmp):
        if trial_times < max_times:
            trial_times += 1
            if userResult < L_cmp:
                return render_template("ramsey.html", functionname=functionnames[pagenum], pagenum=pagenum,
                                       paragraph=paragraphs[pagenum], title=titles[1],
                                       comment="Your answer is too small, please try again", labels=["n ="])
            else:
                return render_template("ramsey.html", functionname=functionnames[pagenum], pagenum=pagenum,
                                       paragraph=paragraphs[pagenum], title=titles[1],
                                       comment="Your answer is too big, please try again", labels=["n ="])
        else:
            trial_times = 0
            return render_template("ramsey.html", functionname=functionnames[pagenum], pagenum=pagenum,
                                   paragraph=paragraphs[pagenum], title=titles[1],
                                   comment="Correct answer is " + str(L_cmp) + ", please try again", labels=["n ="])

    else:
        pagenum = pagenum + 1
        trial_times = 0
        paragraphs.append("However, I highly doubt the correctness of the above lower bound because in its proof, it is consciously fixing the location of K_s with respect to K_n, where a monochromatic K_s can appear elsewhere other than the location it is focusing on. A constructive lower bound on R(s,t) with distinct s and t can be found by applying the following formula iteratively:"+"\n"+
          "R(s,t+1) >= R(s,t)+2*s-2 for s >= 5, t >= 2"+"\n"+
          "which comes from this article:"+"\n"+
          "https://www.researchgate.net/publication/220533059"+"\n"+
          "_More_Constructive_Lower_Bounds_on_Classical_Ramsey_Numbers"+"\r\r\n"+
          "Recall that the given Ramsey number to be found is"+
          "R(" + str(s) + "," + str(t) + ")"+"\n"+
          "Now we need to select a known Ramsey number as a base for iterations. Remember that one of s and t needs to be greater than or equal to 5 while the other is greater than or equal to 2."+"\r\n")
        return render_template("ramsey.html", functionname=functionnames[pagenum], pagenum=pagenum,
                               paragraph=paragraphs[pagenum], title=titles[1], labels=["s_base =", "t_base ="])

@app.route('/function4', methods=['POST'])
def function4():
    result = request.form
    global pagenum, s, t, m;
    s_base = int(result["fillbox1"])  # Improvement: check input for robustness
    t_base = int(result["fillbox2"])
    print(s_base)
    L_base = RL.knownRst(min(s_base, t_base), max(s_base, t_base))
    if (L_base == -1):
        return render_template("ramsey.html", functionname=functionnames[pagenum], pagenum=pagenum,
                               paragraph=paragraphs[pagenum], title=titles[1],
                               comment="R(" + str(s_base) + "," + str(t_base) + ") is unknown"+"\r\n"+
                                                           "Try again"+"\r\n", labels=["s_base =", "t_base ="])
    else:
        iteList = RL.ramseyLB_ite(s, t, s_base, t_base, L_base)
        pagenum = pagenum + 1
        text = ""
        for it in iteList:
            text += str(it[0]) + ": R(" + str(it[1]) + "," + str(it[2]) + ")>=" + str(it[3]) +"\r\n"
        paragraphs.append(text)
        return render_template("ramsey.html", functionname=functionnames[pagenum], pagenum=pagenum,
                               paragraph=paragraphs[pagenum], title=titles[1])

@app.route('/function5', methods=['POST'])
def function5():
    global pagenum, s, t, m;
    paragraphs.append("A upper bound on the Ramsey numbers R(s,t) was obtained by double induction on s and t."+"\n"+
          "Since we have observed the relationship between R(s,t) and R(s-1,t), R(s, t-1)."+"\n"+
          "Such that: R(s,t) <= R(s-1,t) + R(s,t-1)"+"\n"+
          "Then apply the double induction assuming R(s,t) <= C(s+t-2, t-1) works for all s+t = n."+"\n"+
          "Since R(s-1,t) <= C(s+t-2, t-1) = C(n-2, t-1) and R(s,t-1) <= C(s+t-2, t-2) = C(n-2, t-2)."+"\n"+
          "Applying Pascal's rule: C(n-2, t-1) + C(n-2, t-2) = C(n-1, t-1) which proves that R(s,t) <= R(s-1,t) + R(s,t-1) <= C(n-2, t-1) + C(n-2, t-2) = C(n-1, t-1). then it also works for s+t= n+1."+"\n"+
          "Take R("+str(s)+","+str(t)+") for example."+"\n"+
          "Given R(s,t) <= R(s-1,t) + R(s,t-1)"+"\n"+
          "To find upper bound of R(s,t)"+"\n"+
          "Which two Ramsey numbers should we use?"+"\r\n")
    pagenum = pagenum + 1
    options = ["R("+str(s)+","+str(t)+")", "R("+str(s-1)+","+str(t)+")", "R("+str(s)+","+str(t-1)+")", "R("+str(s-1)+","+str(t-1)+")"]
    return render_template("ramsey.html", functionname=functionnames[pagenum], pagenum=pagenum,
                           paragraph=paragraphs[pagenum], title=titles[2], options=options)

@app.route('/function6', methods=['POST'])
def function6():
    global pagenum, s, t, m;
    result = request.form
    print(result)
    if "B" in result and "C" in result:
        paragraphs.append("Then we take one step further"+"\n"+
            "Select combinations in order to calculate the upper bound of R("+str(s)+","+str(t)+")"+"\n"+
            "Which two combinations we should use?"+"\r\n")
        pagenum = pagenum + 1
        options = ["C("+str(s+t-1)+","+str(t-2)+")   C("+str(s+t-1)+","+str(t-1)+")",
                   "C("+str(s+t-1)+","+str(t-2)+")   C("+str(s+t-1)+","+str(t-2)+")",
                   "C("+str(s+t-1)+","+str(t-2)+")   C("+str(s+t-1)+","+str(t-1)+")",
                   "C("+str(s+t-2)+","+str(t-1)+")   C("+str(s+t-2)+","+str(t-2)+")"]
        return render_template("ramsey.html", functionname=functionnames[pagenum], pagenum=pagenum,
                           paragraph=paragraphs[pagenum], title=titles[2], options=options)
    else:
        options = ["R(" + str(s) + "," + str(t) + ")", "R(" + str(s - 1) + "," + str(t) + ")",
                   "R(" + str(s) + "," + str(t - 1) + ")", "R(" + str(s - 1) + "," + str(t - 1) + ")"]
        return render_template("ramsey.html", functionname=functionnames[pagenum], pagenum=pagenum,
                               paragraph=paragraphs[pagenum], title=titles[2], comment="Please try again.", options=options)

@app.route('/function7', methods=['POST'])
def function7():
    global pagenum, s, t, m;
    result = request.form
    if result["option"] == "D":
        paragraphs.append("Here we have known where to find the upper bound of R(s,t)."+"\r\n"+
          "Now to calculate the upper bound of R("+str(s)+","+str(t)+")"+"\r\n"+
          "Here are some results of combinations:"+"\r\n"+
          
          "C("+str(s+t-1)+","+str(t-3)+"): "+str(nCr(s+t-1, t-3))+"\n"+
          "C("+str(s+t-2)+","+str(t-2)+"): "+str(nCr(s+t-2, t-2))+"\n"+
          "C("+str(s+t-2)+","+str(t-3)+"): "+str(nCr(s+t-1, t-3))+"\n"+
          "C("+str(s+t-2)+","+str(t-1)+"): "+str(nCr(s+t-2, t-1))+"\r\n"+

          "Calculate the upper bound of R("+str(s)+","+str(t)+")"+"\n"+
          "And Write down your answer below:"+"\r\n")
        pagenum = pagenum + 1
        return render_template("ramsey.html", functionname=functionnames[pagenum], pagenum=pagenum,
                           paragraph=paragraphs[pagenum], title=titles[2], labels=["upperbound="])
    else:
        options = ["C("+str(s+t-1)+","+str(t-2)+")   C("+str(s+t-1)+","+str(t-1)+")",
                   "C("+str(s+t-1)+","+str(t-2)+")   C("+str(s+t-1)+","+str(t-2)+")",
                   "C("+str(s+t-1)+","+str(t-2)+")   C("+str(s+t-1)+","+str(t-1)+")",
                   "C("+str(s+t-2)+","+str(t-1)+")   C("+str(s+t-2)+","+str(t-2)+")"]
        return render_template("ramsey.html", functionname=functionnames[pagenum], pagenum=pagenum,
                               paragraph=paragraphs[pagenum], title=titles[2], comment="Please try again.", options=options)


@app.route('/function8', methods=['POST'])
def function8():
    global pagenum, s, t, m, trial_times, max_times;
    result = request.form
    userInput = int(result["fillbox1"])
    correctAnswer = nCr(s+t-2, t-1) + nCr(s+t-2, t-2)
    print(correctAnswer)
    if userInput == correctAnswer:
        paragraphs.append("You have understood how to calculate upper bound of Ramsey Number."+"\r\n"
                    "Congradulations!"+"\r\n")
        pagenum = pagenum + 1
        trial_times = 0
        return render_template("ramsey.html", functionname=functionnames[pagenum], pagenum=pagenum,
                               paragraph=paragraphs[pagenum], title=titles[2])
    elif trial_times < max_times:
        trial_times += 1
        if userInput < correctAnswer:
            return render_template("ramsey.html", functionname=functionnames[pagenum], pagenum=pagenum,
                                   paragraph=paragraphs[pagenum], title=titles[2], comment="Your answer is too small. Please try again.", labels=["upperbound="])
        else:
            return render_template("ramsey.html", functionname=functionnames[pagenum], pagenum=pagenum,
                                   paragraph=paragraphs[pagenum], title=titles[2],
                                   comment="Your answer is too big. Please try again.", labels=["upperbound="])
    else:
        trial_times = 0
        return render_template("ramsey.html", functionname=functionnames[pagenum], pagenum=pagenum,
                               paragraph=paragraphs[pagenum], title=titles[2],
                               comment="Correct answer is " + str(correctAnswer) + ". Please try again.", labels=["upperbound="])



@app.route('/function9', methods=['POST'])
def function9():
    global pagenum
    paragraphs.append("Great! You have got the basic idea of Ramsey's Theorem."+"\r\n"+
          "Since we have learned how to calculate the upper bound and lower bound of Ramsey Number and the time estimation of calculating bounds in 2-colour case."+"\r\n"+
          "Nowadays, there are still many Ramsey numbers that human can not calculate due to limited computational ability."+"\r\n"+
          "For example, as for a K100 complete graph, there are C(100, 2) = 4950 edges. In 2-color case, each edge has two choices of coloring. We need to calculate 2^4950 possible ways to find it. It is a really huge number compared to approximate 10^78 to 10^82 atoms in the universe."+"\n"+
          "Actually, Ramsey's Theorem is not formed by Ramsey himself."+"\n"+
          "British mathematician Frank Ramsey pubulished his paper 'On a Problem of Formal Logic' presenting the initial version: 'Given any r, n, and mu we can find an m0 such that, if m >= m0 and the r-combinations of any gamma(m) are divided in any manner into mu mutually exclusive classes Ci (i = 1, 2, ... ,mu), then gamma(m) must contain a sub-class delta(n) such that all the r-combinations of members of delta(n) belong to the same Ci."+"\r\n"+

          "After that, Ramsey's Theory has been shaping throughout the 1970s from new results and two surveys by Graham and Rothschild. In 1980, the book 'Ramsey Theory' by Graham, Rothschild, and Spencer assured the name of theorem. The Ramsey's Theory finally completed in 1972 at the Combinatorial Conference at Balatonfüred, Hungary, 1973 with the great work of Paul Erdos and other mathematicians. Ramsey's Theorem does not only focus on 2-color case, Ramsey's Theorem also works in infinite graphs. When it applies to infinite graphs, it also named as 'Infinite Ramsey theorem. The theorem states as follows:"+"\n"+
          "Let X be some infinite set and colour the elements of X(n) (the subsets of X of size n) in c different colours."+"\n"+
          "Then there exists some infinite subset M of X such that the size n subsets of M all have the same colour."+"\r\n"+"\r\n"+
                      "Thank you for using our web!")
    pagenum = pagenum + 1
    return render_template("ramsey.html", functionname="finish", pagenum=pagenum,
                               paragraph=paragraphs[pagenum], title=titles[3])
if __name__ == '__main__':
    app.run()