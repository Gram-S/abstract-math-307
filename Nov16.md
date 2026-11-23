 # Theorem 6.20

For all integers $n \geq 2$, then $(2)9^n − (10)3^n$ is divisible by $4$.

We proceed by induction, so there are two cases. 

*(i).* Let $n = 2$, then we know $(2)81 − (10)9 = 162 - 90 = 72$. Since $4(18) = 72$, the definition of divisibility implies $4$ divides $72$. So our original statement holds for $n = 2$. 

*(ii).* Assume for some arbitrary $n \in \mathbb{Z}$ and $n \geq 2$, then $2 \cdot 9^n - 10 \cdot 3^n$ is divisible by $4$. Then the definition of divisibility tells us $2 \cdot 9^n = 4k + 10 \cdot 3^n$ for some $k \in \mathbb{Z}$. Now consider $2 \cdot 9^{n+1} - 10 \cdot 3^{n+1}.$ We then know

$$
\begin{align}
2 \cdot 9^{n+1} - 10 \cdot 3^{n+1} &= 9 \cdot (2 \cdot 9^{n}) - 3^{n} \cdot 30 \\
&= 9 \cdot (4k + 3^n \cdot 10) - 3^{n} \cdot 30 \\
&= 36k + 3^n \cdot 90 - 3^{n} \cdot 30 \\
&= 36k + 3^n \cdot (90 - 30) \\
&= 36k + 3^n \cdot 60 \\
&= 4(9k + 3^n \cdot 15).
\end{align}
$$

Recall that Fact 2.3 tells us $(9k + 3^n \cdot 15)$ is an integer. Now, Theorem 2.15 implies $4$ divides $4(9k + 3^n \cdot 15)$. Therefore, $4$ divides $2 \cdot 9^{n+1} - 10 \cdot 3^{n+1}$ whenever $4$ divides $2 \cdot 9^{n} - 10 \cdot 3^{n}$. 

Thus, by the GPMI, $4$ divides $2 \cdot 9^{n} - 10 \cdot 3^{n}$ for all integers $n \geq 2$. 

$\blacksquare$

---

# Theorem 6.21

For all integers $n \geq 0$, then $1 + \frac{n}{2} \leq \sum^{2^n}_{k=1} \frac{1}{k}$.

*Proof.*

We proceed by induction.

*Base Case.* Let $n = 0$. Now $1 + 0 \leq \sum^{2^0}_{k=1} \frac{1}{k}$. Then, the summation is $1$. So our original statement holds when $n = 0$.

*Inductive Case.* Assume there exists some arbitrary integer $n \geq 0$ such that $1 + \frac{n}{2} \leq \sum^{2^n}_{k=1} \frac{1}{k}.$ Now consider $\sum^{2^{n+1}}_{k=1} \frac{1}{k} = \sum^{2^n}_{k=1} \frac{1}{k} + \sum^{2^{n+1}}_{k=2^n+1} \frac{1}{k}.$ Note that the minimum term of the sum of $2^n+1$ to $2^{n+1}$ is $\frac{1}{2^{n}+1}$. Then, we know that for the smallest value, $n = 0$, makes this term $\frac{1}{2}.$ Hence, the total sum must always be equal to or greater than $\frac{1}{2}.$ Subsequently, by the inductive hypothesis, we know $\sum^{2^n}_{k=1} \frac{1}{k} \geq 1 + \frac{n}{2}.$ Thus, $\sum^{2^n}_{k=1} \frac{1}{k} + \sum^{2^{n+1}}_{k=2^n+1} \frac{1}{k} \geq (1 + \frac{n}{2}) + \frac{1}{2}$ is true whenever $1 + \frac{n}{2} \leq \sum^{2^n}_{k=1} \frac{1}{k}$ is true. 

Now, by the GPMI, $1 + \frac{n}{2} \leq \sum^{2^n}_{k=1} \frac{1}{k}$ is true for all $n \geq 0$.

$\blacksquare$

---

# Theorem 6.22

*Proof.*

Assume we have a sequence of statements $P(a), P(a+1), P(a + 2), ...$ for some integer $a$. Let $Q(n)$ be the statement $P(j)$ is true for all integers $a \geq j \geq n.$ We proceed by Weak Induction.

*Base Step.* Let $n = a$. By assumption, we know $P(a)$ is true. Therefore, $Q(a)$ is true.

*Inductive Step.* Let $n\ge a$ be an integer, and assume $Q(n)$ is true. Thus, $P(j)$ is true for all integers $j$ satisfying $a\le j\le n$. By our assumption, $P(n+1)$ is true. The inductive hypothesis already gives $P(j)$ for every integer from $a$ through $n$. Therefore, $P(j)$ is true for all integers $j$ satisfying $a\le j\le n+1$. Thus, $Q(n+1)$ is true whenever $Q(n)$ is true. By Axiom 6.16, $Q(n)$ is true for all integers $n\ge a$. Since $Q(n)$ implies $P(n)$, $P(n)$ is true for all integers $n\ge a$. 

Therefore, by the PMI, the Complete Induction theorem is true. 

$\blacksquare$

---

# Problem 6.23

$(\exists a : a \in \mathbb{Z})(\exists k : k \in \mathbb{Z} \land k \geq a)(\forall j)(a \leq j \leq k)P(j) \implies (\forall n \geq a)P(n).$

