﻿init python:
    config.use_cpickle = False
    style.menu_choice_button.background = Frame("Graphics/ui/choice_bg_idle.jpg",28,9) #These two commands set the background of all in-game choice-buttons.
    style.menu_choice_button.hover_background = Frame("Graphics/ui/choice_bg_hover.jpg",28,9)
    style.menu_choice.color = "#fff" #These two commands set the color of the font in the in-game choice buttons.
    
    style.menu_choice_button_disabled.background = Frame("Graphics/ui/choice_bg_disabled.jpg",28,9)
    
    import datetime
    
    eventlibrary = {}
    presetdays = {}
    datelibrary = {}
    girllist = ['BE', 'GTS', 'AE', 'FMG', 'BBW', 'PRG']
    girlsizes = {'BE': 1, 'GTS': 1, 'AE': 1, 'FMG': 1, 'BBW': 1, 'PRG': 1}
    locationlist = ['arcade', 'auditorium', 'cafeteria', 'campuscenter', 'classroom', 'cookingclassroom', 'dormBBW', 'dormBE', 'dormexterior', 'dorminterior', 'festival', 'gym', 'hallway', 'library', 'musicclassroom', 'office', 'pool', 'roof', 'schoolfront', 'schoolplanter', 'schoolexterior', 'town', 'track']
    debuginfo = False
    debugenabled = True
    debuginput = ""
    debugpriorities = ""
    gametime = datetime.date(2005, 4, 4)
    
    import math

    class Shaker(object):       #This is Python code to implement a feature to shake the screen around at random, not just in one direction like with the punch commands
    
        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0,
            }
    
        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            #
            self.start = [ self.anchors.get(i, i) for i in start ]  # central position
            self.dist = dist    # maximum distance, in pixels, from the starting point
            self.child = child
            
        def __call__(self, t, sizes):
            # Float to integer... turns floating point numbers to
            # integers.                
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x

            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

            xpos = xpos - xanchor
            ypos = ypos - yanchor
            
            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

            return (int(nx), int(ny), 0, 0)
        
    def _Shake(start, time, child=None, dist=100.0, **properties):

        move = Shaker(start, child, dist=dist)
        
        return renpy.display.layout.Motion(move,
                        time,
                        child,
                        add_sizes=True,
                        **properties)

    Shake = renpy.curry(_Shake)
    
    class WeightedChoicePicker(object): #Class for weighted selection (used for favored girl selection)
            def __init__(self, dict):
                #"dict" is a dict of {"value": chance, "value": chance...}
                self.dict = dict
                self.sum = sum([ val for key, val in dict.iteritems()])
           
            def pick(self):
                rand = renpy.random.uniform(0, self.sum)
                sum = 0.0
                ret = None
                for key, val in self.dict.iteritems():
                    sum += val
                    if rand < sum:
                        ret = key
                        break
                if ret == None:
                    ret = key
               
                self.sum -= val
                del self.dict[key]
                return ret
               
            def hasKeysLeft(self):
                return len(self.dict) != 0
    #Condition enums/stuff
    class ConditionEnum:
        EVENT, NOEVENT, FLAG, NOFLAG, GAMETIME, AFFECTION, SKILL, PRESET, OR, ISDAYFREE, ROUTECLEAR = range(11)
    
    #EVENT: arg1 = (string) event code, true if event has been seen
    #NOEVENT: arg1 = (string) event code, true if event has NOT been seen
    #FLAG: arg1 = (string) flag name, true if flag has been raised
    #NOFLAG: arg1 = (string) flag name, true if flag has NOT been raised
    #GAMETIME: arg1 = ConditionEqualityEnum, arg2 = (date, from datelibrary) date in question, true if the comparison is true (between gametime and arg2)
    #AFFECTION: arg1 = (string, in girls list) girl, arg2 = ConditionEqualityEnum, arg3 = (int) affection score, true if the comparison is true (between girl specified in arg1's affection score and arg3)
    #SKILL: arg1 = (string, in skills list) skill, arg2 = ConditionEqualityEnum, arg3 = (int) skill score, true if the comparison is true (between skill specified in arg1 and arg3)
    #PRESET: no args, always returns false (ie event is only used in preset dates)
    #OR: arg1 = condition, arg2 = condition, returns true if either arg1 or arg2 are true
    #ISDAYFREE: arg1 = DeltaTimeEnum, arg2 = (int) number of days OR (date) date OR (DayOfWeekEnum) day of week, arg3 = (boolean) evening, returns true if the specified time (with time of day from arg3) is not a preset/meeting day
    #ROUTECLEAR: arg1 = (string, in girls list), returns true if there are no events in the eventlibrary that haven't been cleared but are still available to select

    class DeltaTimeEnum:
        NUMDAYS, DATE, DAYOFWEEK = range(3)
    
    class ConditionEqualityEnum:
        EQUALS, NOTEQUALS, GREATERTHAN, LESSTHAN, GREATERTHANEQUALS, LESSTHANEQUALS = range(6)
    
    class DayOfWeekEnum:
        MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY = range(7)
    
    class WeekendEnum:
        MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY, WEEKDAY, WEEKEND, ANY = range(10)
    
    class TimeEnum:
        DAY, NIGHT, AFTERSCHOOL, ANY = range(4)
    
    def checkCriteria(clist, checkRouteClear=True):
        criteriavalid = True
        for c in clist:
            if c[0] == ConditionEnum.EVENT:
                if c[1] not in clearedevents:
                    criteriavalid = False
                    break
                else:
                    continue
            elif c[0] == ConditionEnum.NOEVENT:
                if c[1] in clearedevents:
                    criteriavalid = False
                    break
                else:
                    continue
            elif c[0] == ConditionEnum.FLAG:
                if c[1] not in flags:
                    criteriavalid = False
                    break
                else:
                    continue
            elif c[0] == ConditionEnum.NOFLAG:
                if c[1] not in flags:
                    continue
                else:
                    criteriavalid = False
                    break
            elif c[0] == ConditionEnum.GAMETIME:
                if c[1] == ConditionEqualityEnum.LESSTHAN:
                    if gametime >= c[2]:
                        criteriavalid = False
                        break
                    else:
                        continue
                elif c[1] == ConditionEqualityEnum.GREATERTHAN:
                    if gametime <= c[2]:
                        criteriavalid = False
                        break
                    else:
                        continue
                elif c[1] == ConditionEqualityEnum.LESSTHANEQUALS:
                    if gametime > c[2]:
                        criteriavalid = False
                        break
                    else:
                        continue
                elif c[1] == ConditionEqualityEnum.GREATERTHANEQUALS:
                    if gametime < c[2]:
                        criteriavalid = False
                        break
                    else:
                        continue
                elif c[1] == ConditionEqualityEnum.EQUALS:
                    if gametime != c[2]:
                        criteriavalid = False
                        break
                    else:
                        continue
                else:
                    renpy.log("Invalid criteria equality enum ID: %s" % str(c[1]))
                    criteriavalid = False
                    break
            elif c[0] == ConditionEnum.AFFECTION:
                if c[2] == ConditionEqualityEnum.LESSTHAN:
                    if getAffection(c[1]) >= int(c[3]):
                        criteriavalid = False
                        break
                    else:
                        continue
                elif c[2] == ConditionEqualityEnum.GREATERTHAN:
                    if getAffection(c[1]) <= int(c[3]):
                        criteriavalid = False
                        break
                    else:
                        continue
                else:
                    renpy.log("Invalid criteria equality enum ID: %s" % str(c[2]))
                    criteriavalid = False
                    break
            elif c[0] == ConditionEnum.PRESET:
                criteriavalid = False
                break
            elif c[0] == ConditionEnum.OR:
                if checkCriteria([c[1]]) or checkCriteria([c[2]]):
                    continue
                else:
                    criteriavalid = False
                    break
            elif c[0] == ConditionEnum.ISDAYFREE:
                if c[1] == DeltaTimeEnum.NUMDAYS:
                    t = gametime + datetime.timedelta(days=c[2])
                elif c[1] == DeltaTimeEnum.DATE:
                    t = c[2]
                elif c[1] == DeltaTimeEnum.DAYOFWEEK:
                    tmp = c[2] - gametime.weekday()
                    if tmp < 0: #if the day of the week we're considering has already passed, we need to do it next week
                        tmp += 7
                    t = gametime + datetime.timedelta(days=tmp)
                else:
                    renpy.log("Invalid DeltaTimeEnum: %s" % str(c[1]))
                    criteriavalid = False
                    break
                if getTimeCode(t, c[3]) in presetdays.keys() or getTimeCode(t, c[3]) in meetingdays.keys():
                    criteriavalid = False
                    break
            elif c[0] == ConditionEnum.ROUTECLEAR:
                if checkRouteClear:
                    for k, v in eventlibrary.iteritems():
                        if k in clearedevents:
                            continue
                        if len(v["girls"]) == 0 or c[1] != v["girls"][0]:
                            continue
                        if not checkCriteria(v["conditions"], False):
                            continue
                        criteriavalid = False
                        break
                    if not criteriavalid:
                        break
            else:
                renpy.log("Invalid criteria enum ID: %s" % str(c[0]))
                criteriavalid = False
                break
        return criteriavalid    
    
    def isEventTimeOk(time, day):
        #Weekday = Mon-Sat, Weekend = Sun, Any = Do not check
        d = (day == WeekendEnum.ANY or (day == WeekendEnum.WEEKEND and gametime.weekday() == 6) or (day == WeekendEnum.WEEKDAY and gametime.weekday() != 6))
        d = d or (gametime.weekday() == day)
        #Day = Day time period, Night = Night time period, Afterschool = Night time period OR Sunday, Any = Do not check, Day of week = that day specifically
        t = (time == TimeEnum.ANY or (time == TimeEnum.DAY and not gametime_eve))
        t = t or ((time == TimeEnum.NIGHT or time == TimeEnum.AFTERSCHOOL) and gametime_eve)
        t = t or (time == TimeEnum.AFTERSCHOOL and gametime.weekday() == 6)
        return d and t
        
    def isEventDateOk(start, end):
        return gametime > datelibrary[start] and gametime < datelibrary[end]
    
    #Other misc functions
    def setAffection(girl, val):
        if not girl in girllist and not girl == "RM":
            renpy.log("ERROR: Could not change affection: Girl %s does not exist" % girl)
            return
        affection[girl] += val
        
    def getAffection(girl):
        if not girl in girllist and not girl == "RM":
            renpy.log("ERROR: Could not fetch affection: Girl %s does not exist" % girl)
            return 0
        return affection[girl]

    ##Checks which of the girls has the second highest affection. Doesn't account for ties.
    def getSecondHighest(ignoreGirl):
        highestAffection = 0
        secondGirl = ""
        for girl in girllist:
            if girl == ignoreGirl:
                continue

            affection = getAffection(girl)
            if affection > highestAffection:
                highestAffection = affection
                secondGirl = girl
        return secondGirl
        
    def isEventCleared(event):
        return event in clearedevents
        
    def setEventCount(girl, val):
        if not girl in girllist:
            renpy.log("ERROR: Could not change affection: Girl %s does not exist" % girl)
            return
        eventcounter[girl] += val
        
    def setFlag(flag, state=True):
        if state:
            if flag in flags:
                return
            else:
                flags.append(flag)
        else:
            if flag in flags:
                flags.remove(flag)
            else:
                return
            
    def getFlag(flag):
        return flag in flags
    
    def setVar(id, val):
        vars[id] = val
    
    def getVar(id):
        if id in vars.keys():
            return vars[id]
        else:
            return 0
    
    def debugListFlags():
        l = ""
        for f in flags:
            l += f + ", "
        return l
    
    def debugListEvents():
        l = ""
        for s in allpool:
            l += s + ", "
        return l
        
    def debugListClearedEvents():
        l = ""
        for s in clearedevents:
            l += s + ", "
        return l
        
    def addMeeting(event, deltatime, val, eve):
        if deltatime == DeltaTimeEnum.NUMDAYS:
            t = gametime + datetime.timedelta(days=val)
        elif deltatime == DeltaTimeEnum.DATE:
            t = val
        elif deltatime == DeltaTimeEnum.DAYOFWEEK:
            t = gametime + datetime.timedelta(days=((val + 7) - gametime.weekday()))
        meetingdays[getTimeCode(t, eve)] = [event]
    
    def getSize(g):
        if g in girllist:
            return girlsizes[g]
        else:
            return -1
    
    def updateSizes():
        for g in girllist:
            for i in range(6, 1, -1):
                if i == 1:
                    girlsizes[g] = i
                    break
                s = g + '_size_' + str(i)
                if gametime > datelibrary[s]:
                    girlsizes[g] = i
                    break
        
    def setSkill(s, val):
        if s not in skills.keys():
            renpy.log("Unknown skill ID: %s" % s)
            return -1
        else:
            skills[s] += val
            return skills[s]
            
    def getSkill(s):
        if s not in skills.keys():
            renpy.log("Unknown skill ID: %s" % s)
            return -1
        else:
            return skills[s]
    
    def getTimeString():
        s = gametime.strftime("%a %B %d, 20XX")
        if gametime_eve == TimeEnum.NIGHT:
            s += " (Evening)"
        else:
            s += " (Morning)"
        return s
        
    def getTimeCode(date=None, eve=None):
        if date == None:
            date = gametime
        if eve == None:
            eve = gametime_eve
        s = str(date.month) + "-" + str(date.day)
        if eve == TimeEnum.NIGHT:
            s += "-T"
        else:
            s += "-F"
        return s
            
    def pickPreferredGirl():
        sc = eventcounter.copy()
        scsort = sorted(sc.iteritems(), key=lambda x: x[1], reverse=True)
        # Finally, we pick out the heaviest items by picking off the heaviest side of the array.
        topweight = scsort[0][1]
        weightlist = {}
        weightlist[scsort[0][0]] = 3
        i = 1
        while i < len(scsort) and scsort[i][1] + 2 >= topweight:
            if scsort[i][1] == topweight:
                weightlist[scsort[i][0]] = 3
            elif scsort[i][1] + 1 == topweight:
                weightlist[scsort[i][0]] = 2
            else:
                weightlist[scsort[i][0]] = 1
            i += 1
        picker = WeightedChoicePicker(weightlist)
        return picker.pick()

