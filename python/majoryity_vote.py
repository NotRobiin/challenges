def majority_vote(l):
    for i in list(set(l)):
        if l.count(i) > len(l) / 2:
            return i


    # length = len(l)

    # if length == 0:
    #     return None

    # votes = {v: l.count(v) for v in l}
    # sorted_votes = {
    #     k: v for k, v in sorted(votes.items(), key=lambda v: v[1], reverse=True)
    # }
    # first_key = list(sorted_votes.keys())[0]
    # first_value = sorted_votes[first_key]

    # if first_value > (length / 2):
    #     return first_key

    # return None


print(majority_vote(["A", "B", "B"]) == "B")