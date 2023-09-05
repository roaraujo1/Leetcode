class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda i : i[0])
        prev = intervals[0][1]
        for start,end in intervals[1:]:
            if prev > start:
                return False
            prev = end
        return True