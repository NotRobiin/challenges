def total_distance(height, length, tower):
	return round(((tower / height) * (height + length)), 1)


if __name__ == "__main__":
    print(total_distance(0.2, 0.4, 100.0)) # 300.0
