#!/usr/bin/env python

def linear_search(list_, item):
    if item in list_:
        for i in range(len(list_)):
            if list_[i] == item:
                return i
    else:
        return None


'''
Worst-case performance	O(n)
Best-case performance	O(1)
Average performance	O(n/2)
Worst-case space complexity	O(1) iterative
'''

if __name__ == "__main__":
    list_ = input("Enter list items : ")
    list_ = list_.split()
    item = input("Enter item to be searched : ")
    pos = linear_search(list_, item)
    if pos:
        print(f'{item} is present at position {pos+1}')
    else:
        print("Item is not present in the list...")
