import csv
import numpy as np
import pandas as pd
from io import StringIO


def main() -> str:
    # Чтение CSV-файла 'task2.csv'
    edges = []
    with open('task2.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            edges.append((int(row[0]), int(row[1])))  # Чтение ребер из файла

    # Определим количество узлов (максимальный номер узла)
    nodes = set()
    for edge in edges:
        nodes.update(edge)
    num_nodes = max(nodes)  # Максимальная вершина определяет количество узлов
    
    # Инициализация матрицы смежности
    adj_matrix = np.zeros((num_nodes, num_nodes), dtype=int)
    
    # Заполняем матрицу смежности
    for edge in edges:
        adj_matrix[edge[0] - 1][edge[1] - 1] = 1  # Ребро от node A к node B

    # Инициализируем матрицу для хранения результатов (r₁ - r₅ для каждого узла)
    result_matrix = np.zeros((num_nodes, 5), dtype=int)

    # r₁: непосредственное управление (прямые связи)
    result_matrix[:, 0] = np.sum(adj_matrix, axis=1)

    # r₂: непосредственное подчинение (обратные связи)
    result_matrix[:, 1] = np.sum(adj_matrix, axis=0)

    # r₃: опосредованное управление (косвенные связи)
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j and adj_matrix[i][j] == 0:
                paths = np.dot(adj_matrix[i], adj_matrix[:, j])
                if paths > 0:
                    result_matrix[i, 2] += 1

    # r₄: опосредованное подчинение (обратные косвенные связи)
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j and adj_matrix[j][i] == 0:
                paths = np.dot(adj_matrix[j], adj_matrix[:, i])
                if paths > 0:
                    result_matrix[i, 3] += 1

    # r₅: соподчинение на одном уровне (узлы с одинаковым уровнем управления)-???
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j and adj_matrix[i, j] == 0 and adj_matrix[j, i] == 0 and result_matrix[i, 4]<= 0:
                result_matrix[i, 4] += 1
    result_matrix[0][4]=0

    # Преобразование результата в CSV строку
    output = StringIO() 
    writer = csv.writer(output) 
    writer.writerows(result_matrix) # Запись результата в файл 
    with open("task2_result.csv", "w") as file: file.write(output.getvalue())

# Запуск функции
if __name__ == "__main__":
    print(main())