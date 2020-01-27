def sum_of_intervals(intervals):
    return len(set(i for start, end in intervals for i in list(range(start, end))))
