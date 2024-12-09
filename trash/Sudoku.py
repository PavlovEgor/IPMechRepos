


class Sudoku:
    def __init__(self, initial_matrix):
        self.matrix = [[0 for _ in range(9)] for __ in range(9)]

        for i in range(9):
            for j in range(9):
                if initial_matrix[i][j] == 0:
                    self.matrix[i][j] = {"Assumption": {1, 2, 3, 4, 5, 6, 7, 8, 9}}

                else:
                    self.matrix[i][j] = {"Answer": initial_matrix[i][j]}

    def print_matrix(self, with_Assumptions=False):
        for i in range(9):
            for j in range(9):
                if list(self.matrix[i][j].keys())[0] == "Assumption":
                    if with_Assumptions:
                        print(self.matrix[i][j]["Assumption"], end=' ')
                    else:
                        print("_", end=' ')
                else:
                    print(self.matrix[i][j]["Answer"], end=' ')
            print(end='\n')

    def update_assumption(self):

        for i in range(9):
            for j in range(9):
                if list(self.matrix[i][j].keys())[0] == "Answer":
                    continue

                cur = self.matrix[i][j]["Assumption"]

                for k in range(9):
                    if k == i:
                        continue
                    elif list(self.matrix[k][j].keys())[0] == "Assumption":
                        continue
                    else:
                        cur.discard(self.matrix[k][j]["Answer"])


                for k in range(9):
                    if k == j:
                        continue
                    elif list(self.matrix[i][k].keys())[0] == "Assumption":
                        continue
                    else:
                        cur.discard(self.matrix[i][k]["Answer"])

                a = i // 3
                b = j // 3

                for k in range(3*a, 3*a+3):
                    for m in range(3*b, 3*b + 3):
                        if k == i and j == m:
                            continue
                        elif list(self.matrix[k][m].keys())[0] == "Assumption":
                            continue
                        else:
                            cur.discard(self.matrix[k][m]["Answer"])


    def update_answer(self):
        count_of_update = 0
        for i in range(9):
            for j in range(9):
                if list(self.matrix[i][j].keys())[0] == "Assumption":
                    if len(self.matrix[i][j]["Assumption"]) == 1:
                        self.matrix[i][j] = {"Answer": list(self.matrix[i][j]["Assumption"])[0]}
                        print(i, j, self.matrix[i][j])
                        count_of_update += 1

        for i in range(9):
            for j in range(9):
                if list(self.matrix[i][j].keys())[0] == "Answer":
                    continue

                cur_assum = self.matrix[i][j]["Assumption"]
                column_neib_assum = set()
                row_neib_assum = set()
                box_neib_assum = set()

                for k in range(9):
                    if k == i:
                        continue
                    elif list(self.matrix[k][j].keys())[0] == "Assumption":
                        column_neib_assum = column_neib_assum.union(self.matrix[k][j]["Assumption"])

                for k in range(9):
                    if k == j:
                        continue
                    elif list(self.matrix[i][k].keys())[0] == "Assumption":
                        row_neib_assum = row_neib_assum.union(self.matrix[i][k]["Assumption"])

                a = i // 3
                b = j // 3

                for k in range(3*a, 3*a+3):
                    for m in range(3*b, 3*b + 3):
                        if k == i and j == m:
                            continue
                        elif list(self.matrix[k][m].keys())[0] == "Assumption":
                            box_neib_assum = box_neib_assum.union(self.matrix[k][m]["Assumption"])

                row_diff = cur_assum - row_neib_assum
                col_diff = cur_assum - column_neib_assum
                box_diff = cur_assum - box_neib_assum

                if len(row_diff) == 1:
                    self.matrix[i][j] = {"Answer": list(row_diff)[0]}
                    print(i, j, self.matrix[i][j])
                    count_of_update += 1
                elif len(col_diff) == 1:
                    self.matrix[i][j] = {"Answer": list(col_diff)[0]}
                    print(i, j, self.matrix[i][j])
                    count_of_update += 1
                elif len(box_diff) == 1:
                    self.matrix[i][j] = {"Answer": list(box_diff)[0]}
                    print(i, j, self.matrix[i][j])
                    count_of_update += 1

        if count_of_update == 0:
            return True
        else:
            return False

    def ready(self):
        count = 0
        for i in range(9):
            for j in range(9):
                if list(self.matrix[i][j].keys())[0] == "Assumption":
                    count += 1

        if count == 0:
            return True
        else:
            return False





initial_matrix = [[1, 0, 0, 0, 0, 0, 0, 0, 3],
                  [0, 0, 7, 2, 6, 0, 4, 8, 0],
                  [4, 0, 0, 9, 3, 5, 0, 0, 6],
                  [0, 3, 0, 4, 8, 0, 2, 0, 0],
                  [0, 4, 1, 6, 0, 9, 3, 0, 0],
                  [0, 0, 6, 0, 0, 0, 8, 9, 0],
                  [5, 7, 8, 0, 4, 0, 0, 0, 2],
                  [0, 0, 0, 3, 0, 0, 0, 7, 0],
                  [2, 0, 0, 0, 6, 0, 0, 0, 5]]

S = Sudoku(initial_matrix)
S.update_assumption()
S.update_answer()
S.print_matrix(False)

# while not S.ready():
#     S.update_assumption()
#     NOT_UPDATE = S.update_answer()
#     S.print_matrix(False)
#     if NOT_UPDATE:
#         break
#     print("_____________________")
#
#
# S.print_matrix(True)
# print("_____________________")
# S.print_matrix(False)
