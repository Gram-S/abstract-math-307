### Theorem 3.12 
*For any propositions $A, B$, the statement "$A \iff B$" is equivalent to the statement “$(A \Rightarrow B) \wedge (B \Rightarrow A)$”*

*Proof*.

Assume that for propositions $A, B$, we have $(A \Rightarrow B) \wedge (B \Rightarrow A)$. Assign values $a, b$ to $A, B$ respectively. Let a value $=1$ if their respective proposition is true and $=0$ otherwise. Now, without the loss of generality, there are two cases. When $a = 1$, we know that $b = 1$ because $A \Rightarrow B$. However, when $a = 0$, we know $b \not= 1$, because if $b = 1$, then $a$ must equal $1$ since $B \Rightarrow A$, which is not true for this case. Thus, $b$ must be $0$. So in both cases, $a = b$. Notice that, the definition of $\iff$ also implies $a = b$. Therefore, since both of these statements can be expressed as $a = b$, the statement "$A \iff B$" is equivalent to the statement “$(A \Rightarrow B) \wedge (B \Rightarrow A)$”. 

$\blacksquare$

<div style="break-after: page;"></div>

### Theorem 3.16
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

