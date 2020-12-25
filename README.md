# MATH303_Ramsey_App


##Running requirements:
    Python 3
    Python Flask package
You can use pip to install flask by
```bash
pip install flask
```
   
##Usage:
To generate and view the tutorial webpage, please go to webapp directory
```bash
python testMain.py
```
Then you can open browser and access the generated ip address. By default, it should be http://127.0.0.1:5000/

During the tutorial, please refrain from going backwards. If you want to go to previous page, please click the home icon on the topleft corner and start from the begining step.

## Content
Math 303 term project: An app related to Ramsey's Theorem

Ramsey's theorem states that for any integer s and t greater than 2, there exists a finite n such that R(s,t) = n, that
for any 2-coloring of the edges of K_n, we can always find a monochromatic K_s or a K_t.

The following lists some ideas on how to integrate the theorem into an app.

Introduction:

  The introduction should serve as an educational part of the program. Users will learn what Ramsey's theorem is and
what they would expect from the program.
  - Prompt the general statement of Ramsey's Theorem
  - Provide a specific example of 2-coloring on a complete graph, e.g. R(3,3)=6
  - Prompt an overview of the program

Part 1: Inducing an upper bound

  Part 1 shows users how to find an upper bound of the Ramsey number N such that R(s,t)</=N. It first gives an example
on how an induction on Ramsey number works, then it lets users to try on their own.
  - Prompt a general statement addressing the upper bound of Ramsey numbers
  - Provide an example on finding an upper bound by induction, e.g. R(3,4)=9 --> R(4,4)</=18
  - Let users input values for s and t and guide users to find a N such that R(s,t)</=N

Part 2: Reducing the upper bound

  Part 2 is an extension of part 1 where it attempts to use certain techniques to reduce the upper bound of a Ramsey
number.

Part 3: Providing a lower bound
  
  Given that the lower bound of R(s,s) is 2^(s/2) for s >/= 3, can we find a lower bound for R(s,t)?
  - Provide users with the information that R(s,s)>2^(s/2) and it was proved by Paul Erdos
  - Deliver the idea on determining the probability of not finding a monochromatic K_s in K_n is more than 0, that the
    existance of a coloring of K_n with no monochromatic K_s is certain
  - Attempt to find a lower bound for R(s,t), t>s

Part 4: Estimate the machine testing time

  The previous parts have given an upper bound and a lower bound for a Ramsey number R(s,t) with users provided inputs
s and t. Part 4 estimates the order of the time required for a laptop PC to determine the exact Ramsey number n. The
algorithm on finding n is assumed as check by each coloring cases disregarding homomorphism.

Part 5: Conclusion

  Part 5 concludes the program by listing details of the known Ramsey numbers.



