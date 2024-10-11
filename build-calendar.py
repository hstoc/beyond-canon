import datetime

# 0 is Monday, 6 is Sunday
WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

LAST_DAY_OF_ROW = WEEKDAYS.index("Sun")

meat_updates = [
    datetime.date(2023, 10, 8),
    datetime.date(2023, 12, 16),
    datetime.date(2024, 3, 15),
    datetime.date(2024, 4, 13),
]

candy_updates = [
    datetime.date(2023, 10, 8),
    datetime.date(2023, 10, 25),
    datetime.date(2023, 11, 16),
    datetime.date(2024, 1, 15),
    datetime.date(2024, 2, 10),
    datetime.date(2024, 5, 8),
    datetime.date(2024, 5, 22),
    datetime.date(2024, 6, 12),
    datetime.date(2024, 6, 26),
]

helltier_updates = [
    datetime.date(2024, 7, 6),
    datetime.date(2024, 7, 22),
    datetime.date(2024, 7, 24),
    datetime.date(2024, 8, 11),
    datetime.date(2024, 8, 24),
    datetime.date(2024, 9, 14),
    datetime.date(2024, 9, 29),
]

newsposts = [
    datetime.date(2023, 10, 8),
    datetime.date(2023, 10, 18),
    datetime.date(2023, 10, 25),
    datetime.date(2023, 10, 30),
    datetime.date(2023, 11, 16),
    datetime.date(2023, 12, 1),
    datetime.date(2023, 12, 16),
    datetime.date(2024, 1, 1),
    datetime.date(2024, 1, 15),
    datetime.date(2024, 2, 2),
    datetime.date(2024, 2, 10),
    datetime.date(2024, 3, 5),
    datetime.date(2024, 3, 15),
    datetime.date(2024, 4, 1),
    datetime.date(2024, 4, 13),
    datetime.date(2024, 5, 2),
    datetime.date(2024, 5, 8),
    datetime.date(2024, 6, 1),
    datetime.date(2024, 6, 12),
    datetime.date(2024, 7, 23),
    datetime.date(2024, 8, 11),
    datetime.date(2024, 9, 14),
]

commentary_writer = [
    datetime.date(2023, 11, 1), # Actually two that day
    datetime.date(2023, 12, 1),
    datetime.date(2024, 1, 1),
    datetime.date(2024, 2, 1),
    datetime.date(2024, 3, 1),
    datetime.date(2024, 4, 1),
    datetime.date(2024, 5, 1),
    datetime.date(2024, 6, 1), # None in July
    datetime.date(2024, 8, 3),
    datetime.date(2024, 9, 1),
    datetime.date(2024, 9, 13),
]

commentary_artist = [
    datetime.date(2023, 11, 1), # Actually two that day
    datetime.date(2023, 12, 1),
    datetime.date(2024, 1, 1),
    datetime.date(2024, 2, 1),
    datetime.date(2024, 3, 1),
    datetime.date(2024, 4, 1),
    datetime.date(2024, 5, 1),
    datetime.date(2024, 6, 1),
    datetime.date(2024, 7, 12),
    datetime.date(2024, 8, 3),
    datetime.date(2024, 9, 1),
]

bonus_comics = [
    datetime.date(2023, 11, 1), # 1, 2
    datetime.date(2023, 12, 1), # 3, 4
    datetime.date(2024, 1, 1),  # 5, 6
    datetime.date(2024, 2, 1),  # 7, 8
    datetime.date(2024, 3, 1),  # 9, 10
    datetime.date(2024, 4, 15), # 11
    datetime.date(2024, 4, 22), # 12
    datetime.date(2024, 5, 12), # 13
    datetime.date(2024, 5, 17), # 14
    datetime.date(2024, 6, 14), # 15
    datetime.date(2024, 6, 21), # 16
    datetime.date(2024, 7, 19), # 17
    datetime.date(2024, 7, 26), # 18
    datetime.date(2024, 8, 16), # 19
    datetime.date(2024, 8, 23), # 20
    datetime.date(2024, 9, 20), # 21
    datetime.date(2024, 9, 27), # 22
]

