class Solution:
    def maxArea(self, height: List[int]) -> int:
        r = len(height)-1
        l = 0
        max_area = (r-l)*min(height[l],height[r])
        while l<r:
            # print(l,r)
            curr_area = (r-l)*min(height[l],height[r])
            if curr_area > max_area:
                max_area = curr_area
            # print('curr_area', curr_area)
            curr_height = height[l] if height[l]<height[r] else height[r]
            if height[l]<height[r]:
                # print('move left')
                while height[l]<=curr_height:
                    if r==l: break
                    # print('l', l)
                    l+=1
            else:
                # print('move right')
                while height[r]<=curr_height:
                    if r==l: break
                    # print('r', r)
                    r-=1
        return max_area

