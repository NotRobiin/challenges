def time_adjust(now: str, h: int, m: int, s: int) -> str:
    hrs, mts, sec = [int(t) for t in now.split(":")]

    hrs += h
    mts += m
    sec += s

    # Cover Seconds
    s_m = sec / 60
    s = sec % 60

    # Cover Minutes
    m_h = (mts + s_m) / 60
    m = (mts + s_m) % 60

    # Cover Hours
    h = (hrs + m_h) % 24

    return "%02d:%02d:%02d" % (h, m, s)


print(time_adjust("01:00:00", 1, 30, 10), "02:30:10")
print(time_adjust("18:22:30", 4, 60, 30), "23:23:00")
print(time_adjust("00:00:00", 72, 120, 120), "02:02:00")
print(time_adjust("23:59:59", 0, 0, 1), "00:00:00")
print(time_adjust("12:17:43", 0, 0, 0), "12:17:43")
print(time_adjust("14:11:29", 1000, 23466, 171626), "12:57:55")
print(time_adjust("21:02:55", 39, 62525, 332), "22:13:27")

