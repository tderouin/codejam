# # Qualification Round 2022
# Punched Cards
# https://bit.ly/3xN5swW
# Passes tests
# Approach
# Pretty straight forward, just recognize that the each row
# is two lines of text, and that row 0 is a base case,
# rows 1..R are the same. Columns are 2 chars each and
# each row starts with a single leading char.

def draw_punchcard(rows, columns):
    if columns < 1:
        raise Exception('Need at least one column')
    for row in range(0, rows):
        if row == 0:
            # base case
            print('..+' + '-+'*(columns - 1))
            print('..|' + '.|'*(columns - 1))
        else:
            print('+' + '-+' * columns)
            print('|' + '.|' * columns)
    print('+' + '-+' * columns)



if __name__ == '__main__':
    # capture the # of test cases
    t = int(input())
    for case in range(1, t+1):
        # process each test case
        R, C = list(map(int, input().split()))
        print(f'Case #{case}:')
        draw_punchcard(R, C)