label start:
    python:
        #Global Variables
        affection = {'BE': 0, 'GTS': 0, 'AE': 0, 'FMG': 0, 'BBW': 0, 'PRG': 0, 'RM': 0}
        skills = {"Athletics": 0, "Art": 0, "Academics": 0}
        eventcounter = {'BE': 5, 'GTS': 5, 'AE': 5, 'FMG': 5, 'BBW': 5, 'PRG': 5}
        globalsize = 1
        flags = []
        vars = {}
        eventcountmax = 10
        eventchoices = []
        activeevent = ""
        gametime = datetime.date(2005, 4, 4)
        gametime_eve = TimeEnum.DAY
        meetingdays = {}
        eventpool = []
        preferredpool = []
        clearedevents = []
        prefgirl = ""
        freeday = True
        prefevent = True
    jump global000

label splashscreen:
    scene black
    with Pause(1)
    
    show splash with dissolve
    with Pause(2)
    
    scene black with dissolve
    with Pause(1)
    
    return

#Remember to hide choicetimer for each choice made before the timer finishes.
screen choicetimer:
    timer 0.01 repeat True action If(timer_count > 0, true=SetVariable('timer_count', timer_count - 0.01), false=[Hide('choicetimer'), Jump(timer_jump)])

screen daymenu:
    if gametime_eve == TimeEnum.NIGHT:
        add "Graphics/ui/bg/menubg-evening.png"
    else:
        add "Graphics/ui/bg/menubg-day.png"
    
    if debuginfo:
        vbox:
            xalign 0
            yalign 0
            text ("Debug info:")
            text ("Prefgirl: %s" % prefgirl)
            text ("Preferred events exist? %s" % prefevent)
            text ("Girls w/ Priority: %s" % debugpriorities)
            text ("Event limit: %d" % eventcountmax)
            text ("Girl/Aff/Events")
            text ("BE %(aff)d %(event)d" % {"aff": affection["BE"], "event": eventcounter["BE"]})
            text ("GTS %(aff)d %(event)d" % {"aff": affection["GTS"], "event": eventcounter["GTS"]})
            text ("AE %(aff)d %(event)d" % {"aff": affection["AE"], "event": eventcounter["AE"]})
            text ("FMG %(aff)d %(event)d" % {"aff": affection["FMG"], "event": eventcounter["FMG"]})
            text ("BBW %(aff)d %(event)d" % {"aff": affection["BBW"], "event": eventcounter["BBW"]})
            text ("PRG %(aff)d %(event)d" % {"aff": affection["PRG"], "event": eventcounter["PRG"]})
            text ("Athletics: %d" % skills["Athletics"])
            text ("Art: %d" % skills["Art"])
            text ("Academics: %d" % skills["Academics"])
            text ("Events:")
            for e in eventchoices:
                text ("%s" % e)
    
    text(getTimeString()):
        xalign 0.1
        yalign 0.1
        
    #event choices (3-choice day)
    if len(eventchoices) <= 3:
        vbox:
            xalign 0.5
            ypos 120
            spacing 60
            for c in eventchoices:
                vbox:
                    fixed:
                        xmaximum 600
                        ymaximum 60
                        if eventlibrary[c]["location"] in locationlist:
                            imagebutton idle "Graphics/ui/icons/bgicon-%s.png" % eventlibrary[c]["location"] action [SetVariable("activeevent", c), Jump("startevent")]
                        else:
                            imagebutton idle "Graphics/ui/icons/bgicon-missing.png" % eventlibrary[c]["location"] action [SetVariable("activeevent", c), Jump("startevent")]
                        hbox:
                            hbox:
                                spacing -120
                                order_reverse True
                                if len(eventlibrary[c]["girls"]) == 0:
                                    add "Graphics/ui/icons/charicon-missing.png"
                                else:
                                    for g in eventlibrary[c]["girls"]:
                                        add "Graphics/ui/icons/charicon-%s.png" % g
                            fixed:
                                frame:
                                    xalign 0.5
                                    yalign 0.5
                                    background Solid(Color((0, 0, 0, 100)))
                                    text eventlibrary[c]["name"] size 16

                
    #event choices (6-choice day)
    if len(eventchoices) > 3:
        grid 2 3:
            xalign 0.5
            ypos 120
            spacing 60
            for c in eventchoices:
                fixed:
                    xmaximum 250
                    ymaximum 60
                    if eventlibrary[c]["location"] in locationlist:
                        imagebutton idle im.Crop("Graphics/ui/icons/bgicon-%s.png" % eventlibrary[c]["location"], (0, 0, 250, 60)) action [SetVariable("activeevent", c), Jump("startevent")]
                    else:
                        imagebutton idle im.Crop("Graphics/ui/icons/bgicon-missing.png" % eventlibrary[c]["location"], (0, 0, 250, 60)) action [SetVariable("activeevent", c), Jump("startevent")]
                    hbox:
                        spacing -120
                        order_reverse True
                        if len(eventlibrary[c]["girls"]) == 0:
                            add "Graphics/ui/icons/charicon-missing.png"
                        else:
                            for g in eventlibrary[c]["girls"]:
                                add "Graphics/ui/icons/charicon-%s.png" % g
                        #FIXME this looks awful and breaks tables, needs harder adjustments
                        #fixed:
                        #    frame:
                        #        xalign 0.5
                        #        yalign 0.5
                        #        background Solid(Color((0, 0, 0, 100)))
                        #        text eventlibrary[c]["name"]
    
    #studying activities (non-special day)
    if freeday:
        textbutton "Train Athletics" xalign 0.1 yalign 0.8 action [SetVariable("activeevent", "Athletics"), Jump("train")]
        textbutton "Train Art" xalign 0.5 yalign 0.8 action [SetVariable("activeevent", "Art"), Jump("train")]
        textbutton "Train Academics" xalign 0.9 yalign 0.8 action [SetVariable("activeevent", "Academics"), Jump("train")]
    
    #debug menu toggle (if debug is enabled)
    if debugenabled:
        textbutton "Profiles" xalign 0.1 yalign 0.9 action Jump("profileselect")
        textbutton "Toggle Debug" xalign 0.9 yalign 0.9 action SetVariable("debuginfo", not debuginfo)
        textbutton "Enter Debug Menu" xalign 0.9 yalign 0.95 action Jump("debugmenu")
        
