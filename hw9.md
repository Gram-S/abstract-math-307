**Def 3.22.** Two statements $A$ and $B$ are (logically) equivalent, expressed symbolically as $A \iff B$, if and only if they have the same truth table. 



### Theorem 3.16

*Assume $x \in \R$. Then $x^3 - 1 > 0 \iff x \gt 1$.*

*Proof*.

Assume $x \in \R$. We use $x^3 - 1 > 0$ to state the inequality $x^3 > 1$, which has two possibilities for $x$. Either $x \leq 1$ or $x \gt 1$. 

First assume that $x \leq 1$. If $x = 0, 1$, then $x^3 = 0, 1$, which makes the stated inequality false. Then, $x$ can either be a decimal in the range $(0, 1)$ or a negative number. If $x$ is a decimal, then $x^3$ cannot exceed $1$ as multiplication by a number in the range $0, 1$ cannot increase the function. If $x$ is negative, then $x^3$ is negative. So in both cases, the stated inequality is false. Therefore, the $x^3 > 1$ is false for all $x \leq 1$.

Now assume that $x \gt 1$. Observe that the above cases are the only cases where $x^3 \leq x$. Thus, for $x \gt 1$, then $x^3 \gt x \gt 1$. So the stated inequality is true when $x \gt 1$. 

Since $x^3 \gt 1$ is true exactly when $x \gt 1$ and no other case, by **Def 3.3**, $x^3 \gt 1 \iff x \gt 1$. Therefore, $x^3 - 1 > 0 \iff x \gt 1$. 


*Assume $x \in \R$. Then $x^3 - 1 > 0 \iff x \gt 1$.*

*Proof.*

Assume $x \in \R$. 

$\RightArrow$ Assume $x^3 - 1 \gt 0$. Then, $x^3 \gt 1$. Now, we show that $x^3 \gt 1 \iff x \not= 0, 1$ because $x^3 \gt 1$ is false exactly when $x = 0, 1$. Then we show $x^3 \gt 1 \iff x \lt 1$ because $x^3$ would be a decreasing function for such values of $x$. 

$\LeftArrow$ Assume $x \gt 1$. Now we can cube each side and subtract $1$ from each side. Thus, $x^3 - 1 \gt 0$. 

$\blacksquare$

<div style="break-after: page;"></div>



### Theorem 3.17 
*Let $x$ be a real number. Then $x^2 = x \iff x = 0 \text{ or } x = 1$*

*Proof.*

*Assume $x \in \R$. Then $ (x^2 = x) \iff (x = 0 \text{ or } x = 1)$.*

<!-- Need to use 'if' instead of the arrow this time. -->

*Proof*.

First we show that $(x^2 = x) \Rightarrow (x = 0 \text{ or } x = 1)$. Assume $x \in \R$. Now there are two cases, $x = 0$ and $x \not= 0$. 

Let $x = 0$, then $0^2 = 0$ is true, so $(x^2 = x) \Rightarrow (x = 0)$ is also true assuming $x$ can only be $0$. <!-- This works because it is ONLY for the case x = 0. It does not affect the other case. I believe this is if and only if too. -->

Let $x \in \R$ but $x \not= 0$, then we can divide each side of $x^2 = x$ by $x$. Then, $x = 1$, so $x^2 = x$ for some nonzero $x \in \R$, so $(x^2 = x) \Rightarrow (x = 1)$. 

