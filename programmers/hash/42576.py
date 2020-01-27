def solution(participant, completion):
    names = {}
    for p in participant:
        names[p] = names[p] + 1 if p in names else 1
    for c in completion:
        names[c] -= 1
    for (name, value) in names.items():
        if value:
            return name
