"""算法题目元数据，供 catalog.html 展示。"""

from __future__ import annotations

import re

from meta.helpers import _m


def get_problem_info(filepath: str, func_name: str, docstring: str) -> dict:
    """Returns dict with keys: no, title, statement, examples, steps, code_notes, complexity, pattern."""
    from meta import ALL_PROBLEMS

    key = f"{filepath}::{func_name}"
    if key in ALL_PROBLEMS:
        return ALL_PROBLEMS[key].copy()
    no, title = "", func_name
    if docstring:
        first_line = docstring.strip().split("\n")[0]
        match = re.match(r"(\d+)\.\s*(.+)", first_line)
        if match:
            no, title = match.group(1), match.group(2)
        else:
            title = first_line
    return {
        "no": no,
        "title": title,
        "statement": docstring.strip() if docstring else "",
        "examples": [],
        "steps": [],
    }


def __getattr__(name: str):
    if name == "PROBLEMS":
        from meta import ALL_PROBLEMS
        return ALL_PROBLEMS
    raise AttributeError(name)


__all__ = ["_m", "PROBLEMS", "get_problem_info"]
