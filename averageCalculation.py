def average_length(lists):
    # Check if the input is not empty
    if not lists:
        return 0
    
    # Calculate the total length of all lists combined
    total_length = sum(len(lst) for lst in lists)
    
    # Calculate the average length
    return total_length / len(lists)

# Example usage:
list1 = [0, 11, 16, 17, 9, 8, 12, 7, 12, 3, 12, 8, 18, 5, 4, 8, 4, 2, 4, 8, 19]
list2 = [0, 1, 0, 1, 8, 1, 0, 13, 4, 17, 14, 11, 16, 5, 18, 0, 1, 0, 18, 0, 13, 7, 10, 4, 10, 16, 17, 19]
list3 = [0, 12, 0, 18, 15, 17, 19]
list4 = [0, 1, 8, 16, 8, 18, 0, 18, 0, 1, 9, 17, 14, 15, 10, 18, 14, 15, 16, 13, 3, 5, 19]
list5 = [0, 18, 1, 9, 1, 12, 0, 12, 3, 14, 11, 5, 4, 10, 4, 18, 4, 13, 14, 3, 18, 15, 2, 15, 9, 8, 12, 0, 1, 8, 16, 10, 16, 4, 5, 3, 2, 11, 5, 4, 8, 19]
list6 = [0, 11, 0, 13, 4, 6, 2, 4, 13, 16, 15, 18, 8, 18, 15, 11, 15, 9, 17, 15, 1, 12, 7, 12, 3, 14, 11, 5, 18, 4, 5, 13, 12, 7, 12, 1, 7, 15, 16, 17, 2, 6, 14, 15, 1, 9, 2, 12, 8, 12, 2, 4, 8, 19]
list7 = [0, 11, 3, 13, 5, 3, 14, 4, 16, 13, 7, 1, 18, 15, 2, 11, 15, 11, 0, 13, 14, 3, 12, 3, 12, 0, 12, 8, 1, 0, 13, 3, 12, 3, 6, 14, 13, 14, 13, 19]
list8 = [0, 13, 16, 17, 16, 5, 13, 4, 5, 3, 5, 19]
list9 = [0, 18, 10, 4, 5, 4, 18, 3, 11, 15, 9, 1, 9, 2, 19]
list10 = [0, 1, 18, 1, 12, 7, 1, 8, 9, 2, 3, 6, 19]



lists = [list1, list2, list3, list4, list5, list6, list7, list8, list9, list10]
avg_length = average_length(lists)

print(f"The average length of the lists is: {avg_length}")