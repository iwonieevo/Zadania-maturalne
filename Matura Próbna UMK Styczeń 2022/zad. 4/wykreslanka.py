# https://www.youtube.com/watch?v=Z8Gy8r1Qv0U

with open("wykreslanka.txt") as f:
    rows = [line.rstrip() for line in f.readlines()]

columns = [""] * 200
for i in range(len(rows)):
    for j in range(len(columns)):
        columns[j] += rows[i][j]

maturaRows, maturaColumns, longest_length, longest_rows, answer = [], [], 0, [], [0, 0, 0, 0]
for row in rows:
    if 'matura' in row:
        maturaRows.append(rows.index(row))
    curr = row[0]
    length = 0
    for letter in row:
        if letter == curr:
            length += 1
        else:
            if length == longest_length:
                longest_rows.append(rows.index(row))
            elif length > longest_length:
                longest_length = length
                longest_rows.clear()
                longest_rows.append(rows.index(row))
            curr = letter
            length = 1

for column in columns:
    if 'matura' in column:
        maturaColumns.append(columns.index(column))


def subsequence():
    for rowIndex in range(len(rows)):
        for columnIndex in range(len(columns)):
            if columnIndex < 174:
                mylist = [_ for _ in rows[rowIndex][columnIndex: columnIndex + 26]]
                if len(list(dict.fromkeys(mylist))) == 26:
                    return [rowIndex, columnIndex, 26, 1]
            if rowIndex < 74:
                mylist = [_ for _ in columns[columnIndex][rowIndex: rowIndex + 26]]
                if len(list(dict.fromkeys(mylist))) == 26:
                    return [rowIndex, columnIndex, 1, 26]
            if columnIndex < 187 and rowIndex < 99:
                mylist = [_ for _ in rows[rowIndex][columnIndex: columnIndex + 13]] + [_ for _ in rows[rowIndex + 1][columnIndex: columnIndex + 13]]
                if len(list(dict.fromkeys(mylist))) == 26:
                    return [rowIndex, columnIndex, 13, 2]
            if rowIndex < 87 and columnIndex < 199:
                mylist = [_ for _ in columns[columnIndex][rowIndex: rowIndex + 13]] + [_ for _ in columns[columnIndex + 1][rowIndex: rowIndex + 13]]
                if len(list(dict.fromkeys(mylist))) == 26:
                    return [rowIndex, columnIndex, 2, 13]


print(maturaRows)
print(maturaColumns)
print(longest_length)
print(longest_rows)
print(subsequence())
