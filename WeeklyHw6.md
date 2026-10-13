
### Theorem 4.15

<i>"Let $U$ be the universe of discourse. Suppose that for each $x \in U$ we have a statement $P(x)$, which might be true or false depending on $x$. Then:"</i> 


**a.** We know $\lnot[(\forall x \in U) P(x)]$ is equivalent to $(\exists x \in U)(\lnot P(x))$.

*Proof.*

$\implies$ Assume it is not true that for all $x \in U$, $P(x)$ is true. Then there exists at least one $x$ which implies $P(x)$ is false. 

$\impliedby$ Assume there exists an $x \in U$ called $x'$, which implies $P(x)$ is false. Then $\forall x$ includes $x'$. Thus $\forall x$ does not imply $P(x)$ is true. 

Thus, the two statements imply each other. Therefore, the original statement is true. 

$\blacksquare$

*Proof.*

**b.** We know $\lnot (( \exists x \in U ) P(x) )$ is equivalent to $(\forall x \in U)(\lnot P(x))$.

$\implies$ Assume there exists no $x$ such that $P(x)$ is true. Then for $\forall x$, we know $P(x)$ is never true. 

$\impliedby$ Assume $\forall x$, then $P(x)$ is always false. Then there exists no $x$ which makes $P(x)$ true.

Thus, the two statements imply each other. Therefore, the original statement is true. 

$\blacksquare$

<div style="break-after: page;"></div> 



### Theorem 4.23

*Proof.* 

We use proof by contradiction. Thus, assume that $\exists n : 3n^2 + n + 14$ is odd. There are two cases, where $n$ is even or not. 

If $n$ is even, then, $n = 2k$ for some integer $k$. Thus, $3n^2 + n + 14$

$$
= 3(2k)^2 + 2k + 14
= 12k^2 + 2k + 14
= 2(6k^2 + k + 7). 
$$

Now, we know the term $2(6k^2 + k + 7)$ is even by **Def 2.2**, which contradictions our original assumption.

If $n$ is odd, then $n = 2k + 1$ for some integer $k$. Thus, $3n^2 + n + 14$

$$
= 3(2k + 1)^2 + 2k + 15
= 12k^2 + 14k + 18
= 2(6k^2 + 7k + 9).
$$

Now, we know the term $2(6k^2 + 7k + 9)$ is even, which contradicts our original assumption. 

So, assuming that $\exists n : 3n^2 + n + 14$ is odd always leads to a contradiction. Therefore, $\forall n : 3n^2 + n + 14$ is even.

$\blacksquare$
