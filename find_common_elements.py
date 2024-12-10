

#brute force
def find_common_elements_brute_force(arr1,arr2):

    common_elements = set()
    for e1 in arr1:
        for e2 in arr2:
            if e1 == e2:
                common_elements.add(e1)
            
    return list(common_elements)

#using a map and a set
def find_common_elements_simple(arr1,arr2):
    mapped_arr1 = {}
    common_elements = set()
    for e in arr1:
        mapped_arr1[e] = e
        
    for e in arr2:
        if e in mapped_arr1:
            common_elements.add(e)
    
    return list(common_elements)

#using sets union
def find_common_elements(arr1, arr2):
    return list(set(arr1) & set(arr2))

def find_common_elements_three_arrays_short(arr1, arr2, arr3):
    return list(set(arr1) & set(arr2) & set(arr3))

def find_common_elements_three_arrays(arr1, arr2, arr3):
    
    set1 = set(arr1)
    set2 = set(arr2)
    common_elements = set()
    
    for e3 in arr3:
        if e3 in set1 and e3 in set2:
            common_elements.add(e3)
            
    return list(common_elements)







# Test cases
print(find_common_elements([1, 2, 3, 4], [3, 4, 5, 6]))  # Expected: [3, 4]
print(find_common_elements([1, 2, 3], [4, 5, 6]))        # Expected: []
print(find_common_elements([], [1, 2, 3]))               # Expected: []
print(find_common_elements([1, 1, 2, 2], [2, 2, 3, 3]))  # Expected: [2]

print(find_common_elements_three_arrays([1, 2, 3], [2, 3, 4], [3, 4, 5]))  # Expected: [3]
print(find_common_elements_three_arrays([1, 2, 3], [4, 5, 6], [7, 8, 9]))  # Expected: []
print(find_common_elements_three_arrays([1, 1, 2], [1, 3, 4], [1, 5, 6]))  # Expected: [1]
print(find_common_elements_three_arrays([], [1, 2, 3], [3, 4, 5]))          # Expected: []
print(find_common_elements_three_arrays([1, 2, 3], [1, 2, 3], [1, 2, 3]))