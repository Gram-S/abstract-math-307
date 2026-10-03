### Theorem 3.53

<i>"If $p$ is prime, then either $p = 2$ or $p$ is odd."</i> <!-- Original claim -->

*Proof*.
<!-- begin -->

Assume that $p$ is prime. For the sake of contradiction, assume that $p \not= 2$ and $p$ is even. Now $p = 2k$. Since $p \not= 2$, then $k$ cannot be $1$. So $p$ now has a factor of $2$, so $p$ is not prime. Thus, assuming $p$ is not $2$ and even leads to a contradiction. Therefore, if $p$ is prime, then either $p = 2$ or $p$ is odd.

$\blacksquare$

<div style="break-after: page;"></div> <!-- omit if the last question -->



### Theorem 3.43

<i>"The real number $\sqrt{2}$ is not rational."</i> <!-- Original claim -->

*Proof*.
<!-- begin -->

For the sake of contradiction, assume that the real number $\sqrt{2}$ is rational. Now by **Def 3.42**, we know $\sqrt{2}=\frac{p}{q}$ for some $p, q \in \Z$ and $q \not =0$. Let $\frac{p}{q}$ be written such that $p, q$ have no common factor greater than $1$. Now, 

$$
2= \frac{p^2}{q^2}
$$
$$
p^2 = 2 q^2.
$$

By **Theorem 2.10**, then $p$ is now even. Now **Def 2.1** implies $p = 2k_p$ for some $k_p \in \mathbb{Z}$,

$$
{2k_p}^2 = 4k_p^2 = 2(2k_p^2) =  2 q^2
$$
$$
2k_p^2 = q^2.
$$

Which means $q$ is also even. Since both $p$ and $q$ are even, they have a common factor of $2$. This contradicts our earlier assumption that they do not have a common factor greater than $1$. Hence, assuming that $\sqrt{2}$ is rational leads to a contradiction. Therefore the $\sqrt{2}$ is not rational.  

$\blacksquare$
