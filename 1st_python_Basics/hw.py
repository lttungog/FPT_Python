def homework_01():
    array = [1, 3, 10, 7, 5, 11, 6, 4]
    print(f"The array has the following numbers: {array}")
    
    def odd_number(arr):
        for num in arr:
            if num % 2 != 0:
                print(num, end=" ")
        
    print("The odd numbers are: ")         
    odd_number(array)
    
def homework_02():
    array = [2, 4, 6, 10]
    print(f"The array currently has the following numbers: {array}")
    number = int(input("Please enter a whole number: "))
    array.append(number)
    print(f"The new array: {array}")
    
def homework_03():
    array = [3, 5, 6, 8, 12]
    number = int(input("Please enter a whole number: "))
    array.append(number)
    
    length = len(array)
    print(f"The array has: {length} elements")
    
    def largest(arr, n):
        max = arr[0]
        
        for i in range(1, n):
            if arr[i] > max:
                max = arr[i]
        return max
    
    n = len(array)
    large = largest(array, n)
    print(f"The largest number of the array is: {large}")
    
    def smallest(arr, m):
        min = arr[0]
        
        for i in range(1, m):
            if arr[i] < min:
                min = arr[i]
        return min
        
    m = len(array)
    small = smallest(array, m)
    print(f"The largest number of the array is: {small}")
    
    def odd_sum(arr):
        
        odd_total = 0
        for num in arr:
            if num % 2 == 1:
                odd_total = odd_total + num
        return odd_total
    
    odd_num_total = odd_sum(array)
    print(f"The sum of all odd numbers in the array is: {odd_num_total}")
    
    def even_sum(arr):
        
        even_total = 0
        for num in arr:
            if num % 2 == 0:
                even_total = even_total + num
        return even_total
    
    even_num_total = even_sum(array)
    print(f"The sum of all even numbers in the array is: {even_num_total}")
    
def homework_04():
    array_1 = [1, 2, 3, 4, 5, 6, 7, 8]
    array_2 = [6, 7, 8, 9, 10, 11, 12, 13]
    print(f"The numbers is the 1st array are: {array_1}")
    print(f"The numbers is the 2nd array are: {array_2}")
    
    len1 = len(array_1)
    len2 = len(array_2)
    
    def largest(arr, n):
        max = arr[0]
        for i in range(1, n):
            if arr[i] > max:
                max = arr[i]
        return max
    
    max_arr_1 = largest(array_1, len1)
    max_arr_2 = largest(array_2, len2)
    print(f"Largest number of the first array is: {max_arr_1}")
    print(f"Largest number of the second array is: {max_arr_2}")
    
    if (max_arr_1 > max_arr_2):
        print(f"The largest number from both arrays is: {max_arr_1}")
    else:
        print(f"The largest number from both arrays is: {max_arr_2}")
        
    
    def smallest(arr, n):
        min = arr[0]
        for i in range(1, n):
            if arr[i] < min:
                min = arr[i]
        return min
    
    min_arr_1 = smallest(array_1, len1)
    min_arr_2 = smallest(array_2, len2)
    print(f"Smallest number of the first array is: {min_arr_1}")
    print(f"Smallest number of the second array is: {min_arr_2}")
    
    def compare_diff(arr1, arr2):
        diff = []
        for element in arr1:
            if element not in arr2:
                diff.append(element)
        for element in arr2:
            if element not in arr1:
                diff.append(element)
        return diff
                
    diff = compare_diff(array_1, array_2)
    print(f"The numbers available in one table but not the other are: {diff}")
    
    def compare_same(arr1, arr2):
        same = []
        for element in arr1:
            if element in arr2:
                same.append(element)
        return same
    
    same = compare_same(array_1, array_2)
    print(f"The numbers available in both tables are: {same}")
    
if __name__ == '__main__':
    # homework_01()
    # homework_02()
    # homework_03()
    homework_04()
    