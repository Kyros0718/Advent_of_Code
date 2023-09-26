# Day 05: Supply Stacks

<img src=https://github.com/Kyros0718/Advent_of_Code/blob/main/Media/baby%20elf%20sitting%20on%20crates.png>

The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

| `     [D]     `<br>`[N] [C]    `<br>`[Z] [M] [P]`<br>`  1   2   3  `<br><br>move 1 from 2 to 1<br>move 3 from 1 to 3<br>move 2 from 2 to 1<br>move 1 from 1 to 2 |
| :--- |

In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

|`[D]        `<br>`[N] [C]    `<br>`[Z] [M] [P]`<br>`  1   2   3  ` |
| --- |

In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

| `        [Z]`<br>`        [N]`<br>`    [C] [D]`<br>`    [M] [P]`<br>`  1   2   3  ` |
| --- |

Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

| `        [Z]`<br>`        [N]`<br>`[M]     [D]`<br>`[C]     [P]`<br>`  1   2   3  ` |
| --- |

Finally, one crate is moved from stack 1 to stack 2:

| `        [Z]`<br>`        [N]`<br>`        [D]`<br>`[C] [M] [P]`<br>`  1   2   3  ` |
| --- |

The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top of each stack?

> Your puzzle answer was **`ANSWER`**

<br>

##  Part Two
It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that $\color{VioletRed}{\textbf{overlap}}$ $\color{VioletRed}{\textbf{at}}$ $\color{VioletRed}{\textbf{all}}$.

In the above example, the first two pairs (`2-4,6-8` and `2-3,4-5`) don't overlap, while the remaining four pairs (`5-7,7-9`, `2-8,3-7`, `6-6,4-6`, and `2-6,4-8`) do overlap:

- `5-7,7-9` overlaps in a single section, `7`.
- `2-8,3-7` overlaps all of the sections `3` through `7`.
- `6-6,4-6` overlaps in a single section, `6`.
- `2-6,4-8` overlaps in sections `4`, `5`, and `6`.

So, in this example, the number of overlapping assignment pairs is `4`.

$\color{VioletRed}{\textbf{In}}$ $\color{VioletRed}{\textbf{how}}$ $\color{VioletRed}{\textbf{many}}$ $\color{VioletRed}{\textbf{assignment}}$ $\color{VioletRed}{\textbf{pairs}}$ $\color{VioletRed}{\textbf{do}}$ $\color{VioletRed}{\textbf{the}}$ $\color{VioletRed}{\textbf{ranges}}$ $\color{VioletRed}{\textbf{overlap?}}$

The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top of each stack?

> Your puzzle answer was **`ANSWER`**.

<br>
<br>

# Credits

> [!NOTE]  
> **Image:** [_imagine.art_](https://www.imagine.art/)<br>
> **Puzzles:** [_Advent of Code_](https://adventofcode.com/)




