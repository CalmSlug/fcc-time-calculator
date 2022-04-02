def add_time(start, duration, day=False):
    hours = int(start.split()[0].split(":")[0])
    minutes = int(start.split()[0].split(":")[1])
    am_pm = start.split()[1]
    days = 0
    dotw = False


    # Converting time into 24h format
    if am_pm == "AM" and hours == 12:
        hours = 0
    elif am_pm == "PM" and hours != 12:
        hours += 12

    hours += int(duration.split(":")[0])
    minutes += int(duration.split(":")[1])

    if minutes > 59:
        hours += 1
        minutes -= 60
    if minutes < 10:
        minutes = "0" + str(minutes)

    days = hours // 24

    if day:
        dotw_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for d in dotw_list:
            if d == day.capitalize():
                dotw = dotw_list.index(d)
                break
        dotw += days
        dotw = dotw_list[dotw % 7]

    # Converting time into 12h format
    hours = hours % 24
    if hours == 0:
        am_pm = "AM"
        hours = 12
    elif hours < 12:
        am_pm = "AM"
    elif hours == 12:
        am_pm = "PM"
    else:
        am_pm = "PM"
        hours -= 12

    if days == 1 and day:
        new_time = f"{hours}:{minutes} {am_pm}, {dotw} (next day)"
    elif days > 1 and day:
        new_time = f"{hours}:{minutes} {am_pm}, {dotw} ({days} days later)"
    elif day:
        new_time = f"{hours}:{minutes} {am_pm}, {dotw}"
    elif days == 1:
        new_time = f"{hours}:{minutes} {am_pm} (next day)"
    elif days > 1:
        new_time = f"{hours}:{minutes} {am_pm} ({days} days later)"
    else:
        new_time = f"{hours}:{minutes} {am_pm}"

    return new_time


# Output showcase
print(add_time("3:30 PM", "2:12"), "\n")
print(add_time("11:55 AM", "3:12"), "\n")
print(add_time("9:15 PM", "5:30"), "\n")
print(add_time("11:40 AM", "0:25"), "\n")
print(add_time("2:59 AM", "24:00"), "\n")
print(add_time("11:59 PM", "24:05"), "\n")
print(add_time("8:16 PM", "466:02"), "\n")
print(add_time("5:01 AM", "0:00"), "\n")
print(add_time("3:30 PM", "2:12", "Monday"), "\n")
print(add_time("2:59 AM", "24:00", "saturDay"), "\n")
print(add_time("11:59 PM", "24:05", "Wednesday"), "\n")
print(add_time("8:16 PM", "466:02", "tuesday"), "\n")