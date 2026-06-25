class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]

        heapq.heapify(stones)
        while len(stones) >1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x-y ==0:
                continue
            else:
                heapq.heappush(stones,x-y)
        
        if stones:
            return (heapq.heappop(stones))*-1
        else:
            return 0