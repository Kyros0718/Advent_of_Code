# Day 01: Calorie Counting

<img src=https://github.com/Kyros0718/Advent_of_Code/blob/main/Media/baby%20elf%20carrying%20bags%20of%20cookies.png>

Santa's reindeer typically eat regular reindeer food, but they need a lot of ${\color{green}magical}$ ${\color{green}energy}$ to deliver presents on Christmas. For that, their favorite snack is a special type of ${\color{yellow}star}$ fruit that only grows deep in the jungle. The Elves have brought you on their annual expedition to the grove where the fruit grows.

To supply enough magical energy, the expedition needs to retrieve a minimum of ${\color{yellow}fifty}$ ${\color{yellow}stars}$ by December 25th. Although the Elves assure you that the grove has plenty of fruit, you decide to grab any fruit you see along the way, just in case.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants ${\color{yellow}one}$ ${\color{yellow}star}$. Good luck!

<br>

The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; the Elves' expedition traditionally goes on foot. As your boats approach land, the Elves begin taking inventory of their supplies. One important consideration is food - in particular, the number of  $\color{VioletRed}{\textbf{Calories}}$ each Elf is carrying (your puzzle input).

The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc. that they've brought with them, one item per line. Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.

For example, suppose the Elves finish writing their items' Calories and end up with the following list:

| 1000<br>2000<br>3000<br><br>4000<br><br>5000<br>6000<br><br>7000<br>8000<br>9000<br><br>10000 |
| :--- |

This list represents the Calories of the food carried by five Elves:

- The first Elf is carrying food with `1000`, `2000`, and `3000` Calories, a total of **`6000`** Calories.
- The second Elf is carrying one food item with **`4000`** Calories.
- The third Elf is carrying food with `5000` and `6000` Calories, a total of **`11000`** Calories.
- The fourth Elf is carrying food with `7000`, `8000`, and `9000` Calories, a total of **`24000`** Calories.
- The fifth Elf is carrying one food item with **`10000`** Calories.

In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the ${\color{white}most}$ Calories. In the example above, this is **`24000`** (carried by the fourth Elf).

Find the Elf carrying the most Calories. ${\color{white}How}$ ${\color{white}many}$ ${\color{white}total}$ ${\color{white}Calories}$ ${\color{white}is}$ ${\color{white}that}$ ${\color{white}Elf}$ ${\color{white}carrying?}$
> Your puzzle answer was **`71934`**

<br>

##  Part Two
By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually ${\color{white}run}$ ${\color{white}out}$ ${\color{white}of}$ ${\color{white}snacks}$.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the ${\color{white}top}$ ${\color{white}three}$ Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with `24000` Calories), then the third Elf (with `11000` Calories), then the fifth Elf (with `10000` Calories). The sum of the Calories carried by these three elves is **`45000`**.

Find the top three Elves carrying the most Calories. ${\color{white}How}$ ${\color{white}many}$ ${\color{white}Calories}$ ${\color{white}are}$ ${\color{white}those}$ ${\color{white}Elves}$ ${\color{white}carrying}$ ${\color{white}in}$ ${\color{white}total?}$

> Your puzzle answer was **`211447`**.

<br>
<br>

# Credits

> [!NOTE]  
> **Image:** [_imagine.art_](https://www.imagine.art/)<br>
> **Puzzles:** [_Advent of Code_](https://adventofcode.com/)




