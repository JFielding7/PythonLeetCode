def accumulate_package_sizes(packages):
    accumulated = [0]
    total = 0

    for package in packages:
        total += package
        accumulated.append(total)

    return accumulated


def least_not_fitting_package_idx(packages, start, size):
    end = len(packages) - 1

    while start <= end:
        mid = start + end >> 1
        if packages[mid] > size:
            end = mid - 1
        else:
            start = mid + 1

    return start


def supplier_wasted(packages, accumulated, supplier):
    supplier.sort()
    if packages[-1] > supplier[-1]:
        return -1

    wasted = 0
    start = 0

    for size in supplier:
        least_not_fitting_idx = least_not_fitting_package_idx(packages, start, size)
        wasted += size * (least_not_fitting_idx - start) - accumulated[least_not_fitting_idx] + accumulated[start]
        start = least_not_fitting_idx

    return wasted


class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        packages.sort()
        accumulated = accumulate_package_sizes(packages)
        min_wasted = -1

        for supplier in boxes:
            wasted = supplier_wasted(packages, accumulated, supplier)
            if wasted != -1 and (min_wasted == -1 or wasted < min_wasted):
                min_wasted = wasted

        return -1 if min_wasted == -1 else min_wasted % (10 ** 9 + 7)
