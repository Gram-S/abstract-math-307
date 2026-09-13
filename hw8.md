
### Theorem 3.17 
*Let $x$ be a real number. Then $x^2 = x \iff x = 0 or x = 1$*

*Proof.*

*Assume $x \in \R$. Then $ (x^2 = x) \iff (x = 0 \text{ or } x = 1)$.*

<!-- Need to use 'if' instead of the arrow this time. -->

*Proof*.

First we show that $(x^2 = x) \Leftarrow (x = 0 \text{ or } x = 1)$. Assume $x \in \R$. Now there are two cases, $x = 0$ and $x \not= 0$. 

Let $x = 0$, then $0^2 = 0$ is true, so $(x^2 = x) \Leftarrow (x = 0)$ assuming $x$ can only be $0$. <!-- This works because it is ONLY for the case x = 0. It does not affect the other case. I believe this is if and only if too. -->

Let $x \in \R$ but $x \not= 0$, then we can divide each side of $x^2 = x$ by $x$. Then, $x = 1$, so $x^2 = x$ for some nonzero $x \in \R$, so $(x^2 = x) \Rightarrow (x = 1)$. 

Since $x^2 = x$ is true in both cases, we can say that $(x^2 = x) \Leftarrow (x = 0 \text{ or } x = 1)$.

Now, we show that $(x^2 = x) \Rightarrow (x = 0 \text{ or } x = 1)$. We have already showed this naively for $x = 0$ above, so just consider $x = 1$, then $1^2 = 1$, so $(x = 1) \Rightarrow (x^2 = x)$.

We have now shown both $(x^2 = x) \Leftarrow (x = 0 \text{ or } x = 1)$ and $(x^2 = x) \Rightarrow (x = 0 \text{ or } x = 1)$ are true for $x \in \R$. Therefore, by *Theorem 3.12*, we have proved $ (x^2 = x) \iff (x = 0 \text{ or } x = 1)$. 


$\blacksquare$

<div style="break-after: page;"></div>



### Exercise 3.20 
*Create a truth table for each of $A \wedge B, \lnot A, \lnot (A \wedge B), $ and $\lnot A \wedge \lnot B$. Feel free to
add additional columns to your tables to assist you with intermediate steps. (For example, for the last one, you might want to include columns for $\lnot A$ and $\lnot B$.)*


| $A$ | $B$ | $\lnot A$ | $\lnot (A \wedge B)$ | $\lnot A \wedge \lnot B$ |
|---|---|---|---|---|
|  T  |  T  |   F       |F                     |F                         | 
|  T  |  F  |   F       |T                     |F                         |
|  F  |  T  |   T       |T                     |F                         |
|  F  |  F  |T          |T                     |T                         |


<div style="break-after: page;"></div>



### Problem 3.21 
*A coach promises, “If we win tonight, then I will buy you pizza tomorrow.” Determine the case(s) in which the players can rightly claim to have been lied to. Use this to help create a truth table for the proposition $A \Rightarrow B$.*

The only time the promise is false (a lie), is if the players win but they are not bought pizza tomorrow. In that case, $A \Rightarrow B$ is false because $A$ is true but $B$ is not.

| $A$ | $B$ | $A \Rightarrow B$ |
| --- | --- | --- |
| T   | T   | T
| T   | F   | F
| F   | T   | T
| F   | F   | T

<div style="break-after: page;"></div>



### Exercise 3.23
*Explain why Definition 3.22 and Definition 3.3 both assign the same meaning to the symbol $\iff$.*

**Def 3.3.** . Given two propositions $A, B$, we say $A$ is true if and only if $B$ is true (or “$A$ iff $B$” or “$A \iff B$”) if $A$ is true exactly when $B$ is true. That is, $A \iff B$ means that if $A$ is true then $B$ is true, and if $A$ is false then $B$ is false

**Def 3.22.** Two statements $A$ and $B$ are (logically) equivalent, expressed symbolically as $A \iff B$, if and only if they have the same truth table. 

We know **Def 3.3** explicitly states that $A$ and $B$ are either both true or both false if $A \iff B$. Now, if they have the same truth table, then are both true or both false at the same times. Thus, if $A$ and $B$ have the same truth table, then $A \iff B$. Therefore, they have the same meaning for $\iff$. 


<div style="break-after: page;"></div>
