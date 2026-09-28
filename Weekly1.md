*def 1.0.* Define the set of integers as $\Z = \{..., -2, -1, 0, 1, 2, .. \}$.

*def 2.1.* An integer $n$ is even if $n = 2k$ for some $k \in \Z$.

*def 2.2.* An integer $n$ is odd if $n = 2k + 1$ for some $k \in \Z$.

*Fact 2.3.1.* Every integer is either even or odd, but never both.

*Fact 2.3.2* Sums and products of integers are integers.

*def 2.11.* An integer $n$ divides the integer $m$ written $\frac{m}{n}$, if and only if, there exists $k \in \Z : m = nk$.  

<hr />

### Theorem 2.4.
**Claim**: If $z \in \Z$ then the sum of $z$ and $z+1$ is odd.

<u>Proof</u>: 

Assume that $z \in \Z$.

Note that $1 \in \Z$, making it an integer by *def 1.0*.

Since both $1$ and $z$ are integers, $z+1 \in \Z$ by *Fact 2.3.2*.

Once again, we know $z + (z+1)$ must be an integer by *Fact 2.3.2*.

Now $z + z + 1 = 2z + 1$.

Since $z \in \Z$, let $k = z$ by *def 2.2*.

So $2z + 1 = 2k + 1$

Therefore, by *def 2.2*, the sum of $z$ and $z+1$ is odd.

$\blacksquare$

<div style="break-after: page;"></div>

### Problem 2.9. 
**Claim**: The product of two odd integers is odd.

<u>Proof</u>:

Assume $x$ and $y$ are odd integers.

Using *def 2.2*, fix values of $k$ called $k_x, k_y$ so that $x = 2k_x + 1, y = 2k_y + 1$.

Then, $x * y = (2k_x + 1)(2k_y+1) = 4k_xk_y + 2k_x + 2k_y + 1 = 2(2k_xk_y + k_x + k_y) + 1$.

Note that $2$ is an integer by *def 1.0* and $k_x, k_y$ are integers because of *def 2.2*.

Thus, by *Fact 2.3.2*, the term $2k_xk_y + k_x + k_y \in \Z$. 

So, by *def 2.2*, let $k = 2k_xk_y + k_x + k_y$. 

Then $x * y = 2(2k_xk_y + k_x + k_y) + 1 = 2k + 1$.

Thus, by *def 2.2*, the product of two odd integers is odd.

$\blacksquare$

<div style="break-after: page;"></div>

### Theorem 2.17.

**Claim**: If $n, m \in \Z$ and $n$ divides $m$, then $n$ divides $-m$.

<u>Proof</u>:

Assume that $n, m \in \Z$, since $n$ divides $m$, using *def 2.11*, fix an integer value of $k$ called $k'$ so that 
$
m = nk'.
$
Note that $-1$ is an integer by *def 1.0*. We can multiply both sides of the equation by the integer $-1$ and it will remain equal. 
Doing so, 
$-m = n(-k').$
Since $-k'$ is an integer by *fact 2.3.2*, we can let $k = -k'$, so $-m=nk$.
Thus, by *def 2.11*, $n$ divides $-m$. Therefore, if $n, m \in \Z$ and $n$ divides $m$, then $n$ also divides $-m$. 

$\blacksquare$

<div style="break-after: page;"></div>

### Theorem 2.21.

**Claim**: If $n, p, m \in \Z$ are such that $n$ divides $p$ and $p$ divides $m$, then $n$ divides $m$. 

<u>Proof</u>:

Assume that $n, p, m \in \Z$ and $n$ divides $p$ and $p$ divides $m$.
Using *def 2.11* fix integer values of $k$ called $k_p, k_m$ so that $p = nk_p, m = pk_m$. 
Note that $k_p$ and $k_m$ are integers, by *fact 2.3.2*, their product is also an integer. With, *def 2.11*, let $k = k_pk_m$. Now,
$$
m = pk_m = nk_pk_m = nk.
$$
Thus, $m = nk$, and by *def 2.11*, this means $n$ divides $m$. 
Therefore, if $n, p, m \in \Z$ and $n$ divides $p$ and $p$ divides $m$, then $n$ also divides $m$. 

$\blacksquare$
