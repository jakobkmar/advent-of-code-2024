#import "../shared/aoc.typ": *

#{
  let reports = read("test_input.txt")
    .trim().split(newlineRegex)
    .map(line => line.split(whitespaceRegex).map(int))

  let check(r) = (
    sorted: r == r.sorted() or r == r.sorted().rev(),
    differ: r.windows(2).all(w => calc.abs(w.at(0) - w.at(1)) in range(1,4)),
  )

  // part 1
    
  let checked = reports.map(check)
  let safe = checked.map(c => c.sorted and c.differ)

  // part 2

  let dampedReports = reports.map(r => {
    let damped = (r,)
    for i in range(0, r.len()) {
      let tmpReport = r
      let _ = tmpReport.remove(i)
      damped.push(tmpReport)
    }
    damped
  })
  
  let dampedChecked = dampedReports.map(dr => dr.map(check))
  let dampedSafe = dampedChecked.map(dc => dc.any(c => c.sorted and c.differ))
  
  // visualization

  let displayValidity(bool) = if bool {
    emoji.checkmark.box
  } else {
    emoji.crossmark
  }

  aoc(
    day: 2,
    part1: [
      To be safe, all reports must be ascending or descending with a distance between two adjacent levels between 1 and 3.
      
      #grid(
        columns: 5, gutter: 2em,
        [
          *Parsed reports* \
          #reports
        ],
        followsArrow,
        [
          *The two validity checks* \
          #checked
        ],
        followsArrow,
        [
          *Safe reports* \
          `(`
          #pad(left: 1em, y: -0.5em, {
            for s in safe.slice(0, calc.min(safe.len(), 40)) {
              raw(displayValidity(s))
              linebreak()
            }
          })
          `)`
        ]
      )

      #let safeAmount = safe.filter(s => s).len()
      $arrow.half.cw$ In total there are #result(safeAmount) safe reports.
    ],
    part2: [
      The same rules as above still apply, but now one level entry can be removed if it makes the report safe.
      
      #grid(
        columns: 5, gutter: 2em,
        [
          *Damped variants* \
          #dampedReports
        ],
        followsArrow,
        [
          *Validity check for each variant* \
          #dampedChecked
        ],
        followsArrow,
        [
          *Safe reports* \
          `(`
          #pad(left: 1em, y: -0.5em, {
            for s in dampedSafe.slice(0, calc.min(safe.len(), 40)) {
              raw(displayValidity(s))
              linebreak()
            }
          })
          `)`
        ]
      )

      #let safeAmount = dampedSafe.filter(s => s).len()
      $arrow.half.cw$ In total there are #result(safeAmount) safe reports.
    ]
  )
}
