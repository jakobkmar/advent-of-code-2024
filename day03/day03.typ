#import "../shared/aoc.typ": *

#{
  let program = read("test_input.txt")
    .trim()

  // part 1

  let regexMatches = program.matches(regex("mul\((\d+),(\d+)\)"))
  let results = regexMatches.map(m => int(m.captures.at(0)) * int(m.captures.at(1)))

  // part 2

  let improvedMatches = program.matches(regex("mul\((\d+),(\d+)\)|do\(\)|don't\(\)"))
  let enabled = true
  let improvedResults = ()
  for m in improvedMatches {
    if m.text == "do()" { enabled = true }
    else if m.text == "don't()" { enabled = false }
    else if enabled {
      improvedResults.push(int(m.captures.at(0)) * int(m.captures.at(1)))
    }
  }
  
  // visualization

  aoc(
    day: 2,
    part1: [
      First, read the program.
      
      #pad(left: 1em, raw(program))

      Then, use the regex #raw(lang: "re", "mul\((\d+),(\d+)\)") to find all valid `mul` sequences.
      
      #pad(left: 1em, [#regexMatches])

      By following all instructions, we get the following results:

      #pad(left: 1em, [#results])

      Which in sum total to #result(results.sum()).
    ],
    part2: [
      First, read the program.
      
      #pad(left: 1em, raw(program))

      Then, use the expanded regex #raw(lang: "re", "mul\((\d+),(\d+)\)|do\(\)|don't\(\)") to find all valid `mul` sequences, as well as all `do()` and `don't()` statements.
      
      #pad(left: 1em, [#improvedMatches])

      By following all instructions, we get the following results:

      #pad(left: 1em, [#improvedResults])

      Which in sum total to #result(improvedResults.sum()).
    ]
  )
}
