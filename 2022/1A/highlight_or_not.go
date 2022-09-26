/*

Generates all of the possibilities for the Double or One Thing challenge,
and prints out the correct answer. Useful for debugging without test samples.

*/
package main

import (
  "fmt"
  "sort"
)

func highlight_words(word string, i int) []string {
  if i >= len(word) - 1 {
    return []string {word}
  }
  t1 := word[:i+1] + string(word[i]) + word[i+1:]
  t2 := word
  tree1 := highlight_words(t1 , i+2)
  tree2 := highlight_words(t2, i+1)
  return append(tree1, tree2...)
}

func main() {
  var word string
  fmt.Scan(&word)
  results := highlight_words(word, 0)
  sort.Strings(results)
  fmt.Printf("Answer: %s\n", results[0])
}
