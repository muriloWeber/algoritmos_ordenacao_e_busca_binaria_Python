# Busca Binária

def binary_search(array, item, begin=0, end=None):
    if end is None:
        end = len(array)-1
    if begin <= end:
        middle = (begin + end)//2
        if array[middle] == item:
            return middle
        if item < array[middle]:
            return binary_search(array, item, begin, middle-1)
        else:
            return binary_search(array, item, middle+1, end)
    return None

# lista = [2,3,4]
# binary_search(lista, 4, 0, len(lista)-1)
# print(binary_search(lista, 4))