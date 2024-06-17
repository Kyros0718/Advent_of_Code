# Day 04: Scratchcards
> File contains list of Scratchcards with winning numbers and numbers you have. Calculate the total points of the winning scratchcards. Count the total amount of scratchcards with their increasing copies. 
<img src=https://github.com/Kyros0718/Advent_of_Code/blob/main/Media/2023/baby_elf_on_gondala.png>

The gondola takes you up. Strangely, though, the ground doesn't seem to be coming with you; you're not climbing a mountain. As the circle of Snow Island recedes below you, an entire new landmass suddenly appears above you! The gondola carries you to the surface of the new island and lurches into the station.

As you exit the gondola, the first thing you notice is that the air here is much $\color{VioletRed}{\textbf{warmer}}$ than it was on Snow Island. It's also quite $\color{VioletRed}{\textbf{humid}}$. Is this where the water source is?

The next thing you notice is an Elf sitting on the floor across the station in what seems to be a pile of colorful square cards.

"Oh! Hello!" The Elf excitedly runs over to you. "How may I be of service?" You ask about water sources.

"I'm not sure; I just operate the gondola lift. That does sound like something we'd have, though - this is $\color{VioletRed}{\textbf{Island}}$ $\color{VioletRed}{\textbf{Island}}$, after all! I bet the $\color{VioletRed}{\textbf{gardener}}$ would know. He's on a different island, though - er, the small kind surrounded by water, not the floating kind. We really need to come up with a better naming scheme. Tell you what: if you can help me with something quick, I'll let you $\color{VioletRed}{\textbf{borrow}}$ $\color{VioletRed}{\textbf{my}}$ $\color{VioletRed}{\textbf{boat}}$ and you can go visit the gardener. I got all these ${\color{green}scratchcards}$ as a gift, but I can't figure out what I've won."

The Elf leads you over to the pile of colorful cards. There, you discover dozens of scratchcards, all with their opaque covering already scratched off. Picking one up, it looks like each card has two lists of numbers separated by a vertical bar (`|`): a list of $\color{VioletRed}{\textbf{winning}}$ $\color{VioletRed}{\textbf{numbers}}$ and then a list of $\color{VioletRed}{\textbf{numbers}}$ $\color{VioletRed}{\textbf{you}}$ $\color{VioletRed}{\textbf{have}}$. You organize the information into a table (your puzzle input).

As far as the Elf has been able to figure out, you have to figure out which of the $\color{VioletRed}{\textbf{numbers}}$ $\color{VioletRed}{\textbf{you}}$ $\color{VioletRed}{\textbf{have}}$ appear in the list of $\color{VioletRed}{\textbf{winning}}$ $\color{VioletRed}{\textbf{numbers}}$. The first match makes the card worth $\color{VioletRed}{\textbf{one}}$ $\color{VioletRed}{\textbf{point}}$ and each match after the first $\color{VioletRed}{\textbf{doubles}}$ the point value of that card.

For example:

| `Card 1: 41 48 83 86 17 \| 83 86  6 31 17  9 48 53`<br>`Card 2: 13 32 20 16 61 \| 61 30 68 82 17 32 24 19`<br>`Card 3:  1 21 53 59 44 \| 69 82 63 72 16 21 14  1`<br>`Card 4: 41 92 73 84 69 \| 59 84 76 51 58  5 54 83`<br>`Card 5: 87 83 26 28 32 \| 88 30 70 12 93 22 82 36`<br>`Card 6: 31 18 13 56 72 \| 74 77 10 23 35 67 36 11` |
| --- |

In the above example, card 1 has five winning numbers (`41`, `48`, `83`, `86`, and `17`) and eight numbers you have (`83`, `86`, `6`, `31`, `17`, `9`, `48`, and `53`). Of the numbers you have, four of them (`48`, `83`, `17`, and `86`) are winning numbers! That means card 1 is worth **`8`** points (1 for the first match, then doubled three times for each of the three matches after the first).

