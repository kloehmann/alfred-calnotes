#!/usr/bin/env python3
import json
from os import listdir, getenv
from os.path import isfile, join
from lib import orgparse as org
from operator import itemgetter
from datetime import datetime, time

NOTES_DIR = getenv("notesdir")

if __name__ == "__main__":
    items = []
    start_of_day = datetime.combine(datetime.now(), time.min)
    end_of_day = datetime.combine(datetime.now(), time.max)
    items.append(
        {
            "date": start_of_day,
            "title": "---------------------------- TODAY ---------------------------- ",
        }
    )
    items.append(
        {
            "date": end_of_day,
            "title": "---------------------------- LATER---------------------------- ",
        }
    )

    for filename in listdir(NOTES_DIR):
        full_filename = join(NOTES_DIR, filename)
        if isfile(full_filename):
            base = org.load(full_filename)
            node = base[1]
            if node.scheduled and node.scheduled.has_time():
                sched = node.scheduled.start
                if not sched < start_of_day:
                    sched_str = sched.strftime("%d. %b %Y <%a> %H:%M")
                    title = "%s  [ %s ]" % (node.get_heading(), sched_str)
                    items.append({"date": sched, "title": title, "arg": full_filename})

    json_data = {"items": sorted(items, key=itemgetter("date"))}
    for item in items:
        del item["date"]
    print(json.dumps(json_data))
