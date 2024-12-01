#import "../shared/aoc.typ": *

#{
  import calc: max, min

  let inputNums = read("input.txt")
    .trim().split("\n")
    .map(line => line.split(whitespace).map(int))

  let leftSide = inputNums.map(l => l.at(0)).sorted()
  let rightSide = inputNums.map(l => l.at(1)).sorted()

  // part 1
  let sortedNums = leftSide.zip(rightSide)
  let distances = sortedNums.map(p => calc.abs(p.at(0) - p.at(1)))
  let sumDistances = distances.sum()

  // part 2
  let similarityScores = leftSide.map(n => n * rightSide.filter(r => r == n).len())
  let sumSimilarityScores = similarityScores.sum()
  
  // visualization

  aoc(
    day: 1,
    part1: [
      First, we sort the number columns on the left side and the right side of each pair. \
      Then, we calculate the distance between the two numbers in each pair.

      #grid(
        columns: 5, gutter: 2em,
        [
          *Parsed Number Pairs* \
          #inputNums
        ],
        followsArrow,
        [
          *Sorted Number Pairs* \
          #sortedNums
        ],
        followsArrow,
        [
          *Calculated Distances* \
          #distances
        ]
      )

      $arrow.cw.half$ The sum of all distances is #result(sumDistances).
    ],
    part2: [
      Next, we calculate the similarity score for each number on the left side. \
      The similarity score is the product of the number and the count of the number on the right side.

      #grid(
        columns: 3, gutter: 2em,
        [
          *Parsed Number Pairs* \
          #inputNums
        ],
        followsArrow,
        [
          *Similarity Scores* \
          #similarityScores
        ]
      )

      $arrow.cw.half$ The sum of all similarity scores is #result(sumSimilarityScores).
    ]
  )
}