screen debugmenu:
    $debuginput = ""
    grid 3 13:
        xalign 0.5
        yalign 0.5
        
        text "Input:"
        input value VariableInputValue("debuginput")
        text ""
        
        text "Show Event:"
        textbutton "Go!" action Jump("debugevent")
        text ""
        
        textbutton "List Available Events" action Jump("debugeventlist")
        textbutton "List Cleared Events" action Jump("debugclearedeventlist")
        text ""
        
        textbutton "List Flags" action Jump("debugflaglist")
        textbutton "Set Flag" action Jump("setflag")
        textbutton "Unset Flag" action Jump("unsetflag")
        
        text "Girl"
        text "Affection"
        text "Events"

        text "BE"
        hbox:
            textbutton "-" action Function(setAffection, "BE", -1)
            text str(affection["BE"])
            textbutton "+" action Function(setAffection, "BE", 1)
            
        hbox:
            textbutton "-" action Function(setEventCount, "BE", -1)
            text str(eventcounter["BE"])
            textbutton "+" action Function(setEventCount, "BE", 1)
            
        text "GTS"
        hbox:
            textbutton "-" action Function(setAffection, "GTS", -1)
            text str(affection["GTS"])
            textbutton "+" action Function(setAffection, "GTS", 1)
            
        hbox:
            textbutton "-" action Function(setEventCount, "GTS", -1)
            text str(eventcounter["GTS"])
            textbutton "+" action Function(setEventCount, "GTS", 1)
            
        text "AE"
        hbox:
            textbutton "-" action Function(setAffection, "AE", -1)
            text str(affection["AE"])
            textbutton "+" action Function(setAffection, "AE", 1)
            
        hbox:
            textbutton "-" action Function(setEventCount, "AE", -1)
            text str(eventcounter["AE"])
            textbutton "+" action Function(setEventCount, "AE", 1)
            
        text "FMG"
        hbox:
            textbutton "-" action Function(setAffection, "FMG", -1)
            text str(affection["FMG"])
            textbutton "+" action Function(setAffection, "FMG", 1)
            
        hbox:
            textbutton "-" action Function(setEventCount, "FMG", -1)
            text str(eventcounter["FMG"])
            textbutton "+" action Function(setEventCount, "FMG", 1)

        text "BBW"
        hbox:
            textbutton "-" action Function(setAffection, "BBW", -1)
            text str(affection["BBW"])
            textbutton "+" action Function(setAffection, "BBW", 1)
            
        hbox:
            textbutton "-" action Function(setEventCount, "BBW", -1)
            text str(eventcounter["BBW"])
            textbutton "+" action Function(setEventCount, "BBW", 1)
            
        text "PRG"
        hbox:
            textbutton "-" action Function(setAffection, "PRG", -1)
            text str(affection["PRG"])
            textbutton "+" action Function(setAffection, "PRG", 1)
            
        hbox:
            textbutton "-" action Function(setEventCount, "PRG", -1)
            text str(eventcounter["PRG"])
            textbutton "+" action Function(setEventCount, "PRG", 1)
            
        text "RM"
        hbox:
            textbutton "-" action Function(setAffection, "RM", -1)
            text str(affection["RM"])
            textbutton "+" action Function(setAffection, "RM", 1)
        text ""
        
        #hbox:
        #    text "Athletics:"
        #    textbutton "-" action Function(setSkill, "Athletics", -1)
        #    text str(skills["Athletics"])
        #    textbutton "+" action Function(setSkill, "Athletics", 1)
            
        #hbox:
        #    text "Art:"
        #    textbutton "-" action Function(setSkill, "Art", -1)
        #    text str(skills["Art"])
        #    textbutton "+" action Function(setSkill, "Art", 1)
            
        #hbox:
        #    text "Academics:"
        #    textbutton "-" action Function(setSkill, "Academics", -1)
        #    text str(skills["Academics"])
        #    textbutton "+" action Function(setSkill, "Academics", 1)
        
        textbutton "Return to game" action Jump("daymenu_noadvance")
        textbutton "Change Time" action Jump("timemachine")
        textbutton "Load Test" action Jump("debugloadtest")

