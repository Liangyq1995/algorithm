from abc import abstractmethod


class BackTracking:

    @abstractmethod
    def combine(self, n: int, k: int) -> list[list[int]]:
        """
        给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
        示例: 输入: n = 4, k = 2 输出: [ [2,4], [3,4], [2,3], [1,2], [1,3], [1,4], ]
        """
        def backtracking(n, k, startIndex, path, result):
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(startIndex, n + 1):  # 需要优化的地方
            # for i in range(startIndex, n - (k - len(path)) + 2):  # 优化的地方, 保证有足够的元素满足path的长度
                path.append(i)  # 处理节点
                self.backtracking(n, k, i + 1, path, result)
                path.pop()  # 回溯，撤销处理的节点
        result = []  # 存放结果集
        backtracking(n, k, 1, [], result)
        return result
    
    @abstractmethod
    def generate_parenthesis(n: int) -> list[str]:
        """
        数字 n代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

        示例 1：
        输入：n = 3
        输出：["((()))","(()())","(())()","()(())","()()()"]
        示例 2：
        输入：n = 1
        输出：["()"]
        """
        ans = []

        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()

        backtrack([], 0, 0)
        return ans
    
    @abstractmethod
    def letter_combinations(digits: str) -> list[str]:
        """
        给定一个仅包含数字2-9的字符串，返回所有它能表示的字母组合。答案可以按任意顺序返回。给出数字到字母的映射如下（与电话按键相同）。
        注意1不对应任何字母。
        示例 1：
        输入：digits = "23"
        输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
        """
        if not digits:
            return list()

        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index: int):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phone_map[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        combination = list()
        combinations = list()
        backtrack(0)
        return combinations
    
    @abstractmethod
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        """
        找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：

        只使用数字1到9
        每个数字 最多使用一次 
        返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。
        """
        def backtracking(k, n, startIndex, path, result):
            if len(path) == k:
                if sum(path) == n:
                    result.append(path[:])
                return
            for i in range(startIndex, 10):
                path.append(i)
                backtracking(k, n, i + 1, path, result)
                path.pop()
        result = []
        backtracking(k, n, 1, [], result)
        return result
    
    @abstractmethod
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
        candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 
        对于给定的输入，保证和为 target 的不同组合数少于 150 个。

        示例 1：
        输入：candidates = [2,3,6,7], target = 7
        输出：[[2,2,3],[7]]
        """
        def backtracking(candidates, target, startIndex, path, result):
            if sum(path) == target:
                result.append(path[:])
                return 
            elif sum(path) > target:
                return 
            else:
                for i in range(startIndex, len(candidates)):
                    path.append(candidates[i])
                    backtracking(candidates, target, i, path, result)
                    path.pop()
        result = []
        backtracking(candidates, target, 0, [], result)
        return result
    
    @abstractmethod
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
        candidates 中的每个数字在每个组合中只能使用 一次 。

        示例 1:
        输入: candidates = [10,1,2,7,6,1,5], target = 8,
        输出:
        [
        [1,1,6],
        [1,2,5],
        [1,7],
        [2,6]
        ]
                """
        def backtracking(candidates, target, startIndex, path, result):
            if sum(path) == target:
                result.append(path[:])
                return 
            elif sum(path) > target:
                return 
            else:
                for i in range(startIndex, len(candidates)):
                    if i > startIndex and candidates[i] == candidates[i - 1]:
                        continue
                    path.append(candidates[i])
                    backtracking(candidates, target, i+1, path, result)
                    path.pop()
        result = []
        candidates.sort()
        backtracking(candidates, target, 0, [], result)
        return result
    
    @abstractmethod
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
        示例: 输入: nums = [1,2,3] 输出: [ [3],   [1],   [2],   [1,2,3],   [1,3],   [2,3],   [1,2],   [] ]
        """
        def backtracking(nums, startIndex, path, result):
            result.append(path[:])  # 收集子集，要放在终止添加的上面，否则会漏掉自己
            # if startIndex >= len(nums):  # 终止条件可以不加
            #     return
            for i in range(startIndex, len(nums)):
                path.append(nums[i])
                backtracking(nums, i + 1, path, result)
                path.pop()
        result = []
        path = []
        backtracking(nums, 0, path, result)
        return result
    
    @abstractmethod
    def subsets_with_dup(self, nums: list[int]) -> list[list[int]]:
        """
        给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的 子集（幂集）。解集 不能 包含重复的子集。
        返回的解集中，子集可以按 任意顺序 排列。

        示例 1：
        输入：nums = [1,2,2]
        输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
        """
        def backtracking(nums, startIndex, path, result):
            result.append(path[:])
            for i in range(startIndex, len(nums)):
                if i > startIndex and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtracking(nums, i + 1, path, result)
                path.pop()
        nums.sort()
        result = []
        backtracking(nums, 0, [], result)
        return result
    
    @abstractmethod
    def restore_ip_addresses(self, s: str) -> list[str]:
        """
        给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
        有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
        例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效的 IP 地址。

        示例 1：
        输入：s = "25525511135"
        输出：["255.255.11.135","255.255.111.35"]
        """
        def backtracking(s, start_index, point_num, current, result):
            if point_num == 3:  # 逗点数量为3时，分隔结束
                if self.is_valid(s, start_index, len(s) - 1):  # 判断第四段子字符串是否合法
                    current += s[start_index:]  # 添加最后一段子字符串
                    result.append(current)
                return

            for i in range(start_index, len(s)):
                if self.is_valid(s, start_index, i):  # 判断 [start_index, i] 这个区间的子串是否合法
                    sub = s[start_index:i + 1]
                    backtracking(s, i + 1, point_num + 1, current + sub + '.', result)
                else:
                    break
        result = []
        backtracking(s, 0, 0, "", result)
        return result
    
    @abstractmethod
    def is_valid(self, s, start, end):
        if start > end:
            return False
        if s[start] == '0' and start != end:  # 0开头的数字不合法
            return False
        num = 0
        for i in range(start, end + 1):
            if not s[i].isdigit():  # 遇到非数字字符不合法
                return False
            num = num * 10 + int(s[i])
            if num > 255:  # 如果大于255了不合法
                return False
        return True
    
    @abstractmethod
    def partition(self, s: str) -> list[list[str]]:
        """
        给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
        返回 s 所有可能的分割方案。

        示例: 输入: "aab" 输出: [ ["aa","b"], ["a","a","b"] ]
        """
        def backtracking(s, start_index, path, result ):
            # Base Case
            if start_index == len(s):
                result.append(path[:])
                return
            
            # 单层递归逻辑
            for i in range(start_index, len(s)):
                # 若反序和正序相同，意味着这是回文串
                if s[start_index: i + 1] == s[start_index: i + 1][::-1]:
                    path.append(s[start_index:i+1])
                    backtracking(s, i+1, path, result)   # 递归纵向遍历：从下一处进行切割，判断其余是否仍为回文串
                    path.pop()             # 回溯
        result = []
        backtracking(s, 0, [], result)
        return result
    
    @abstractmethod
    def find_sub_sequences(self, nums: list[int]) -> list[list[int]]:
        """
        给你一个整数数组 nums ，找出并返回所有该数组中不同的递增子序列，递增子序列中 至少有两个元素 。你可以按 任意顺序 返回答案。
        数组中可能含有重复元素，如出现两个整数相等，也可以视作递增序列的一种特殊情况。

        示例 1：
        输入：nums = [4,6,7,7]
        输出：[[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
        """
        def backtracking(nums, startIndex, path, result):
            if len(path) >= 2:
                result.append(path[:])
            
            uset = set()  # 使用集合对本层元素进行去重
            for i in range(startIndex, len(nums)):
                if (path and nums[i] < path[-1]) or nums[i] in uset:
                    continue
                
                uset.add(nums[i])  # 记录这个元素在本层用过了，本层后面不能再用了
                path.append(nums[i])
                backtracking(nums, i + 1, path, result)
                path.pop()
                    
        result = []
        backtracking(nums, 0, [], result)
        return result
    
    @abstractmethod
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

        示例 1：
        输入：nums = [1,2,3]
        输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        """

        def backtracking(nums, path, result):
            if len(path) == len(nums):
                result.append([nums[i] for i in path])
            
            for i in range(len(nums)):
                if i in path:
                    continue
                path.append(i)
                backtracking(nums, path, result)
                path.pop()
        result = []
        backtracking(nums, [], result)
        return result
    
    @abstractmethod
    def permute_unique(self, nums: list[int])->list[list[int]]:
        """
        给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

        示例 1：
        输入：nums = [1,1,2]
        输出： [[1,1,2], [1,2,1], [2,1,1]]
        """
        def backtracking(nums, path, used, result):
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]) or used[i]:
                    # 保证了对于重复数的集合，一定是从左往右逐个填入的
                    continue
                used[i] = True
                path.append(nums[i])
                self.backtracking(nums, path, used, result)
                path.pop()
                used[i] = False
        nums.sort()  # 排序
        result = []
        backtracking(nums, [], [False] * len(nums), result)
        return result
    

    @abstractmethod
    def word_search_exist(self, board: list[list[str]], word: str) -> bool:
        """给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
        单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。"""
        m, n = len(board), len(board[0])

        def dfs(board, r, c, word, index):
            if index == len(word):
                return True
            if r < 0 or r >=m or c < 0 or c >=n or board[r][c] != word[index]:
                return False
            board[r][c] = '*'  # 避免重复使用
            res = dfs(board, r-1, c, word, index+1) or dfs(board, r+1, c, word, index+1) or dfs(board, r, c-1, word, index+1) or dfs(board, r, c+1, word, index+1)
            board[r][c] = word[index]
            return res
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    if dfs(board, r, c, word, 0):
                        return True
        return False
    

    @abstractmethod
    def make_square(self, matchsticks: list[int]) -> bool:
        """
        你将得到一个整数数组 matchsticks ，其中 matchsticks[i] 是第 i 个火柴棒的长度。你要用 所有的火柴棍 拼成一个正方形。
        你 不能折断 任何一根火柴棒，但你可以把它们连在一起，而且每根火柴棒必须 使用一次 。
如果    你能使这个正方形，则返回 true ，否则返回 false 。
        """
        side = sum(matchsticks) // 4
        sides = [0] * 4
        if side * 4 != sum(matchsticks):
            return False
        matchsticks.sort(reverse=True)
        def backtracking(i):
            if i == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3] == side
            for j in range(4):
                if sides[j] + matchsticks[i] <= side:
                    sides[j] += matchsticks[i]
                    if backtracking(i + 1):
                        return True
                    sides[j] -= matchsticks[i]
            return False
        
        return backtracking(0)
    


    


    
  





    



    



    




    


