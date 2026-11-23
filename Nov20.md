
# Exercise 7.4

1. Let $S = \mathbb{Z}$ and $a, b \in S$. Let there be an arbitrary relation $N$. Then let $a$ be $R$-related to $b$, if and only if, $a$ is not $N$-related to $b$.
2. Let the universe of $S$ be the set of English words. Consider the anagram relation on $S$, which is given by, $a$ is a anagram of $b$, if and only if, $a$ contains the same letters, in the same quantities, as $b$. 
3. Let the universe of $S$ be the set of mathematicians. Consider the $P$ (Pythagoreas) relation on $S$, which is given by $aPb$, if and only if, $a$ is a member of a cult which $b$ owns (such Pythagoreas').
4.  Let $S=\mathbb{N}$. Define $xR_1y\iff x\le y$.

# Exercise 7.7

1. Consider the relation "greater than or equal to" on the set of integers. 

*Proof.* 
*Reflexive.* We know every element $x \in S$ is equal to itself. So $xRx$ for all $x$.
*Transitive.* Whenever $x \geq y$ and $y \geq z$ is true, then $x \geq z$ is true. 
*Not symmetric.* But, if $xRy$, then $x \gt y$ is possible. In this case, $y \gt x$ is false. So $xRy$ is satisfied but $yRx$ is not. $\blacksquare$

2. Define distance as $|x - y|$ for $x, y \in \mathbb{Z}$. Then, consider the relation "distance to $y$ is at most $1$" on the set of integers.

*Proof.* 
*Reflexive.* We know, for all integers $i$, then $|i - i| = 0$. 
*Symmetric.* Since addition is transitive, the sum is the same no matter if $xRy$ or $yRx$.
*Not Transitive.* Consider $1R2$ and $2R3$, but $|1 - 3| = 2$. So $1R2$ and $2R3$ is satisfied but $1R3$ is not.  

3. Define a null relation on a set $S$ to be a relation $R$ with the following property. For all elements of $S$, denoted $a,b$, then $a \not R b$. Then,

*Not Reflexive.* A null relation cannot be reflexive, since by definition, $a \not R a$.
*Symmetric & Transitive.* A null relation must be both symmetric and transitive. We show this by contradiction, so without the loss of generality, assume it is not symmetric. Thus, there exists some $x,y \in S$ such that $xRy$ but $y \not R x$. But, $xRy$ is a contradiction. So, null relations must symmetric. $\blacksquare$

