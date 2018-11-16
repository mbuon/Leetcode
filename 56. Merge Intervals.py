# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        
        intervals = sorted(intervals, key = lambda k: k.start)
        output = []
        
        i = 0
        j = 1
        
        while (j < len(intervals)):

            if (intervals[i].end >= intervals[j].start):
                interval = Interval(intervals[i].start, max(intervals[i].end, intervals[j].end))
                intervals[i] = interval
                
                if (j == len(intervals) - 1):
                    output.append(intervals[i])

            else:
                output.append(intervals[i])                
                i = j
                
                if (j == len(intervals) - 1):
                    output.append(intervals[j])
                
            j += 1

        if (len(output) == 0):
            return intervals
        
        else:
            return output