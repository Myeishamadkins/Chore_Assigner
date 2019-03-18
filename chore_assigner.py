from random import shuffle


def main():
    students = [
        'Cole Anderson', 'Timothy Bowling', 'Logan Harrell', 'Desma Hervey',
        'Ginger Keys', 'Matt Lipsey', 'Myeisha Madkins', 'Henry Moore',
        'John Morgan', 'Irma Patton', 'Danny Peterson Jakylan Standifer',
        'Justice Taylor', 'Ray Turner', 'Cody van der Poel', 'Andrew Wheeler'
    ]

    chores = [
        'chore_1', 'chore_2', 'chore_3', 'chore_4', 'chore_5', 'chore_6',
        'chore_7', 'chore_8', 'chore_9', 'chore_10', 'chore_11', 'chore_12',
        'chore_13', 'chore_14', 'chore_15', 'chore_16'
    ]
    shuffle(chores)
    for student in students:
        print(student, chores.pop())


if __name__ == '__main__':
    main()
