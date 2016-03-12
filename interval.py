# !/usr/bin/env python
# coding=utf-8

# Given a collection of intervals, merge all overlapping intervals.

def merge(intervals):
    if len(intervals) == 0:
        return intervals
    
    intervals = sorted(intervals, key=lambda interval: interval.start)
    merge_intervals = []
    cur_interval = intervals[0]
    for targe_interval in intervals:
        if cur_interval.end < targe_interval.start:
            merge_intervals.append(cur_interval)
            cur_interval = targe_interval
            continue
        cur_interval.end = max(targe_interval.end, cur_interval.end)
        
    merge_intervals.append(cur_interval)
    return merge_intervalsGivenga collection of intervals, merge all overlapping intervals.

# Givengangintervalglist which are flying and landing time 
# of the flight. How many airplanes are on the sky at most?

def count_airplanes(airplanes):
    def sorter(x, y):
        if x[0] != y[0]:
            return x[0] - y[0]
        return x[1] - y[1]

    timepoints = []
    for airplane in airplanes:
        timepoints.append((airplane[0], 1))
        timepoints.append((airplane[1], -1))
    timepoints = sorted(timepoints, cmp=sorter)
    sum, most = 0, 0
    for t, delta in timepoints:
        sum += delta
        most = max(most, sum)

    return most

if __name__ == "__main__":
    # airplanes = [[1,2],[2,3], [5,8], [4,7]]
    # count_airplanes(airplanes)
