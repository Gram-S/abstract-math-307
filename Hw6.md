### Exercise 3.2
**Determine if the following are propositions or not.**

**Proposition.** All cars are red.

Proposition because its always False. 2025 Toyota RAV4 & RAV4 Hybrid is a car of the color blue.

**(b)** Every person whose name begins with J has the name Joe.

Proposition because its always False. Josh is a persons name which starts with J but is not the word Joe.

**(c)** $x^2 = 4.$ 

Not a proposition. We do not know what $x$ is (integer, real number, etc). 

Note: I am not sure I buy $x=1$ is not a proposition, though I definitely think that $x^2  = 4$ is a proposition (maybe contextually? Like $x = 2$ is an equivalent expression which I would say is ALWAYS proposition because it is a declarative statement, like 'this car is red'.) Perhaps this is a double standard? Otherwise, we could not say $x^2 = 4$ is true for $x = 2$, because $x = 2$ is not always true? 

**(d)** There exists an x such that $x^2 = 4.$

Proposition because always true. $2$ is something that exists, therefore $x = 2$ makes the equation true.

**(e)** For all real numbers $x, x^2 = 4$.

Proposition because always false. $X = 3$, since $3$ is a real number and the equation is false, not true for all. 

**(f)** √2 is an irrational number.

I think always true. I don't know what an irrational number is but that is not an integer or a nice (finite?) decimal and that seems pretty irrational to me. 

**(g)** p is prime.

False. $p$ is a letter.

**(h)** Led Zeppelin is the best band of all time

Can be either depending on how you define 'best'. For example, if it is a numeric metric then you can show the statement is always true. But since this term is generally used in a subjective way, I'd say this is an opinion which are never true nor false.  



### Exercise 3.6

**Describe the meaning of ¬(A ∧ B) and ¬(A ∨ B).**

The opposite of the conjunction of A and B.

Not (A and B).

The opposite of the disjunction of A and B.

Not (A or B).



### Exercise 3.7 

**Let A represent “6 is an even number” and B represent “6 is a multiple of 4.”
First, explain why A and B are statements. Then, express each of the following statements in
ordinary English sentences. Which of these statements are true? Why?**

By *Def 2.1*, statement A is true because $6$ is even because $6 = 2(3)$. Statement $B$ is false because $\frac{6}{4} \notin \Z$.

**(a)** A ∧ B

6 is an even number and 6 is a multiple of 4.

**(b)** A ∨ B

6 is either an even number or a multiple of 4.

**(c)** ¬A

$6$ is NOT an even number.

**(d)** ¬B

$6$ is NOT a multiple of $4$.
    
**(e)** ¬(A ∧ B)
   
$6$ is either NOT an even number, NOT a multiple of $4$, or both NOT an even number and NOT a multiple of $4$.

**(f)** ¬(A ∨ B)

$6$ is neither an even number or a multiple of $4$. (Since the only condition where A v B is false).
    
**(g)** A =⇒ B

$6$ is an even number if $6$ is a multiple of $4$.



### Question 3.5

**What’s the difference between “A =⇒ B” and “A ⇐⇒ B”?**

In $A \if B$, the state of A (true or false) is only reliant on the state of $B$. That is, for a fixed state of $B$, we can deduce the value of $A$ by either $A = B$ or ¬$A = B$ depending on their relationship. However, if we have a fixed state of $A$, we cannot deduce $B$. This is not the same for $A \iff B$, if we know one value, we can always deduce the other in the same manner.

**Can you give an example statements A, B where A =⇒ B is true but A ⇐⇒ B is false?**

$B$ = The (modern) theory of gravity is true (as opposed to some other theory).

$A$ = An object will fall if dropped.

An object will fall if dropped if gravity is true. This statement is true because the theory of gravity would explain a dropped object falling.

An object will fall if and only if gravity is true. This statement is false because a dropped object falling does not prove that gravity is true. So it's realistic to have $A$ be true and $B$ be false. 

**Can you give an example of two statements A, B where A ⇐⇒ B is true but A =⇒ B is false?**

No. Because if $A \iff B$ then $A \if B$ is implied. Recall the definition of $\iff$, you can derive $A$ if $B$ is known.



### Theorem 3.9

*Def 2.2.* An integer $n$ is odd if $n = 2k + 1$ for some $k \in \Z$.

*Fact 2.3.2* Sums and products of integers are integers.

**If $n$ is an odd integer, then $n^3$ is odd**.

*Proof*.

Assume that $n$ is an odd integer. By *Def 2.2*, there exists a value of $k$ called $j$ so that $n = 2j + 1$ for some $k \in \Z$. Now,

$$
n^3 = (2j + 1)^3 = (4j^2 + 4j + 1)(2j + 1) = 8j^3 + 4j^2 + 8j^2 + 4j + 2j + 1 = 2(4j^3 + 2j^2 + 4j^2 + 2j + j) + 1.
$$

By *Fact 2.3.2*, we know that the following term is an integer, so let $k = 4j^3 + 2j^2 + 4j^2 + 2j + j$. Hence, $n^3 = 2k + 1$ and thus is an odd integer. Therefore, since $n$ is an odd integer $\if$ $n^3$ is an odd integer.



