from typing import List, Optional


def contains(s_list: List[int], target: int, lo: int = 0, hi: Optional[int] = None) -> bool:
    # Wenn der Standardwert von hi nicht geändert wurde, dann gilt hi = maxIndex von s_list
    if hi is None:
        hi = len(s_list) - 1

    # Nested Function, um in einer übersichtlichen Art die Übergabe der Liste zu ersparen
    def do_search(target: int, lo: int, hi: int) -> bool:
        # Wenn hi kleiner als lo gilt, gibt es den target nicht
        if hi < lo:
            return False

        # Mitte erstellen, welcher der Pointer der binary_search ist
        mid = (hi + lo) // 2

        # Element ist vorhanden
        if s_list[mid] == target:
            return True
        # Pointer Element ist kleiner als target, daher muss der obere Teil der Liste gelten
        elif s_list[mid] < target:
            return do_search(target, mid + 1, hi)
        # Pointer Elemnt ist größer als target, daher muss der untere Teil der Liste gelten
        elif s_list[mid] > target:
            return do_search(target, lo, mid - 1)

    return do_search(target, lo, hi)


print(contains([1, 3, 4, 5, 7], 7, lo=0, hi=3))
