### Problem 1
<i>"Is the following statement true or false? Please prove your assertion. Let $n, k \in \mathbb{Z}$. If $k^2|n^3$ then $k|n$."</i>

*Proof*.

Assume that $n, k \in \mathbb{Z}$ and $k^2|n^3$. Since we already denote $k$, we use $a$ in place of $k$ for **Def 2.11**. We then know there exists some $a_0$ so that $a = (a_0)^3k$ due to **Fact 2.3**. Now

$$
n^3 = k^2a = k^2(a_0^3k) = k^3a_0^3. 
$$

By taking the cube root of the equation, we get $n = a_0k$. Thus $k|n$. Therefore, If $k^2|n^3$ then $k|n$.

$\blacksquare$

<div style="break-after: page;"></div> <!-- omit if the last question -->



### Problem 2

*Proof.*

<i>"Let $P, Q, R$ be statements. Are the following pairs of statements equivalent? Prove your answer."

<i>"$(P \lor (Q \implies R))$ and $((\lnot P) \implies (Q \land R))$."</i>

Consider the following truth table.



<i>"$\lnot (P \iff (Q \land R))$ and $(P \land (\lnot Q \lor \lnot R)) \lor (Q \land R \land \lnot P)$"</i>



### Problem 3

<i>"Use proof by contrapositive to prove the theorem: Assume $a, b \in \mathbb{Z}$. If $(a^2 + 4)(b^2 - 2ab)$ is odd, then $a$ and $b$ are odd."</i>

The contrapositive of our original statement is "If $a$ and $b$ are even, then $(a^2 + 4)(b^2 - 2ab)$ is even". So assume $a$ and $b$ are even. Now due to **Theorem 2.10**, we know $(b^2 - 2ab) = b(b - 2a)$ is even because $b$ is even. By the same **Theorem**, $(a^2 + 4)b(b - 2a)$ is even. Thus, the contrapositive of our original statement is true. Therefore, If $(a^2 + 4)(b^2 - 2ab)$ is odd, then $a$ and $b$ are odd.

$\blacksquare$

<div style="break-after: page;"></div> <!-- omit if the last question -->



### Problem 4

<i>"Suppose $n \in \mathbb{Z}$ with $n \geq 1$. Then $3|(4^n - 1)$."</i>

Assume that $n \in \mathbb{Z}$ and $n \geq 1$. Because of **Theorem 2.22**, we know $3|3a + 3$, so $3a + 3 = 3k$ for some $a \in \mathbb{Z}$. Then

$$
3a + 3 = 3k 
$$
$$
a + 1 = k
$$
$$
-a - 1 = -k.
$$

Note that $4^n$ is an integer when $n \geq 1$ because it is always a product of other integers (by **Fact 2.3**). So let $a = -4^n$. There also exists some $k'$ such that $k = -3k'$. This results in

$$
4^n - 1 = 3k.
$$

Thus, by **Def 2.11**, $3|4^n - 1$. Therefore, if $n \geq 1$, then $3|(4^n - 1)$.

$\blacksquare$

<div style="break-after: page;"></div> <!-- omit if the last question -->



### Problem 5

<i>"Let $j, k, n$ be integers. At least one of $n-j, n-k, j-k$ is even."</i>

Assume that $j, k, n \in \mathbb{Z}$. 

There are then $3$ cases, either $n, j, k$ are all odd, all even, or not. If all $n, j, k$ are odd, then apply **Def 2.1** to any term to get $2a + 1 - 2a' - 1 = 2(a - a')$. By **Def 2.2**, this results in an even number. If all are even, then $2a - 2a' = 2(a - a')$, which is also even. If not all terms are even or odd, then without the loss of generality, pick $n$ to be either even or odd and let $j, k$ be the opposite. Now $j - k$ can be expressed as $2a + y - 2a' - y = 2(a - a')$ for $y = 0, 1$. Thus, at least $1$ term is even in every case. Therefore, at least one of $n-j, n-k, j-k$ is even.

$\blacksquare$
