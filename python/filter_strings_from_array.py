def filter_list(l):
    return [i for i in l if isinstance(i, int)]


if __name__ == "__main__":
    filter_list(["a",1,3,"b",5])
