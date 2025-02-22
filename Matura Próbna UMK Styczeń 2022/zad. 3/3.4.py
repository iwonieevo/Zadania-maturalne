def flip(a, b, tab):
    answer = []
    a -= 1
    b -= 1
    if a > 0:
        answer += tab[:a]
    temp = tab[a:(b + 1)]
    temp.reverse()
    answer += temp
    if b < len(tab) - 1:
        answer += tab[(b + 1):]
    return answer


def operations_to_sort(tab):
    answer = []
    for i in range(len(tab)):
        minIndex = tab.index(min(tab[i:]))
        if minIndex != i:
            tab = flip(i + 1, minIndex + 1, tab)
            answer.append(f"flip({i + 1},{minIndex + 1})")
    return answer


TAB = [int(_) for _ in input("tab = ").replace("[", "").replace("]", "").rstrip().split(",")]

for operation in operations_to_sort(TAB):
    print(operation, end=" ")



