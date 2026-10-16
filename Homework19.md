Grant Smith, Connor Flannagan

### Exercise 5.10

*Are $\emptyset$ and \set{\emptyset} the same?*

No. $|\emptyset| = 0$. But the $|\set{\emptyset}| = 1$.

---

### Theorem 5.11

*Suppose that $A, B$, and $C$ are sets. If $A \subseteq B$ and $B \subseteq C$, then $A \subseteq C$.*

*Proof.*

Assume that $B, C$ are sets. Also assume that $B \subseteq C$ and  $A \subseteq B$. Note that, by Definition **5.6**, every element of $B$ is also an element of $C$. Then the set $A$ can only contain elements of $C$. Thus, $A \subseteq C$.

$\blacksquare$

---

### Exercise 5.16 

*Suppose that the universe of discourse is $U = \set{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}$. Let $A = \set{1, 2, 3, 4, 5}$, $B = \set{1, 3, 5}$, and $\set{C = {2, 4, 6, 8}}$. Find each of the following.*

**(a)** $A \cap C = \set{2, 4}$

**(b)** $B \cap C = \emptyset$

**(c)** $A \cup B = A$

**(d)** $B^c = \set{2, 4, 6, 7, 8, 9, 10}$

**(e)** $(A \cup B)^c = A^c$

**(f)** $A^c \cap B^c = \set{6, 7, 8, 9, 10}$

--- 

### Exercise 5.17

*Suppose that the universe of discourse is $U = \mathbb{R}$. Let $A = [-3,-1), B = (-2.5, 2), \text{ and } C = (-2, 0]$. Find each of the following.*

**(a)** $A^c = \set{x \in \mathbb{R} : x < -3 \text{ or } x \geq -1}$.

**(b)** $A \cap B = \set{x \in \mathbb{R} : -2.5 < x < -1}$.

**(c)** $A \cup B = \set{x \in \mathbb{R} : -3 \leq x \leq 2}$.

**(d)** $(A \cap B)^c = \set{x \in \mathbb{R} : x \notin (A \cap B)}$.

**(e)** $(A \cup B)^c  = \set{x \in \mathbb{R} : x \notin (A \cup B)}$.

**(f)** $A$ \ $(B \cup C) = \set{x \in \mathbb{R} : x \in A \text{ and } x \notin (B \cup C) }$.

---

### Theorem 5.18

Let $A$ and $B$ be sets. If $A \subseteq B$, then $B^c \subseteq A^c$.

Assume $A$ and $B$ are sets with a universe of discourse $U$. Also assume $A \subseteq B$. Let there $\exists x : x \notin B$. By Definition **5.6**, then $x \notin A$ as well. Thus, $x \in A^c$ and $x \in B^c$. Therefore, 

---

### Proposition 5.20

*The statement “$A = B$” is equivalent to the statement “$A$ and $B$ contain precisely the same elements.”*

*Proof.*

We use proof by contradiction, so assume that $A = B$ is equivalent to the statement “$A$ and $B$ **do not** contain precisely the same elements.” Now, without the loss of generality, let there $\exists x \in A$ for some $x \notin B$. But now $A$ cannot be equal to $B$, because $x \notin B$. Thus, our previous assumption leads to a contradiction. Therefore, the statement “$A = B$” is equivalent to the statement “$A$ and $B$ contain precisely the same elements.”

$\blacksquare$