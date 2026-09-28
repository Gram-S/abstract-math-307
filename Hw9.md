**Def 3.22.** Two statements $A$ and $B$ are (logically) equivalent, expressed symbolically as $A \iff B$, if and only if they have the same truth table. 

### Theorem 3.16

*Assume $x \in \R$. Then $x^3 - 1 > 0 \iff x \gt 1$.*

*Proof*.

Assume $x^3 - 1 \gt 0$. 

$\implies$ We know that $x^3-1 = (x-1)(x^2+x+1)$ and $x^2+x+1 = (x + \frac{1}{2})^2 + \frac{3}{4}$. Notice that $(x + \frac{1}{2})^2$ cannot be negative because it is squared. Thus, $(x + \frac{1}{2})^2 + \frac{3}{4}$ has an inclusive lower bound of $\frac{3}{4}$. Now  $(x-1)(x^2+x+1) \gt 0$ is only true, $x-1 \gt 0$ when is true, and they are both false otherwise. Thus, $x^3 - 1$ implies $x \gt 1$.

$\impliedby$ Assume that $x \gt 1$. Cube both sides of the inequality, then subtract $1$ from both sides to get $x^3 - 1 \gt 0$. Thus, $x^3 - 1 > 0 \impliedby x \gt 1$. 

We have shown both $x^3 - 1 > 0 \implies x \gt 1$ and  $x^3 - 1 > 0 \impliedby x \gt 1$. Therefore, by **Theorem 3.12** $x^3 - 1 > 0 \iff x \gt 1$. 

$\blacksquare$

<div style="break-after: page;"></div>



### Theorem 3.17 
*Let $x$ be a real number. Then $x^2 = x \iff x = 0 \text{ or } x = 1$.*

*Proof.*

Assume $x \in \R$.

<!-- Need to use 'if' instead of the arrow this time. -->

$( \implies )$ Assume $x^2 = x$. Now there are two cases, $x = 0$ and $x \not= 0$. 

In the case of $x = 0$, then $x^2 = x \implies x = 0$ is inherently true. 

Now let $x \in \R$ but $x \not= 0$. Then we divide each side of $x^2 = x$ by $x$. Hence, $x = 1$. So $x^2 = x \implies x = 1$ whenever $x \in \R$ is nonzero. 

Therefore, for both $x = 0$ and $x \not= 0$, then $(x^2 = x) \implies (x = 0 ) \text{ or } (x = 1)$. 

$( \impliedby )$ Now, we show that $(x^2 = x) \impliedby (x = 0 \text{ or } x = 1)$. We have already showed this naively for $x = 0$ above, so just consider $x = 1$, then $1^2 = 1$, so $(x = 1) \implies (x^2 = x)$.

We have now shown both $(x^2 = x) \impliedby (x = 0 \text{ or } x = 1)$ and $(x^2 = x) \implies (x = 0 \text{ or } x = 1)$ are true for $x \in \R$. Therefore, by *Theorem 3.12*, we have proved $ (x^2 = x) \iff (x = 0 \text{ or } x = 1)$. 

$\blacksquare$

<div style="break-after: page;"></div>



### Problem 3.21
*A coach promises, “If we win tonight, then I will buy you pizza tomorrow.” Determine the case(s) in which the players can rightly claim to have been lied to. Use this to help create a truth table for the proposition $A \implies B$.*

The only time the promise is false (a lie), is if the players win but they are not bought pizza tomorrow. In that case, $A \implies B$ is false because $A$ is true but $B$ is false.

| $A$ | $B$ | $A \implies B$ |
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

Assume that $A$ and $B$ are propositions. We know from **Def 3.4.b** that $(A  \wedge B)$ is only true when both $A$ and $B$ are true. Thus, its negation is only false when both $A$ and $B$ are true. Now observe that $\lnot A \vee \lnot B$ is false only if both $A$ and $B$ are true. Otherwise, one would be inverted and make the statement true. Note that **Def 3.1** tells us that propositions can only be true or false. So if the statements are false at the same times, then they must then be true at the same times. Thus, their truth tables are equal and by **Def 3.22**, $\lnot (A  \wedge B) \iff \lnot A \vee \lnot B$. Therefore, if $A$ and $B$ are propositions, then $\lnot (A  \wedge B) \iff \lnot A \vee \lnot B$.

$\blacksquare$

<div style="break-after: page;"></div>



### Problem 3.25
*Let $A$ and $B$ be propositions. Conjecture a statement similar to* **Theorem 3.24** *for the proposition $\lnot(A \vee B)$ and then prove it. This is also called DeMorgan's Law.*

**Theorem 3.25.** *If $A$ and $B$ are propositions, then $\lnot(A \vee B) \iff (\lnot A \wedge \lnot B)$*.

Assume that $A$ and $B$ are propositions. We know from **Def 3.4** that $(A \vee B)$ is only false when both $A$ and $B$ are false. Thus, its negation is only true when both $A$ and $B$ are false. Now observe that $(\lnot A \wedge \lnot B)$ is true only if $A$ and $B$ are false, because they will be inverted. Note that **Def 3.1** tells us that propositions can only be true or false. So if the statements are false at the same times, then they must then be true at the same times. Thus, their truth tables are equal, so by **Def 3.22**, then $\lnot(A \vee B) \iff (\lnot A \wedge \lnot B)$. Therefore, If $A$ and $B$ are propositions, then $\lnot(A \vee B) \iff (\lnot A \wedge \lnot B)$. 

$\blacksquare$

<div style="break-after: page;"></div>



### Problem 3.26
*Rephrase $\lnot(A \implies B)$ using $\wedge$ or $\vee$. (Hint: Think about when $A \implies B$ is false.) Explain why $\lnot (A \implies B)$ is not an implication.*

| $A$ | $B$ | \lnot $A \implies B$ | new: $A \wedge \lnot B$
| --- | --- | --- | --- |
| T   | T   | F   | F
| T   | F   | T   | T
| F   | T   | F   | F
| F   | F   | F   | F

We propose that $\lnot (A \implies B)$ is not an implication because the cases where $A$ is false do not tell us anything about $B$. So the statement may not be actually true in those cases.  