monthly_illustrations = [
    datetime.date(2023, 11, 1),
    datetime.date(2023, 12, 1),
    datetime.date(2024, 1, 1),
    datetime.date(2024, 2, 10),
    datetime.date(2024, 3, 1),
    datetime.date(2024, 4, 13),
    datetime.date(2024, 5, 24),
    datetime.date(2024, 6, 7),
    datetime.date(2024, 7, 1),
    datetime.date(2024, 9, 2), # Delayed from August
    datetime.date(2024, 9, 13),
]

track_previews = [
    datetime.date(2024, 3, 5),  # Vriska and Aradia
    datetime.date(2024, 6, 4),  # Entering the Plot Point
    datetime.date(2024, 7, 9),  # Vriska and Tavros
    datetime.date(2024, 7, 31), # Nannasprite
    datetime.date(2024, 8, 20), # Doc Scratch
    datetime.date(2024, 9, 10), # Davesprite
]

update_types = {
    "meat": meat_updates,
    "candy": candy_updates,
    "helltier": helltier_updates,
    "newspost": newsposts,
    "commentary_writer": commentary_writer,
    "commentary_artist": commentary_artist,
    "bonus_comic": bonus_comics,
    "monthly_illustration": monthly_illustrations,
    "track_preview": track_previews,
}

icon_names = {
    "meat": "meat.png",
    "candy": "candy.png",
    "helltier": "helltier.png",
    "newspost": "news.png",
    "commentary_writer": "writer-commentary.png",
    "commentary_artist": "artist-commentary.png",
    "bonus_comic": "comic.png",
    "monthly_illustration": "illustration.png",
    "track_preview": "music.png",
}


# Each month is one table
# Row is a week
# Cell is a day

# Only the first table of the section needs the weekday header

class DayEvents:
    def __init__(self, day, events):
        self.day = day
        self.events = events

    def __str__(self):
        return f"day_{self.day}={self.events}"
    
    def __repr__(self):
        return str(self)

def build_month(year, month):
    day = datetime.date(year, month, 1)
    weeks = []
    week = []

    # Rows end on LAST_DAY_OF_ROW.
    # If a month starts on a LAST_DAY_OF_ROW, the first row has one cell.
    # If there are X days before that LAST_DAY_OF_ROW, the first row has X cells.
    week_1_real_days = LAST_DAY_OF_ROW - day.weekday() + 1
    
    for i in range((7 - week_1_real_days) % 7):
        week.append(None)
    
    while day.month == month:
        day_events = DayEvents(day.day, [])

        for event_type, event_dates in update_types.items():
            if day in event_dates:
                day_events.events.append(event_type)

        week.append(day_events)

        if day.weekday() == LAST_DAY_OF_ROW:
            weeks.append(week)
            week = []
        day += datetime.timedelta(days=1)
    weeks.append(week)
    return weeks

def month_to_html(year, month):
    weeks = build_month(year, month)
    html = '<table class="calendar">\n'
    html += "<tr>\n"
    for week in weeks:
        #html += "<tr>\n"
        for day in week:
            if day is None:
                html += "<td></td>\n"
            else:
                html += '<td>'
                if day.day == 1:
                    html += f'<span class="monthname">{MONTHS[month-1]}</span><span class="date">{day.day}</span>'
                else:
                    html += f'<span class="date">{day.day}</span>'
                for event in day.events:
                    icon = icon_names[event]
                    html += f'<img class="icon" src="{icon}" alt="{event}">'
                html += '</td>\n'
        #html += "</tr>\n"
    html += "</tr>\n"
    html += "</table>\n"
    return html

header = "<table class='calendar'>\n"
header += "<tr>\n"
for weekday_offset in range(7):
    weekday = WEEKDAYS[(LAST_DAY_OF_ROW + weekday_offset + 1) % 7]
    header += f"<th>{weekday}</th>\n"
header += "</tr>\n"
header += "</table>\n"
print(header)

for month in range(10, 13):
    print(month_to_html(2023, month))
    print()
for month in range(1, 11):
    print(month_to_html(2024, month))
    print()