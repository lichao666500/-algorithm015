class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        max_index = height.index(max(height))
        for i in range(max_index):
            if height[i] != 0:
                del height[:i]
                break
        for i in range(len(height)-1,max_index,-1):
            if height[i] != 0:
                del height[i+1:]
                break
        sums = 0
        max_index = height.index(max(height))
        list_ = [0 for _ in range(len(height))]
        for i in range(1,max_index):
            list_[i] = max(list_[i-1],height[i-1])
            if list_[i] > height[i]:
                sums += list_[i] - height[i]
        for i in range(len(height)-2,max_index,-1):
            list_[i] = max(list_[i+1],height[i+1])
            if list_[i] > height[i]:
                sums += list_[i] - height[i]
        return sums
