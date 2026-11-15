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

Recall that Fact 2.3 tells us $(9k + 3^n \cdot 15)$ is an integer. Now, Theorem 2.15 implies $4$ divides $4(9k + 3^n \cdot 15)$. Therefore, $4$ divides $2 \cdot 9^{n+1} - 10 \cdot 3^{n+1}$ only when $4$ divides $2 \cdot 9^{n} - 10 \cdot 3^{n}$. 

Thus, by the PMI, $4$ divides $2 \cdot 9^{n} - 10 \cdot 3^{n}$ for all integers $n \geq 2$. 

$\blacksquare$

---

# Theorem 6.21

For all integers $n \geq 0$, then $1 + \frac{n}{2} \leq \sum^{2^n}_{k=1} \frac{1}{k}$.

*Proof.*

We proceed by induction.

*Base Case.* Let $n = 0$. Now $1 + 0 \leq \sum^{2^0}_{k=1} \frac{1}{k}$. Then, the summation is $1$. So our original statement holds when $n = 0$.

*Inductive Case.* Assume that there exists some arbitrary integer, $n \geq 0$ such that our original statement is true. Now consider $\sum^{2^{n+1}}_{k=1} \frac{1}{k} = \sum^{2^n}_{k=1} (\frac{1}{k}) + \frac{1}{2^{n+1}}.$ Our assumption tells us the summation bounded by $2^n$ is greater than or equal to $1 + \frac{n}{2}$. Then, observe that $\frac{1}{2^{n+1}}$ is greater than or equal to $\frac{1}{2}$. Thus, $\sum^{2^n}_{k=1} (\frac{1}{k}) + \frac{1}{2^{n+1}} \geq (1 + \frac{n}{2}) + \frac{1}{2}$ is true only when our assumption is true.

By the PMI, we conclude for all integers $n \geq 0$, then $1 + \frac{n}{2} \leq \sum^{2^n}_{k=1} \frac{1}{k}$.

$\blacksquare$

---

# Theorem 6.22

We use proof by contradiction, so assume ($P(a..k) \implies P(k+1)$), but $(\exists n \geq a)$ such that $\lnot P(n)$.

We know that $P(a)$ is true. We also know that $P(k) \implies P(k+1)$ for some integer $k \geq a$. Thus, by the GPMI, $P(n)$ is true for all $n \geq a$, which is a contradiction. 

Thus, the statement $[P(a..k) \implies P(k+1)] \implies$ $(\forall n \geq a)P(n).$

$\blacksquare$

---

# Problem 6.23

$(\exists a : a \in \mathbb{Z})(\exists k : k \in \mathbb{Z} \land k \geq a)(\forall j)(a \leq j \leq k)P(j) \implies (\forall n \geq a)P(n).$

