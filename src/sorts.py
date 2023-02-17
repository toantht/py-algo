from typing import List


def bubble_sort(nums: List[int]):
    n = len(nums)
    for i in range(n - 1):
        swap = False
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swap = True
        if not swap:
            break

    return nums


def insertion_sort(nums: List[int]):
    n = len(nums)
    for i in range(n - 1):
        j = i
        while j >= 0 and nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            j -= 1

    return nums


def selection_sort(nums: List[int]):
    n = len(nums)
    for i in range(n - 1):
        minIndex = i
        for j in range(i + 1, n):
            if nums[j] < nums[minIndex]:
                minIndex = j
        nums[i], nums[minIndex] = nums[minIndex], nums[i]

    return nums


def heap_sort(nums: List[int]):
    def heapify(nums, index, size):
        mx = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < size and nums[left] > nums[mx]:
            mx = left

        if right < size and nums[right] > nums[mx]:
            mx = right

        if mx != index:
            nums[mx], nums[index] = nums[index], nums[mx]
            heapify(nums, mx, size)

    n = len(nums)
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, i, n)

    # Recursion swap nums[0] to the right, heapify
    for i in range(n - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, 0, i)

    return nums


def merge_sort(nums: List[int]):
    def helper(nums, l, r):
        if l >= r:
            return
        m = (l + r) // 2
        helper(nums, l, m)
        helper(nums, m + 1, r)
        merge(nums, l, r)

    def merge(nums, l, r):
        m = (l + r) // 2
        res = []
        i, j = l, m + 1
        while i <= m and j <= r:
            if nums[i] < nums[j]:
                res.append(nums[i])
                i += 1
            else:
                res.append(nums[j])
                j += 1

        while i <= m:
            res.append(nums[i])
            i += 1

        while j <= r:
            res.append(nums[j])
            j += 1

        for k in range(len(res)):
            nums[l] = res[k]
            l += 1

    helper(nums, 0, len(nums) - 1)
    return nums


def quick_sort(nums: List[int]):
    def helper(nums, l, r):
        if l >= r:
            return

        p = partition(nums, l, r)
        helper(nums, l, p - 1)
        helper(nums, p + 1, r)

    def partition(nums, l, r):
        pivot = nums[r]
        i, j = l, r - 1
        while i <= j:
            if nums[i] <= pivot:
                i += 1
            elif nums[j] >= pivot:
                j -= 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        nums[i], nums[r] = nums[r], nums[i]

        return i

    helper(nums, 0, len(nums) - 1)
    return nums
