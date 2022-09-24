# Qualification Round 2022
# 3D Printing
# https://bit.ly/3UyZuJR
# Passes tests
# Approach
# Pretty straight forward, grab the input and then transpose
# the matrix of printers to the individual colours
# Iterate over the list of colours, consume the minimum
# available quantity of ink unit available
# If there are any ink units "left" after processing
# all 4 colours, there is no possible solution
# If a solution exists, there could be multiple possible
# solutions, this program only outputs one of them. :)

def print_three_d_solution(printers):
    c = list(map(lambda n: n[0], printers))
    m = list(map(lambda n: n[1], printers))
    y = list(map(lambda n: n[2], printers))
    k = list(map(lambda n: n[3], printers))
    result = []
    left = pow(10, 6)

    # iterate over each colour
    for colour in [c, m, y, k]:
        # select how many ink_units to use
        # it's the min of how many ink units are remaining (left)
        # and the minimum ink units available for this colour
        ink_units = min(left, min(colour))
        result.append(ink_units)
        left -= ink_units

    if left > 0:
        return None

    if left < 0:
        # shouldn't happen, but it's good to check
        raise Exception('We have a problem')

    return result


if __name__ == '__main__':
    # capture the # of test cases
    t = int(input())
    for case in range(1, t+1):
        printer1 = list(map(int, input().split()))
        printer2 = list(map(int, input().split()))
        printer3 = list(map(int, input().split()))
        solution = print_three_d_solution([printer1, printer2, printer3])
        if solution is None:
            print(f'Case #{case}: IMPOSSIBLE')
        else:
            print(f'Case #{case}: ' + ' '.join([str(x) for x in solution]))
