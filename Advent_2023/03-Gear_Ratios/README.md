# Day 03: Gear Ratios
> SUMMARY
<img src=https://github.com/Kyros0718/Advent_of_Code/blob/main/Media/2023/babyelf_surounded_by_mechanicalgears.png>

You and the Elf eventually reach a ${\color{green}gondola}$ ${\color{green}lift}$ station; he says the gondola lift will take you up to the $\color{VioletRed}{\textbf{water}}$ $\color{VioletRed}{\textbf{source}}$, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can $\color{VioletRed}{\textbf{add}}$ $\color{VioletRed}{\textbf{up}}$ $\color{VioletRed}{\textbf{all}}$ $\color{VioletRed}{\textbf{the}}$ $\color{VioletRed}{\textbf{part}}$ $\color{VioletRed}{\textbf{numbers}}$ in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently $\color{VioletRed}{\textbf{any}}$ $\color{VioletRed}{\textbf{number}}$ $\color{VioletRed}{\textbf{adjacent}}$ $\color{VioletRed}{\textbf{to}}$ $\color{VioletRed}{\textbf{a}}$ $\color{VioletRed}{\textbf{symbol}}$, even diagonally, is a "part number" and should be included in your sum. (Periods (`.`) do not count as a symbol.)

Here is an example engine schematic:

| `467..114..`<br>`...*......`<br>`..35..633.`<br>`......#...`<br>`617*......`<br>`.....+.58.`<br>`..592.....`<br>`......755.`<br>`...$.*....`<br>`.664.598..` |
| --- |

In this schematic, two numbers are $\color{VioletRed}{\textbf{not}}$ part numbers because they are not adjacent to a symbol: `114` (top right) and `58` (middle right). Every other number is adjacent to a symbol and so $\color{VioletRed}{\textbf{is}}$ a part number; their sum is **`4361`**.

Of course, the actual engine schematic is much larger. $\color{VioletRed}{\textbf{What}}$ $\color{VioletRed}{\textbf{is}}$ $\color{VioletRed}{\textbf{the}}$ $\color{VioletRed}{\textbf{sum}}$ $\color{VioletRed}{\textbf{of}}$ $\color{VioletRed}{\textbf{all}}$ $\color{VioletRed}{\textbf{of}}$ $\color{VioletRed}{\textbf{the}}$ $\color{VioletRed}{\textbf{part}}$ $\color{VioletRed}{\textbf{numbers}}$ $\color{VioletRed}{\textbf{in}}$ $\color{VioletRed}{\textbf{the}}$ $\color{VioletRed}{\textbf{engine}}$ $\color{VioletRed}{\textbf{schematic?}}$

> Your puzzle answer was **`528819`**

<br>

##  Part Two
The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A $\color{VioletRed}{\textbf{gear}}$ is any `*` symbol that is adjacent to $\color{VioletRed}{\textbf{exactly}}$ $\color{VioletRed}{\textbf{two}}$ $\color{VioletRed}{\textbf{part}}$ $\color{VioletRed}{\textbf{numbers}}$. Its $\color{VioletRed}{\textbf{gear}}$ $\color{VioletRed}{\textbf{ratio}}$ is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

|`467..114..`<br>`...*......`<br>`..35..633.`<br>`......#...`<br>`617*......`<br>`.....+.58.`<br>`..592.....`<br>`......755.`<br>`...$.*....`<br>`.664.598..` |
| --- |

In this schematic, there are $\color{VioletRed}{\textbf{two}}$ gears. The first is in the top left; it has part numbers `467` and `35`, so its gear ratio is `16345`. The second gear is in the lower right; its gear ratio is `451490`. (The `*` adjacent to `617` is $\color{VioletRed}{\textbf{not}}$ a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces **`467835`**.

$\color{VioletRed}{\textbf{What}}$ $\color{VioletRed}{\textbf{is}}$ $\color{VioletRed}{\textbf{the}}$ $\color{VioletRed}{\textbf{sum}}$ $\color{VioletRed}{\textbf{of}}$ $\color{VioletRed}{\textbf{all}}$ $\color{VioletRed}{\textbf{of}}$ $\color{VioletRed}{\textbf{the}}$ $\color{VioletRed}{\textbf{gear}}$ $\color{VioletRed}{\textbf{ratios}}$ $\color{VioletRed}{\textbf{in}}$ $\color{VioletRed}{\textbf{your}}$ $\color{VioletRed}{\textbf{engine}}$ $\color{VioletRed}{\textbf{schematic?}}$

> Your puzzle answer was **`ANSWER`**.

<br>
<br>

# Credits

> [!NOTE]  
> **Image:** [_imagine.art_](https://www.imagine.art/)<br>
> **Puzzles:** [_Advent of Code_](https://adventofcode.com/)




