*def 1.0.* Define the set of integers as $\Z = \{..., -2, -1, 0, 1, 2, .. \}$.

*def 2.1.* An integer $n$ is even if $n = 2k$ for some $k \in \Z$.

*def 2.2.* An integer $n$ is odd if $n = 2k + 1$ for some $k \in \Z$.

*Fact 2.3.1.* Every integer is either even or odd, but never both.

*Fact 2.3.2* Sums and products of integers are integers.

*def 2.11.* An integer $n$ divides the integer $m$ written $n|m$, if and only if, there exists $k \in \Z : m = nk$.  

#### Corollary 2.16

**Claim**: If $n, m \in \Z$ and $n|m$, then $n|m^2$.

<u>Proof</u>: Assume that $n, m \in \Z$ and $n|m$. Since $n|m$, by *def 2.11* fix an integer value of $k$ called $k'$ so that $m = nk'$. We can multiply both sides of the equation by the integer $m$ to get $m^2 = nk'm$. By *fact 2.3.2*, we know the product of $k'$ and $m$ is an integer, so let $k = k'm$. Now $m^2 = nk$, and thus, by *def 2.11*, $n|m^2$. Therefore, if $n, m \in \Z$ and $n|m$, then $n|m^2$.

$\blacksquare$

<div style="break-after: page;"></div>


#### Theorem 2.17

**Claim**: If $n, m \in \Z$ and $n|m$, then $n|-m$.

<u>Proof</u>: Assume that $n, m \in \Z$ and $n|m$. Since $n|m$, by *def 2.11* there exists $k' \in \Z : m = nk'$. We can multiply both sides of the equation by $-1$ to get $-m = -nk'$. By *fact 2.3.2*, we know the product of $k'$ and $-1$ is an integer, so let $k = -k'$. Now $-m = nk$, and thus, by *def 2.11*, $n|-m$. Therefore, if $n, m \in \Z$ and $n|m$, then $n|-m$.

$\blacksquare$

<div style="break-after: page;"></div>



