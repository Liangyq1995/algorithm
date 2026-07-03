"""按模块拆分的题目元数据，合并后供 catalog.html 使用。"""

from meta.common_array_hash import PROBLEMS as _COMMON_ARRAY_HASH
from meta.linked_patterns import PROBLEMS as _LINKED_PATTERNS
from meta.stack_strings import PROBLEMS as _STACK_STRINGS
from meta.tree import PROBLEMS as _TREE
from meta.paradigms import PROBLEMS as _PARADIGMS
from meta.supplement import PROBLEMS as _SUPPLEMENT
from meta.hot200 import PROBLEMS as _HOT200
from meta.hot200_batch2 import PROBLEMS as _HOT200_B2

ALL_PROBLEMS: dict = {}
for part in (_COMMON_ARRAY_HASH, _LINKED_PATTERNS, _STACK_STRINGS, _TREE, _PARADIGMS, _SUPPLEMENT, _HOT200, _HOT200_B2):
    ALL_PROBLEMS.update(part)
