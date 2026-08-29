*def 1.0.* Define the set of integers as $\Z = \{..., -2, -1, 0, 1, 2, .. \}$.

*def 2.1.* An integer $n$ is even if $n = 2k$ for some $k \in \Z$.

*def 2.2.* An integer $n$ is odd if $n = 2k + 1$ for some $k \in \Z$.

*Fact 2.3.1.* Every integer is either even or odd, but never both.

*Fact 2.3.2* Sums and products of integers are integers.

*def 2.11.* An integer $n$ divides the integer $m$ written $n|m$, if and only if, there exists $k \in \Z : m = nk$.  



### Question 2.12

**Question**: How are $n|m$ and $n/m$ different?

**Answer**: Assume that $n$ and $m$ are integers, though $n/m$ does not require them to be, $n|m$ does by *def 2.11*. Now note that by *def 2.11*, $n|m$ is a statement that is either true or false. However, $n/m$ is not a statement that is true or false, but a mathematical operation that is not strictly true of false. 

<div style="break-after: page;"></div>



### Problem 2.13

**Claim**: If $m \in \Z$ and $6|m$, then $3|m$. 

<u>Proof</u>:

Assume that $m \in \Z$ and $6|m$. Since $6|m$, using *def 2.11*, fix an integer value of $k$ called $k'$ so that $m = 6k' = 3(2k')$. Note that $2$ and $k'$ are integers, thus, by *fact 2.3.2*, their product is an integer. So, by *def 2.11*, we let $k = 2k'$. Now $3(2k') = 3k$ and thus, $m = 3k$. Therefore, by *def 2.11*, if $6|m$, then $3|m$.  

$\blacksquare$

<div style="break-after: page;"></div>



### Problem 2.14

**Claim**: If $m \in \Z$ and $6|m$, then $4|m$.

<u>Proof</u>:

Assume that $m \in \Z$ and $6|m$. Now let $m = 6$. Then, $6|6$ is true because of *def 2.11*, where $6 = 6(1)$. However, $4|6$ is false because of *def 2.11*, where $6 = 4k$. We know $k = \frac{6}{4} = \frac{3}{2}$. But $\frac{3}{2} \notin \Z$ by *def 1.0* and thus $k \neq \frac{3}{2}$. Thus, $4$ cannot divide $m = 6$. Therefore, the claim is false since for $m = 6$, then $6|m$ is true but $4|m$ is not.

$\blacksquare$

<div style="break-after: page;"></div>



### Theorem 2.15

**Claim**: If $n, m, a \in \Z$ and $a|m$, then $a|mn$.

<u>Proof</u>:

Assume that $n, m, a \in \Z$ and $a|m$. Since $a|m$, using *def 2.11*, fix an integer value of $k$ called $k'$ so that $m = ak'$. Note that both $k'$ and $n$ are integers, so by *def 2.11*, let $k = nk'$. We know that, if $a|mn$, then $mn = ak = ank'$. We can divide both sides by $n$ and this equation remains true, so $m = ak'$. So, there must be some value of $k$ that makes this equation true. Thus, $a|mn$ is true. Therefore, if $a|m$, then $a|mn$.

$\blacksquare$

<div style="break-after: page;"></div>
