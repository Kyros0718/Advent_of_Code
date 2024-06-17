# Day 05: Supply Stacks

<img src=https://github.com/Kyros0718/Advent_of_Code/blob/main/Media/2022/baby%20elf%20sitting%20on%20crates.png>

The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked $\color{VioletRed}{\textbf{crates}}$, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

The ship has a $\color{VioletRed}{\textbf{giant}}$ $\color{VioletRed}{\textbf{cargo}}$ $\color{VioletRed}{\textbf{crane}}$ capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her $\color{VioletRed}{\textbf{which}}$ crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates $\color{VioletRed}{\textbf{and}}$ the rearrangement procedure (your puzzle input). For example:

| `     [D]     `<br>`[N] [C]    `<br>`[Z] [M] [P]`<br>`  1   2   3  `<br><br>`move 1 from 2 to 1`<br>`move 3 from 1 to 3`<br>`move 2 from 2 to 1`<br>`move 1 from 1 to 2` |
| :--- |

In this example, there are three stacks of crates. Stack 1 contains two crates: crate `Z` is on the bottom, and crate `N` is on top. Stack 2 contains three crates; from bottom to top, they are crates `M`, `C`, and `D`. Finally, stack 3 contains a single crate, `P`.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

|`[D]        `<br>`[N] [C]    `<br>`[Z] [M] [P]`<br>`  1   2   3  ` |
| --- |

In the second step, three crates are moved from stack 1 to stack 3. Crates are moved $\color{VioletRed}{\textbf{one}}$ $\color{VioletRed}{\textbf{at}}$ $\color{VioletRed}{\textbf{a}}$ $\color{VioletRed}{\textbf{time}}$, so the first crate to be moved (`D`) ends up below the second and third crates:

| `        [Z]`<br>`        [N]`<br>`    [C] [D]`<br>`    [M] [P]`<br>`  1   2   3  ` |
| --- |

Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved $\color{VioletRed}{\textbf{one}}$ $\color{VioletRed}{\textbf{at}}$ $\color{VioletRed}{\textbf{a}}$ $\color{VioletRed}{\textbf{time}}$, crate `C` ends up below crate `M`:

| `        [Z]`<br>`        [N]`<br>`[M]     [D]`<br>`[C]     [P]`<br>`  1   2   3  ` |
| --- |

Finally, one crate is moved from stack 1 to stack 2:

| `        [Z]`<br>`        [N]`<br>`        [D]`<br>`[C] [M] [P]`<br>`  1   2   3  ` |
| --- |

The Elves just need to know $\color{VioletRed}{\textbf{which}}$ $\color{VioletRed}{\textbf{crate}}$ $\color{VioletRed}{\textbf{will}}$ $\color{VioletRed}{\textbf{end}}$ $\color{VioletRed}{\textbf{up}}$ $\color{VioletRed}{\textbf{on}}$ $\color{VioletRed}{\textbf{top}}$ $\color{VioletRed}{\textbf{of}}$ $\color{VioletRed}{\textbf{each}}$ $\color{VioletRed}{\textbf{stack}}$; in this example, the top crates are `C` in stack 1, `M` in stack 2, and `Z` in stack 3, so you should combine these together and give the Elves the message **`CMZ`**.

$\color{VioletRed}{\textbf{After}}$ $\color{VioletRed}{\textbf{the}}$ $\color{VioletRed}{\textbf{rearrangement}}$ $\color{VioletRed}{\textbf{procedure}}$ $\color{VioletRed}{\textbf{completes,}}$ $\color{VioletRed}{\textbf{what}}$ $\color{VioletRed}{\textbf{crate}}$ $\color{VioletRed}{\textbf{ends}}$ $\color{VioletRed}{\textbf{up}}$ $\color{VioletRed}{\textbf{on}}$ $\color{VioletRed}{\textbf{top}}$ $\color{VioletRed}{\textbf{of}}$ $\color{VioletRed}{\textbf{each}}$ $\color{VioletRed}{\textbf{stack?}}$

> Your puzzle answer was **`ANSWER`**

<br>

##  Part Two


> Your puzzle answer was **`ANSWER`**.

<br>
<br>

# Credits

> [!NOTE]  
> **Image:** [_imagine.art_](https://www.imagine.art/)<br>
> **Puzzles:** [_Advent of Code_](https://adventofcode.com/)




