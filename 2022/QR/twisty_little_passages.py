# Qualification Round 2022
# Twisty Little Passages
# https://bit.ly/3feJTid

# Passes 100/100 of the cases with the CodeJam provided testing tool
# Scores Wrong Answer (WA) on submission :)

# To connect twisty_little_passage_local_testing_tool.py3 and twisty_little_passages.py:
# mkfifo myfifo
# <myfifo python twisty_little_passage_local_testing_tool.py3 | python twisty_little_passages.py >myfifo
# rm myfifo

# Approach
# A test case specifies N rooms and K + 1 operations or "exchanges"
# A simple approach would be walk or teleport K + 1 times and
# estimate the number of passages to be the average # of passages seen / 2
# This has a problem when a small number of rooms deviate significantly
# from the median
# Uses "importance sampling" give an unbiased estimate (suggested by CodeJam)
# Executes a teleport (T) followed by a walk (W)
# Passages returned by a teleport have a weight of 1
# Passages returned by a walk have a weight of A/B where
#   A = # of passages returned by the teleport
#   B = # of passages returned by the walk
# Because the program provides us a room before we can issue a W or T, we
# process the very first exchange as a walk and then execute a teleport
import random

if __name__ == '__main__':
    # capture the # of test cases
    t = int(input())
    for case in range(1, t+1):
        # process each test case
        N, K = list(map(int, input().split()))
        rooms_seen = {}
        weighted_passages = []
        # intialize the weights, interpret the very first exchange as W
        A = B = 1
        for exchange in range(0, K + 1, 2):
            # process the response from a W command
            room, num_passages = list(map(int, input().split()))
            rooms_seen[room] = 1
            weight = A / B
            weighted_passages.append(num_passages * weight)
            B = num_passages

            # we've processed K + 1 exchanges, break
            if exchange == K:
                break

            # teleport to a random room we haven't seen yet
            r = random.randrange(1, N)
            while r in rooms_seen:
                r = random.randrange(1, N)
            print(f'T {r}')
            room, num_passages = list(map(int, input().split()))
            rooms_seen[room] = 1
            weight = 1
            weighted_passages.append(num_passages * weight)
            A = num_passages
            print('W')

        # estimate
        weighted_average = sum(weighted_passages) / len(weighted_passages)
        e = int(N * weighted_average / 2)
        print(f'E {e}')
