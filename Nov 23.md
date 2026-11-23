
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

*Proof.* Define $R$ as the relation of congruence modulo $a$. Let $nRk$ and $kRj$ for all integers $n,k,j$, then consider the following. 

*R is Symmetric.* The definition of congruence modulo tells us that $a$ divides $n-k$. Then, we know $a$ divides $-(k-n)$. Now, theorem $2.17$ implies $a$ divides $(k-n)$. So $kRn$. Thus, $R$ is symmetric. 

*R is Transitive.* The definition of divisibility implies $ax = n-k$ and $ay = k - j$ for some integers $x, y$. Then, $k = ay + j$. Now,
$$
\begin{align}
ax &= n-(ay+j) \\
ax &= n - ay - j \\
ax + ay &= n - j \\
a(x+y) &= n - j.
\end{align}
$$
Fact 2.3 now implies $x+y$ is an integer. So, $a$ divides $n-j$. Thus, $R$ is transitive. 

Since $R$ is symmetric and transitive, exercise $7.7$ tells us that $R$ must be reflexive. So, $R$ is symmetric, transitive, and reflexive. Therefore, congruence modulo is an equivalence relation. $\blacksquare$

---

# Exercise 7.12

Consider the equivalence relation on $\mathbb{Z}$ of congruence modulo $6$. What is [2]?
What about [5]? How many distinct equivalence classes are there?

Definition $7.11$ tells us [2] $= \set{n \in \mathbb{Z} : 6|(2-n)}$ and [5] $= \set{n \in \mathbb{Z} : 6|(5-n)}$. We know there are infinite multiples of $6$. We also know $i - n$ for some $i$ and for all $n$ can generate any integer. So, we know there will always be some $n$ that makes $i-n$ divisible by $6$. So there are an infinite number of relations.



---

# Theorem 7.14

Fix an equivalence relation $R$ on a set $S$.

1. If $x \in [y]$ then $[x] = [y]$.

*Proof.*

Assume $x\in[y]$. By Definition 7.11, $yRx$. Since $R$ is symmetric, $xRy$. We first show $[x]\subseteq[y]$. Let $z\in[x]$ be arbitrary. \textit{Definition 7.11} implies $xRz$. Since $yRx\text{ and }xRz$, transitivity implies $yRz$. Thus, $z\in[y]$. Therefore, $[y]\subseteq[x]$. We now show $[y]\subseteq[x]$. Let $z\in[y]$ be arbitrary. Then $yRz$. Since $xRy\text{ and }yRz$, transitivity implies $xRz$. Thus, $z\in[x]$. Therefore, $[y]\subseteq[x]$. By \textit{Definition 5.19}, $[x]=[y]$. Therefore, if $x\in[y]$, then $[x]=[y]$. %Thought process: Membership is an equivalence class gives us a relation between the two class representatives. Symmetry and transitivity then let us transfer membership from one class to the other. $\blacksquare$

2. If $x \notin [y]$ then $[x] \cap [y] = \emptyset$. 

*Proof.* Assume $x\notin[y]$. We will prove this statement by contradiction. Thus, assume $[x]\cap[y]\neq\emptyset$. Then there exists $z\in[x]\cap[y]$. Therefore, $z\in[x]$ and $z\in[y]$. \textit{Definition 7.11} implies $xRz$ and $yRz$. Since $R$ is symmetric, $zRx$. Since $yRz$ and $zRx$, transitivity implies $yRx$. Definition 7.11 then implies $x\in[y]$. This contradicts the assumption that $x\notin[y]$. Therefore, $[x]\cap[y]=\emptyset$. Thus, if $x\notin[y]$, then $[x]$ and $[y]$ are disjoint. $\blacksquare$

3. $\bigcup_{x \in S} [x] = S$.

*Proof.* We prove equality by showing both set inclusions. 

$(\subseteq)$ Let $y\in\bigcup_{x\in S}[x]$. By Definition 7.13, $y\in[x]$ for some $x\in S$. Definition 7.11 implies $y\in S$. Thus, $\bigcup_{x\in S}[x]\subseteq S$. 

$(\supseteq)$ Let $y\in S$ be arbitrary. Since $R$ is reflexive, $yRy$. Definition 7.11 implies $y\in[y]$. Since $y\in S$, the equivalence class $[y]$ is one of the sets included in $\bigcup_{x\in S}[x]$. Therefore, $S\subseteq\bigcup_{x\in S}[x]$. By Definition 5.19, $\bigcup_{x\in S}[x]=S$. 

Therefore, the union of all equivalence classes of $R$ is $S$.


---

# Theorem 7.15

Consider the following cases. 

($[a]=[b]\implies a\sim b$) Assume $[a]=[b]$. Since $\sim$ is reflexive, $a\sim a$. Thus, Definition 7.11 implies $a\in[a]$. Since $[a]=[b]$, we have $a\in[b]$. Definition 7.11 implies $b\sim a$. Since $\sim$ is symmetric, $a\sim b$. Therefore, $[a]=[b]\implies a\sim b$. 

($a\sim b\implies[a]\cap[b]\neq\emptyset$) Assume $a\sim b$. Definition 7.11 implies $b\in[a]$. Since $\sim$ is reflexive, $b\sim b$, so $b\in[b]$. Thus, $b\in[a]\cap[b]$. Therefore, $[a]\cap[b]\neq\emptyset$. Hence, $a\sim b\implies[a]\cap]b]\neq\emptyset$. 

($[a]\cap[b]\neq\emptyset\implies a\in[b]$) Assume $[a]\cap[b]\neq\emptyset$. Then there exists $x\in[a]\cap[b]$. Thus, $x\in[a]$ and $x\in[b]$. Definition 7.11 implies $a\sim x$ and $b\sim x$. Since $\sim$ is symmetric, $x\sim a$. Since $b\sim x$ and $x\sim a$, transitivity implies $b\sim a$. Definition 7.11 implies $a\in[b]$. Therefore, $[a]\cap[b]\neq\emptyset\implies a\in[b]$. 

($a\in[b]\implies[a]=[b]$) Assume $a\in[b]$. Theorem 7.14 implies $[a]=[b]$. Therefore, $a\in[b]\implies[a]=[b]$. 

Since we have proved $$[a]=[b]\implies a\sim b\implies[a]\cap[b]\neq\emptyset\implies a\in[b]\implies[a]=[b]$$ all four statements are equivalent. $\blacksquare$