Since the statements $(x^2 = x)$ and $(x = 0 \text{ or } x = 1$ is true in both cases, we can say that $(x^2 = x) \Rightarrow (x = 0 \text{ or } x = 1)$.

Now, we show that $(x^2 = x) \Rightarrow (x = 0 \text{ or } x = 1)$. We have already showed this naively for $x = 0$ above, so just consider $x = 1$, then $1^2 = 1$, so $(x = 1) \Rightarrow (x^2 = x)$.

We have now shown both $(x^2 = x) \Leftarrow (x = 0 \text{ or } x = 1)$ and $(x^2 = x) \Rightarrow (x = 0 \text{ or } x = 1)$ are true for $x \in \R$. Therefore, by *Theorem 3.12*, we have proved $ (x^2 = x) \iff (x = 0 \text{ or } x = 1)$. 

$\blacksquare$

<div style="break-after: page;"></div>



### Problem 3.21
*A coach promises, “If we win tonight, then I will buy you pizza tomorrow.” Determine the case(s) in which the players can rightly claim to have been lied to. Use this to help create a truth table for the proposition $A \Rightarrow B$.*

The only time the promise is false (a lie), is if the players win but they are not bought pizza tomorrow. In that case, $A \Rightarrow B$ is false because $A$ is true but $B$ is false.

| $A$ | $B$ | $A \Rightarrow B$ |
| --- | --- | --- |
| T   | T   | T
| T   | F   | F
| F   | T   | T
| F   | F   | T

<div style="break-after: page;"></div>



### Theorem 3.24
*If $A$ and $B$ are propositions, then $\lnot (A  \wedge B) \iff \lnot A \vee \lnot B$*.

*Proof.*

<!-- There's some definition here -->

Assume that $A$ and $B$ are propositions. We know from **Def 3.4.b** that $(A  \wedge B)$ is only true when both $A$ and $B$ are true. Thus, its inverse is only false when both $A$ and $B$ are true. Now observe that $\lnot A \vee \lnot B$ is false only if both $A$ and $B$ are true. Otherwise, one would be inverted and make the statement true. Note that **Def 3.1** tells us that propositions can only be true or false. So if the statements are false at the same times, then they must then be true at the same times. Thus, their truth tables are equal and by **Def 3.22**, $\lnot (A  \wedge B) \iff \lnot A \vee \lnot B$. Therefore, if $A$ and $B$, then $\lnot (A  \wedge B) \iff \lnot A \vee \lnot B$.

$\blacksquare$

<div style="break-after: page;"></div>



### Problem 3.25
*Let $A$ and $B$ be propositions. Conjecture a statement similar to* **Theorem 3.24** *for the proposition $\lnot(A \vee B)$ and then prove it. This is also called DeMorgan's Law.*

**Theorem 3.25.** *If $A$ and $B$ are propositions, then $\lnot(A \vee B) \iff (\lnot A \wedge \lnot B)$*.

Assume that $A$ and $B$ are propositions. We know from **Def 3.4** that $(A \vee B)$ is only false when both $A$ and $B$ are false. Thus, its inverse is only true when both $A$ and $B$ are false. Now observe that $(\lnot A \wedge \lnot B)$ is true only if $A$ and $B$ are false, because they will be inverted. Note that **Def 3.1** tells us that propositions can only be true or false. So if the statements are false at the same times, then they must then be true at the same times. Thus, their truth tables are equal, so by **Def 3.22**, then $\lnot(A \vee B) \iff (\lnot A \wedge \lnot B)$. Therefore, If $A$ and $B$ are propositions, then $\lnot(A \vee B) \iff (\lnot A \wedge \lnot B)$. 

$\blacksquare$

<div style="break-after: page;"></div>



### Problem 3.26
*Rephrase $\lnot(A \Rightarrow B)$ using $\wedge$ or $\vee$. (Hint: Think about when $A \Rightarrow B$ is false.) Explain why $\lnot (A \Rightarrow B)$ is not an implication.*

| $A$ | $B$ | $A \Rightarrow B$ | new: $A \wedge \lnot B$
| --- | --- | --- | --- |
| T   | T   | T   | F
| T   | F   | F   | T
| F   | T   | T   | F
| F   | F   | T   | F

We propose that $\lnot (A \Rightarrow B)$ is not an implication because the cases where $A$ is false do not tell us anything about $B$. So the statement may not be actually true in those cases.  
