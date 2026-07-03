"""题目元数据构建函数。"""

from __future__ import annotations


def _m(
    no: str,
    title: str,
    statement: str,
    example: str | list[str],
    steps: list[str] | str,
    pattern: str | None = None,
    code_notes: list[str] | None = None,
    complexity: str | None = None,
) -> dict:
    if isinstance(steps, str):
        steps = [steps]
    if isinstance(example, str):
        examples = [example]
    else:
        examples = example
    info: dict = {
        "no": no,
        "title": title,
        "statement": statement,
        "examples": examples,
        "steps": steps,
    }
    if pattern:
        info["pattern"] = pattern
    if code_notes:
        info["code_notes"] = code_notes
    if complexity:
        info["complexity"] = complexity
    return info
