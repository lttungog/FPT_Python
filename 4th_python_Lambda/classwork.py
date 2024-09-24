def numbers():
    
    number_list = [1, 3, 5, 6, 7, 9, 12, 16]
    print(f"The given list: {number_list}\n")
    
    # Đề bài cho chuỗi số hãy tìm và in ra các số chan
    
    even_numbers = list(filter(lambda x: (x % 2 == 0), number_list))
    print(f"The even numbers are: {even_numbers}")
    
    # Đề bài cho chuỗi số hãy tìm và in ra các số le
    
    odd_numbers = list(filter(lambda x: (x % 2 != 0), number_list))
    print(f"The odd numbers are: {odd_numbers}")
    
    # Đề bài cho chuỗi số hãy tìm và in ra các số chia hết cho số 3
    
    div_three = list(filter(lambda x: (x % 3 == 0), number_list))
    print(f"The numbers divisible by 3 are: {div_three}")
    
    # Sắp xếp chuỗi số tăng dần theo danh sách cho sẵn
    
    asc_list = sorted(number_list, key=lambda x:x)
    print(f"Ascending sort: {asc_list}")
    
    # Sắp xếp chuỗi số giảm dần theo danh sách cho sẵn
    
    desc_list = sorted(number_list, key=lambda x:x, reverse=True)
    print(f"Descending sort: {desc_list}")
    
def app():
    list = [1, 2, 3, 5, 7, 6, 86, 12]
    print(f"Original list: {list}")
    
    # Viết chương trình thêm vào một danh sách
    
    while True:
        try:
            add_num = int(input("Please enter a number: "))
        except ValueError:
            print("Please enter an integer value!")
        else:
            break
        
    list.append(add_num)
    
    print(f"Appended list: {list}")
    
    asc_list = sorted(list)
    print(f"Ascending list: {asc_list}")
    
    desc_list = sorted(list, reverse=True)
    print(f"Descending list: {desc_list}")
    
    list_length = len(list)
    
    max = list[0]
    for i in range(1, list_length):
        if list[i] > max:
            max = list[i]
    print(f"The largest number: {max}")
    
    min = list[0]
    for i in range(1, list_length):
        if list[i] < min:
            min = list[i]
    print(f"The smallest number: {min}")
    

if __name__ == '__main__':
    # numbers()
    app()