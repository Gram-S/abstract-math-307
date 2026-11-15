# Theorem 6.18

Let $A$ be a finite set containing $n$ elements. Then $P(A)$ is a set with $2^n$ elements.

*Proof.*

Let there be set of binary strings $S = \set{1^*(0^*1^*)^*}$, such that every element of $S$ is length $n$. Now we can uniquely encode any arbitrary subset of $a \subseteq A$ with an element of $S$ since $S_i = 1$ if $A_i \in a$ and $0$ otherwise. Then the number of abritrary subsets for $A$ is equal to the number of binary strings of length $n$. Thus, there are exactly $2^n$ subsets of $A$. Therefore, by definition of the power set, $\mathcal{P}(A)$ contains $2^n$ elements.

$\blacksquare$