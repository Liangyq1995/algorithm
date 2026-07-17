"""字符串基础操作。"""


def reverse_string(s: list[str]) -> None:
    """344. 反转字符串"""
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def reverse_str(s: str, k: int) -> str:
    """541. 反转字符串 II"""
    chars = list(s)
    for start in range(0, len(chars), 2 * k):
        end = min(start + k, len(chars))
        chars[start:end] = reversed(chars[start:end])
    return "".join(chars)


def reverse_words(s: str) -> str:
    """151. 反转字符串中的单词"""
    return " ".join(reversed(s.split()))


def length_of_last_word(s: str) -> int:
    """58. 最后一个单词长度"""
    end = len(s) - 1
    while end >= 0 and s[end] == " ":
        end -= 1
    start = end
    while start >= 0 and s[start] != " ":
        start -= 1
    return end - start


def replace_space(s: str) -> str:
    """剑指 Offer 05. 替换空格"""
    return s.replace(" ", "%20")


def minimum_deletion(s: str) -> int:
    """1249. 移除无效的括号"""
    balance = 0
    result: list[str] = []
    for ch in s:
        if ch == "(":
            balance += 1
            result.append(ch)
        elif ch == ")":
            if balance > 0:
                balance -= 1
                result.append(ch)
        else:
            result.append(ch)
    return len(s) - len(result)


def longest_valid_parentheses(s: str) -> int:
    """32. 最长有效括号"""
    stack = [-1]
    best = 0
    for i, ch in enumerate(s):
        if ch == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                best = max(best, i - stack[-1])
    return best


def is_palindrome(s: str) -> bool:
    """125. 验证回文串"""
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


def longest_common_prefix(strs: list[str]) -> str:
    """14. 最长公共前缀"""
    if not strs:
        return ""
    prefix: list[str] = []
    for group in zip(*strs):
        if len(set(group)) == 1:
            prefix.append(group[0])
        else:
            break
    return "".join(prefix)


def shortest_distance_to_char(s: str, c: str) -> list[int]:
    """821. 字符的最短距离"""
    n = len(s)
    ans = [0] * n
    prev = -n
    for i, ch in enumerate(s):
        if ch == c:
            prev = i
        ans[i] = i - prev
    prev = 2 * n
    for i in range(n - 1, -1, -1):
        if s[i] == c:
            prev = i
        ans[i] = min(ans[i], prev - i)
    return ans


def remove_palindrome_sub(s: str) -> int:
    """1332. 删除回文子串"""
    if not s:
        return 0
    if s == s[::-1]:
        return 1
    return 2


def reverse_integer(x: int) -> int:
    """7. 整数反转"""
    sign = -1 if x < 0 else 1
    value = int(str(abs(x))[::-1])
    value *= sign
    if value < -(2 ** 31) or value > 2 ** 31 - 1:
        return 0
    return value


def convert_zigzag(s: str, num_rows: int) -> str:
    """6. Z 字形变换"""
    if num_rows <= 1:
        return s
    rows: list[list[str]] = [[] for _ in range(num_rows)]
    for index, ch in enumerate(s):
        cycle = index % (2 * num_rows - 2)
        row = cycle if cycle < num_rows else 2 * num_rows - 2 - cycle
        rows[row].append(ch)
    return "".join("".join(row) for row in rows)


def repeated_string_match(a: str, b: str) -> int:
    """686. 重复叠加字符串匹配"""
    if not set(b).issubset(set(a)):
        return -1
    repeated = a
    count = 1
    limit = 2 * len(a) + len(b)
    while len(repeated) < limit:
        if b in repeated:
            return count
        count += 1
        repeated += a
    return -1


def my_atoi(s: str) -> int:
    """8. 字符串转换整数 (atoi)"""
    i = 0
    while i < len(s) and s[i] == " ":
        i += 1
    sign = 1
    if i < len(s) and s[i] in "+-":
        sign = -1 if s[i] == "-" else 1
        i += 1
    result = 0
    bound = 2 ** 31
    while i < len(s) and s[i].isdigit():
        digit = ord(s[i]) - ord("0")
        if result > (bound - digit) // 10:
            return bound - 1 if sign > 0 else -bound
        result = result * 10 + digit
        i += 1
    return sign * result


def multiply_strings(num1: str, num2: str) -> str:
    """43. 字符串相乘"""
    if num1 == "0" or num2 == "0":
        return "0"
    m, n = len(num1), len(num2)
    result = [0] * (m + n)
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            mul = int(num1[i]) * int(num2[j])
            total = mul + result[i + j + 1]
            result[i + j + 1] = total % 10
            result[i + j] += total // 10
    start = 0
    while start < len(result) - 1 and result[start] == 0:
        start += 1
    return "".join(map(str, result[start:]))


def add_binary(a: str, b: str) -> str:
    """67. 二进制求和"""
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    result: list[str] = []
    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1
        result.append(str(total % 2))
        carry = total // 2
    return "".join(reversed(result))


def add_strings(num1: str, num2: str) -> str:
    """415. 字符串相加"""
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0
    result: list[str] = []
    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += ord(num1[i]) - 48
            i -= 1
        if j >= 0:
            total += ord(num2[j]) - 48
            j -= 1
        result.append(chr(total % 10 + 48))
        carry = total // 10
    return "".join(reversed(result))


def is_one_edit_distance(s: str, t: str) -> bool:
    """161. 相隔为 1 的编辑距离"""
    m, n = len(s), len(t)
    if abs(m - n) > 1:
        return False
    if m > n:
        s, t = t, s
        m, n = n, m
    for i in range(m):
        if s[i] != t[i]:
            if m == n:
                return s[i + 1 :] == t[i + 1 :]
            return s[i:] == t[i + 1 :]
    return m + 1 == n


def largest_number(nums: list[int]) -> str:
    """179. 最大数"""
    nums_str = list(map(str, nums))
    nums_str.sort(key=lambda x: x * 3, reverse=True)
    return "0" if nums_str[0] == "0" else "".join(nums_str)


def shortest_palindrome(s: str) -> str:
    """214. 最短回文串"""
    combined = s + "#" + s[::-1]
    nxt = [0] * len(combined)
    for i in range(1, len(combined)):
        j = nxt[i - 1]
        while j and combined[i] != combined[j]:
            j = nxt[j - 1]
        if combined[i] == combined[j]:
            j += 1
        nxt[i] = j
    return s[nxt[-1] :][::-1] + s


def text_justification(words: list[str], max_width: int) -> list[str]:
    """68. 文本左右对齐"""
    result: list[str] = []
    index = 0
    n = len(words)
    while index < n:
        count = words[index].__len__()
        last = index + 1
        while last < n and count + 1 + len(words[last]) <= max_width:
            count += 1 + len(words[last])
            last += 1
        line_count = last - index
        if last == n or line_count == 1:
            line = " ".join(words[index:last])
            result.append(line + " " * (max_width - len(line)))
        else:
            spaces = max_width - sum(len(w) for w in words[index:last])
            gaps = line_count - 1
            space_each, extra = divmod(spaces, gaps)
            line = ""
            for i in range(line_count - 1):
                line += words[index + i] + " " * (space_each + (1 if i < extra else 0))
            line += words[last - 1]
            result.append(line)
        index = last
    return result
