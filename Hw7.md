### Theorem 3.10 
*If $a, b$ are integers and $a|b$, then $a^2|b^2$.*

Assume $a, b$ are integers and $a|b$. Because of *Def 2.11*, we know that $b = ak$. Now *Fact 2.3.2* implies there exists some values of $k$ so that $k = ak_1, k_2 = bk_1$. We can then multiply both sides of $b = ak$ by $b$. Now

<!-- I suspect that $k_1$ will always be =1 because I've done some traces with 2|4.-->
$$
b^2 = ak(b) = a(ak_1)b = a^2k_1b = a^2k_2. 
$$

Then, by *Def 2.11*, we know $a^2|b^2$. Therefore, if $a, b$ are integers and $a|b$, then $a^2|b^2$.



### Exercise 3.11
*Give at least two equivalent ways to say $A \iff B$ using the words "necessary" and/or "sufficient".*

- This definition is sufficient. Let a proposition $=1$ if it is true and $0$ otherwise. Then $A = B$.
- Given $A$ to be true, then it is necessary $B$ is true. Given $A$ to be false, then it is necessary $B$ is false. Given $B$ to be true, then it is necessary $A$ is true. Given $B$ to be false, then it is necessary $A$ is false. 



### Theorem 3.12 
*For any propositions $A, B$, the statement "$A \iff B$" is equivalent to the statement “$(A \Rightarrow B) \wedge (B \Rightarrow A)$”*

Assume that for propositions $A, B$, we have $(A \Rightarrow B) \wedge (B \Rightarrow A)$. Assign a value $a, b$ to $A, B$ respectively. Let a value $=1$ if their respective proposition is true and $=0$ otherwise. Now, without the loss of generality, there are two cases. When $a = 1$, we know that $b = 1$ because $A \Rightarrow B$. However, when $a = 0$, we know $b /not= 1$, because if $b = 1$, then $a$ must equal $1$ since $B \Rightarrow A$, which is not true for this case. Thus, $b$ must be $0$. So in both cases, $a = b$. Notice that, the definition of $\iff$ also implies $a = b$. Therefore, since both of these statements can be expressed as $a = b$, the statement "$A \iff B$" is equivalent to the “$(A \Rightarrow B) \wedge (B \Rightarrow A)$”. 



### Question 3.14
*Can you think of any other ways to approach a proof of the form $A \iff B$? Write a skeleton proof for your strategies.*

Proof:

Assume $A$.

Derive $B$ from definitions and known results.

Therefore, $A \Rightarrow B$.

Now assume $B$.

Derive $A$ from known results and definitions.

Therefore, $A \Rightarrow B$.

Thus, since $A \Rightarrow B$ and $B \Rightarrow A$, by *Def 3.3*, we know $A \iff B$. 



### Theorem 3.16
*Assume $x \in \R$. Then $ (x^2 = x) \iff (x = 0 \text{ or } x = 1)$.*

<!-- Need to use 'if' instead of the arrow this time. -->

First we show that $(x^2 = x) \Leftarrow (x = 0 \text{ or } x = 1)$. Assume $x \in \R$. Now there are two cases, $x = 0$ and $x \not= 0$. 

Let $x = 0$, then $0^2 = 0$ is true, so $(x^2 = x) \Leftarrow (x = 0)$ assuming $x$ can only be $0$. <!-- This works because it is ONLY for the case x = 0. It does not affect the other case. I believe this is if and only if too. -->

Let $x \in \R$ but $x \not= 0$, then we can divide each side of $x^2 = x$ by $x$. Then, $x = 1$, so $x^2 = x$ for some nonzero $x \in \R$, so $(x^2 = x) \Rightarrow (x = 1)$. 

Since $x^2 = x$ is true in both cases, we can say that $(x^2 = x) \Leftarrow (x = 0 \text{ or } x = 1)$.

Now, we show that $(x^2 = x) \Rightarrow (x = 0 \text{ or } x = 1)$. We have already showed this naively for $x = 0$ above, so just consider $x = 1$, then $1^2 = 1$, so $(x = 1) \Rightarrow (x^2 = x)$.

We have now shown both $(x^2 = x) \Leftarrow (x = 0 \text{ or } x = 1)$ and $(x^2 = x) \Rightarrow (x = 0 \text{ or } x = 1)$ are true for $x \in \R$. Therefore, by *Theorem 3.12*, we have proved $ (x^2 = x) \iff (x = 0 \text{ or } x = 1)$. 

