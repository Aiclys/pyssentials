#!/usr/bin/env python3

def sort(array):
    e = len(array)
    for i in range(e-1):
        moved = False

        for j in range(0, e-i-1):
            if order in ["asc", "ascending"]:
                if array[j] > array[j+1]:
                    moved = True
                    array[j], array[j+1] = array[j+1], array[j]
            elif order in ["desc", "descending"]:
                if array[j] < array[j+1]:
                    moved = True
                    array[j], array[j+1] = array[j+1], array[j]

        if not moved:
            return

def bin_search(array, element, is_sorted):
    if is_sorted == False:
        sort(array, "asc")
