Grant Smith

CSCI 432 

Homework 11

1. No, all classical reversible operations cannot be valid quantum operations. Consider the following algorithm $ReversibleRoot$ with a square number $x : x, \sqrt{x} \in \Z+$ and a bit $i$:


```
ReversibleRoot(x, i):
    s = sqrt(x)
    if i = 0, return s, i
    if i = 1, return -s, i
```

Recall that the standard square root proceedure is not reversable, as $-2$ and $2$ squared both can equal $4$. Thus, given $4$ we do not know if we should output a negative or positive number. The above algorithm, however, ommits this issue by passing a 'flag' with the input integer that tells us if the root is negative or positive, which we do by negating the result. Therefore, any computational system, such as classical, capable of doing $sqrt$ and $negate$ can also do $ReversibleRoot$. But, the $sqrt$ operation is not reversable, so a quantum computing system cannot perform it. So, a quantum computing system cannot perform $ReversibleRoot$. 

<div style="page-break-after: always;"></div>

2. The following quantum algorithm on two qubits perserves the unitary property.

```
DoubleHadamard(A, B):
    Hadamard A
    Hadamard B
    A, B = extract A, B
    return |AB}
```

| state | amplitude |
| --- | --- | 
| $\vert 00 \rangle$ | $\sqrt{1/4}$ |
| $\vert 01 \rangle$ | $\sqrt{1/4}$ |
| $\vert 10 \rangle$ | $\sqrt{1/4}$ |
| $\vert 11 \rangle$ | $\sqrt{1/4}$ |

Since $4 * sqrt{1/4}^2 = 1$


<div style="page-break-after: always;"></div>

3. We know that Hadamard distributes values evenly between a single $\vert i \rangle $. We also know that, due to the unitary property, the magnitude of this ket is $1$. Treat kets as vectors $\langle a_0, a_1 \rangle$ where $a$ is the amplitude for the given value. Therefore, if these amplitudes are multiplied together, they will be evenly distrubuted amongst all bits. We can do this similiarly to how we compress probabilities, i.e. if $a_0$ and $b_0$ are for the same value, $0$, then they can multiplied to get the total amplitude for the entire bit sequence, (if it's just comprised of bits $a$ and $b$), but this can extended to any number of bits.  

<div style="page-break-after: always;"></div>

$\texttt{Sources}$
1. https://www.sciencedirect.com/topics/computer-science/hadamard-gate

