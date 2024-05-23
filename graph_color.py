class Subject:
    def __init__(self, name, code, clashes_with=None):
        self.name = name
        self.code = code
        self.clashes_with = clashes_with if clashes_with is not None else []

def generate_timetable(subjects):
    adjacency_list = build_adjacency_list(subjects)
    color_map = graph_coloring(adjacency_list)
    print_timetable(color_map, subjects)

def build_adjacency_list(subjects):
    adjacency_list = {}
    for subject in subjects:
        adjacency_list[subject.code] = []
        for other_subject in subjects:
            if subject.code != other_subject.code and other_subject.code in subject.clashes_with:
                adjacency_list[subject.code].append(other_subject.code)
    return adjacency_list

def graph_coloring(adjacency_list):
    color_map = {}
    for node in adjacency_list:
        available_colors = set(range(1, len(adjacency_list) + 1))
        for neighbor in adjacency_list[node]:
            if neighbor in color_map:
                available_colors.discard(color_map[neighbor])
        color_map[node] = min(available_colors)
    return color_map

def print_timetable(color_map, subjects):
    timetable = {}
    for subject, color in color_map.items():
        if color not in timetable:
            timetable[color] = []
        timetable[color].append(subject)

    for color, subjects in timetable.items():
        print("Time Slot", color)
        for subject in subjects:
            print("   Subject:", subject)
    print()

subjects = [
    Subject("DAA", "DAA24", []),
    Subject("BES", "BES24", ["DAA24"]),
    Subject("WT", "WT24", []),
    Subject("AI", "AI24", []),
    Subject("MFDS", "MFDS24", ["DAA24"]),
]

generate_timetable(subjects)
