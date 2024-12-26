import argparse
import csv
import math


def read_csv(file: str):
    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        matrix = list(reader)
    return [row[1:] for row in matrix[1:]]


def joint_entropy(matrix):
    total_entropy = 0
    for row in matrix:
        for p in row:
            if p > 0:
                total_entropy += p * math.log2(p)
    return round(-total_entropy, 2)


def entropy_b(matrix):
    column_sums = [0] * len(matrix[0])
    for row in matrix:
        for j in range(len(row)):
            column_sums[j] += row[j]
    total_entropy = 0
    for p in column_sums:
        if p > 0:
            total_entropy += p * math.log2(p)
    return round(-total_entropy, 2), column_sums


def entropy_a(matrix):
    total_entropy = 0
    row_sums = []
    for row in matrix:
        p = sum(row)
        row_sums.append(p)
        if p > 0:
            total_entropy += p * math.log2(p)
    return round(-total_entropy, 2), row_sums


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help="Path to the CSV file")
    args = parser.parse_args()

    matrix = read_csv(args.filepath)

    int_matrix = [[int(element) for element in row] for row in matrix]

    total_sum = sum(sum(row) for row in int_matrix)
    for i, row in enumerate(int_matrix):
        int_matrix[i] = [element / total_sum for element in row]

    share_entropy = joint_entropy(int_matrix)
    entropyA, row_sums = entropy_a(int_matrix)
    entropyB, column_sums = entropy_b(int_matrix)

    conditional_entropy = share_entropy - entropyA
    mutual_information = entropyB - conditional_entropy

    result_values = [
        round(share_entropy, 2),
        round(entropyA, 2),
        round(entropyB, 2),
        round(conditional_entropy, 2),
        round(mutual_information, 2)
    ]

    result_description = [
        ("H(AB) - Совместная энтропия", round(share_entropy, 2)),
        ("H(A) - Энтропия A", round(entropyA, 2)),
        ("H(B) - Энтропия B", round(entropyB, 2)),
        ("H(A|B) - Условная энтропия", round(conditional_entropy, 2)),
        ("I(A, B) - Взаимная информация", round(mutual_information, 2))
    ]

    return result_values, result_description


if __name__ == '__main__':
    result_values, result_description = main()

    for label, value in result_description:
        print(f"{label}: {value}")

    print(result_values)