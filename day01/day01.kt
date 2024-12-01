import kotlin.io.path.Path
import kotlin.io.path.readLines
import kotlin.math.absoluteValue

val whitespace = "\\s+".toRegex()

fun main() {
    val part1 = Path("input.txt")
        .readLines()
        .map { it.split(whitespace).map { it.toInt() } }
        .let { p -> p.map { it[0] }.sorted() zip p.map { it[1] }.sorted() }
        .map { (it.first - it.second).absoluteValue }
        .sum()
    println(part1)
}
