
# Exercise 7.4

1. Let $S = \mathbb{Z}$ and $a, b \in S$. Let there be an arbitrary relation $N$. Then let $a$ be $R$-related to $b$ if $a$ is not $N$-related to $b$.
2. Let the universe of $S$ be the set of English words. Consider the anagram relation on $S$, which is given by, $a$ is a anagram of $b$, if and only if, $a$ contains the same letters, in the same quantities, as $b$. 
3. Let the universe of $S$ be the set of mathematicians. Consider the $P$ (Pythagoreas) relation on $S$, which is given by $aPb$, if and only if, both $a$ and $b$ owned a cult (like Pythagoreas).
4.  Let the universe of $S$ be the human proteome. Consider the following relation "=" on $S$, for proteins $a$ and $b$, given by $a = b$, if and only if, $a$ and $b$ are modifications of the same protein. 

# Exercise 7.7

1. Consider the relation "greater than or equal to" on the set of integers. 

We know every element $x \in S$ is equal to itself. So $xRx$ for all $x$.
Whenever $x \geq y$ and $y \geq z$ is true, then $x \geq z$ is true. 
But, if $xRy$, then $x \gt y$ is possible. In this case, $y \gt x$ is false. So $xRy$ is satisfied but $yRx$ is not. 

2. Define distance as $|x - y|$ for $x, y \in \mathbb{Z}$. Then, consider the relation "distance is at most $1$" on the set of integers.

We know, for all integers $i$, then $|i - i| = 0$. 
Since addition is transitive, the sum is the same no matter if $xRy$ or $yRx$.
Consider $1R2$ and $2R3$, but $|1 - 3| = 2$. So $1R2$ and $2R3$ is satisfied but $1R3$ is not.  

3. No.

*Proof.* Let $S$ be an arbitrary set. We proceed by proof by contradiction, so assume, for some arbitrary $x, y \in S$ that $xRy$ such that $R$ is symmetric and transitive but not reflexive. Recall that definition of a symmetric relation implies $yRx$. Then, since $xRy$ and $yRx$, the definition of a transitive relation implies $xRx$. Since $x$ and $y$ are arbitrary, this is true for all $xRy$. Therefore, assuming $R$ exists is a contradiction. 

$\blacksquare$

