#!/usr/bin/python3
import sys


def help_N_queen(N):
    def possible_to_place(pos, position_oc):
        for i in range(len(position_oc)):
            if position_oc[i] == pos or \
                    position_oc[i] - i == pos - len(position_oc) or \
                    position_oc[i] + i == pos + len(position_oc):
                return False
        return True

    def plc_queen(position_oc, row_target, N):
        if row_target == N:
            result.append(position_oc)
            return
        for column in range(N):
            if possible_to_place(column, position_oc):
                plc_queen(position_oc + [column], row_target + 1, N)

    result = []
    plc_queen([], 0, N)
    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    sol = help_N_queen(N)
    for sol in sol:
        print([[i, sol[i]] for i in range(N)])