screen debugflaglist:
    vbox:
        text debugListFlags()
        textbutton "Return" action Jump("debugmenu")

screen debugeventlist:
    vbox:
        text debugListEvents()
        textbutton "Return" action Jump("debugmenu")
        
screen debugclearedeventlist:
    vbox:
        text debugListClearedEvents()
        textbutton "Return" action Jump("debugmenu")
        
label debugevent:
    if debuginput in eventlibrary:
        $activeevent = debuginput
        jump startevent
    "I couldn't call that event. Check the spelling and case (it's case sensitive, for example 'BE001')"
    jump debugmenu

label setflag:
    $setFlag(debuginput, True)
    jump debugmenu

label unsetflag:
    $setFlag(debuginput, False)
    jump debugmenu

label daymenu:
    $updateSizes()
    $renpy.choice_for_skipping()
    scene black
    play music Daymenu
    #Roll random events
    python:
        if gametime_eve == TimeEnum.NIGHT:
            gametime_eve = TimeEnum.DAY
            gametime += datetime.timedelta(days=1)
        else:
            gametime_eve = TimeEnum.NIGHT
        
        eventchoices = []
        prefpool = []
        allpool = []
        priorities = []
        prefevent = False
        #It's a preset day, don't worry about pools, just use whatever the preset says
        if getTimeCode() in presetdays.keys():
            eventchoices = presetdays[getTimeCode()]
            freeday = False
        #It's a meeting day, don't worry about pools, just use whatever the meeting says
        elif getTimeCode() in meetingdays.keys():
            eventchoices = meetingdays[getTimeCode()]
            freeday = False
        #It's not a preset day, randomly select 3 events
        else:
            freeday = True
            #Determine preferred girl
            prefmax = 0
            prefgirl = pickPreferredGirl()
            
            #While we've figured out the preferred girl, update the weight limit, which is floor(average of all non-preferred girls) + 5
            tmpeventmax = 0
            for g in girllist:
                if g == prefgirl:
                    continue
                tmpeventmax += eventcounter[g]
            eventcountmax = math.floor(tmpeventmax / 5) + 5
            
            #Fill allpool (and prefpool, if applicable)
            for k, v in eventlibrary.iteritems():
                if k in clearedevents:
                    continue
                criteriavalid = checkCriteria(v["conditions"]) and isEventTimeOk(v["time"][0], v["time"][1]) and isEventDateOk(v["startdate"], v["enddate"])
                if not criteriavalid:
                    continue
                if "priority" in v.keys() and v["priority"]:
                    for priogirl in v["girls"]: #If event is priority, add all girls to the priority list (if they aren't already)
                        if priogirl in priorities:
                            continue
                        priorities.append(priogirl)
                if prefgirl in v["girls"]:
                    prefevent = True
                    prefpool.append(k)
                allpool.append(k)

            #Scan for priorities and purge non-priorities
            if len(priorities) != 0:
                for e in allpool[:]: #use a copy of the list, python gets cranky if you modify a list you're iterating over
                    event = eventlibrary[e]
                    for g in event["girls"]:
                        if g in priorities:
                            if not "priority" in event.keys() or not event["priority"]:
                                allpool.remove(e)
                
                if prefgirl in priorities:
                    for e in prefpool[:]: #use a copy of the list, python gets cranky if you modify a list you're iterating over
                        event = eventlibrary[e]
                        if not "priority" in event.keys() or not event["priority"]:
                            prefpool.remove(e)
            
            #Select from preferred pool
            if len(prefpool) != 0:
                tmp = renpy.random.choice(prefpool)
                eventchoices.append(tmp)
                prefpool.remove(tmp)
                if tmp in allpool:
                    allpool.remove(tmp)
            elif len(allpool) != 0: #...or the allpool, if the preferred pool is empty
                tmp = renpy.random.choice(allpool)
                eventchoices.append(tmp)
                allpool.remove(tmp)
            
            #Pick 2 more "allpool" events
            if (len(allpool) >= 2):
                eventchoices += renpy.random.sample(allpool, 2)
            else:
                eventchoices += allpool
        debugpriorities = "".join(priorities)
    window hide None
    call screen daymenu
    window show None
    
