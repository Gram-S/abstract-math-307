*Def 1.0.* Define the set of integers as $\Z = \{..., -2, -1, 0, 1, 2, .. \}$.

*Def 2.1.* An integer $n$ is even if $n = 2k$ for some $k \in \Z$.

*Def 2.2.* An integer $n$ is odd if $n = 2k + 1$ for some $k \in \Z$.

*Fact 2.3.1.* Every integer is either even or odd, but never both.

*Fact 2.3.2* Sums and products of integers are integers.

*Def 2.11.* An integer $n$ divides the integer $m$ written $n|m$, if and only if, there exists $k \in \Z : m = nk$.  



### Theorem 2.18

**Claim**: Assume $n,m,a \in \Z$. If $a$ divides $m$ and $a$ divides $n$, then $a$ divides $m + n$.

<u>Proof</u>: Assume that $n,m,a \in \Z$. Also assume that $a$ divides $m$ and $a$ divides $n$. We know that $m + n = m + n$. Since $a$ divides $m$, by *Def 2.11*, there exists $k_m \in \Z : m = ak_m$. We also know that since $a$ divides $n$, by *Def 2.11*, there exists $k_n \in \Z : n = ak_n$. Hence, $m + n = ak_m + ak_n = a(k_n + k_m)$. Since $k_n$ and $k_m$ are integers, by *Fact 2.3.2*, their sum is an integer, so let $k = k_n + k_m$. Thus, $m + n = ak$, so by *Def 2.11*, $a$ divides $n + m$. Therefore, given $n,m,a \in \Z$, if $a$ divides $m$ and $a$ divides $n$, then $a$ divides $m + n$. 

$\blacksquare$

<div style="break-after: page;"></div>



### Theorem 2.19

**Claim**: Assume $n,m,a \in \Z$. If $a$ divides $m$ and $a$ divides $n$, then $a$ divides $m - n$.

<u>Proof</u>: Assume that $n,m,a \in \Z$. Also assume that $a$ divides $m$ and $a$ divides $n$. We know that $m + n = m + n$. Since $a$ divides $n$, *Theorem 2.17* shows $a|-n$. Now, since $a$ divides $m$ and $a$ divides $-n$, *Theorem 2.18* implies $a$ must also divide their sum, $m + (-n) = m - n$. Therefore, given $n,m,a \in \Z$, if $a$ divides $m$ and $a$ divides $n$, then $a$ divides $m - n$.

$\blacksquare$

<div style="break-after: page;"></div>



### Problem 2.20

**Claim**: Given $a, b, m \in \Z$, the following statement is always true. If $ab$ divides $m$, then $a$ divides $m$ and $b$ divides $m$. 

<u>Proof</u>: Assume $a, b, m \in \Z$ and $ab$ divides $m$. Since $ab$ divides $m$, by *Def 2.11* there exists $k_1 \in \Z : m = abk_1$. If $a$ divides $m$, then by *Def 2.11* there also exists $k_2 \in \Z : m = ak_2$. Now, *Fact 2.3.2* tells us that the product of $k_1$ and $b$ is an integer. Since $m = abk_1$, we know if $k_2 = bk_1$, then $m = ak_2$ is true. Thus, by *Def 2.11*, $a$ divides $m$. Note a symmetrical proof exists if we say that, by *Def 2.11* there exists $k_3 \in \Z : m = bk_3$. Therefore, given $a, b, m \in \Z$ and $ab$ divides $m$, then it is always the case that,  $a$ divides $m$ and $b$ divides $m$.

$\blacksquare$

<div style="break-after: page;"></div>



### Theorem 2.21 - Transitivity of division of integers

**Claim**: If $a, b, c \in \Z$ are such $a$ divides $b$ and $b$ divides $c$, then $a$ divides $c$.

<u>Proof</u>: Let $a, b, c \in \Z$. Also assume that $a$ divides $b$ and $b$ divides $c$, then $a$ divides $c$. By *Def 2.11*, since $a$ divides $b$ and $b$ divides $c$, respectively, there exists $ k_b, k_c \in \Z : b = ak_b$ and $c = bk_c$. We then see that $c = ak_bk_c$. Since $k_b$ and $k_c$ are both integers, *Fact 2.3.2* implies their product is also an integer, so we let $k = k_bk_c$. Thus, $c = ak$ and as such, *Def 2.11* means that $a$ divides $c$. Therefore, if $a, b, c \in \Z$ are such $a$ divides $b$ and $b$ divides $c$, then $a$ divides $c$.

$\blacksquare$

<div style="break-after: page;"></div>



### Theorem 2.22

**Claim**: If $n \in \Z$ then $3$ divides $n + (n + 1) + (n + 2)$.

<u>Proof</u>: Assume that $n \in \Z$. By *Def 2.11* we show that $n = nk'$ because there exists $k' = 1$. Now, we can produce an equivalent equation by multiplying both sides by $3$ and adding $3$ to both sides like so 

$$3n = 3nk'$$

$$3n + 3 = 3nk' + 3 = 3(nk' + 1).$$

We know *Fact 2.3.2* implies $nk'$ is an integer, and further implies $nk' + 1$ is an integer. Thus, let $k = nk' + 1$ and now, $3n + 3 = 3k$. We can then show $n + (n + 1) + (n + 2) = 3n + 3$. Therefore, by *Def 2.11*, $3$ divides $n + (n + 1) + (n + 2)$. Therefore, if $n \in \Z$ then $3$ divides $n + (n + 1) + (n + 2)$.

$\blacksquare$

<div style="break-after: page;"></div>

