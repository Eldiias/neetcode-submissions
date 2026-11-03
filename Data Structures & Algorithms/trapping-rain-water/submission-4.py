class Solution:
    def trap(self, height: List[int]) -> int:
        
        zones = []
        completed=True
        hole = False
        l=0
        if len(height)<3: return 0
        while l<len(height)-1:
            if completed:
                zone=[]
            if height[l]>0:
                zone.append(l)
                completed=False
            for r in range(l+1, len(height)):
                if height[r]<height[l]:
                    if height[r]>height[r-1]: hole = True
                    zone.append(r)
                    completed=False
                else:
                    if zone: 
                        zone.append(r)
                        zones.append(zone)
                        completed=True
                    l=r
                    break
            if not completed:
                if not hole:
                    zone=[]
                    l+=1
                else:
                    while len(zone)>1:
                        lz = zone.pop()
                        plz = zone.pop()
                        zone.append(plz)
                        if height[plz]<=height[lz]:
                            zone.append(lz)
                            break

                    zones.append(zone)
                    l = r
                completed=True
        res = 0
        for z in zones:
            h = min(height[z[0]], height[z[-1]])
            res+=sum(h-height[i] for i in z if (h-height[i])>0)
        return res