- Card 2 has two winning numbers (`32` and `61`), so it is worth `2` points.
- Card 3 has two winning numbers (`1` and `21`), so it is worth `2` points.
- Card 4 has one winning number (`84`), so it is worth `1` point.
- Card 5 has no winning numbers, so it is worth no points.
- Card 6 has no winning numbers, so it is worth no points.

So, in this example, the Elf's pile of scratchcards is worth **`13`** points.

Take a seat in the large pile of colorful cards. $\color{VioletRed}{\textbf{How}}$ $\color{VioletRed}{\textbf{many}}$ $\color{VioletRed}{\textbf{points}}$ $\color{VioletRed}{\textbf{are}}$ $\color{VioletRed}{\textbf{they}}$ $\color{VioletRed}{\textbf{worth}}$ $\color{VioletRed}{\textbf{in}}$ $\color{VioletRed}{\textbf{total?}}$

> Your puzzle answer was **`21959`**

<br>

##  Part Two
Just as you're about to report your findings to the Elf, one of you realizes that the rules have actually been printed on the back of every card this whole time.

There's no such thing as "points". Instead, scratchcards only cause you to $\color{VioletRed}{\textbf{win more scratchcards}}$ equal to the number of winning numbers you have.

Specifically, you win $\color{VioletRed}{\textbf{copies}}$ of the scratchcards below the winning card equal to the number of matches. So, if card 10 were to have 5 matching numbers, you would win one copy each of cards 11, 12, 13, 14, and 15.

Copies of scratchcards are scored like normal scratchcards and have the $\color{VioletRed}{\textbf{same card number}}$ as the card they copied. So, if you win a copy of card 10 and it has 5 matching numbers, it would then win a copy of the same cards that the original card 10 won: cards 11, 12, 13, 14, and 15. This process repeats until none of the copies cause you to win any more cards. (Cards will never make you copy a card past the end of the table.)

This time, the above example goes differently:

| `Card 1: 41 48 83 86 17 \| 83 86  6 31 17  9 48 53`<br>`Card 2: 13 32 20 16 61 \| 61 30 68 82 17 32 24 19`<br>`Card 3:  1 21 53 59 44 \| 69 82 63 72 16 21 14  1`<br>`Card 4: 41 92 73 84 69 \| 59 84 76 51 58  5 54 83`<br>`Card 5: 87 83 26 28 32 \| 88 30 70 12 93 22 82 36`<br>`Card 6: 31 18 13 56 72 \| 74 77 10 23 35 67 36 11` |
| --- |

- Card 1 has four matching numbers, so you win one copy each of the next four cards: cards 2, 3, 4, and 5.
- Your original card 2 has two matching numbers, so you win one copy each of cards 3 and 4.
- Your copy of card 2 also wins one copy each of cards 3 and 4.
- Your four instances of card 3 (one original and three copies) have two matching numbers, so you win $\color{VioletRed}{\textbf{four}}$ copies each of cards 4 and 5.
- Your eight instances of card 4 (one original and seven copies) have one matching number, so you win $\color{VioletRed}{\textbf{eight}}$ copies of card 5.
- Your fourteen instances of card 5 (one original and thirteen copies) have no matching numbers and win no more cards.
- Your one instance of card 6 (one original) has no matching numbers and wins no more cards.

Once all of the originals and copies have been processed, you end up with `1` instance of card 1, `2` instances of card 2, `4` instances of card 3, `8` instances of card 4, `14` instances of card 5, and `1` instance of card 6. In total, this example pile of scratchcards causes you to ultimately have `30` scratchcards!

Process all of the original and copied scratchcards until no more scratchcards are won. Including the original set of scratchcards, $\color{VioletRed}{\textbf{how many total scratchcards do you end up with?}}$

> Your puzzle answer was **`5132675`**

<br>
<br>

# Credits

> [!NOTE]  
> **Image:** [_imagine.art_](https://www.imagine.art/)<br>
> **Puzzles:** [_Advent of Code_](https://adventofcode.com/)

