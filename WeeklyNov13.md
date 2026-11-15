# Problem 6.14

---

A special chessboard is $2$ squares wide and n squares long. Using $n$ blank
dominoes that are $1$ square by $2$ squares, there are many ways to perfectly cover this chessboard
with no overlap. How many? Prove your answer.

Claim: For all $n \in \mathbb{N}$, for any $2 \times n$ chessboard, the number of ways to cover it with dominoes is $F_{n+1}$.

We proceed by induction, so there are two cases.

*(i).* Consider $n = 1$ and $n = 2$. If $n = 1$, then we can only fit $1$ domino on the board. So, there is only $1$ way to cover it. We know $1 = F_2$. Subsequently, if $n = 2$, then we can either fit $2$ dominos vertically or horizontally. So, there are $2$ ways to cover it. We know $2 = F_3$. Therefore, our original claim holds when $n = 1$ and $n = 2$.
 
*(ii).* Assume there exists some $n \in \mathbb{N}$ such that a $2 \times n$ board can be covered in $F_{n+1}$ ways and a $2 \times n-1$ board can be covered in $F_n$ ways. Now consider a $2 \times (n+1)$ board called $B$. There are two ways to cover $B$. 

1. Let $B$ have a horizontal domino in the $n+1^{st}$ row. Now, the uncovered tiles of $B$ make a $2 \times n$ board. By our inductive hypothesis, there are $F_{n+1}$ ways to cover $B$ in this case.

2. Let $B$ have two vertical dominoes in the $n + 1^{st}$ and $n^{th}$ rows. Now the uncovered tiles of $B$ make a $2 \times n-1$ board. By our inductive hypothesis, there are $F_n$ ways to cover $B$ in this case.

Then, the total number of ways to cover $B$ is $F_{n+1} + F_n$. Now the Definition of Fibonacci Numbers tells us that there are $F_{n+2}$ ways to cover $B$. Therefore, there are $F_{n+2}$ ways to cover a $2 \times n+1$ board only when there are $F_{n+1}$ ways to cover a $2 \times n$ board and $F_n$ ways to cover a $2 \times n - 1$ board. 

So by the PMI, the number of ways to cover a $2 \times n$ board is $F_{n+1}$.

$\blacksquare$

---

# Problem 6.15

---

Consider a grid of squares that is $2^n$ squares wide by $2^n$ squares long, where $n \in \mathbb{N}$. One of the squares has been cut out, but you don’t know which one! You have a bunch of L-shapes made up of 3 squares. Prove that you can perfectly cover this chessboard with the
L-shapes (with no overlap) for any $n \in \mathbb{N}$. Figure 6.1 depicts one possible covering for the case involving $n = 2$.

*Proof.*

We proceed by induction, so there are two cases.

*(i).* Consider a $2 \times 2$ board. Observe that if any tile is empty, we can fill the remaining tiles with $1$ piece. Thus, our original statement holds when $n = 1$.

*(ii).* Assume there exists some $n \in \mathbb{N}$ such that we can perfectly cover every $2^n \times 2^n$ board with an empty square. Now consider a $2^{n+1} \times 2^{n+1}$ board, with some square removed, called $B$. Then $B$ has a length and width of $2^n(2^n)$. Thus, we can split $B$ into four $2^n \times 2^n$ quadrants. Now assume the removed square is in quadrant $B_i$. Our inductive hypothesis implies we can perfectly cover $B_i$. Now, define the middle to be the $2 \times 2$ area in the middle of $B$. Now, temporarily remove every square in the middle that doesn't belong to $B_i$. By our inductive hypothesis, there is a way to cover every quadrant except for the $3$ squares in the middle. But we can always cover those $3$ squares with an L-shaped piece. Thus, we can always cover every quandrant. Therefore, we can cover $B$. 

Thus, by the PMI, we can cover every $2^n \times 2^n$ board.

$\blacksquare$