label daymenu_noadvance:
    scene black
    window hide None
    call screen daymenu
    window show None
    
label debugmenu:
    scene black
    window hide None
    call screen debugmenu
    window show None

label debugflaglist:
    scene black
    window hide None
    call screen debugflaglist
    window show None

label debugeventlist:
    scene black
    window hide None
    call screen debugeventlist
    window show None
    
label debugclearedeventlist:
    scene black
    window hide None
    call screen debugclearedeventlist
    window show None

label startevent:
    python:
        if activeevent[0:10] != "specialday":
            for g in eventlibrary[activeevent]["girls"]:
                eventcounter[g] += 1
                if eventcounter[g] >= eventcountmax:
                    eventcounter[g] = eventcountmax

        clearedevents.append(activeevent)
    stop music
    play sound EventStart
    scene black with dissolve
    pause .5
    $renpy.block_rollback()
    $renpy.jump(activeevent)
    
label train:
    stop music
    if activeevent == "Athletics":
        jump trainathletics
    elif activeevent == "Art":
        jump trainart
    elif activeevent == "Academics":
        jump trainacademics
    else:
        "Error: Unknown skill selected. ID selected was [activeevent]. Please report to your local coder."
        jump daymenu

label trainathletics:
    scene Track with fade
    $tmp = renpy.random.randint(1, 2)
    if tmp == 1:
        "I ran around for a while."
    elif tmp == 2:
        "I lifted weights for a while."
    if getSkill("Athletics") < 5:
        "I'm pretty out of shape, so it was exhausting, but it was a good workout."
    else:
        "It wasn't too tough, but it was a good workout."
    $tmp = setSkill("Athletics", 1)
    "(Your athletics skill has increased to [tmp])"
    jump daymenu
    
