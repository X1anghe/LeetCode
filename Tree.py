# MAX DEEP
class Solution:
    def maxDepth(self, root):
        if root is None: 
            return 0 
        else: 
            left_height = self.maxDepth(root.left) 
            right_height = self.maxDepth(root.right) 
            return max(left_height, right_height) + 1 


# DFS
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(x: int):
            vis.add(x)
            nonlocal num
            num += 1
            for it in rooms[x]:
                if it not in vis:
                    dfs(it)
        
        n = len(rooms)
        num = 0
        vis = set()
        dfs(0)
        return num == n


# BFS
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        num = 0
        vis = {0}
        que = collections.deque([0])

        while que:
            x = que.popleft()
            num += 1
            for it in rooms[x]:
                if it not in vis:
                    vis.add(it)
                    que.append(it)
        
        return num == n

# 并查集
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # def adjustHeap(nums, start, end):
        #     cur = start
        #     child = cur * 2 + 1
        #     if child < end:
        #         right = child+1
        #         if right < end and nums[child] < nums[right]:
        #             child = right
        #         if nums[cur] < nums[child]:
        #             nums[cur], nums[child] = nums[child], nums[cur]
        #             cur = child
        #             adjustHeap(nums, child, end)

        # n = len(nums)
        # count = 1
        # # build heads
        # for i in reversed(range(n//2)):
        #     adjustHeap(nums, i, n)
        # for i in reversed(range(n)):
        #     if count == k:
        #         return nums[0]
        #     nums[0], nums[i] = nums[i], nums[0]
        #     adjustHeap(nums, 0, i)
        #     count += 1
        # return nums[0]

        # quick sort
        # def partition(nums, low, high):
        #     pivot = nums[low]
        #     left, right = low, high

        #     while left < right:
        #         while left < right and pivot <= nums[right]:
        #             right -= 1
        #         nums[left] = nums[right]
        #         while left < right and pivot >= nums[left]:
        #             left += 1
        #         nums[right] = nums[left]
            
        #     nums[left] = pivot
        #     return left

        # def random_choice(nums, low, high):
        #     pivot_index = random.randint(low, high)
        #     nums[low], nums[pivot_index] = nums[pivot_index], nums[low]
        #     return partition(nums, low, high)

        # def quicksort(nums, low, high):
        #     if low > high:
        #         return
        #     mid = random_choice(nums, low, high)
        #     quicksort(nums, low, mid-1)
        #     quicksort(nums, mid+1, high)

        # quicksort(nums, 0, len(nums)-1)
        # return nums[-k]

        # quick sort2
        def quick_sort(nums):
            if len(nums) <= 1:
                return nums

            pivot = random.choice(nums)
            left  = quick_sort([x for x in nums if x < pivot])
            right = quick_sort([x for x in nums if x > pivot])
            mid  = [x for x in nums if x == pivot]

            return left + mid + right
        return quick_sort(nums)[-k]























                