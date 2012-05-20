import datetime

container = r"""<style type="text/css">
a:link {
text-decoration: none;
color: #000000
}

a:visited {
text-decoration: none;
color: #000000
}

a:hover {
text-decoration: none;
color: #FFFFFF;
}
</style>
<div style="overflow: auto; width: 100%%; padding:0px; margin: 0px; border-radius: 15px; font-family: arial; position: relative">
  <div style="background-image:url('../Capture2.PNG'); padding:0px; margin: 0px; border-radius: 15px; border-bottom-right-radius: 0px; border-bottom-left-radius: 0px; width: %d">
    <br />
    %s
    %s
  </div>
</div>
"""
#
timeline = r"""<div style="height: 100; padding: 0px; margin: 0px; position: relative">
      %s
    </div>
"""

item = r"""<div style="background-image:url('../Capture.PNG'); background-repeat: repeat-x; position: absolute; top: {layer}; left: {position}; width: {duration}; height: 19; padding: 0px; margin: 0px; border-style: solid; border-color: #777777; border-width: 2px; padding-left: 4px; padding-top: 1px; border-radius: 15px">
        <a href="http://cslab2-24.stuy.edu:8080/activity/{idnum}"><span style="white-space: nowrap; width: 100%">{content}</span></a>
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
    
def genItem(layernum, position, duration, content, idnum):
    return item.format(**{"layer":(30 * layernum + 8), "position":position, "duration": duration, "content":content, "idnum":idnum})

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
        item = genItem(layernum, 5 + 3 * start, 3 * (end - start) - 5, name, idnum)
        items.append(item)
    return timeline % ("\n".join(items)), max(maxTime)

def genPage(info):
    earliest = None
    for (name, activities) in info:
        if activities and (not earliest or calcTime(activities[0][3]) < earliest):
            earliest = calcTime(activities[0][3])
            start = activities[0][3]
    timelines = []
    latest = None
    for (name, activities) in info:
        txt, last = genTimeline(activities, earliest)
        timelines.append(("""<div style="padding-left: 20"><h2>%s</h2></div>\n""" % name) + txt)
        if last:
            if not latest or (last > latest):
                latest = last
    label = """<div style="padding:0px; margin: 0px; width: 200px; height: 20px; position:absolute; top: 10px; left: {position}">{content}</div>\n"""
    labels = ""
    text = start
    year = int(text[0:4])
    month = int(text[5:7])
    day = int(text[8:10])
    hour = int(text[11:13])
    minute = int(text[14:16])
    total = 0
    if minute != 0:
        total = 60 - minute
    labelData = datetime.datetime(year, month, day, hour, minute) + datetime.timedelta(0, total * 60)
    while total <= 160 or total <= latest - 40:
        labels+= label.format(position = total * 3, content = "&darr; " + str(labelData)[-8:-3])
        total += 60
        labelData = labelData + datetime.timedelta(0, 3600)
    return container % (3 * ((latest > 200 and latest) or 200) + 20, labels, "\n".join(timelines))
