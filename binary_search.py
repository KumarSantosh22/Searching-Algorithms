#!/usr/bin/env python

def binary_search(list_, item):
    lower_bound = 0
    upper_bound = len(list_)-1

    if item in list_:
        list_.sort()
        while lower_bound <= upper_bound:
            mid = (lower_bound + upper_bound) // 2

            if list_[mid] == item:
                return mid
            else:
                if list_[mid] < item:
                    lower_bound = mid+1
                else:
                    upper_bound = mid-1
    else:
        return None


'''
Worst-case space complexity‎: ‎O(1)
Worst-case performance‎: ‎O(log n)
Best-case performance‎: ‎O(1)
Average performance‎: ‎O(log n)
'''

if __name__ == "__main__":
    list_ = input("Enter list data : ")
    list_ = list_.split()
    item = input("Enter item to be searched : ")
    pos = binary_search(list_, item)

    if pos:
        print(f'{item} is present at position {pos+1}')
    else:
        print("Item is not in the list...")
