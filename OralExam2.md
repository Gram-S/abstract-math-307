


3. Are the following statements true or false? Please prove your answers.

**a.** For any set $S$ and any $x \in S$, there is an element $T \in \mathcal{P}(S)$ such that $x \not\in T$.

*Proof.*

By the **Definition of a Power Set**, we know the $\emptyset$ is an element of every power set. So consider when $T = \emptyset$. By the **Definition of the Empty Set**, then $x \not\in \emptyset$.

$\blacksquare$

**b.** $(\exists m \in \mathbb{Z}) : (\forall k \in \mathbb{N}) (m^2 \leq k)$.

*Proof.*

Consider the case where $m = 0$. We know $0^2 = 0$. By the **Definition of Natural Numbers**, we know that no $k$ is less than or equal to 0. 

$\blacksquare$

---

4. Prove the following Theorem by contradiction.

If $a, b$ are real numbers, $a$ is rational, and $b$ is not rational, then $a + b$ is not rational. 

We use proof by contradiction. So assume $a + b$ is a rational number. Then, by the **Definition of Rational Numbers**, then $a + b = \frac{p}{q}$ for some $p, q \in \mathbb{Z}$. We know $a$ is also rational, so $\frac{n}{d} + b = \frac{p}{q}$ for some $n, m \in \mathbb{Z}$. Now, 

$$
b = \frac{p}{q} - \frac{n}{d} = \frac{p*d}{q*d} - \frac{n*q}{d*q} = \frac{p*d - n*q}{q*d - d*q}.
$$

Then, **Fact 2.3** implies the terms $p*d - n*q$ and $q*d - d*q$ are integers. So $b$ is an integer divided by another integer. Thus, by the **Definition of Rational Numbers**, then $b$ is a rational number, which is a contradiction. Therefore, if $a, b$ are real numbers, $a$ is rational, and $b$ is not rational, then $a + b$ is not rational.
