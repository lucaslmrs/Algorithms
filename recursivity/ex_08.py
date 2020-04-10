from random import randint
def binary_search(n, num_list, start=0, end=-1):
    if end == -1:
        end = len(num_list) - 1
    current = int((start + end) / 2)

    if start != end:
        if n < num_list[current]:
            return binary_search(n, num_list, start, current - 1)
        elif n > num_list[current]:
            return binary_search(n, num_list, current + 1, end)
        else:
            return current
    else:
        return current if n == num_list[current] else -1


number_list = [n for n in range(0, 10000, 2)]
target = randint(0, 10000)
print(f'target -> ', target)
print('Position -> ', binary_search(target, number_list))