label trainart:
    scene Library with fade
    $tmp = renpy.random.randint(1, 2)
    if tmp == 1:
        "I spent some time doodling."
    elif tmp == 2:
        "I spent some time playing guitar."
    if getSkill("Art") < 5:
        "It didn't really turn out great, but I think I'm learning from my mistakes. It was pretty good practice."
    else:
        "It turned out alright. It was pretty good practice."
    $tmp = setSkill("Art", 1)
    "(Your art skill has increased to [tmp])"
    jump daymenu

label trainacademics:
    scene Library with fade
    $tmp = renpy.random.randint(1, 2)
    if tmp == 1:
        "I studied the next chapter in my math book."
    elif tmp == 2:
        "I studied the next chapter in my history book."
    if getSkill("Academics") < 5:
        "I'm having trouble remembering everything, but I did learn a few things. I hope I get a good score on the next test."
    else:
        "I feel like I'm starting to master this material. I hope I get a good score on the next test."
    $tmp = setSkill("Academics", 1)
    "(Your academics skill has increased to [tmp])"
    jump daymenu

label timemachine:
    menu:
        "Set to size 1":
            $gametime = datetime.date(2005, 4, 5)
            "Time now 4/5"
        "Set to size 2":
            $gametime = datetime.date(2005, 4, 15)
            "Time now 4/15"
        "Return":
            "Time unchanged"
    jump debugmenu
            
