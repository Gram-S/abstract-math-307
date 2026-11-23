
Grant Smith, Lexi Gladeau
# Exercise 7.6

Which of these properties are satisfied by which of your examples from Exercise
$7.4$? Make sure to prove your answers.

Impossible for $1$ since $N$ is dependent on another relation. Thus, if the $R$ relation is transitive, then $N$ is not transitive because $xRx$ would mean $x \not N x$. This is the case for all properties. 

*Proof.* We know $2$ is reflexive, symmetric, and transitive, but not antisymmetric. Consider, 
* By the definition of an anagram, a word is always an anagram of itself. So, all words in $S$ are anagrams of themselves, thus $R$ is reflexive. 
* Assume $aRb$. It follows then that $b$ contains the same letters, in the same quanities as $a$. So $bRa$. Thus, $2$ is symmetric. 
* Consider the word "Eat". Assume "Eat"$R$"Tea" and "Tea"$R$"Eat". But these words are not the same because their letters are in different positions. So $2$ is not antisymmetric.
* We know by Exercise $7.7$ that since $2$ is symmetric and reflexive, that $2$ must also be transitive. 
Therefore, $2$ is reflexive, symmetric, and transitive, but not antisymmetric.
$\blacksquare$

*Proof.* We know $3$ is reflexive and antisymmetric, but not symmetric or transitive. Consider, 
* For all mathematicians, they are a member of their own cult. So $3$ is reflexive. 
* For different mathematicians $x, y$, assume $xRy$. Since it isn't possible for a cult to have $2$ owners, then $yRx$ is impossible. So $3$ is not symmetric. 
* Let $x, y$ be mathematicians. Assume $xRy$ and $yRx$. We know $x \not = y$ is impossible, so $x = y$. Thus, $3$ is antisymmetric.
* Let $x, y, z$ be mathematicians. Assume $xRy$ and $yRz$. But this does not imply that $z$ is a member of $x$'s cult. So $3$ is not transitive. 
Therefore, $3$ is reflexive and antisymmetric, but not symmetric or transitive.
$\blacksquare$

*Proof.* We know $4$ is reflexive, antisymmetric, and transitive, but not symmetric. Consider,
* We know for natural numbers, $x$, then $x \leq x$. So $4$ is reflexive. 
* Consider $1 \leq 2$. Then $2 \leq 1$ is a contradiction. So $4$ is not symmetric. 
* For all natural numbers $x, y$ assume $x \leq y$ and $y \leq x$. It follows that $x = y$. So $4$ is antisymmetric. 
* Assume $x \leq y$ and $y \leq z$ for all natural numbers $x, y, z$. It follows that $x \leq z$. So $4$ is transitive. 
Therefore, $4$ is reflexive, antisymmetric, and transitive, but not symmetric.
$\blacksquare$

---

# Theorem 7.10

Fix $a \in \mathbb{Z}$. The relation of congruence modulo $a$ is an equivalence relation.

*Proof.* Define $R$ as the relation of congruence modulo $a$. Let $xRy$ and $yRz$ for all integers $x, y, z$. consider the following. 

*Reflexive Case.* For all natural numbers $i$, consider the definition of congruent modulo for $n = i$, $k = i$. We know any integer divides $0$, so $a|(i-i)$. Thus, $iRi$ for all $i$. The definition of reflexive relations tells us $R$ is reflexive. 

*Symmetric.* 

---

# Exercise 7.12

Consider the equivalence relation on $\mathbb{Z}$ of congruence modulo $6$. What is [2]?
What about [5]? How many distinct equivalence classes are there?

---

# Theorem 7.14

Fix an equivalence relation $R$ on a set $S$.

1. If $x \in [y]$ then $[x] = [y]$.
2. If $x \notin [y]$ then $[x] \cap [y] = \emptyset$. 
3. $\bigcup_{x \in S} [x] = S$.

---

# Theorem 7.15

* $[a] = [b]$ 
* $a \sim b$ 
* $[a] \cap [b] \neq \emptyset$ 
* $a \in [b]$

