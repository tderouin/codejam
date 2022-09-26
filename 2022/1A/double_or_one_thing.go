package main

import (
  "bytes"
  "fmt"
)

/*
Approach:

Iterate over each word, letter by letter, making a decision about whether or not to double the letter.

Working through some simple cases by hand can reveal a good algorithm.

e.g.

AZ -> AAZ

This is sort of obvious. But it can be confusing with even simple examples.

LAH

See the accompanying generator program that will pick the correct result given a word.

Cases:
  * Base case: The current letter is less than the next letter - double it
  * If there is a tie - and the current letter matches the next letter:
    * iterate through the rest of the word
    * if there is a higher letter, but no lower letter (to later handle it), double the letter
  * Otherwse, do nothing
*/

func main() {
  var cases int
  fmt.Scan(&cases)
  for i := 0; i < cases; i++ {
    var input string
    // use a buffer to avoid expensive string copying
    var buffer bytes.Buffer
    fmt.Scan(&input)
    var n = len(input)
    for i := 0; i < n; i++ {
      c := input[i]
      buffer.WriteByte(c)
      if i < n - 1 {
        if c < input[i+1] {
          // the base case
          buffer.WriteByte(c)
        } else if c == input[i + 1] {
          // there is tie, move through the rest of the word beyond our next letter
          for j := i + 2; j < n; j++ {
            if c > input[j] {
              // the correct solution will be handled by a later letter
              break
            }
            if c < input[j] {
              // we found a larger letter, so the our doubling of our c is needed
              buffer.WriteByte(c)
              break
            }
          }
        }
      }
    }
    fmt.Printf("Case #%d: %s\n", i+1, buffer.String())
  }
}
