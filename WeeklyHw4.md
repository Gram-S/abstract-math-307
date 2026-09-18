### Theorem 3.17 
*Let $x$ be a real number. Then $x^2 = x \iff x = 0 \text{ or } x = 1$.*

*Proof.*

Assume $x \in \R$.

$( \implies )$ Assume $x^2 = x$. Now there are two cases, $x = 0$ and $x \not= 0$. 

In the case of $x = 0$, then $x^2 = x \implies x = 0$ is inherently true. 

Now let $x \in \R$ but $x \not= 0$. Then we divide each side of $x^2 = x$ by $x$. Hence, $x = 1$. So when $x$ is nonzero, then $x^2 = x \implies x = 1$. 

Therefore, for both $x = 0$ and $x \not= 0$, then $x^2 = x \implies x = 0 \text{ or } x = 1$. 

$( \impliedby )$ Now assume $x = 0$ or $1$. Then consider $0 = 0^2$ and $1 = 1^2$. Therefore, if $x = 0$ or $1$, then $x^2 = x$.  

By **Theorem 3.12**, we conclude that if $x \in \R$, then $x^2 = x \iff x = 0 \text{ or } x = 1$.

$\blacksquare$

<div style="break-after: page;"></div>



### Theorem 3.34 

<i>The implication $A \implies B$ is equivalent to its contrapositive.

The upshot of **Theorem 3.34** is that if you want to prove a conditional proposition, you
can prove its contrapositive instead. This proof strategy is called proof by contrapositive.</i>

*Proof.*

Consider the following truth table. 

| $A$ | $B$ | $A \implies B$ | $\lnot B \implies \lnot A$
| --- | --- | --- |  --- |
| T | T | T | T
| T | F | F | F
| F | T | T | T
| F | F | T | T

Now, by  **Def 2.22**, $A \implies B$ is equivalent to its contrapositive.

$\blacksquare$
