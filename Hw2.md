*def 1.* Denote the set of integers $\Z = \{..., -2, -1, 0, 1, 2\}$

*def 2.* An integer $o$ is odd if $2k + 1: k \in \Z$

*def 3.* An integer $e$ is even if $2i : i \in \Z$

*axiom 1.* Sums and products of integers are integers.

### Problem 2.8
**Claim**: The product of an odd integer & even integer is odd.

<u>Proof</u>:

Recall $o$ is an odd integer & $e$ is an even integer

Now there are two cases:

Just kidding 

Note that $2(0) + 1 = 1$, thus $1$ is odd

Note that $2(0) = 0$, thus $0$ is even

Observe that $1 * 0 = 0$, results in an even product

Thus, by counter example, the claim is false

$\blacksquare$

### Problem 2.9 
**Claim**: The product of two odd integers is odd.

<u>Proof</u>:

Assume $n$ and $m$ are odd integers.

Using *def 2* fix values of $k$, called integers $k_n, k_m : n = 2k_n + 1, m = 2k_m + 1$

Now, we know $n * m = (2k_n + 1)(2k_m + 1) = 4k_nk_m + 2k_n + 2k_m + 1 = 2(2k_nk_m + k_n + k_m) + 1$

Note that $2$, $k_n$, and $k_m$ are all integers. 

Thus, by *axiom 1* the term $2k_nk_m + k_n + k_m$, is an integer, so let $k = 2k_nk_m + k_n + k_m$

Then, $2(2k_nk_m + k_n + k_m) + 1 = 2k + 1$

Therefore, $n * m = 2k + 1 = o$

So, by *def 2*, the product of two odd integers is odd.

$\blacksquare$

### Problem 2.10
**Claim**: If at least one of a pair of integers is even, then their product is even. 

<u>Proof</u>:

Let $n$ and $m$ be a pair of integers. 

Since at least $1$ integer of the pair must be even, assume $n$ to always be even. 

Now, from *def 3*, fix some value of $i$ called $i' : n = 2i'$

So, $n * m = 2i' * m$

Since $2, i', m \in \Z$, by *axiom 1* and the definition of $m$, the term $(i'*m)$ is an integer.

Thus, let $i = i' * m$ 

Now $2(i' * m) = 2i = e$

Therefore, by *def 3*, the product of a pair of integers is even, if at least $1$ of the pair is even. 

$\blacksquare$
