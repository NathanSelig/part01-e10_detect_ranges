#!/usr/bin/env python3

def detect_ranges(L):

    L.sort()
    streaks = findStreak(L)
    result = []

    print(streaks)

    for streak in streaks:
        # group pairs and format
        # if 1 item in streak
        if len(streak) == 1:
            pair = min(streak)
            result.append(pair)

        else:  # if more then 1
            pair = (min(streak), max(streak) + 1)
            result.append(pair)

    return result


def findStreak(L):

    streaks = []
    streak = []
    for i in range(len(L)-1):
        # ? why is last value not working

        if L[i] + 1 == L[i + 1]:
            streak.append(L[i])
            #TODO index + 1 or min 
        elif L[i] + 1 != L[i + 1] and len(streak) == 0:
            streak.append(L[i])
            streaks.append(streak)
            streak = []
        else:
            streaks.append(streak)
            streak = []

    return streaks


def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)


if __name__ == "__main__":
    main()
