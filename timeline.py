import datetime

container = r"""<div style="overflow: auto; width: 100%%; padding:0px; margin: 0px; border-radius: 15px; font-family: arial">
<div style="background-image:url('Capture2.PNG'); padding:0px; margin: 0px; border-radius: 15px; width: %d">
  %s
</div>
</div>
"""

timeline = r"""
  <div style="height: 100; padding: 0px; margin: 0px; position: relative">
    %s
  </div>
"""

item = r"""<div style="background-image:url('Capture.PNG'); background-repeat: repeat-x; position: absolute; top: {layer}; left: {position}; width: {duration}; height: 19; padding: 0px; margin: 0px; border-style: solid; border-color: #777777; border-width: 2px; padding-left: 4px; padding-top: 1px; border-radius: 15px">
      <span style="white-space: nowrap; width: 100%">{content}</span>
    </div>
"""
def calcTime(text):# in minutes
    year = int(text[0:4])
    month = int(text[5:7])
    day = int(text[8:10])
    hour = int(text[11:13])
    minute = int(text[14:16])
    dur = (datetime.datetime(year, month, day, hour, minute) - datetime.datetime(1970, 1, 1))
    return dur.days * 24 * 60 + dur.seconds / 60
    
def genItem(layernum, position, duration, content):
    return item.format(**{"layer":(30 * layernum + 8), "position":position, "duration": duration, "content":content})

def genTimeline(activities, startTime = None):
    if not activities:
        return timeline % "", None
    items = []
    maxTime = [0, 0, 0]
    if not startTime:
        startTime = calcTime(activities[0][3])
    for (idnum, name, event, start, end, description) in activities:
        start = calcTime(start) - startTime
        end = calcTime(end) - startTime
        if start >= maxTime[0]:
            layernum = 0
            maxTime[0] = end
        elif start >= maxTime[1]:
            layernum = 1
            maxTime[1] = end
        else:
            layernum = 2
            maxTime[2] = end
        item = genItem(layernum, 5 + 3 * start, 3 * (end - start) - 5, name)
        items.append(item)
    return timeline % ("\n".join(items)), max(maxTime)

def genPage(info):
    earliest = None
    for (name, activities) in info:
        if activities and (not earliest or calcTime(activities[0][3]) < earliest):
            earliest = calcTime(activities[0][3])
    timelines = []
    latest = None
    for (name, activities) in info:
        txt, last = genTimeline(activities, earliest)
        timelines.append(("""<div style="padding-left: 20"><h2>%s</h2></div>\n""" % name) + txt)
        if last:
            if not latest or (last > latest):
                latest = last
    return container % (3 * latest + 20, "\n".join(timelines))
