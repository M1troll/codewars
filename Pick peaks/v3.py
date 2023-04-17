
from typing import TypedDict, Sequence


class Peaks(TypedDict):
    """Typed dict for store peaks info."""
    pos: list[int]
    peaks: list[int]


def pick_peaks(array: Sequence) -> Peaks:
    """."""
    pos, peaks = [], []
    if not array:
        return Peaks(pos=pos, peaks=peaks)

    current_maxima, current_index = array[0], 0
    for index in range(2, len(array) - 1):
        value = array[index]
        if array[index - 1] <= value:
            if array[index - 1] != value:
                current_index, current_maxima = index, value
            if value > array[index + 1]:
                if current_index not in pos:
                    pos.append(current_index)
                    peaks.append(current_maxima)
            
    return Peaks(pos=pos, peaks=peaks)


if __name__ == "__main__":
    cases: dict[tuple, dict] = {
        (1,2,3,6,4,1,2,3,2,1): {"pos":[3,7], "peaks":[6,3]},
        (3,2,3,6,4,1,2,3,2,1,2,3): {"pos":[3,7], "peaks":[6,3]},
        (3,2,3,6,4,1,2,3,2,1,2,2,2,1): {"pos":[3,7,10], "peaks":[6,3,2]},
        (2,1,3,1,2,2,2,2,1): {"pos":[2,4], "peaks":[3,2]},
        (2,1,3,1,2,2,2,2): {"pos":[2], "peaks":[3]},
        (2,1,3,2,2,2,2,5,6): {"pos":[2], "peaks":[3]},
        (2,1,3,2,2,2,2,1): {"pos":[2], "peaks":[3]},
        (1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3): {"pos":[2,7,14,20], "peaks":[5,6,5,5]},
        (18, 18, 10, -3, -4, 15, 15, -1, 13, 17, 11, 4, 18, -4, 19, 4, 18, 10, -4, 8, 13, 9, 16, 18, 6, 7): {'pos': [5, 9, 12, 14, 16, 20, 23], 'peaks': [15, 17, 18, 19, 18, 13, 18]},
        (): {"pos":[],"peaks":[]},
        (1,1,1,1): {"pos":[],"peaks":[]},
    }
    for test, result in cases.items():
        check = pick_peaks(test)
        if check == result:
            print(True)
            continue
        print(f"{check} vs {result}")
