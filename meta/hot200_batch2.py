"""Hot 200 第二批新增题目的元数据。"""
from meta.helpers import _m

PROBLEMS = {
    'data_structures/array/basic.py::is_palindrome_number': _m(
        '9', '回文数',
        '给你一个整数 x，'
        '如果 x 是一个回文整数，返回 true；否则返回 false。\n\n'
        '回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。\n\n'
        '本实现反转数字的后半部分与前半部分比较，'
        '避免字符串转换，O(log₁₀ x) 时间。\n\n'
        '约束：-2³¹ ≤ x ≤ 2³¹ - 1；'
        '负数及末尾为 0 的非零数不是回文。',
        [
            '示例 1：x = 121 → true。'
            '121 正读倒读均为 121。',
            '示例 2：x = -121 → false。'
            '负数不是回文。',
            '示例 3：x = 10 → false。'
            '01 倒读为 10，不相等。',
        ],
        [
            '若 x < 0 或 x 为 10 的倍数且 x ≠ 0，直接返回 False。',
            '初始化 reversed_half = 0，循环 while x > reversed_half。',
            '每轮 reversed_half = reversed_half * 10 + x % 10，x //= 10。',
            '循环结束：偶数位 x == reversed_half；'
            '奇数位 x == reversed_half // 10。',
            '满足任一条件返回 True，否则 False。',
        ],
        '数学',
        code_notes=[
            'if x < 0 or (x % 10 == 0 and x != 0): return False — 负数与 10/20/… 排除。',
            'reversed_half = 0 — 累积反转的后半段数字。',
            'while x > reversed_half — 处理到数字中点即停，避免溢出。',
            'reversed_half = reversed_half * 10 + x % 10 — 从末尾逐位反转。',
            'x //= 10 — 原数去掉已反转的末位。',
            'return x == reversed_half or x == reversed_half // 10 — 偶/奇数位分别判断。',
            '仅反转一半，比全转字符串更省空间；x=0 时循环不执行，正确返回 True。',
        ],
        complexity='时间 O(log₁₀ x)，空间 O(1)。',
    ),
    'data_structures/array/basic.py::divide': _m(
        '29', '两数相除',
        '给你两个整数 dividend 和 divisor，'
        '将两数相除，要求不使用乘法、除法和 mod 运算符，'
        '返回商（向零截断）。\n\n'
        '本实现用位运算模拟「减去除数 × 2^k」的倍增减法，'
        '从高位到低位累加商。\n\n'
        '约束：-2³¹ ≤ dividend, divisor ≤ 2³¹ - 1；'
        'divisor ≠ 0；结果在 32 位有符号整数范围内；'
        '溢出时返回 2³¹ - 1。',
        [
            '示例 1：dividend = 10, divisor = 3 → 3。',
            '示例 2：dividend = 7, divisor = -3 → -2。'
            '向零截断。',
            '示例 3：dividend = -2³¹, divisor = -1 → 2147483647。'
            '溢出边界特判。',
        ],
        [
            '特判 dividend == -2³¹ 且 divisor == -1，返回 2³¹ - 1。',
            '根据符号异或确定 sign，取 a = |dividend|、b = |divisor|。',
            'for i in range(31, -1, -1)：若 (a >> i) >= b，'
            'result += 1 << i，a -= b << i。',
            '返回 sign * result。',
        ],
        '位运算',
        code_notes=[
            'if dividend == -2 ** 31 and divisor == -1: return 2 ** 31 - 1 — 溢出特判。',
            'sign = -1 if (dividend < 0) ^ (divisor < 0) else 1 — 异或定符号。',
            'a, b = abs(dividend), abs(divisor) — 转为正数处理。',
            'for i in range(31, -1, -1) — 从 2³¹ 到 2⁰ 逐位尝试。',
            'if (a >> i) >= b: result += 1 << i; a -= b << i — 能减则累加商并更新余量。',
            'return sign * result — 恢复符号。',
            '倍增减法等价于 long division；O(log a) 轮，每轮 O(1)。',
        ],
        complexity='时间 O(log |dividend|)，空间 O(1)。',
    ),
    'data_structures/matrix/matrix.py::is_valid_sudoku': _m(
        '36', '有效的数独',
        '请你判断一个 9×9 的数独是否有效。'
        '只需要根据以下规则，'
        '验证已经填入的数字是否有效即可。\n\n'
        '数字 1-9 在每一行、每一列、'
        '每一个 3×3 宫内均只出现一次。\n\n'
        '空白用 "." 表示，'
        '已填数字需满足上述约束。\n\n'
        '约束：board.length == 9；board[i].length == 9；'
        'board[i][j] 为数字 1-9 或 "."。',
        [
            '示例 1：有效数独（含部分 "."）→ true。',
            '示例 2：同一行出现重复 "8" → false。',
            '示例 3：同一 3×3 宫出现重复 → false。',
        ],
        [
            '初始化 rows、cols、boxes 各 9 个空 set。',
            '双重循环遍历每个格子 (r, c)，取 ch = board[r][c]。',
            '若 ch == "." 跳过；否则 box = (r//3)*3 + c//3。',
            '若 ch 已在 rows[r]、cols[c] 或 boxes[box] 中，返回 False。',
            '将 ch 加入三个 set；全部通过返回 True。',
        ],
        '哈希表',
        code_notes=[
            'rows = [set() for _ in range(9)] — 每行已见数字。',
            'cols = [set() for _ in range(9)] — 每列已见数字。',
            'boxes = [set() for _ in range(9)] — 每个 3×3 宫已见数字。',
            'if ch == ".": continue — 空格不参与校验。',
            'box = (r // 3) * 3 + c // 3 — 宫格编号 0..8。',
            'if ch in rows[r] or ch in cols[c] or ch in boxes[box]: return False — 重复检测。',
            'rows[r].add(ch); cols[c].add(ch); boxes[box].add(ch) — 登记数字。',
        ],
        complexity='时间 O(81) = O(1)，空间 O(1)（固定 9×9）。',
    ),
    'paradigms/backtracking/core.py::solve_sudoku': _m(
        '37', '解数独',
        '编写一个程序，'
        '通过填充空格来解决数独问题。\n\n'
        '数独解法需满足：'
        '数字 1-9 在每一行、每一列、'
        '每一个 3×3 宫内均只出现一次。\n\n'
        '空白用 "." 表示，'
        '保证输入有唯一解。\n\n'
        '约束：board.length == 9；board[i].length == 9；'
        'board[i][j] 为 "1"-"9" 或 "."。',
        [
            '示例 1：部分填写的 9×9 棋盘 → 原地填充为完整有效解。',
            '示例 2：仅少量空格 → 回溯填入唯一解。',
            '示例 3：多行多列 "." → 按约束逐格填数。',
        ],
        [
            '预处理：收集 empty 列表，'
            '同时用 rows/cols/boxes 三个 set 记录已填数字。',
            'backtrack(index)：index == len(empty) 时返回 True。',
            '取 (r, c) = empty[index]，box = (r//3)*3 + c//3。',
            '遍历 digit "1".."9"：若不在三个 set 中，'
            '填入并递归 index+1；失败则回溯撤销。',
            'backtrack(0) 完成求解，board 原地修改。',
        ],
        '回溯',
        code_notes=[
            'empty: list[tuple[int, int]] = [] — 空格坐标列表，决定搜索顺序。',
            'rows[r].add(ch); cols[c].add(ch); boxes[...].add(ch) — 预处理登记。',
            'def backtrack(index: int) -> bool — 按 empty 顺序逐格填数。',
            'for digit in map(str, range(1, 10)) — 尝试 1 到 9。',
            'if digit in rows[r] or digit in cols[c] or digit in boxes[box]: continue — 剪枝。',
            'board[r][c] = digit; rows/cols/boxes.add — 做选择。',
            'if backtrack(index + 1): return True — 成功则向上传递。',
            'board[r][c] = "."; rows/cols/boxes.remove — 撤销选择。',
            '无返回值（None），board 原地修改即为答案。',
        ],
        complexity='时间 O(9^m)，m 为空格数；空间 O(1)（不含递归栈）。',
    ),
    'strings/operations.py::multiply_strings': _m(
        '43', '字符串相乘',
        '给定两个以字符串形式表示的非负整数 num1 和 num2，'
        '返回 num1 和 num2 的乘积，'
        '它们的乘积也表示为字符串形式。\n\n'
        '不能使用任何内置的 BigInteger 库或 convert 直接转换。\n\n'
        '本实现模拟竖式乘法，'
        'result 数组长度 m+n，逐位相乘并处理进位。\n\n'
        '约束：1 ≤ num1.length, num2.length ≤ 200；'
        'num1 和 num2 都只包含数字 0-9；'
        '不含前导零（除非数字本身是 0）。',
        [
            '示例 1：num1 = "2", num2 = "3" → "6"。',
            '示例 2：num1 = "123", num2 = "456" → "56088"。',
            '示例 3：num1 = "0", num2 = "123" → "0"。'
            '任一为 0 则返回 "0"。',
        ],
        [
            '若 num1 == "0" 或 num2 == "0"，返回 "0"。',
            '创建 result = [0] * (m + n)，从低位到高位双重循环。',
            'mul = int(num1[i]) * int(num2[j])，'
            'total = mul + result[i+j+1]，更新个位与进位。',
            '跳过前导零，join 剩余位为字符串返回。',
        ],
        '字符串',
        code_notes=[
            'if num1 == "0" or num2 == "0": return "0" — 零乘特判。',
            'result = [0] * (m + n) — 乘积最多 m+n 位。',
            'for i in range(m - 1, -1, -1) — 从 num1 末位向前。',
            'for j in range(n - 1, -1, -1) — 从 num2 末位向前。',
            'mul = int(num1[i]) * int(num2[j]); total = mul + result[i + j + 1] — 竖式相乘。',
            'result[i + j + 1] = total % 10; result[i + j] += total // 10 — 个位与进位。',
            'while start < len(result) - 1 and result[start] == 0: start += 1 — 去前导零。',
            'return "".join(map(str, result[start:])) — 数组转字符串。',
        ],
        complexity='时间 O(m × n)，空间 O(m + n)，m、n 为两数长度。',
    ),
    'paradigms/backtracking/core.py::total_n_queens': _m(
        '52', 'N 皇后 II',
        'n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，'
        '且使它们不能互相攻击（即任意两个皇后都不能处于同一行、'
        '同一列或同一斜线上）。\n\n'
        '给你一个整数 n，'
        '返回 n 皇后不同的解决方案的数量。\n\n'
        '约束：1 ≤ n ≤ 9。',
        [
            '示例 1：n = 4 → 2。'
            '4 皇后共有 2 种解法。',
            '示例 2：n = 1 → 1。',
            '示例 3：n = 8 → 92。',
        ],
        [
            '维护 cols、diag1（row-col）、diag2（row+col）三个 set 记录占用。',
            'backtrack(row)：row == n 时 count += 1 返回。',
            '对 col in range(n)：若三 set 冲突则 continue。',
            '加入三个 set，递归 row+1，回溯 remove。',
            'backtrack(0) 后返回 count。',
        ],
        '回溯',
        code_notes=[
            'count = 0 — 解法计数，nonlocal 在 backtrack 内更新。',
            'cols: set[int] — 已占列号。',
            'diag1: set[int] — row - col 对角线标识。',
            'diag2: set[int] — row + col 对角线标识。',
            'if col in cols or row - col in diag1 or row + col in diag2: continue — 冲突剪枝。',
            'cols.add(col); diag1.add(row - col); diag2.add(row + col) — 做选择。',
            'backtrack(row + 1) — 下一行放皇后。',
            'cols.remove(col); diag1.remove(...); diag2.remove(...) — 撤销选择。',
        ],
        complexity='时间 O(n!) 量级，空间 O(n)（三个 set + 递归栈）。',
    ),
    'data_structures/matrix/matrix.py::generate_matrix': _m(
        '59', '螺旋矩阵 II',
        '给你一个正整数 n，'
        '生成一个包含 1 到 n² 所有元素、'
        '且元素按顺时针螺旋顺序排列的 n×n 矩阵。\n\n'
        '约束：1 ≤ n ≤ 20。',
        [
            '示例 1：n = 3 → [[1,2,3],[8,9,4],[7,6,5]]。',
            '示例 2：n = 1 → [[1]]。',
            '示例 3：n = 4 → 1..16 顺时针螺旋填充。',
        ],
        [
            '初始化 n×n 零矩阵，'
            '边界 top/bottom/left/right，num = 1。',
            'while top <= bottom and left <= right：',
            '从左到右填 top 行，top++；'
            '从上到下填 right 列，right--。',
            '若 top <= bottom，从右到左填 bottom 行，bottom--。',
            '若 left <= right，从下到上填 left 列，left++。',
            '返回 matrix。',
        ],
        '矩阵',
        code_notes=[
            'matrix = [[0] * n for _ in range(n)] — 初始化零矩阵。',
            'top, bottom, left, right = 0, n - 1, 0, n - 1 — 四边界。',
            'num = 1 — 当前填入数字，逐格递增。',
            'for c in range(left, right + 1): matrix[top][c] = num — 填顶行。',
            'top += 1 — 顶边界内缩。',
            'for r in range(top, bottom + 1): matrix[r][right] = num — 填右列。',
            'if top <= bottom / if left <= right — 防止 n 为奇偶时重复填充。',
            '反向循环 range(right, left-1, -1) 与 range(bottom, top-1, -1) — 填底行与左列。',
        ],
        complexity='时间 O(n²)，空间 O(n²)（输出矩阵）。',
    ),
    'strings/operations.py::add_binary': _m(
        '67', '二进制求和',
        '给你两个二进制字符串 a 和 b，'
        '返回它们的和作为二进制字符串。\n\n'
        '本实现从低位到高位逐位相加，'
        '维护 carry 进位。\n\n'
        '约束：1 ≤ a.length, b.length ≤ 10⁴；'
        'a 和 b 仅由 "0" 或 "1" 组成；'
        '字符串不含前导零（除非数字本身是 0）。',
        [
            '示例 1：a = "11", b = "1" → "100"。'
            '3 + 1 = 4。',
            '示例 2：a = "1010", b = "1011" → "10101"。',
            '示例 3：a = "0", b = "0" → "0"。',
        ],
        [
            'i, j 分别从 a、b 末尾开始，carry = 0。',
            'while i >= 0 or j >= 0 or carry：累加 total = carry + 各位。',
            'result.append(str(total % 2))，carry = total // 2。',
            '双指针递减；循环结束后 reverse join 返回。',
        ],
        '字符串',
        code_notes=[
            'i, j = len(a) - 1, len(b) - 1 — 从末位对齐。',
            'carry = 0 — 进位初始为 0。',
            'while i >= 0 or j >= 0 or carry — 含最终进位。',
            'total = carry; if i >= 0: total += int(a[i]); i -= 1 — 加 a 当前位。',
            'if j >= 0: total += int(b[j]); j -= 1 — 加 b 当前位。',
            'result.append(str(total % 2)) — 当前位二进制。',
            'carry = total // 2 — 进位传递。',
            'return "".join(reversed(result)) — 低位先入栈，需反转。',
        ],
        complexity='时间 O(max(m, n))，空间 O(max(m, n))，m、n 为字符串长度。',
    ),
    'strings/operations.py::text_justification': _m(
        '68', '文本左右对齐',
        '给定一个单词数组 words 和一个长度 maxWidth，'
        '重新排版单词，'
        '使其成为每行恰好 maxWidth 个字符、'
        '且左右两端对齐的文本。\n\n'
        '最后一行左对齐，'
        '单词间仅一个空格；'
        '非末行单词间空格尽量均匀，'
        '左侧间隙多一个。\n\n'
        '约束：1 ≤ words.length ≤ 300；'
        '1 ≤ words[i].length ≤ 20；'
        'words[i] 仅含大写和小写英文字母；'
        '1 ≤ maxWidth ≤ 300。',
        [
            '示例 1：words = ["This","is","an","example",...], maxWidth = 16 → 左右对齐多行。',
            '示例 2：words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16。',
            '示例 3：words = ["Science","is","what","we","understand","well","enough","to","explain"], maxWidth = 20。',
        ],
        [
            'index 从 0 开始，贪心确定每行能容纳的单词范围 [index, last)。',
            '末行或单行：join 后右侧补空格至 maxWidth。',
            '否则计算 spaces 与 gaps，divmod 分配 space_each 与 extra。',
            '逐词拼接，前 line_count-1 个词后加空格（前 extra 个间隙多 1）。',
            'index = last，循环至处理完所有词。',
        ],
        '贪心',
        code_notes=[
            'while index < n — 逐行贪心分组。',
            'count = len(words[index]); last = index + 1 — 首词长度与下一词下标。',
            'while last < n and count + 1 + len(words[last]) <= maxWidth — 尽量多放词。',
            'if last == n or line_count == 1 — 末行或单行左对齐。',
            'line = " ".join(...) + " " * (max_width - len(line)) — 右侧补空格。',
            'spaces = max_width - sum(len(w)...); space_each, extra = divmod(spaces, gaps) — 均匀分配。',
            'line += words[index + i] + " " * (space_each + (1 if i < extra else 0)) — 前 extra 间隙多 1 空格。',
        ],
        complexity='时间 O(n × maxWidth)，空间 O(输出行数 × maxWidth)。',
    ),
    'patterns/binary_search/basic.py::my_sqrt': _m(
        '69', 'x 的平方根',
        '给你一个非负整数 x，'
        '计算并返回 x 的算术平方根。\n\n'
        '由于返回类型是整数，'
        '结果只保留整数部分，'
        '小数部分将被舍去。\n\n'
        '本实现二分查找最大的 mid 使 mid² ≤ x。\n\n'
        '约束：0 ≤ x ≤ 2³¹ - 1。',
        [
            '示例 1：x = 4 → 2。',
            '示例 2：x = 8 → 2。'
            '√8 ≈ 2.828，取整为 2。',
            '示例 3：x = 0 → 0。',
        ],
        [
            '若 x < 2，直接返回 x（0 或 1）。',
            'lo = 1，hi = x // 2，二分搜索。',
            'mid² ≤ x 时 lo = mid + 1（尝试更大）；'
            '否则 hi = mid - 1。',
            '循环结束返回 hi（最大满足 mid² ≤ x 的值）。',
        ],
        '二分查找',
        code_notes=[
            'if x < 2: return x — 0 和 1 的平方根即自身。',
            'lo, hi = 1, x // 2 — 搜索范围，√x ≤ x/2（x≥4）。',
            'while lo <= hi — 闭区间二分。',
            'mid = (lo + hi) // 2 — 中点。',
            'if mid * mid <= x: lo = mid + 1 — 平方不超过 x，尝试更大。',
            'else: hi = mid - 1 — 平方过大，缩小上界。',
            'return hi — lo 越过 hi 后 hi 即为 floor(√x)。',
        ],
        complexity='时间 O(log x)，空间 O(1)。',
    ),
    'data_structures/stack_queue/stack_queue.py::simplify_path': _m(
        '71', '简化路径',
        '给你一个字符串 path，'
        '表示指向某一文件或目录的 Unix 风格绝对路径，'
        '请你将其转化为更加简洁的规范路径。\n\n'
        '规范路径需满足：'
        '以斜杠 "/" 开头；'
        '两个目录名之间仅一个斜杠；'
        '不含 "." 或 ".." 分量；'
        "路径仅由小写英文字母、数字、'.'、'/' 组成。\n\n"
        '约束：1 ≤ path.length ≤ 3000。',
        [
            '示例 1：path = "/home/" → "/home"。',
            '示例 2：path = "/../" → "/"。'
            '".." 回到根目录。',
            '示例 3：path = "/home//foo/" → "/home/foo"。'
            '合并连续斜杠。',
        ],
        [
            '用 stack 存储路径分量，'
            '按 "/" split path。',
            '空串或 "." 跳过；'
            '".." 时若 stack 非空则 pop。',
            '其他分量 push 入栈。',
            '返回 "/" + "/".join(stack)。',
        ],
        '栈',
        code_notes=[
            'stack: list[str] = [] — 存储有效目录名。',
            'for part in path.split("/") — 按斜杠分割。',
            'if part in ("", "."): continue — 忽略空段与当前目录。',
            'if part == "..": if stack: stack.pop() — 返回上级，根目录不再 pop。',
            'else: stack.append(part) — 普通目录入栈。',
            'return "/" + "/".join(stack) — 重组规范路径。',
            '空 path 或全 ".." 返回 "/"；无需处理相对路径。',
        ],
        complexity='时间 O(n)，空间 O(n)，n = len(path)。',
    ),
    'foundations/bit_manipulation.py::gray_code': _m(
        '89', '格雷编码',
        'n 位格雷码序列是一个由 2ⁿ 个整数组成的序列，'
        '其中每个整数都在范围 [0, 2ⁿ - 1] 内，'
        '且满足：相邻整数二进制表示仅一位不同；'
        '第一个整数为 0。\n\n'
        '本实现镜像反射法：'
        '每增加一位，在现有序列前补 0、'
        '逆序镜像后最高位 OR (1<<i)。\n\n'
        '约束：1 ≤ n ≤ 16。',
        [
            '示例 1：n = 2 → [0, 1, 3, 2]。'
            '00→01→11→10，相邻仅一位不同。',
            '示例 2：n = 1 → [0, 1]。',
            '示例 3：n = 3 → 8 个数的格雷序列。',
        ],
        [
            'result = [0]，从 i = 0 到 n-1 迭代。',
            '对每个 i，从 result 末尾到开头逆序遍历 j。',
            'result.append(result[j] | (1 << i)) — 镜像并置最高新位。',
            'i 轮后 result 长度为 2ⁿ，返回。',
        ],
        '位运算',
        code_notes=[
            'result = [0] — 1 位格雷码起点。',
            'for i in range(n) — 逐位扩展至 n 位。',
            'for j in range(len(result) - 1, -1, -1) — 逆序镜像现有序列。',
            'result.append(result[j] | (1 << i)) — 镜像值 OR 第 i 位为 1。',
            '每轮长度翻倍：|result| 从 2^i 变为 2^(i+1)。',
            '相邻数仅一位不同；首元素恒为 0。',
            '也可公式 G(i) = i ^ (i >> 1) 直接生成，本实现用反射法。',
        ],
        complexity='时间 O(2ⁿ)，空间 O(2ⁿ)（输出占主导）。',
    ),
    'paradigms/dynamic_programming/sequence_dp.py::is_interleave': _m(
        '97', '交错字符串',
        '给定三个字符串 s1、s2、s3，'
        '请你帮忙验证 s3 是否是由 s1 和 s2 交错组成的。\n\n'
        '交错：s1 和 s2 字符不改变相对顺序，'
        '合并成 s3。\n\n'
        '约束：s1.length + s2.length == s3.length；'
        '0 ≤ s1.length, s2.length ≤ 100；'
        's1、s2、s3 均由小写英文字母组成。',
        [
            '示例 1：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac" → true。',
            '示例 2：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc" → false。',
            '示例 3：s1 = "", s2 = "", s3 = "" → true。',
        ],
        [
            '若 len(s1)+len(s2) != len(s3)，返回 False。',
            'dp[i][j] 表示 s1 前 i 字符与 s2 前 j 字符能否组成 s3 前 i+j 字符。',
            'dp[0][0] = True；双重循环填充 dp。',
            '若 s1[i-1]==s3[i+j-1]，dp[i][j] |= dp[i-1][j]。',
            '若 s2[j-1]==s3[i+j-1]，dp[i][j] |= dp[i][j-1]。',
            '返回 dp[m][n]。',
        ],
        '动态规划',
        code_notes=[
            'if m + n != len(s3): return False — 长度不匹配直接 false。',
            'dp = [[False] * (n + 1) for _ in range(m + 1)] — (m+1)×(n+1) 表。',
            'dp[0][0] = True — 空串交错为空串。',
            'if i > 0 and s1[i - 1] == s3[i + j - 1]: dp[i][j] = dp[i][j] or dp[i - 1][j] — 取 s1 末字符。',
            'if j > 0 and s2[j - 1] == s3[i + j - 1]: dp[i][j] = dp[i][j] or dp[i][j - 1] — 取 s2 末字符。',
            's3[i + j - 1] — s3 当前末字符下标为 i+j-1。',
            'return dp[m][n] — 两串全部用完能否匹配 s3。',
        ],
        complexity='时间 O(m × n)，空间 O(m × n)，可压缩为一维。',
    ),
    'data_structures/tree/tree.py::recover_tree': _m(
        '99', '恢复二叉搜索树',
        '给你二叉搜索树的根 root，'
        '该树中的恰好两个节点的值被错误地交换。\n\n'
        '请在不改变其结构的情况下，'
        '恢复这棵树。\n\n'
        '本实现中序遍历找两个错位节点，'
        '交换其 val 恢复 BST。\n\n'
        '约束：树上节点数 2 ≤ n ≤ 1000；'
        '节点值 -10⁹ ≤ Node.val ≤ 10⁹；'
        '恰好两个节点被交换。',
        [
            '示例 1：root = [1,3,null,null,2] → [3,1,null,null,2]。'
            '1 与 3 被交换。',
            '示例 2：root = [3,1,4,null,null,2] → [2,1,4,null,null,3]。',
            '示例 3：两相邻节点交换 → 中序仅一处逆序。',
        ],
        [
            '中序遍历，维护 prev 指向前驱节点。',
            '若 prev.val > node.val，'
            '首次记录 first=prev、second=node；'
            '再次仅更新 second=node。',
            '遍历结束后交换 first.val 与 second.val。',
        ],
        '二叉树',
        code_notes=[
            'first = second = prev = None — 两个错位节点与前驱。',
            'def inorder(node) — 递归中序遍历。',
            'if prev and node.val < prev.val — 发现逆序对（BST 中应递增）。',
            'if not first: first = prev — 首个逆序：前驱为 first。',
            'second = node — 后继为 second（相邻或不相邻均适用）。',
            'prev = node — 更新前驱为当前节点。',
            'first.val, second.val = second.val, first.val — 交换值恢复 BST。',
            'O(n) 时间 O(h) 栈空间；Morris 遍历可 O(1) 空间。',
        ],
        complexity='时间 O(n)，空间 O(h)，h 为树高（递归栈）。',
    ),
    'data_structures/tree/tree.py::level_order_bottom': _m(
        '107', '二叉树的层序遍历 II',
        '给你二叉树的根节点 root，'
        '返回其节点值自底向上的层序遍历。'
        '（即按从叶子层所在层到根节点所在的层，'
        '逐层从左向右遍历）。\n\n'
        '约束：树中节点数目在范围 [0, 2000] 内；'
        '-1000 ≤ Node.val ≤ 1000。',
        [
            '示例 1：root = [3,9,20,null,null,15,7] → [[15,7],[9,20],[3]]。',
            '示例 2：root = [1] → [[1]]。',
            '示例 3：root = [] → []。',
        ],
        [
            '调用已有 level_order(root) 得到自上而下层序结果。',
            '对结果 list 执行 reversed() 反转。',
            '返回自底向上的层序列表。',
        ],
        '二叉树',
        code_notes=[
            'return list(reversed(level_order(root))) — 复用标准层序再反转。',
            'level_order 通常 BFS 队列实现，逐层收集节点值。',
            'reversed() 返回迭代器，list() 转为列表。',
            '无需额外 DFS；逻辑简洁，一行完成。',
            '空树 level_order 返回 []，反转仍为 []。',
            '层内顺序保持从左到右，仅层间顺序颠倒。',
            '也可 BFS 时用 deque appendleft 实现，本实现更简洁。',
        ],
        complexity='时间 O(n)，空间 O(n)，n 为节点数。',
    ),
    'data_structures/tree/tree.py::sorted_list_to_bst': _m(
        '109', '有序链表转换二叉搜索树',
        '给定一个单链表，'
        '其中元素按升序排序，'
        '将其转换为高度平衡的二叉搜索树。\n\n'
        '高度平衡：'
        '每个节点的左右两个子树的高度差不超过 1。\n\n'
        '本实现先遍历链表收集 values，'
        '再递归取中点建树。\n\n'
        '约束：head 中的节点数在 [0, 2×10⁴] 范围内；'
        '-10⁵ ≤ Node.val ≤ 10⁵。',
        [
            '示例 1：head = [-10,-3,0,5,9] → [0,-3,9,-10,null,5]。'
            '一种合法 BST。',
            '示例 2：head = [] → null。',
            '示例 3：head = [1] → [1]。',
        ],
        [
            '遍历链表，将值存入 values 列表。',
            '定义 build(lo, hi)：lo > hi 返回 None。',
            'mid = (lo + hi) // 2，以 values[mid] 为根。',
            '递归 build(lo, mid-1) 为左子树，'
            'build(mid+1, hi) 为右子树。',
            'return build(0, len(values)-1)。',
        ],
        '二叉树',
        code_notes=[
            'values: list[int] = [] — 链表值升序数组。',
            'while cur: values.append(cur.val); cur = cur.next — 一次遍历收集。',
            'def build(lo, hi) — 闭区间 [lo, hi] 建树。',
            'if lo > hi: return None — 空区间无节点。',
            'mid = (lo + hi) // 2 — 取中点为根，保证平衡。',
            'node = TreeNode(values[mid]) — 创建根节点。',
            'node.left = build(lo, mid - 1); node.right = build(mid + 1, hi) — 左右子树。',
            '中序性质：左 < 根 < 右；O(n) 时间 O(n) 空间。',
        ],
        complexity='时间 O(n)，空间 O(n)（values 数组 + 递归栈 O(log n)）。',
    ),
    'data_structures/tree/tree.py::connect': _m(
        '116', '填充每个节点的下一个右侧节点指针',
        '给定一棵完美/任意二叉树，'
        '将所有节点的 next 指针指向其同一层的下一个右侧节点。'
        '若右侧无相邻节点则 next 为 null。\n\n'
        '116 为完美二叉树，117 为任意形状；'
        '本实现逐层链表连接，'
        '不依赖 next 指针遍历，'
        '同时覆盖两题。\n\n'
        '约束：节点数 0 ≤ n ≤ 4096；'
        '-1000 ≤ Node.val ≤ 1000。',
        [
            '示例 1（116）：完美树 root = [1,2,3,4,5,6,7] → 每层 next 串联。',
            '示例 2（117）：含 null 子节点的树 → 跳过空节点仍正确连接。',
            '示例 3：root = [] → null。',
        ],
        [
            '若 root 为空返回 None；leftmost 指向当前层最左节点。',
            'while leftmost.left：进入下一层。',
            '用 dummy 头与 tail 构建下一层水平链表。',
            '沿 cur = cur.next 遍历当前层，'
            '将 cur 的非空 left/right 接到 tail.next。',
            'leftmost = leftmost.left，进入再下一层。',
            '返回 root。',
        ],
        '二叉树',
        code_notes=[
            'leftmost = root — 当前层最左节点，驱动逐层下降。',
            'while leftmost.left — 有下一层则继续（完美树用 .left，117 需检查子节点）。',
            'head = tail = ConnectNode() — dummy 简化下一层链表构建。',
            'for child in (cur.left, cur.right): if child: tail.next = child; tail = child — 串联非空子节点。',
            'cur = cur.next — 沿已有 next 指针水平遍历当前层。',
            'leftmost = leftmost.left — 移到下一层最左。',
            'O(n) 时间 O(1) 额外空间；不依赖递归。',
        ],
        complexity='时间 O(n)，空间 O(1)（不含输出），n 为节点数。',
    ),
    'data_structures/tree/tree.py::connect_ii': _m(
        '117', '填充每个节点的下一个右侧节点指针 II',
        '给定一棵二叉树，'
        '将所有节点的 next 指针指向其同一层的下一个右侧节点。'
        '若右侧无相邻节点则 next 为 null。\n\n'
        '与 116 的区别在于树可能非完美，'
        '存在缺失子节点；'
        '本实现调用 connect，'
        '逐层 dummy 链表连接已能处理任意形状。\n\n'
        '约束：节点数 0 ≤ n ≤ 6000；'
        '-100 ≤ Node.val ≤ 100。',
        [
            '示例 1：root = [1,2,3,4,5,null,7] → 每层 next 正确串联。',
            '示例 2：root = [] → null。',
            '示例 3：root = [1] → 单节点 next 为 null。',
        ],
        [
            'connect_ii 直接调用 connect(root)。',
            'connect 逐层遍历，用 dummy 头构建下一层水平链表。',
            '跳过 null 子节点，仅连接存在的 left/right。',
            'leftmost 下移到下一层最左非空节点继续。',
            '返回处理后的 root。',
        ],
        '二叉树',
        code_notes=[
            'return connect(root) — 117 与 116 算法相同，复用实现。',
            'connect 对任意二叉树均正确：只连接非空子节点。',
            'while leftmost.left 在 117 中 leftmost 可能无 left，循环自然终止。',
            'dummy + tail 模式避免使用额外队列存储层节点。',
            'cur = cur.next 利用已建立的 next 指针 O(1) 遍历当前层。',
            '与 116 完美树版本共享同一套 O(n) 时间 O(1) 空间解法。',
        ],
        complexity='时间 O(n)，空间 O(1)，n 为节点数。',
    ),
    'patterns/graph/extended.py::ladder_length': _m(
        '127', '单词接龙',
        '字典 wordList 中两个单词 beginWord 和 endWord 的转换序列，'
        '每次只能改变一个字母，'
        '且中间单词必须在 wordList 中。\n\n'
        '返回从 beginWord 到 endWord 的最短转换序列长度；'
        '若不存在则返回 0。\n\n'
        '本实现 BFS 逐层扩展，'
        '变换后从 word_set 移除避免重复访问。\n\n'
        '约束：1 ≤ beginWord.length ≤ 10；'
        'endWord.length == beginWord.length；'
        '1 ≤ wordList.length ≤ 5000；'
        'wordList[i].length == beginWord.length；'
        'beginWord != endWord；'
        '所有字符串仅含小写字母。',
        [
            '示例 1：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"] → 5。',
            '示例 2：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"] → 0。',
            '示例 3：beginWord = "a", endWord = "c", wordList = ["a","b","c"] → 2。',
        ],
        [
            'word_set = set(wordList)；若 endWord 不在其中返回 0。',
            'BFS 队列 (word, steps)，初始 (beginWord, 1)。',
            '出队若 word == endWord 返回 steps。',
            '枚举每位替换 26 字母得 nxt，'
            '若在 word_set 中则 remove 并入队 (nxt, steps+1)。',
            '队列空返回 0。',
        ],
        '广度优先搜索',
        code_notes=[
            'word_set = set(word_list) — O(1) 查找。',
            'if end_word not in word_set: return 0 — 终点不可达。',
            'queue = deque([(begin_word, 1)]) — BFS 带步数。',
            'for i in range(len(word)): for c in "abcdefghijklmnopqrstuvwxyz" — 枚举每位变字母。',
            'nxt = word[:i] + c + word[i + 1:] — 构造邻接词。',
            'if nxt in word_set: word_set.remove(nxt); queue.append((nxt, steps + 1)) — 标记访问。',
            'return 0 — 无法到达 endWord。',
        ],
        complexity='时间 O(M² × N)，M 为词长、N 为词表大小；空间 O(N)。',
    ),
    'patterns/graph/extended.py::solve_surrounded_regions': _m(
        '130', '被围绕的区域',
        '给你一个 m×n 的矩阵 board，'
        '由若干 "X" 和 "O" 组成，'
        '找到所有被 "X" 围绕的区域，'
        '并将这些区域里所有的 "O" 用 "X" 填充。\n\n'
        '本实现从边界 "O" 出发 DFS 标记为 "T"，'
        '剩余 "O" 变 "X"，"T" 恢复为 "O"。\n\n'
        '约束：m == board.length；'
        'n == board[i].length；'
        '1 ≤ m, n ≤ 200；'
        'board[i][j] 为 "X" 或 "O"。',
        [
            '示例 1：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]] → 中间 O 被填 X。',
            '示例 2：board = [["X"]] → [["X"]]。',
            '示例 3：边界 O 保留，内部被围 O 变 X。',
        ],
        [
            '从四条边界上所有 "O" 出发 DFS，标记为 "T"（与边界连通）。',
            '遍历全矩阵：剩余 "O" 改为 "X"，"T" 改回 "O"。',
            '原地修改 board，无返回值（None）。',
        ],
        '深度优先搜索',
        code_notes=[
            'if not board: return — 空矩阵特判。',
            'def dfs(r, c): if board[r][c] != "O": return; board[r][c] = "T" — 标记连通 O。',
            'dfs 四方向递归 — 扩散边界连通区域。',
            'for i in range(rows): dfs(i, 0); dfs(i, cols - 1) — 左右边界。',
            'for j in range(cols): dfs(0, j); dfs(rows - 1, j) — 上下边界。',
            'if board[i][j] == "O": board[i][j] = "X" — 被围 O 填 X。',
            'elif board[i][j] == "T": board[i][j] = "O" — 边界连通 O 保留。',
        ],
        complexity='时间 O(m × n)，空间 O(m × n)（递归栈最坏）。',
    ),
    'data_structures/hash_map/hash_map.py::max_points': _m(
        '149', '直线上最多的点数',
        '给定一个数组 points，'
        '其中 points[i] = [xᵢ, yᵢ] 表示 X-Y 平面上的一个点，'
        '求最多有多少个点在同一条直线上。\n\n'
        '本实现对每个点作锚点，'
        '统计到其他点的斜率（约分后标准化），'
        '并单独统计重合点数。\n\n'
        '约束：1 ≤ points.length ≤ 300；'
        'points[i].length == 2；'
        '-10⁴ ≤ xᵢ, yᵢ ≤ 10⁴。',
        [
            '示例 1：points = [[1,1],[2,2],[3,3]] → 3。',
            '示例 2：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]] → 4。',
            '示例 3：points = [[0,0],[1,1],[0,0]] → 3。'
            '含重复点。',
        ],
        [
            '若点数 ≤ 2，直接返回 len(points)。',
            '外层枚举锚点 (x1, y1)，内层统计斜率与重合。',
            'dx, dy 用 gcd 约分，dx<0 时翻转符号统一斜率表示。',
            'local_best + same 更新全局 best。',
            '返回 best。',
        ],
        '哈希表',
        code_notes=[
            'if len(points) <= 2: return len(points) — 两点必共线。',
            'for i, (x1, y1) in enumerate(points) — 锚点枚举。',
            'slopes: dict[tuple[int, int], int] = {} — 斜率 (dx,dy) 计数。',
            'same = 1 — 与锚点重合的点数（含自身）。',
            'if x1 == x2 and y1 == y2: same += 1; continue — 重合点单独计。',
            'g = gcd(dx, dy); dx //= g; dy //= g — 约分斜率。',
            'if dx < 0: dx, dy = -dx, -dy — 统一斜率方向。',
            'best = max(best, local_best + same) — 同线点数 = 斜率最大 + 重合。',
        ],
        complexity='时间 O(n²)，空间 O(n)（每个锚点的 slopes 表）。',
    ),
    'strings/operations.py::is_one_edit_distance': _m(
        '161', '相隔为 1 的编辑距离',
        '给定两个字符串 s 和 t，'
        '如果它们相差恰好一个编辑步骤（插入、删除或替换），'
        '返回 true；否则返回 false。\n\n'
        '约束：0 ≤ s.length, t.length ≤ 10⁴；'
        's 和 t 由字母、数字和 "." 组成。',
        [
            '示例 1：s = "ab", t = "acb" → true。'
            '插入 c。',
            '示例 2：s = "cab", t = "ad" → false。'
            '需超过一步。',
            '示例 3：s = "1203", t = "1213" → true。'
            '替换 0 为 1。',
        ],
        [
            '若 |m-n| > 1 返回 False；保证 m ≤ n（必要时交换 s,t）。',
            '扫描第一个不同字符位置 i。',
            '若 m == n（等长）：检查 s[i+1:] == t[i+1:]（一次替换）。',
            '若 m < n（差 1）：检查 s[i:] == t[i+1:]（一次插入/删除）。',
            '全部相同且 m+1==n 返回 True（末尾插入）。',
        ],
        '字符串',
        code_notes=[
            'if abs(m - n) > 1: return False — 长度差超过 1 不可能。',
            'if m > n: s, t = t, s; m, n = n, m — 保证 s 较短。',
            'for i in range(m): if s[i] != t[i] — 找首个差异。',
            'if m == n: return s[i + 1:] == t[i + 1:] — 替换后剩余相同。',
            'return s[i:] == t[i + 1:] — 短串多删/长串多插一位。',
            'return m + 1 == n — 前缀全同，长串多一位（末尾插入）。',
            'O(n) 单次扫描，无需 DP。',
        ],
        complexity='时间 O(n)，空间 O(1)，n = max(len(s), len(t))。',
    ),
    'patterns/binary_search/basic.py::find_peak_element': _m(
        '162', '寻找峰值',
        '峰值元素是指其值严格大于左右相邻值的元素。\n\n'
        '给定一个整数数组 nums，'
        '找到峰值元素并返回其索引。\n\n'
        '你可以假设 nums[-1] = nums[n] = -∞，'
        '且数组中任意两个相邻元素均不相等。\n\n'
        '本实现二分：'
        '若 nums[mid] < nums[mid+1]，峰值在右侧；'
        '否则在左侧（含 mid）。\n\n'
        '约束：1 ≤ nums.length ≤ 1000；'
        '-2³¹ ≤ nums[i] ≤ 2³¹ - 1；'
        'nums[i] != nums[i+1]。',
        [
            '示例 1：nums = [1,2,3,1] → 2。'
            '3 为峰值。',
            '示例 2：nums = [1,2,1,3,5,6,4] → 5 或 1 均可（返回其一）。',
            '示例 3：nums = [1] → 0。',
        ],
        [
            'lo = 0，hi = len(nums)-1，while lo < hi。',
            'mid = (lo + hi) // 2。',
            '若 nums[mid] < nums[mid+1]，lo = mid + 1（上坡，峰值在右）。',
            '否则 hi = mid（下坡或峰值在 mid）。',
            '返回 lo。',
        ],
        '二分查找',
        code_notes=[
            'lo, hi = 0, len(nums) - 1 — 闭区间二分变体。',
            'while lo < hi — 收敛到唯一峰值下标。',
            'mid = (lo + hi) // 2 — 中点。',
            'if nums[mid] < nums[mid + 1]: lo = mid + 1 — 右侧更高，峰值不在 mid。',
            'else: hi = mid — mid 可能是峰值或在峰值左侧。',
            'return lo — 循环结束 lo 即峰值索引。',
            '无需比较 nums[mid-1]；边界视为 -∞ 保证存在峰值。',
        ],
        complexity='时间 O(log n)，空间 O(1)。',
    ),
    'foundations/math_sort.py::fraction_to_decimal': _m(
        '166', '分数到小数',
        '给定两个整数 numerator 和 denominator，'
        '以字符串形式返回小数结果。\n\n'
        '若小数部分重复，'
        '将重复部分用括号括起。\n\n'
        '本实现长除法，'
        '用 seen 记录余数首次出现位置以检测循环节。\n\n'
        '约束：-2³¹ ≤ numerator, denominator ≤ 2³¹ - 1；'
        'denominator != 0。',
        [
            '示例 1：numerator = 1, denominator = 2 → "0.5"。',
            '示例 2：numerator = 2, denominator = 1 → "2"。',
            '示例 3：numerator = 4, denominator = 333 → "0.(012)"。',
        ],
        [
            'numerator == 0 返回 "0"；处理符号 sign。',
            '整数部分 integer = num // den；余数 remainder = num % den。',
            '余数为 0 返回整数；否则开始小数 long division。',
            '余数重复时在 seen 记录处插入 "("，末尾加 ")"。',
            '无循环则返回完整小数串。',
        ],
        '数学',
        code_notes=[
            'if numerator == 0: return "0" — 零特判。',
            'sign = "-" if (numerator < 0) ^ (denominator < 0) else "" — 异或定符号。',
            'num, den = abs(numerator), abs(denominator) — 正数长除。',
            'integer = num // den; remainder = num % den — 整数与小数余数。',
            'seen: dict[int, int] = {} — 余数 → 结果串中的起始下标。',
            'if remainder in seen: start = seen[remainder]; return result[:start] + "(" + result[start:] + ")" — 循环节。',
            'remainder *= 10; result += str(remainder // den); remainder %= den — 经典长除法。',
        ],
        complexity='时间 O(d)，空间 O(d)，d 为输出小数位数（含循环节）。',
    ),
    'strings/operations.py::largest_number': _m(
        '179', '最大数',
        '给定一组非负整数 nums，'
        '重新排列每个数的顺序（每个数不可拆分）'
        '使之组成一个最大的整数。\n\n'
        '注意：结果可能非常大，'
        '需要返回字符串而不是整数。\n\n'
        '约束：1 ≤ nums.length ≤ 100；'
        '0 ≤ nums[i] ≤ 10⁹。',
        [
            '示例 1：nums = [10,2] → "210"。',
            '示例 2：nums = [3,30,34,5,9] → "9534330"。',
            '示例 3：nums = [0,0] → "0"。'
            '全零特判。',
        ],
        [
            '将 nums 转为字符串列表。',
            '按 key=lambda x: x*3 降序排序（自定义比较：ab vs ba）。',
            '若排序后首元素为 "0"，返回 "0"（避免 "00..."）。',
            'join 返回结果字符串。',
        ],
        '贪心',
        code_notes=[
            'nums_str = list(map(str, nums)) — 转字符串便于拼接比较。',
            'nums_str.sort(key=lambda x: x * 3, reverse=True) — 乘 3 足够区分长度不同的拼接序。',
            'return "0" if nums_str[0] == "0" else "".join(nums_str) — 全零输出 "0"。',
            'x * 3 技巧：使 "9" > "34" 因 "999" > "343434"。',
            '等价于 cmp_to_key(lambda a,b: int(b+a)-int(a+b))。',
            'O(n log n) 排序；n ≤ 100 足够。',
        ],
        complexity='时间 O(n log n × k)，k 为数字平均位数；空间 O(n)。',
    ),
    'paradigms/backtracking/core.py::find_words': _m(
        '212', '单词搜索 II',
        '给定一个 m×n 二维字符网格 board 和一个单词列表 words，'
        '返回所有同时在 board 和 words 中出现的单词。\n\n'
        '单词必须按字母顺序通过相邻（上下左右）单元格构成，'
        '同一单元格不能重复使用。\n\n'
        '本实现 Trie + DFS，'
        '在网格上沿 Trie 路径搜索。\n\n'
        '约束：m == board.length；'
        'n == board[i].length；'
        '1 ≤ m, n ≤ 12；'
        '1 ≤ words.length ≤ 3×10⁴；'
        '1 ≤ words[i].length ≤ 10；'
        'words[i] 由小写英文字母组成；'
        'board 由小写英文字母组成。',
        [
            '示例 1：board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"] → ["eat","oath"]。',
            '示例 2：board = [["a","b"],["c","d"]], words = ["abcb"] → []。',
            '示例 3：单格 board，words 含该字母 → 匹配。',
        ],
        [
            '将所有 words 插入 Trie。',
            '对每个格子 (r,c) 启动 DFS(r, c, trie, "")。',
            'DFS：沿 Trie 走，path 累加字符；'
            'node.is_end 时将 path 加入 result。',
            '标记 board[r][c]="#" 防重复，四方向递归，回溯恢复。',
            '返回 list(result)。',
        ],
        '回溯',
        code_notes=[
            'from algorithm.data_structures.trie.trie import Trie — 前缀树。',
            'for word in words: trie.insert(word) — 批量插入词典。',
            'def dfs(r, c, node, path) — 网格 DFS 沿 Trie 走。',
            'if ch not in node.children: return — 前缀不匹配剪枝。',
            'node = node.children[ch]; path += ch — 深入 Trie。',
            'if node.is_end: result.add(path) — 找到完整单词。',
            'board[r][c] = "#" — 标记已访问。',
            '四方向 dfs 后 board[r][c] = ch — 回溯恢复格子。',
        ],
        complexity='时间 O(m×n×4^L + W×L)，W 为词数、L 为最大词长；空间 O(W×L) Trie。',
    ),
    'strings/operations.py::shortest_palindrome': _m(
        '214', '最短回文串',
        '给定一个字符串 s，'
        '你可以通过在字符串前面添加字符来将其转换为回文串。\n\n'
        '返回你需要在 s 前面添加的最少字符数后得到的回文串。\n\n'
        '本实现 KMP：'
        '在 s + "#" + s[::-1] 上求最长相等前后缀，'
        '前缀补 s[nxt[-1]:][::-1]。\n\n'
        '约束：0 ≤ s.length ≤ 5×10⁴；'
        's 仅由小写英文字母组成。',
        [
            '示例 1：s = "aacecaaa" → "aaacecaaa"。',
            '示例 2：s = "abcd" → "dcbabcd"。',
            '示例 3：s = "" → ""。',
        ],
        [
            '构造 combined = s + "#" + s[::-1]（# 分隔防重叠）。',
            '对 combined 计算 KMP 的 nxt（前缀函数）数组。',
            'nxt[-1] 为 s 的最长回文前缀长度。',
            '返回 s[nxt[-1]:][::-1] + s（补反转后缀）。',
        ],
        '字符串',
        code_notes=[
            'combined = s + "#" + s[::-1] — 找 s 的最长回文前缀。',
            'nxt = [0] * len(combined) — KMP 前缀函数。',
            'while j and combined[i] != combined[j]: j = nxt[j - 1] — 失配回退。',
            'if combined[i] == combined[j]: j += 1; nxt[i] = j — 扩展匹配。',
            'return s[nxt[-1]:][::-1] + s — 非回文后缀反转后 prepend。',
            'nxt[-1] 即最长 border 长度；等价于找最长 palindrome prefix。',
        ],
        complexity='时间 O(n)，空间 O(n)，n = len(s)。',
    ),
    'patterns/graph/extended.py::get_skyline': _m(
        '218', '天际线问题',
        '城市的天际线是从远处观看该城市所有建筑物形成的轮廓，'
        '由若干线段组成。\n\n'
        '给定 buildings，'
        '其中 buildings[i] = [leftᵢ, rightᵢ, heightᵢ]，'
        '返回由 "关键点" 组成的天际线，'
        '格式 [[x₁,h₁], [x₂,h₂], ...]，'
        '按 x 坐标排序。\n\n'
        '本实现扫描线 + 最大堆。\n\n'
        '约束：1 ≤ buildings.length ≤ 10⁴；'
        '0 ≤ leftᵢ < rightᵢ ≤ 2³¹ - 1；'
        '1 ≤ heightᵢ ≤ 2³¹ - 1；'
        'buildings 按 leftᵢ 非递减排序。',
        [
            '示例 1：buildings = [[2,9,10],[3,7,15],[5,12,12],[13,16,2]] → [[2,10],[3,15],[7,12],[12,0],[15,10],[20,0]]。',
            '示例 2：buildings = [[0,2,3],[2,5,3]] → [[0,3],[5,0]]。',
            '示例 3：单栋建筑 → 左端点升高、右端点降回 0。',
        ],
        [
            '将每栋楼拆为 (left, -height, right) 与 (right, height, 0) 事件。',
            '按 x 排序；维护最大堆存 (-height, right)。',
            '扫描每个 x：弹出 right ≤ x 的过期高度。',
            '若为新楼事件则 push；取堆顶最大高度。',
            '若与 result 末高度不同则 append [x, max_h]。',
        ],
        '扫描线',
        code_notes=[
            'events.append((left, -height, right)); events.append((right, height, 0)) — 左负右正。',
            'events.sort() — 同 x 左事件（负高）先于右事件。',
            'heap = [(0, float("inf"))] — 最小堆存 (-height, right)，堆顶为当前最大高。',
            'while heap[0][1] <= x: heapq.heappop(heap) — 移除已结束建筑。',
            'if neg_h < 0: heapq.heappush(heap, (neg_h, right)) — 新楼入堆。',
            'max_h = -heap[0][0] — 当前天际线高度。',
            'if not result or result[-1][1] != max_h: result.append([x, max_h]) — 高度变化才记录关键点。',
        ],
        complexity='时间 O(n log n)，空间 O(n)，n 为建筑数。',
    ),
    'data_structures/linked_list/linked_list.py::delete_node': _m(
        '237', '删除链表中的节点',
        '有一个单链表 head，'
        '想要删除其中的一个节点 node。\n\n'
        '给你一个需要删除的节点 node，'
        '你将无法访问第一个节点 head。\n\n'
        '本实现将后继节点的值复制到 node，'
        '再删除后继，'
        '等效删除当前节点。\n\n'
        '约束：链表节点数范围 [2, 1000]；'
        '-1000 ≤ Node.val ≤ 1000；'
        'node 不是末尾节点；'
        'val 唯一。',
        [
            '示例 1：head = [4,5,1,9], node = 5 → [4,1,9]。',
            '示例 2：head = [4,5,1,9], node = 1 → [4,5,9]。',
            '示例 3：head = [1,2,3,4], node = 3 → [1,2,4]。',
        ],
        [
            '无法访问前驱，无法常规 unlink node。',
            '将 node.next.val 复制到 node.val。',
            'node.next = node.next.next，跳过原后继。',
            '无返回值，原地修改链表。',
        ],
        '链表',
        code_notes=[
            'node.val = node.next.val — 用后继值覆盖当前（题设保证非尾节点）。',
            'node.next = node.next.next — 删除原后继，等效删除 node。',
            '无法访问 head 时无法找到 node 前驱，故用「复制+删后继」技巧。',
            '题设 node 非末尾且 val 唯一，保证正确性。',
            'O(1) 时间 O(1) 空间；不修改节点引用结构外的部分。',
        ],
        complexity='时间 O(1)，空间 O(1)。',
    ),
    'patterns/graph/extended.py::longest_increasing_path': _m(
        '329', '矩阵中的最长递增路径',
        '给定一个 m×n 整数矩阵 matrix，'
        '找出最长递增路径的长度。\n\n'
        '路径可以从任意单元格出发，'
        '每次只能移动到上下左右相邻且值严格更大的单元格。\n\n'
        '本实现 DFS + 记忆化，'
        '每个格子最多计算一次。\n\n'
        '约束：m == matrix.length；'
        'n == matrix[i].length；'
        '1 ≤ m, n ≤ 200；'
        '-2³¹ ≤ matrix[i][j] ≤ 2³¹ - 1。',
        [
            '示例 1：matrix = [[9,9,4],[6,6,8],[2,1,1]] → 4。'
            '路径 1→2→6→9。',
            '示例 2：matrix = [[3,4,5],[3,2,6],[2,2,1]] → 4。',
            '示例 3：matrix = [[1]] → 1。',
        ],
        [
            '对每个格子 (r,c) DFS 求以该点为起点的最长递增路径。',
            'DFS 四方向，仅走向更大值；memo 缓存结果。',
            '返回 1 + max(合法邻居 DFS)；无邻居则为 1。',
            '全局取所有起点 DFS 的最大值。',
        ],
        '记忆化搜索',
        code_notes=[
            'memo: dict[tuple[int, int], int] = {} — 缓存每格 LIP 长度。',
            'def dfs(r, c) -> int — 以 (r,c) 为起点的最长递增路径。',
            'if (r, c) in memo: return memo[(r, c)] — 避免重复计算。',
            'best = 1 — 至少包含自身。',
            '四方向 (dr,dc)；matrix[nr][nc] > matrix[r][c] — 严格递增才扩展。',
            'best = max(best, 1 + dfs(nr, nc)) — 累加路径长度。',
            'return max(dfs(r,c) for all r,c) — 枚举所有起点。',
        ],
        complexity='时间 O(m × n)，空间 O(m × n)（memo + 栈）。',
    ),
    'patterns/graph/extended.py::calc_equation': _m(
        '399', '除法求值',
        '给你一个变量对数组 equations 和实数值数组 values，'
        '其中 equations[i] = [Aᵢ, Bᵢ]，values[i] 表示 Aᵢ / Bᵢ = values[i]。\n\n'
        '另给出 queries，'
        '每个 query = [Cⱼ, Dⱼ] 表示 Cⱼ / Dⱼ 的结果，'
        '若无法确定则返回 -1.0。\n\n'
        '本实现建无向加权图，'
        '对每个 query DFS 累乘路径权重。\n\n'
        '约束：1 ≤ equations.length ≤ 20；'
        'equations[i].length == 2；'
        '1 ≤ values.length ≤ 20；'
        'values[i] 是 1.0 或 2.0；'
        '1 ≤ queries.length ≤ 20；'
        'queries[i].length == 2；'
        'Cⱼ, Dⱼ, Aᵢ, Bᵢ 由小写英文字母组成且长度 ≤ 5。',
        [
            '示例 1：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"]] → [6.0,0.5,-1.0]。',
            '示例 2：equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]] → [3.75,0.4,5.0,0.2]。',
            '示例 3：query 中变量不在图中 → -1.0。',
        ],
        [
            '建图 graph[a][b]=val，graph[b][a]=1/val。',
            '对每个 query (a,b) 调用 dfs(a, b, visited)。',
            'dfs：a==b 返回 1.0；遍历邻居累乘 weight * dfs(nei, end)。',
            '找不到路径返回 -1.0。',
        ],
        '深度优先搜索',
        code_notes=[
            'graph: dict[str, dict[str, float]] = defaultdict(dict) — 邻接表。',
            'graph[a][b] = val; graph[b][a] = 1 / val — 双向边。',
            'def dfs(start, end, visited) -> float — 求 start/end 比值。',
            'if start not in graph or end not in graph: return -1.0 — 变量不存在。',
            'if start == end: return 1.0 — 同变量比值为 1。',
            'visited.add(start) — 防环。',
            'if nei == end: return weight — 直接邻居。',
            'return weight * dfs(nei, end, visited) — 路径累乘。',
        ],
        complexity='时间 O(Q × (V+E))，V 为变量数、E 为方程数、Q 为查询数。',
    ),
    'data_structures/hash_map/hash_map.py::longest_palindrome': _m(
        '409', '最长回文串',
        '给定一个字符串 s，'
        '找到 s 中最长的回文串长度。\n\n'
        '你可以用其中任意字符来构造回文，'
        '每个字符最多用两次（奇数次字符其中一个可放中间）。\n\n'
        '约束：1 ≤ s.length ≤ 2000；'
        's 仅由小写和/或大写英文字母组成。',
        [
            '示例 1：s = "abccccdd" → 7。'
            '"dccaccd" 长度为 7。',
            '示例 2：s = "a" → 1。',
            '示例 3：s = "bb" → 2。',
        ],
        [
            'Counter 统计各字符频次。',
            '对每个 freq：length += freq // 2 * 2（成对使用）。',
            '若存在奇数频次，odd = True。',
            '返回 length + (1 if odd else 0)。',
        ],
        '哈希表',
        code_notes=[
            'from collections import Counter — 字符频次统计。',
            'counts = Counter(s) — O(n) 计数。',
            'length = 0; odd = False — 成对长度与是否有奇数余量。',
            'length += freq // 2 * 2 — 每字符最多贡献偶数个。',
            'if freq % 2: odd = True — 任一奇数频可占中心一位。',
            'return length + (1 if odd else 0) — 最多一个奇数放中间。',
            '无需构造具体回文串，只求最大长度。',
        ],
        complexity='时间 O(n)，空间 O(1)（字符集大小固定 52）。',
    ),
    'patterns/binary_search/basic.py::split_array_largest_sum': _m(
        '410', '分割数组的最大值',
        '给定一个非负整数数组 nums 和一个整数 k，'
        '将数组分成 k 个非空连续子数组，'
        '使子数组各自和的最大值最小，'
        '返回该最小可能值。\n\n'
        '本实现二分答案 + 贪心验证 can_split(limit)。\n\n'
        '约束：1 ≤ nums.length ≤ 1000；'
        '0 ≤ nums[i] ≤ 10⁶；'
        '1 ≤ k ≤ min(50, nums.length)。',
        [
            '示例 1：nums = [7,2,5,10,8], k = 2 → 18。'
            '分割 [7,2,5] 与 [10,8]。',
            '示例 2：nums = [1,2,3,4,5], k = 2 → 9。',
            '示例 3：nums = [1,4,4], k = 3 → 4。',
        ],
        [
            '二分 lo = max(nums)，hi = sum(nums)。',
            'can_split(limit)：贪心累加，超 limit 则新开一段，'
            '判断段数 ≤ k。',
            '若 can_split(mid) 则 hi = mid，否则 lo = mid + 1。',
            '返回 lo。',
        ],
        '二分查找',
        code_notes=[
            'def can_split(limit: int) -> bool — 验证能否 ≤ k 段且每段和 ≤ limit。',
            'parts = 1; current = 0 — 贪心分段计数。',
            'if current + num > limit: parts += 1; current = num — 超限开新段。',
            'else: current += num — 继续累加当前段。',
            'return parts <= k — 段数不超过 k 则 limit 可行。',
            'lo, hi = max(nums), sum(nums) — 答案下界最大元素、上界总和。',
            'while lo < hi: if can_split(mid): hi = mid else: lo = mid + 1 — 最小化最大段和。',
        ],
        complexity='时间 O(n log S)，S = sum(nums)；空间 O(1)。',
    ),
    'strings/operations.py::add_strings': _m(
        '415', '字符串相加',
        '给定两个字符串形式的非负整数 num1 和 num2，'
        '返回它们的和，同样以字符串形式表示。\n\n'
        '你不能使用任何内置的 BigInteger 库或直接将输入转换为整数。\n\n'
        '本实现从末位逐位相加，'
        '用 ord 处理字符数字。\n\n'
        '约束：1 ≤ num1.length, num2.length ≤ 10⁴；'
        'num1 和 num2 仅由数字 0-9 组成；'
        '不含前导零（除非数字本身是 0）。',
        [
            '示例 1：num1 = "11", num2 = "123" → "134"。',
            '示例 2：num1 = "456", num2 = "77" → "533"。',
            '示例 3：num1 = "0", num2 = "0" → "0"。',
        ],
        [
            '双指针 i, j 从末尾开始，carry = 0。',
            'while i>=0 or j>=0 or carry：累加 total。',
            '用 ord(num[i])-48 取数字；result 追加 chr(total%10+48)。',
            'carry = total // 10；反转 join 返回。',
        ],
        '字符串',
        code_notes=[
            'i, j = len(num1) - 1, len(num2) - 1 — 末位对齐。',
            'total += ord(num1[i]) - 48 — ASCII 转数字（\'0\'=48）。',
            'result.append(chr(total % 10 + 48)) — 数字转字符。',
            'carry = total // 10 — 进位。',
            'return "".join(reversed(result)) — 低位先入栈需反转。',
            '与 add_binary 结构相同，模数改为 10。',
        ],
        complexity='时间 O(max(m, n))，空间 O(max(m, n))。',
    ),
    'paradigms/dynamic_programming/sequence_dp.py::predict_the_winner': _m(
        '486', '预测赢家',
        '给你一个整数数组 nums，'
        '两名玩家 A 和 B 轮流取数，'
        'A 先手，每次从数组两端取一个数，'
        '取完所有数后分数高者胜。\n\n'
        '若 A 能赢（A 得分 ≥ B 得分）返回 true，'
        '否则 false。\n\n'
        '本实现区间 DP：'
        'dp[left][right] 表示当前玩家在 [left,right] 的净胜分。\n\n'
        '约束：1 ≤ nums.length ≤ 20；'
        '0 ≤ nums[i] ≤ 10⁷。',
        [
            '示例 1：nums = [1,5,2] → false。'
            'A 取 1 或 2 均无法保证净胜。',
            '示例 2：nums = [1,5,233,7] → true。',
            '示例 3：nums = [0,0,7,6,5,6,1,2] → false。',
        ],
        [
            'dp[i][i] = nums[i] — 单元素净胜即为该值。',
            '按区间长度递增枚举 [left, right]。',
            'dp[left][right] = max(nums[left]-dp[left+1][right], nums[right]-dp[left][right-1])。',
            '返回 dp[0][n-1] >= 0。',
        ],
        '动态规划',
        code_notes=[
            'dp = [[0] * n for _ in range(n)] — 区间 DP 表。',
            'dp[i][i] = nums[i] — 只剩一个数时净胜分。',
            'for length in range(2, n + 1) — 按区间长度递推。',
            'right = left + length - 1 — 区间右端。',
            'nums[left] - dp[left + 1][right] — 取左端后对手净胜的相反数。',
            'nums[right] - dp[left][right - 1] — 取右端同理。',
            'return dp[0][n - 1] >= 0 — 先手净胜非负即 A 不输。',
        ],
        complexity='时间 O(n²)，空间 O(n²)，n = len(nums)。',
    ),
    'patterns/graph/extended.py::update_board': _m(
        '529', '扫雷游戏',
        '给你一个 m×n 字符矩阵 board 表示扫雷盘，'
        '其中 "M" 代表地雷，"E" 代表未挖空方块，'
        '"B" 代表已挖空（无相邻雷），'
        '数字表示相邻雷数。\n\n'
        'click = [clickr, clickc] 表示点击位置；'
        '返回点击后的盘面。\n\n'
        '规则：点击雷则变 "X"；'
        '否则显示相邻雷数，'
        '若为 0 则 DFS 扩散挖空相邻 "E"。\n\n'
        '约束：m == board.length；'
        'n == board[i].length；'
        '1 ≤ m, n ≤ 50；'
        'board[i][j] 为 "M"、"E"、"B" 或 "1"-"8"；'
        'click.length == 2；'
        '0 ≤ clickr < m；0 ≤ clickc < n；'
        'board[clickr][clickc] 为 "E" 或 "M"。',
        [
            '示例 1：board = [["E","E","E","E","E"],...], click = [3,0] → 挖空并显示数字或 B。',
            '示例 2：点击 "M" → 该格变 "X"。',
            '示例 3：挖到 0 相邻雷时 BFS/DFS 自动扩散。',
        ],
        [
            '若点击格为 "M"，直接改为 "X" 返回。',
            '否则 DFS：count_mines 统计八邻域雷数。',
            '填 "B"（0 雷）或数字 str(mines)。',
            '若 mines==0，八方向递归挖相邻 "E"。',
            '返回 board。',
        ],
        '深度优先搜索',
        code_notes=[
            'def count_mines(cr, cc) -> int — 八邻域统计 "M" 数量。',
            'def dfs(cr, cc) — 挖空并可能扩散。',
            'if board[cr][cc] == "M": board[cr][cc] = "X"; return — 踩雷。',
            'board[cr][cc] = "B" if mines == 0 else str(mines) — 显示结果。',
            'if mines == 0: 八方向 dfs(nr, nc) where board[nr][nc]=="E" — 零雷扩散。',
            'if board[r][c] == "M": board[r][c] = "X" — 首击为雷直接处理。',
            'else: dfs(r, c) — 首击为空从点击处 DFS。',
        ],
        complexity='时间 O(m × n)，空间 O(m × n)（递归栈）。',
    ),
    'paradigms/greedy/greedy.py::least_interval': _m(
        '621', '任务调度器',
        '给定一个用字符数组 tasks 表示的 CPU 任务列表，'
        '其中每个字母表示一种任务；'
        '两个相同种类任务间必须有 n 个冷却间隔。\n\n'
        '返回完成所有任务所需的最少时间单位。\n\n'
        '本实现公式：'
        'max(len(tasks), (max_freq-1)*(n+1)+max_count)。\n\n'
        '约束：1 ≤ tasks.length ≤ 10⁴；'
        'tasks[i] 为大写英文字母；'
        '0 ≤ n ≤ 100。',
        [
            '示例 1：tasks = ["A","A","A","B","B","B"], n = 2 → 8。'
            'A B _ A B _ A B。',
            '示例 2：tasks = ["A","A","A","B","B","B"], n = 0 → 6。',
            '示例 3：tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2 → 16。',
        ],
        [
            'Counter 统计各任务频次，取 max_freq。',
            'max_count = 频次等于 max_freq 的任务种类数。',
            '框架 (max_freq-1) 个完整块，每块 n+1 槽。',
            '最后一块放 max_count 个最高频任务。',
            '与 len(tasks) 取 max（任务多时无需空闲）。',
        ],
        '贪心',
        code_notes=[
            'from collections import Counter — 任务频次。',
            'counts = Counter(tasks); max_freq = max(counts.values()) — 最高频。',
            'max_count = sum(1 for freq in counts.values() if freq == max_freq) — 最高频任务种类数。',
            'return max(len(tasks), (max_freq - 1) * (n + 1) + max_count) — 经典公式。',
            '(max_freq - 1) * (n + 1) — 除最后一轮外的框架长度。',
            '+ max_count — 最后一轮并列最高频任务占槽。',
            'max(len(tasks), ...) — 任务总量更大时无空闲槽。',
        ],
        complexity='时间 O(m)，空间 O(1)，m = len(tasks)（字符集 26）。',
    ),
    'patterns/graph/extended.py::is_bipartite': _m(
        '785', '判断二分图',
        '存在一个无向图，'
        '图中有 n 个节点，'
        '编号从 0 到 n - 1，'
        '附带数组 graph 表示无向图的邻接表。\n\n'
        '若可以将节点集二分，'
        '使每条边连接的两个节点分属不同集合，'
        '则图为二分图。\n\n'
        '本实现 BFS 染色，'
        '相邻节点颜色必须不同。\n\n'
        '约束：graph.length == n；'
        '1 ≤ n ≤ 100；'
        '0 ≤ graph[u].length < n；'
        '0 ≤ graph[u][i] ≤ n - 1；'
        'graph[u] 不含 u；'
        '无重复边；'
        '无自环。',
        [
            '示例 1：graph = [[1,2,3],[0,2],[0,1,3],[0,2]] → false。',
            '示例 2：graph = [[1,3],[0,2],[1,3],[0,2]] → true。',
            '示例 3：graph = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,3,6,9],[7,8],[1,9,5],[5,7],[1,2,5,8],[3,6,9]] → false。',
        ],
        [
            'color 数组初始 -1（未染色）。',
            '对每个未染色节点 BFS，染 color=0。',
            '扩展邻居：未染色则染 1-color[node]；'
            '已染色且同色则 return False。',
            '所有连通分量通过则 True。',
        ],
        '广度优先搜索',
        code_notes=[
            'color = [-1] * len(graph) — -1 表示未访问。',
            'for start in range(len(graph)): if color[start] != -1: continue — 处理非连通图。',
            'queue = deque([start]); color[start] = 0 — BFS 起点染 0。',
            'color[nei] = 1 - color[node] — 邻居染反色。',
            'elif color[nei] == color[node]: return False — 同色相邻非二分。',
            '全部通过 return True。',
        ],
        complexity='时间 O(V+E)，空间 O(V)，V 为节点数、E 为边数。',
    ),
    'patterns/graph/extended.py::find_cheapest_price': _m(
        '787', 'K 站中转内最便宜的航班',
        '有 n 个城市通过 flights 连接，'
        'flights[i] = [fromᵢ, toᵢ, priceᵢ] 表示航班。\n\n'
        '从 src 到 dst 最多 k 站中转，'
        '返回最便宜价格；'
        '无法到达则 -1。\n\n'
        '本实现 Bellman-Ford 松弛 k+1 轮，'
        '每轮用 temp 快照避免同轮连锁更新。\n\n'
        '约束：1 ≤ n ≤ 100；'
        '0 ≤ flights.length ≤ (n×(n-1)/2)；'
        'flights[i].length == 3；'
        '0 ≤ fromᵢ, toᵢ < n；'
        'fromᵢ != toᵢ；'
        '1 ≤ priceᵢ ≤ 10⁴；'
        '航班无重复；'
        '0 ≤ k ≤ n；'
        '0 ≤ src, dst < n；'
        'src != dst。',
        [
            '示例 1：n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1 → 200。',
            '示例 2：n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0 → 500。',
            '示例 3：无法 k 步内到达 → -1。',
        ],
        [
            'prices[src] = 0，其余 inf。',
            '重复 k+1 轮：temp = prices[:] 快照。',
            '对每条边 (u,v,w)：若 prices[u] 可达，'
            'temp[v] = min(temp[v], prices[u]+w)。',
            'prices = temp；返回 prices[dst] 或 -1。',
        ],
        '动态规划',
        code_notes=[
            'prices = [float("inf")] * n; prices[src] = 0 — 最短距离数组。',
            'for _ in range(k + 1) — 最多 k 次中转 = k+1 条边。',
            'temp = prices[:] — 每轮快照，防止同轮多次松弛。',
            'if prices[u] != float("inf"): temp[v] = min(temp[v], prices[u] + w) — 松弛。',
            'prices = temp — 更新到下一轮。',
            'return -1 if prices[dst] == float("inf") else int(prices[dst]) — 不可达返回 -1。',
        ],
        complexity='时间 O(k × E)，空间 O(n)，E 为航班数。',
    ),
    'paradigms/dynamic_programming/grid_dp.py::num_tilings': _m(
        '790', '多米诺和托米诺平铺',
        '有两种形状的瓷砖：'
        '2×1 多米诺和 L 形托米诺，'
        '均可旋转。\n\n'
        '返回覆盖 2×n 面板的不同平铺方案数，'
        '对 10⁹+7 取模。\n\n'
        '本实现双状态 DP：'
        'complete[i] 表示第 i 列完全填满，'
        'partial[i] 表示第 i 列仅上半或下半填满。\n\n'
        '约束：1 ≤ n ≤ 1000。',
        [
            '示例 1：n = 3 → 5。',
            '示例 2：n = 1 → 1。',
            '示例 3：n = 4 → 11。',
        ],
        [
            'complete[1]=1, complete[2]=2；partial[1]=0, partial[2]=1。',
            'i≥2：complete[i] = complete[i-1]+complete[i-2]+2*partial[i-1]。',
            'partial[i] = partial[i-1]+complete[i-2]。',
            '均 mod 10⁹+7；返回 complete[n]。',
        ],
        '动态规划',
        code_notes=[
            'mod = 10 ** 9 + 7 — 取模常量。',
            'complete = [1, 2] + [0] * (n - 2) — 列完全填满方案数。',
            'partial = [0, 1] + [0] * (n - 2) — 列部分填满（留缺口）。',
            'complete[i] = (complete[i-1] + complete[i-2] + 2 * partial[i-1]) % mod — 竖放/两块横放/托米诺补缺口。',
            'partial[i] = (partial[i-1] + complete[i-2]) % mod — 延伸部分填充或托米诺引入。',
            'if n == 1: return 1 — 单列仅一种竖放。',
            'return complete[n - 1] — 第 n 列完全填满的总方案。',
        ],
        complexity='时间 O(n)，空间 O(n)，可压缩为 O(1)。',
    ),
    'patterns/graph/extended.py::all_paths_source_target': _m(
        '797', '所有可能的路径',
        '给你一个有 n 个节点的有向无环图，'
        '节点编号 0 到 n-1，'
        'graph[i] 为节点 i 能到达的所有节点。\n\n'
        '返回从 0 到 n-1 的所有路径，'
        '按任意顺序。\n\n'
        '约束：n == graph.length；'
        '2 ≤ n ≤ 15；'
        '0 ≤ graph[i].length < n；'
        '0 ≤ graph[i][j] < n；'
        'i != graph[i][j]；'
        'graph[i] 互不相同；'
        'graph 不含重复边；'
        'graph 是有向无环图。',
        [
            '示例 1：graph = [[1,2],[3],[3],[]] → [[0,1,3],[0,2,3]]。',
            '示例 2：graph = [[4,3,1],[3,2,4],[3],[4],[]] → 五条路径。',
            '示例 3：graph = [[1],[]] → [[0,1]]。',
        ],
        [
            'target = n - 1；result 存路径。',
            'dfs(node, path)：到达 target 时 append path[:]。',
            '遍历 graph[node]：path.append(nei)，递归，path.pop()。',
            '从 dfs(0, [0]) 开始。',
        ],
        '回溯',
        code_notes=[
            'target = len(graph) - 1 — 终点节点编号。',
            'result: list[list[int]] = [] — 收集所有路径。',
            'def dfs(node, path) — 当前节点与路径。',
            'if node == target: result.append(path[:]) — 到达终点，拷贝路径。',
            'path.append(nei); dfs(nei, path); path.pop() — 标准回溯。',
            'dfs(0, [0]) — 从源点 0 出发。',
            'DAG 无环，无需 visited；n≤15 路径数可控。',
        ],
        complexity='时间 O(2^n × n) 最坏，空间 O(n)（递归栈 + 当前路径）。',
    ),
    'patterns/graph/extended.py::num_buses_to_destination': _m(
        '815', '公交路线',
        '给你一个数组 routes，'
        '其中 routes[i] 表示第 i 辆公交车所能到达的站点。\n\n'
        '从 source 到 target，'
        '返回最少乘坐公交车数；'
        '无法到达则 -1。\n\n'
        '本实现 BFS 按「路线」扩展，'
        'stop_to_routes 建倒排索引。\n\n'
        '约束：1 ≤ routes.length ≤ 500；'
        '1 ≤ routes[i].length ≤ 10⁵；'
        'routes[i] 互不相同；'
        'sum(routes[i].length) ≤ 10⁵；'
        '0 ≤ routes[i][j] < 10⁶；'
        '0 ≤ source, target < 10⁶。',
        [
            '示例 1：routes = [[1,2,7],[3,6,7]], source = 1, target = 6 → 2。',
            '示例 2：source == target → 0。',
            '示例 3：无法换乘到达 → -1。',
        ],
        [
            '建 stop_to_routes[stop] = 经过该站的路线编号列表。',
            'BFS (stop, buses)，初始 (source, 0)。',
            '对每个 stop 的未访问路线，'
            '遍历路线上站点；遇 target 返回 buses+1。',
            '新 stop 入队 (nxt, buses+1)。',
        ],
        '广度优先搜索',
        code_notes=[
            'if source == target: return 0 — 同站无需乘车。',
            'stop_to_routes: dict[int, list[int]] — 站点到路线倒排。',
            'visited_routes: set[int] — 已乘过的路线，避免重复换同线。',
            'visited_stops = {source} — 已到达站点。',
            'for route_idx in stop_to_routes[stop]: if route_idx in visited_routes: continue — 每条线最多乘一次。',
            'if nxt == target: return buses + 1 — 下一站下车即达。',
        ],
        complexity='时间 O(S + R×L)，S 为站点数、R 为路线数、L 为平均站数；空间 O(S+R)。',
    ),
    'patterns/graph/extended.py::can_visit_all_rooms': _m(
        '841', '钥匙和房间',
        '有 n 个房间，'
        'rooms[i] 为第 i 个房间中的钥匙列表，'
        '最初你在 0 号房间（除 0 外其余房间上锁）。\n\n'
        '返回能否访问所有房间。\n\n'
        '本实现从 0 号 DFS/BFS 收集可达房间。\n\n'
        '约束：n == rooms.length；'
        '1 ≤ n ≤ 1000；'
        '0 ≤ rooms[i].length ≤ 1000；'
        '1 ≤ sum(rooms[i].length) ≤ 3000；'
        '0 ≤ rooms[i][j] < n；'
        '所有 rooms[i] 互不相同。',
        [
            '示例 1：rooms = [[1],[2],[3],[]] → true。',
            '示例 2：rooms = [[1,3],[3,0,1],[3],[0],[]] → false。',
            '示例 3：rooms = [[1],[],[3],[]] → false。',
        ],
        [
            'visited = set()；dfs(0) 从 0 号房间出发。',
            'visited.add(room)；遍历 rooms[room] 中钥匙。',
            '若 key 未访问则 dfs(key)。',
            '返回 len(visited) == len(rooms)。',
        ],
        '深度优先搜索',
        code_notes=[
            'visited: set[int] = set() — 可达房间集合。',
            'def dfs(room: int) — 递归访问。',
            'visited.add(room) — 标记已入。',
            'for key in rooms[room]: if key not in visited: dfs(key) — 用钥匙开新房间。',
            'dfs(0) — 从初始房间出发。',
            'return len(visited) == len(rooms) — 是否覆盖全部房间。',
        ],
        complexity='时间 O(N + K)，N 为房间数、K 为钥匙总数；空间 O(N)。',
    ),
    'data_structures/tree/tree.py::distance_k': _m(
        '863', '二叉树中所有距离为 K 的结点',
        '给定一个二叉树的根 root、'
        '一个目标节点 target 和一个整数 k，'
        '返回目标节点 target 到距离为 k 的所有节点的值。\n\n'
        '本实现先建 parent 映射，'
        '再从 target BFS 扩散 k 层。\n\n'
        '约束：节点数 0 ≤ n ≤ 500；'
        '0 ≤ Node.val ≤ 500；'
        '0 ≤ k ≤ 1000；'
        '题目数据保证 target 在树中。',
        [
            '示例 1：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2 → [7,4,1]。',
            '示例 2：target = root, k = 0 → [root.val]。',
            '示例 3：k 大于树高 → []。',
        ],
        [
            'build(root) 递归建立 parent[node] = 父节点。',
            'BFS 从 (target, 0) 开始，visited = {target}。',
            'dist == k 时将 node.val 加入 result。',
            '否则扩展 left、right、parent 中未访问邻居。',
            '返回 result。',
        ],
        '二叉树',
        code_notes=[
            'parent: dict[TreeNode, Optional[TreeNode]] = {root: None} — 父指针映射。',
            'def build(node) — 递归登记 node.left/right 的 parent。',
            'queue = deque([(target, 0)]) — BFS 带距离。',
            'if dist == k: result.append(node.val); continue — 恰 k 层收集。',
            'for nxt in (node.left, node.right, parent.get(node)) — 可向父节点扩散。',
            'if nxt and nxt not in visited — 避免重复访问。',
        ],
        complexity='时间 O(n)，空间 O(n)，n 为节点数。',
    ),
    'foundations/math_sort.py::sort_array': _m(
        '912', '排序数组',
        '给你一个整数数组 nums，'
        '请你将其升序排列。\n\n'
        '本实现归并排序：'
        '分治递归排序两半再 merge。\n\n'
        '约束：1 ≤ nums.length ≤ 5×10⁴；'
        '-5×10⁴ ≤ nums[i] ≤ 5×10⁴。',
        [
            '示例 1：nums = [5,2,3,1] → [1,2,3,5]。',
            '示例 2：nums = [5,1,1,2,0,0] → [0,0,1,1,2,5]。',
            '示例 3：nums = [1] → [1]。',
        ],
        [
            '若 len(nums) <= 1，直接返回。',
            'mid = len(nums)//2，递归 sort_array 左右两半。',
            'merge 两有序数组：双指针比较，'
            '剩余段 extend。',
            '返回 merge 结果。',
        ],
        '排序',
        code_notes=[
            'if len(nums) <= 1: return nums — 递归基。',
            'mid = len(nums) // 2 — 中点划分。',
            'return merge(sort_array(nums[:mid]), sort_array(nums[mid:])) — 分治。',
            'def merge(left, right) — 双指针归并。',
            'while i < len(left) and j < len(right): 取较小 append — 标准 merge。',
            'result.extend(left[i:]); result.extend(right[j:]) — 剩余段。',
            '时间稳定 O(n log n)；空间 O(n) 每层 merge 新数组。',
        ],
        complexity='时间 O(n log n)，空间 O(n)（归并临时数组）。',
    ),
    'patterns/graph/extended.py::oranges_rotting': _m(
        '994', '腐烂的橘子',
        '在给定的 m×n 网格 grid 中，'
        '0 表示空，1 表示新鲜橘子，2 表示腐烂橘子。\n\n'
        '每分钟腐烂橘子四方向传染相邻新鲜橘子；'
        '返回直到无新鲜橘子时的分钟数；'
        '若不可能全部腐烂则 -1。\n\n'
        '本实现多源 BFS，'
        '同时从所有初始腐烂橘子扩散。\n\n'
        '约束：m == grid.length；'
        'n == grid[i].length；'
        '1 ≤ m, n ≤ 10；'
        'grid[i][j] 为 0、1 或 2。',
        [
            '示例 1：grid = [[2,1,1],[1,1,0],[0,1,1]] → 4。',
            '示例 2：grid = [[2,1,1],[0,1,1],[1,0,1]] → -1。'
            '角落新鲜橘子无法被感染。',
            '示例 3：grid = [[0,2]] → 0。'
            '无新鲜橘子。',
        ],
        [
            '统计 fresh 数量，将所有 2 入队 (r,c,0)。',
            'BFS 四方向：感染相邻 1，fresh--，入队 (nr,nc,minutes+1)。',
            '记录最后扩散的 minutes。',
            '返回 minutes if fresh==0 else -1。',
        ],
        '广度优先搜索',
        code_notes=[
            'queue = deque(); fresh = 0 — 多源 BFS 队列与新鲜计数。',
            'if grid[r][c] == 2: queue.append((r, c, 0)) — 初始腐烂橘子全部入队。',
            'elif grid[r][c] == 1: fresh += 1 — 统计新鲜数。',
            'r, c, minutes = queue.popleft() — 带时间层级的 BFS。',
            'if grid[nr][nc] == 1: grid[nr][nc] = 2; fresh -= 1; queue.append((nr, nc, minutes + 1)) — 感染扩散。',
            'return minutes if fresh == 0 else -1 — 仍有新鲜则不可全腐烂。',
        ],
        complexity='时间 O(m × n)，空间 O(m × n)（队列）。',
    ),
}
