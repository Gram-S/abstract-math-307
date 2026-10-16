
### Theorem 5.8

*Let $S$ be a set. Then $S \subseteq S$ and $\emptyset \subseteq S$.*

*Proof.*

Let $S$ be an arbitrary set. By **Def 5.6**, we can show that a set $S'$ is a subset of $S$ by using the following the method to build $S'$. Let $S'$ originally be the $\emptyset$. Then add to $S'$, some elements also in $S$. Now, we can build $S'$ in the following ways.

Add no elements of $S$ into $S'$. Now $S' = \emptyset$. Thus, $\emptyset \subseteq S$. 

Add all elements of $S$ into $S'$. Now $S' = S$. Thus, $S \subseteq S$.

Therefore, if $S$ is a set, then $S \subseteq S$ and $\emptyset \subseteq S$.

$\blacksquare$

---

### Theorem 5.18

Let $A$ and $B$ be sets. If $A \subseteq B$, then $B^c \subseteq A^c$.

Assume we have two sets, $A$ and $B$. We then use proof by contrapositive. Thus we assume $B^c \not\subseteq A^c$. By Definition **5.6**, there exists $x \in B^c$ such that $x \not\in A^c$. Definition **5.14** then tells us that $x$ is in $A$ but not in $B$. Hence, $A \not\subseteq B$. Thus, if $B^c \not\subseteq A^c$, then $A \not\subseteq B$. Therefore, Theorem **3.34** implies if $A \subseteq B$, then $B^c \subseteq A^c$. 

$\blacksquare$