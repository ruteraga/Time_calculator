def add_time(start_time, duration_time, day=False):
  weekdays = [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
    "Sunday"
  ]

  a = start_time.split()
  b = duration_time.find(':')
  d = a[0].find(':')
  current_hour = int(a[0][:d])
  current_minutes = int(a[0][d + 1:])

  hour_to_add = int(duration_time[:b])
  minutes_to_add = int(duration_time[b + 1:])
  new_minutes = int(current_minutes) + int(minutes_to_add)
  new_hour = 0
  time = ""
  if day is not False:
    for i in range(len(weekdays)):
      if day == weekdays[i]:
        date = i
  if new_minutes > 60:
    new_hour = 1
    new_minutes = new_minutes - 60
  if a[1] == 'AM':
    if hour_to_add < 24:
      new_hour = new_hour + int(current_hour) + int(hour_to_add)
      hour_clock = 'AM'
      if new_hour >= 12:
        date = date + 1
        hour_clock = 'PM'
        if new_hour == 12:
          new_hour = 12
        else:
          new_hour = new_hour - 12
      time = weekdays[date] + " " + str(new_hour) + ":" + str(
        new_minutes) + " " + str(hour_clock)
    else:
      days = int(hour_to_add / 24)
      date = date + days
      new_hour_to_add = hour_to_add % 24
      new_hour = new_hour + int(current_hour) + int(new_hour_to_add)
      hour_clock = 'AM'
      if new_hour >= 12:
        hour_clock = 'PM'
        if new_hour == 12:
          new_hour = 12
        else:
          new_hour = new_hour - 12
      time = weekdays[date] + " " + str(new_hour) + ":" + str(
        new_minutes) + " " + str(hour_clock) + " (" + str(
          days) + " days later)"
  elif a[1] == 'PM':
    if hour_to_add < 24:
      new_hour = new_hour + int(current_hour) + int(hour_to_add)
      hour_clock = 'PM'
      if new_hour >= 12:
        hour_clock = 'AM'
        date = date + 1
        if new_hour == 12:
          new_hour = 12
        else:
          new_hour = new_hour - 12
      time = weekdays[date] + " " + str(new_hour) + ":" + str(
        new_minutes) + " " + str(hour_clock) + " (the next day)"
    else:
      days = int(hour_to_add / 24)
      date = date + days + 1
      new_hour_to_add = hour_to_add % 24
      new_hour = new_hour + int(current_hour) + int(new_hour_to_add)
      hour_clock = 'PM'
      if new_hour >= 12:
        hour_clock = 'AM'
        if new_hour == 12:
          new_hour = 12
        else:
          new_hour = new_hour - 12
      time = weekdays[date] + " " + str(new_hour) + ":" + str(
        new_minutes) + " " + str(hour_clock) + " (" + str(days +
                                                          1) + " days later)"

  else:
    print('No time period provided')
  print(time)
