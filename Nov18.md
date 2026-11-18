
# Problem 6.24

Since we use positive integers, something we cannot use our inductive step to prove $k = 1$, as we'd have to prove $P(-1)$. Thus, we prove $P(2), P(1), P(0)$ in the base case. Then, we can assume $P(k-2), P(k-1), P(k)$ in the inductive step, since we use it for integers greater than $2$. 

Let $k \in \mathbb{N}$ with $k \geq 3$. Suppose $P(j)$ is true for all $j \in \mathbb{Z}$ such that $a \geq j \geq k$. 

---

# Theorem 6.26

Define a sequence of numbers by $a_1 = 1$, $a_2 = 3$, and $a_n = 3a_{n−1} − 2a_{n−2}$ for all
natural numbers $n \geq 3$. Then $a_n = 2^n − 1$ for all $n \in \mathbb{N}$.

*Proof.* We proceed by induction. 

*Base Case.* Consider when $n = 1, 2$. Then observe that

$$
2^1 - 1 = 1 = a_1 \\
2^2 - 1 = 3 = a_2.
$$
So, our original statement is true for $n = 1, 2$. 

*Inductive Case.* Let $k \in \mathbb{N}$ with $k \geq 3$. Suppose that, for all $j \in \mathbb{Z}$ such that $3 \leq j \leq k$, then $a_j = 2^j - 1$. Let $k' = k - 1$. Now consider $a_{k+1} = 3a_k - 2a_{k'}$. Then, our inductive hypothesis with $j = k, k-1$ implies $3(2^k - 1) - 2(2^{k'}-1)$, then

$$
\begin{align}
3(2^k - 1) - 2(2^{k'}-1) &= 3(2^k - 1) - 2^{k} + 2 \\
&= (2 + 1)(2^k - 1) - 2^{k} + 2 \\
&= 2^{k+1} - 2 + 2^k - 1 - 2^{k} + 2 \\
&= 2^{k+1} - 1.
\end{align}
$$

Therefore, $a_{k+1} = 2^{k+1} - 1$ is true whenever $a_j = 2^j - 1$ for all $j \in \mathbb{Z}$ such that $3 \leq j \leq k$.

Thus, by the PCMI, then $a_n = 2^{n+1}$ is true for all $n \in \mathbb{N}$.

$\blacksquare$

---

# Theorem 6.27

Define a sequence of numbers by $a_1 = 1$, $a_2 = 2$, $a_3 = 3$ and $a_n = a_{n-1} + a_{n-2} + a_{n-3}$ for all natural numbers $n \geq 4$. Then $a_n < 2^n$ for all $n \in \mathbb{N}$.

*Proof.* We proceed by induction. 

*Base Case.* Consider when $n = 1,2,3$. Then observe, 

$$
1 \leq 2^1 \\
2 \leq 2^2 \\
3 \leq 2^3.
$$
So our original statement is true for $n = 1,2,3$. 

*Inductive Case.* Let $k \in \mathbb{N}$ with $k \geq 4$. Suppose that, for all $j \in \mathbb{Z}$ such that $4 \geq j \geq k$, then $a_j \lt 2^j$. Now consider $a_{k+1} = a_k + a_{k-1} + a_{k-2}$. By our inductive hypothesis, we know that $a_{k+1}$ is less than $2^k + 2^{k-1} + 2^{k-2}$. Then,

$$
\begin{align}
2^k + 2^{k-1} + 2^{k-2} &= 2^{k-2}(2^2 + 2 + 1) \\
&= 2^{k-2}(7).
\end{align}
$$
We then know $2^{k-2}(7) \lt 2^{k-2}(2^3)$. Therefore, $a_{k+1} \lt 2^{k+1}$ is true whenever $a_j \leq 2^j$.

Thus, by the PCMI, then our original statement is true for all $n \in \mathbb{N}$.

$\blacksquare$

---

# Theorem 6.28

Every amount of postage that is at least $12$ cents can be made from $4$-cent and $5$-cent stamps.

*Proof.* We proceed by induction. 

*Base Case.* Consider postage that costs $12, 13, 14, 15$ and $16$ cents. Then, 

$$
12 = 4 + 4 + 4 \\
13 = 5 + 4 + 4 \\
14 = 5 + 5 + 4 \\
15 = 5 + 5 + 5 \\
16 = 4 + 4 + 4 + 4.
$$
So our original statement is true for $12, 13, 14, 15$ and $16$ cents.

*Inductive Case.* Let $k \geq 17$ be a natural number. For some $j \in \mathbb{Z}$ such that $17 \geq j \geq k$, suppose that we can make a postage of $j$ cents using $4$-cent and $5$-cent stamps. Now, for a postage that is $j+1$ cents, there are two cases. 

1. We start with a $4$-cent stamp. Then our inductive hypothesis implies we can make the remaining $j-3$ postage from $4$ and $5$ cent stamps. 
2. We start with a $5$-cent stamp. Then our we can make the remaining $j-4$ postage from $4$ and $5$ cent stamps. 

Thus, we can make $j+1$ postage with $4$ and $5$ cent stamps whenever we can make $j$ postage with $4$ and $5$ cent stamps for $j \in \mathbb{Z}$ such that $17 \leq j \leq k$.

Therefore, by the PCMI, we can make every amount of postage that is at least $12$ cents from $4$ and $5$ cent stamps. 

$\blacksquare$