label debugloadtest:
    menu:
        "Characters":
            $tmpdate = gametime
            scene black
            show AE neutral
            pause .1
            show AE neutral-annoyed
            pause .1
            show AE neutral-eyebrow
            pause .1
            show AE neutral-noglasses
            pause .1
            show AE neutral-smug
            pause .1
            show AE happy
            pause .1
            show AE sad
            pause .1
            show AE sad-2
            pause .1
            show AE surprised
            pause .1
            show AE angry
            pause .1
            show AE angry-2
            pause .1
            show AE angry-3
            pause .1
            show AE aroused
            pause .1
            show AE aroused-2
            pause .1
            show AE aroused-3
            pause .1
            show AE aroused-4
            pause .1
            show AE glasses
            pause .1
            show AE glasses-2
            pause .1
            
            show BBW neutral
            pause .1
            show BBW happy
            pause .1
            show BBW sad
            pause .1
            show BBW surprised
            pause .1
            show BBW angry
            pause .1
            show BBW aroused
            pause .1
            show BBW haughty
            pause .1
            
            show BE neutral
            pause .1
            show BE happy
            pause .1
            show BE sad
            pause .1
            show BE surprised
            pause .1
            show BE angry
            pause .1
            show BE aroused
            pause .1
            show BE zoomin
            pause .1
            
            show FMG neutral
            pause .1
            show FMG happy
            pause .1
            show FMG sad
            pause .1
            show FMG surprised
            pause .1
            show FMG angry
            pause .1
            show FMG aroused
            pause .1
            show FMG flex
            pause .1
            
            show GTS neutral
            pause .1
            show GTS happy
            pause .1
            show GTS sad
            pause .1
            show GTS surprised
            pause .1
            show GTS angry
            pause .1
            show GTS aroused
            pause .1
            show GTS embarrassed
            pause .1
            
            show PRG neutral
            pause .1
            show PRG happy
            pause .1
            show PRG sad
            pause .1
            show PRG surprised
            pause .1
            show PRG angry
            pause .1
            show PRG aroused
            pause .1
            show PRG unique
            pause .1

            scene black
            $gametime = datetime.date(2005, 4, 15)
            show AE neutral
            pause .1
            show AE neutral-annoyed
            pause .1
            show AE neutral-eyebrow
            pause .1
            show AE neutral-noglasses
            pause .1
            show AE neutral-smug
            pause .1
            show AE happy
            pause .1
            show AE sad
            pause .1
            show AE sad-2
            pause .1
            show AE surprised
            pause .1
            show AE angry
            pause .1
            show AE angry-2
            pause .1
            show AE angry-3
            pause .1
            show AE aroused
            pause .1
            show AE aroused-2
            pause .1
            show AE aroused-3
            pause .1
            show AE aroused-4
            pause .1
            show AE glasses
            pause .1
            show AE glasses-2
            pause .1

            show BBW neutral
            pause .1
            show BBW happy
            pause .1
            show BBW sad
            pause .1
            show BBW surprised
            pause .1
            show BBW angry
            pause .1
            show BBW aroused
            pause .1
            show BBW haughty
            pause .1
            
            show BE neutral
            pause .1
            show BE happy
            pause .1
            show BE sad
            pause .1
            show BE surprised
            pause .1
            show BE angry
            pause .1
            show BE aroused
            pause .1
            show BE zoomin
            pause .1
            
            show FMG neutral
            pause .1
            show FMG happy
            pause .1
            show FMG sad
            pause .1
            show FMG surprised
            pause .1
            show FMG angry
            pause .1
            show FMG aroused
            pause .1
            show FMG flex
            pause .1
            
            show GTS neutral
            pause .1
            show GTS happy
            pause .1
            show GTS sad
            pause .1
            show GTS surprised
            pause .1
            show GTS angry
            pause .1
            show GTS aroused
            pause .1
            show GTS embarrassed
            pause .1
            
            show PRG neutral
            pause .1
            show PRG happy
            pause .1
            show PRG sad
            pause .1
            show PRG surprised
            pause .1
            show PRG angry
            pause .1
            show PRG aroused
            pause .1
            show PRG unique
            pause .1
            
            show RM neutral
            pause .1
            show RM angry
            pause .1
            show RM happy
            pause .1
            show RM sad
            pause .1
            show RM smug
            pause .1
             
            show Yuki neutral
            pause .1
            show Yuki happy
            pause .1
            show Yuki sad
            pause .1
            show HR neutral
            pause .1
            
            show Ryoko neutral
            pause .1
            show Ryoko happy
            pause .1
            show Ryoko camera
            pause .1
            show Minori neutral
            pause .1
            show Minori happy
            pause .1
            
            show Rin neutral
            pause .1
            $gametime = tmpdate
            
        "Backgrounds":
            $tmptime = gametime_eve
            $tmpdate = gametime
            $gametime_eve = False
            scene Lake Road
            pause .1
            scene School Front
            pause .1
            scene School Inner
            pause .1
            scene Gate Front
            pause .1
            scene School Planter
            pause .1
            scene Hallway
            pause .1
            scene Classroom
            pause .1
            scene Dorm Exterior
            pause .1
            scene Dorm Interior
            pause .1
            scene Campus Center
            pause .1
            scene Auditorium
            pause .1
            scene School Exterior
            pause .1
            scene F1 Hallway
            pause .1
            scene Library
            pause .1
            scene Office
            pause .1
            scene Cafeteria
            pause .1
            scene Cooking Classroom
            pause .1
            scene Music Classroom
            pause .1
            scene Gym
            pause .1
            scene Track
            pause .1
            scene Roof
            pause .1
            scene Nurse Office
            pause .1
            scene Pool
            pause .1
            scene Festival
            pause .1
            scene Bathroom
            pause .1
            scene Recreation
            pause .1
            scene Town
            pause .1
            scene Arcade
            pause .1
            scene Cafe
            pause .1
            scene Dorm BBW
            pause .1
            scene Dorm BBW Flip
            pause .1
            scene Dorm GTS
            pause .1
            scene Dorm BE
            pause .1
            scene Dorm PRG
            pause .1
            scene Sushi Restaurant
            pause .1
 
            $gametime_eve = True
            
            scene Lake Road
            pause .1
            scene School Front
            pause .1
            scene School Inner
            pause .1
            scene Gate Front
            pause .1
            scene School Planter
            pause .1
            scene Hallway
            pause .1
            scene Classroom
            pause .1
            scene Dorm Exterior
            pause .1
            scene Dorm Interior
            pause .1
            scene Campus Center
            pause .1
            scene Auditorium
            pause .1
            scene School Exterior
            pause .1
            scene F1 Hallway
            pause .1
            scene Library
            pause .1
            scene Office
            pause .1
            scene Cafeteria
            pause .1
            scene Cooking Classroom
            pause .1
            scene Music Classroom
            pause .1
            scene Gym
            pause .1
            scene Track
            pause .1
            scene Roof
            pause .1
            scene Nurse Office
            pause .1
            scene Pool
            pause .1
            scene Festival
            pause .1
            scene Bathroom
            pause .1
            scene Recreation
            pause .1
            scene Town
            pause .1
            scene Arcade
            pause .1
            scene Cafe
            pause .1
            scene Dorm BBW
            pause .1
            scene Dorm BBW Flip
            pause .1
            scene Dorm GTS
            pause .1
            scene Dorm BE
            pause .1
            scene Dorm PRG
            pause .1
            scene Sushi Restaurant
            pause .1
            $gametime_eve = tmptime
            $gametime = tmpdate
        "CGs":    
            show cg BE001
            pause .1
            show cg BE002
            pause .1
            show cg BBW001
            pause .1
        "Sounds":
            play music Daymenu
            pause .1
            play music AE
            pause .1
            play music BE
            pause .1
            play music BBW
            pause .1
            play music GTS
            pause .1
            play music PRG
            pause .1
            play music RM
            pause .1
            play music Bittersweet
            pause .1
            play music Busy
            pause .1
            play music Festival
            pause .1
            play music Rain
            pause .1
            play music Peaceful
            pause .1
            play music Schoolday
            pause .1
            play music Sunset
            pause .1
            play music Tension
            pause .1
            
            play sound EventStart
            pause .1
            play sound AlarmClock
            pause .1
            play sound Bird
            pause .1
            play sound Cheer
            pause .1
            play sound ClockTower
            pause .1
            play sound Boing
            pause .1
            play sound Knock
            pause .1
            play sound Thud
            pause .1
            play sound Victory
            pause .1
        "Nevermind":
            pass
    jump debugmenu