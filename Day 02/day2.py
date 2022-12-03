import os

def getTurnValue(turn):
    if turn == 'A' or turn == 'X':
        return 1
    elif turn == 'B' or turn == 'Y':
        return 2
    elif turn == 'C' or turn == 'Z':
        return 3
    else:
        return 0

def processInputPart1(fileName):

    countRounds= 0
    scoresPlayer1 = []
    scoresPlayer2 = []

    file = open(fileName, "r")

    if os.path.getsize(fileName) > 0:

        for line in file:

            countRounds += 1
            line = line.rstrip()
            (turnPlayer1, turnPlayer2) = line.split(" ")

            roundScorePlayer1 = getTurnValue(turnPlayer1)
            roundScorePlayer2 = getTurnValue(turnPlayer2)

            if getTurnValue(turnPlayer1) - getTurnValue(turnPlayer2) == -2:
                roundScorePlayer1 += 6
            elif getTurnValue(turnPlayer1) - getTurnValue(turnPlayer2) == -1:
                roundScorePlayer2 += 6
            elif getTurnValue(turnPlayer1) - getTurnValue(turnPlayer2) == 0:
                roundScorePlayer1 += 3
                roundScorePlayer2 += 3
            elif getTurnValue(turnPlayer1) - getTurnValue(turnPlayer2) == 1:
                roundScorePlayer1 += 6
            elif getTurnValue(turnPlayer1) - getTurnValue(turnPlayer2) == 2:
                roundScorePlayer2 += 6

            scoresPlayer1.append(roundScorePlayer1)
            scoresPlayer2.append(roundScorePlayer2)

        scorePlayer1 = sum(scoresPlayer1)
        scorePlayer2 = sum(scoresPlayer2)

        print("PART 1")
        print(f"   Score Elf : {scorePlayer1}")
        print(f"   Score Me  : {scorePlayer2}")

def processInputPart2(fileName):

    matrix = {1: {'X': 3, 'Y': 1, 'Z': 2},
              2: {'X': 1, 'Y': 2, 'Z': 3},
              3: {'X': 2, 'Y': 3, 'Z': 1}}

    countRounds= 0
    scoresPlayer1 = []
    scoresPlayer2 = []

    file = open(fileName, "r")

    if os.path.getsize(fileName) > 0:

        for line in file:

            countRounds += 1
            line = line.rstrip()
            (turnPlayer1, turnPlayer2) = line.split(" ")

            roundScorePlayer1 = getTurnValue(turnPlayer1)
            roundScorePlayer2 = matrix[roundScorePlayer1][turnPlayer2]

            if roundScorePlayer1 - roundScorePlayer2 == -2:
                roundScorePlayer1 += 6
            elif roundScorePlayer1 - roundScorePlayer2 == -1:
                roundScorePlayer2 += 6
            elif roundScorePlayer1 - roundScorePlayer2 == 0:
                roundScorePlayer1 += 3
                roundScorePlayer2 += 3
            elif roundScorePlayer1 - roundScorePlayer2 == 1:
                roundScorePlayer1 += 6
            elif roundScorePlayer1 - roundScorePlayer2 == 2:
                roundScorePlayer2 += 6

            scoresPlayer1.append(roundScorePlayer1)
            scoresPlayer2.append(roundScorePlayer2)

        scorePlayer1 = sum(scoresPlayer1)
        scorePlayer2 = sum(scoresPlayer2)

        print("PART 2")
        print(f"   Score Elf : {scorePlayer1}")
        print(f"   Score Me  : {scorePlayer2}")

def main():

    processInputPart1("input.txt")
    processInputPart2("input.txt")
if __name__ == "__main__":
    main()