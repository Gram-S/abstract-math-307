1. Suppose we're given statements $P(x)$ and $Q(x)$ for all real numbers $x$. Must the following statements be equivalent? Consider $\exists x \in \mathbb{R} : P(x) \land Q(x)$ and $(\exists x \in \mathbb{R} : P(x)) \land (\exists x \in \mathbb{R} : Q(x)).$

We claim the statement are not equivalent.

*Proof.*

Since the statements are arbitrary, consider the case where $P(x) = \lnot Q(x)$. We then use proof by contradiction, so assume the original statements are equivalent. Then the **definition of equivalent statements** tells us $(\exists x \in \mathbb{R} : P(x)) \land (\exists x \in \mathbb{R} : Q(x)) \implies \exists x \in \mathbb{R} : P(x) \land Q(x)$. So assume $(\exists x \in \mathbb{R} : P(x)) \land (\exists x \in \mathbb{R} : Q(x))$, now $\exists x \in \mathbb{R} : \lnot Q(x) \land Q(x)$. But the **definition of negation** tells us $\lnot Q(x) \land Q(x)$ is false for all $x$. Thus, $(\exists x \in \mathbb{R} : P(x)) \land (\exists x \in \mathbb{R} : Q(x)) \not\implies \exists x \in \mathbb{R} : P(x) \land Q(x)$, which is a contradiction. Therefore, the original statements are not equivalent.

$\blacksquare$

2. If $A, B, C$ are sets, then $A \setminus (B \cup C) = (A \setminus B) \cap (A \setminus C)$.

*Proof.*

Denote $S = A \setminus (B \cup C)$ and $T = (A \setminus B) \cap (A \setminus C)$.

$(S \subseteq T)$ Let $x \in S$ be arbitrary. By the **Def. of Set Minus**, we know $x \in A$ and $x \not\in (B \cup C)$. The **definition of union** implies that $x \in B \cup C$ if $x \in B$ or $C$. So for $x$ to not be in the union, then $x \not\in B, C$. Now, we know $x \in (A \setminus B), (A \setminus C)$. Thus, the **Def. of Intersection** implies $x \in T$. Since $x \in S$ was arbitrary, we conclude $S \subseteq T$.

$(S \supseteq T)$ Let $x \in T$ be arbitrary. By the **Def. of Intersection**, we know $x \in (A \setminus B), (A \setminus C)$. Then, the **Def. of Set Minus** implies $x \in A$ and $x \not\in B, C$. By the **Def. of Union**, then $x \not\in (B \cup C)$. Thus, $x \in S$. Since $x \in T$ was arbitrary, we conclude $S \supseteq T$.

$\blacksquare$


3. Are the following statements true or false? Please prove your answers.

**a.** For any set $S$ and any $x \in S$, there is an element $T \in \mathcal{P}(S)$ such that $x \not\in T$.

*Proof.*

There are two cases depending on if $S = \emptyset$.

If $S = \emptyset$. The **definition of the power set** means that $T = \emptyset$. We know that $T$ contains no elements. 

The **definition of set minus** tells us that $S \setminus \{x\}$ is a subset of $S$. So consider when $T = S \setminus \{x\}$. Now $T$ does not contain $x$. Since $S$ and $x$ are arbitrary, we there exists a $T$ for all $S$ and $x$.

$\blacksquare$

**b.** $(\exists m \in \mathbb{Z}) : (\forall k \in \mathbb{N}) (m^2 \leq k)$.

*Proof.*

We know $0 \in \mathbb{Z}$. So, consider the case where $m = 0$. We know $0^2 = 0$. By the **Definition of Natural Numbers**, we know that no $k$ is less than or equal to 0. 

$\blacksquare$

---

4. Prove the following Theorem by contradiction.

If $a, b$ are real numbers, $a$ is rational, and $b$ is not rational, then $a + b$ is not rational. 

*Proof.*

We use proof by contradiction. So assume $a + b$ is a rational number. Then, by the **Definition of Rational Numbers**, then $a + b = \frac{p}{q}$ for some $p, q \in \mathbb{Z}$. We know $a$ is also rational, so $\frac{n}{d} + b = \frac{p}{q}$ for some $n, m \in \mathbb{Z}$. Now, 

$$
b = \frac{p}{q} - \frac{n}{d} = \frac{p*d}{q*d} - \frac{n*q}{d*q} = \frac{p*d - n*q}{q*d - d*q}.
$$

Then, **Fact 2.3** implies the terms $p*d - n*q$ and $q*d - d*q$ are integers. So $b$ is an integer divided by another integer. Thus, by the **Definition of Rational Numbers**, then $b$ is a rational number, which is a contradiction. Therefore, if $a, b$ are real numbers, $a$ is rational, and $b$ is not rational, then $a + b$ is not rational.

$\blacksquare$

5. Consider the sets $A = \{8a + 17b : a, b \in \mathbb{N}\}$ and $B = \{c \in \mathbb{N} : c \geq 25\}$. Is $A \subseteq B$ true? Is $B \subseteq A$ true? What about $A = B$? Please prove your answers.


**START** 

We know $A \subseteq B$ is true, but $A \supseteq B$ and $A = B$ is false. 

*Proof.*

$(S \subseteq T)$ Let $x \in S$ be arbitrary. Now $x = 8a + 17b$ for some $a, b \in \mathbb{N}$. Observe that **Theorem 3.48** implies that $x$ is always a natural number for all values of $a, b$. Then, using the **definition of natural numbers**, we know the smallest value of $x$ is 25 when $a, b = 1$. Thus, $x$ must be a natural number equal to or greater than 25. Thus, $x \in B$. Since $x \in S$ was arbitrary, we conclude $S \subseteq T$.

$(S \not\supseteq T)$ We use proof by contradiction, so assume $S \supseteq T$. We know $26 \in T$. Then the **definition of subsets** implies $26 \in S$. But the two smallest values in $S$ are 25 and 33 when $a, b = 2, 1$. Thus, $26 \not\in S$, which is a contradiction. So assuming $S \supseteq T$ leads to a contradiction. Therefore, $S \not\supseteq T$. 

$(S \not= T)$ We use proof by contradiction, so assume $S = T$. Then the **definition of set equality** implies $S \supseteq T$, which has already proven to be false. Thus, assuming $S = T$ leads to a contradiction. Therefore, $S \not= T$.

$\blacksquare$