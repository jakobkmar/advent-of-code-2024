#let aoc(
  day: int,
  part1: content,
  part2: content,
) = [
  #set page(paper: "a4", height: auto, margin: 1.5cm)
  #set text(size: 1em)

  #show heading.where(level: 1): it => {
    set text(size: 1.1em)
    block(
      fill: maroon.darken(10%), inset: 0.5em, radius: 5pt,
      below: 0.8em,
      text(fill: white, it)
    )
  }

  #box(
    fill: gradient.linear(..color.map.rocket.slice(50, 200).map(it => it.lighten(80%))), inset: 1.2em, radius: 5pt,
    text(size: 1.8em, fill: black)[
      #emoji.tree.xmas Advent of Code 2024
    ]
  )
  #h(0.8em)
  #box(
    fill: gradient.linear(..color.map.crest.map(it => it.lighten(80%))), inset: 1.2em, radius: 5pt,
    text(size: 1.8em, fill: black)[
      *Day #day*
    ]
  )

  #let follows = align(horizon)[
    #text(size: 1.2em)[
      *$arrow.cw.half$*
    ]
  ]

  #v(1em)

  = Part 1

  #part1

  #v(2em)

  = Part 2

  #part2
]

#let newlineRegex = regex("\\r?\\n")
#let whitespaceRegex = regex("\\s+")

#let followsArrow = align(horizon)[
  #text(size: 1.2em)[
    *$arrow.cw.half$*
  ]
]

#let result(content) = text(
  size: 1.1em, weight: "bold",
  raw(str(content)))
)
