# CodeJam

Attempts at the Google CodeJam programming challenges.

# 2022
## QR
* [Punched Cards](https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4621b) - pretty straight forward, just need to recognize that each row is 2 lines of text with a single leading char,, row 0 is a base case and each column is 2 chars.
* [Twisty Little Passages](https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a45fc0) - a good head scratcher. One would think teleporting to K random rooms and then estimating the number of passages to be the average # of passages / 2 would be a good solution, but it's not the case. Test cases where there are a small number of rooms whose degrees vary widely from the median can skew the actual estimate.
