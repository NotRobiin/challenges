def correct_stream(user, correct):
    output = []
    
    for word in user:
        if word not in correct:
            output.append(-1)
        else:
            output.append(1)
    
    return output


if __name__ == "__main__":
    correct_stream(["a","b","c"], ["a","b","d"])