"""贪心算法相关题目。"""


def can_jump(nums: list[int]) -> bool:
    """55. 跳跃游戏"""
    farthest = 0
    for index, step in enumerate(nums[:-1]):
        if farthest < index:
            break
        farthest = max(farthest, index + step)
    return farthest >= len(nums) - 1


def min_jumps(nums: list[int]) -> int:
    """45. 跳跃游戏 II"""
    jumps = 0
    current_end = 0
    farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
    return jumps


def find_content_children(g: list[int], s: list[int]) -> int:
    """455. 分发饼干"""
    g.sort()
    s.sort()
    child = 0
    for cookie in s:
        if child < len(g) and g[child] <= cookie:
            child += 1
    return child


def largest_sum_after_k_negations(nums: list[int], k: int) -> int:
    """1005. K 次取反后最大化的数组和"""
    nums.sort(key=abs, reverse=True)
    for i in range(len(nums)):
        if nums[i] < 0 and k > 0:
            nums[i] = -nums[i]
            k -= 1
    if k % 2 == 1:
        nums[-1] = -nums[-1]
    return sum(nums)


def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    """134. 加油站"""
    total = current = 0
    start = 0
    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        current += diff
        total += diff
        if current < 0:
            start = i + 1
            current = 0
    return start if total >= 0 else -1


def candy(ratings: list[int]) -> int:
    """135. 分发糖果"""
    candies = [1] * len(ratings)
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    for i in range(len(ratings) - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    return sum(candies)


def lemonade_change(bills: list[int]) -> bool:
    """860. 柠檬水找零"""
    five = ten = 0
    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if five == 0:
                return False
            five -= 1
            ten += 1
        elif five > 0 and ten > 0:
            five -= 1
            ten -= 1
        elif five >= 3:
            five -= 3
        else:
            return False
    return True


def reconstruct_queue(people: list[list[int]]) -> list[list[int]]:
    """406. 根据身高重建队列"""
    people.sort(key=lambda x: (-x[0], x[1]))
    queue: list[list[int]] = []
    for person in people:
        queue.insert(person[1], person)
    return queue


def find_min_arrow_shots(points: list[list[int]]) -> int:
    """452. 用最少数量的箭引爆气球"""
    if not points:
        return 0
    points.sort(key=lambda x: x[0])
    arrows = 1
    end = points[0][1]
    for i in range(1, len(points)):
        if points[i][0] > end:
            arrows += 1
            end = points[i][1]
        else:
            end = min(end, points[i][1])
    return arrows


def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    """435. 无重叠区间"""
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[0])
    kept = 1
    end = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] >= end:
            kept += 1
            end = intervals[i][1]
        else:
            end = min(end, intervals[i][1])
    return len(intervals) - kept


def partition_labels(s: str) -> list[int]:
    """763. 划分字母区间"""
    last = {ch: i for i, ch in enumerate(s)}
    result: list[int] = []
    start = end = 0
    for i, ch in enumerate(s):
        end = max(end, last[ch])
        if i == end:
            result.append(end - start + 1)
            start = i + 1
    return result


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """56. 合并区间"""
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if merged[-1][1] >= start:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


def insert_interval(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    """57. 插入区间"""
    result: list[list[int]] = []
    start, end = new_interval
    inserted = False
    for lo, hi in intervals:
        if hi < start:
            result.append([lo, hi])
        elif lo > end:
            if not inserted:
                result.append([start, end])
                inserted = True
            result.append([lo, hi])
        else:
            start = min(start, lo)
            end = max(end, hi)
    if not inserted:
        result.append([start, end])
    return result


def monotone_increasing_digits(n: int) -> int:
    """738. 单调递增的数字"""
    digits = list(str(n))
    for i in range(len(digits) - 1, 0, -1):
        if digits[i - 1] > digits[i]:
            digits[i - 1] = str(int(digits[i - 1]) - 1)
            for j in range(i, len(digits)):
                digits[j] = "9"
    return int("".join(digits))


def get_kth_magic_number(k: int) -> int:
    """313. 超级丑数"""
    p3 = p5 = p7 = 0
    dp = [1] * k
    for i in range(1, k):
        dp[i] = min(dp[p3] * 3, dp[p5] * 5, dp[p7] * 7)
        if dp[i] == dp[p3] * 3:
            p3 += 1
        if dp[i] == dp[p5] * 5:
            p5 += 1
        if dp[i] == dp[p7] * 7:
            p7 += 1
    return dp[-1]


def least_interval(tasks: list[str], n: int) -> int:
    """621. 任务调度器"""
    from collections import Counter

    counts = Counter(tasks)
    max_freq = max(counts.values())
    max_count = sum(1 for freq in counts.values() if freq == max_freq)
    return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)
