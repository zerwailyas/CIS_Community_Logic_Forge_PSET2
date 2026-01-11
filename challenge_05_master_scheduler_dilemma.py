def min_cancelled_bookings(intervals):
    if not intervals:
        return 0

    # Sort intervals by end time
    intervals.sort(key=lambda x: x[1])

    removals = 0
    prev_end = intervals[0][1]   # end time of the first booking

    for i in range(1, len(intervals)):
        start, end = intervals[i]

    
        if start < prev_end:
            removals += 1
        else:
            prev_end = end

    return removals

intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(min_cancelled_bookings(intervals))
